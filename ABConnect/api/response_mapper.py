"""Response mapper for casting API responses to Pydantic models.

This module provides mapping from API endpoints to their corresponding
Pydantic models, enabling automatic type casting of responses.
"""

from typing import Any, Dict, Optional, Type, Union
import importlib
import logging

logger = logging.getLogger(__name__)

class ResponseMapper:
    """Maps API responses to Pydantic models based on endpoint and method."""

    def __init__(self):
        """Initialize the response mapper with endpoint mappings."""
        self._model_cache: Dict[str, Type] = {}
        self._models_rebuilt = False

        # Mapping of endpoint patterns to model names
        # Format: (method, path_pattern) -> model_name
        self.endpoint_mappings = {
            # Companies endpoints
            ('GET', '/api/companies/{id}'): 'Company',
            ('GET', '/api/companies/{companyId}/details'): 'CompanyDetails',
            ('GET', '/api/companies/{companyId}/fulldetails'): 'CompanyDetails',
            ('GET', '/api/companies/search'): ['Company'],  # List response
            ('POST', '/api/companies/search/v2'): ['SearchCompanyResponse'],
            ('POST', '/api/companies/list'): ['Company'],
            ('POST', '/api/companies/simplelist'): ['Company'],

            # Address endpoints
            ('GET', '/api/address/{id}'): 'Address',
            ('GET', '/api/address/isvalid'): 'AddressModel',
            ('POST', '/api/address/{addressId}/validated'): 'Address',

            # Contacts endpoints
            ('GET', '/api/contacts/{id}'): 'Contact',
            ('GET', '/api/contacts/search'): ['Contact'],
            ('POST', '/api/contacts'): 'Contact',
            ('PUT', '/api/contacts/{id}'): 'Contact',

            # Users endpoints
            ('GET', '/api/users/me'): 'UserAccessProfileModel',
            ('GET', '/api/users/{id}'): 'UserAccessProfileModel',

            # Account endpoints
            ('POST', '/api/account/login'): 'LoginModel',
            ('POST', '/api/account/changepassword'): 'ChangePasswordModel',
            ('POST', '/api/account/forgotpassword'): 'ForgotPasswordRequest',
            ('POST', '/api/account/resetpassword'): 'ResetPasswordRequest',

            # Add more mappings as needed...
        }

    def _ensure_models_rebuilt(self):
        """Ensure models are rebuilt to resolve forward references."""
        if not self._models_rebuilt:
            try:
                from ABConnect.api.models import rebuild_models
                rebuild_models()
                self._models_rebuilt = True
            except Exception as e:
                logger.warning(f"Failed to rebuild models: {e}")

    def _get_model_class(self, model_name: str) -> Optional[Type]:
        """Get a model class by name, with caching.

        Args:
            model_name: Name of the model class

        Returns:
            Model class or None if not found
        """
        if model_name in self._model_cache:
            return self._model_cache[model_name]

        try:
            # Ensure models are rebuilt
            self._ensure_models_rebuilt()

            # Try to import from models package
            from ABConnect.api import models
            model_class = getattr(models, model_name, None)

            if model_class:
                self._model_cache[model_name] = model_class
                return model_class

            # If not found, try individual module import
            # This handles cases where the model might not be in __init__.py
            module_map = {
                'Company': 'companies',
                'CompanyDetails': 'companies',
                'SearchCompanyResponse': 'companies',
                'Address': 'address',
                'AddressModel': 'address',
                'Contact': 'contacts',
                'UserAccessProfileModel': 'account',
                'LoginModel': 'account',
                'ChangePasswordModel': 'account',
                'ForgotPasswordRequest': 'account',
                'ResetPasswordRequest': 'account',
            }

            if model_name in module_map:
                module_name = module_map[model_name]
                module = importlib.import_module(
                    f'ABConnect.api.models.{module_name}'
                )
                model_class = getattr(module, model_name, None)
                if model_class:
                    self._model_cache[model_name] = model_class
                    return model_class

        except Exception as e:
            logger.warning(f"Failed to load model {model_name}: {e}")

        return None

    def _match_path(self, actual_path: str, pattern: str) -> bool:
        """Check if an actual path matches a pattern with placeholders.

        Args:
            actual_path: The actual API path (e.g., '/api/companies/123')
            pattern: The pattern with placeholders (e.g., '/api/companies/{id}')

        Returns:
            True if the path matches the pattern
        """
        # Split paths into segments
        actual_parts = actual_path.strip('/').split('/')
        pattern_parts = pattern.strip('/').split('/')

        # Must have same number of segments
        if len(actual_parts) != len(pattern_parts):
            return False

        # Check each segment
        for actual, pattern_part in zip(actual_parts, pattern_parts):
            # Skip placeholders
            if pattern_part.startswith('{') and pattern_part.endswith('}'):
                continue
            # Non-placeholder parts must match exactly
            if actual != pattern_part:
                return False

        return True

    def cast_response(
        self,
        response: Any,
        method: str,
        path: str,
        operation_id: Optional[str] = None
    ) -> Union[Any, Dict, list]:
        """Cast an API response to the appropriate Pydantic model.

        Args:
            response: The raw API response
            method: HTTP method (GET, POST, etc.)
            path: API path
            operation_id: Optional OpenAPI operation ID

        Returns:
            Cast model instance or original response if no mapping found
        """
        # Find matching endpoint pattern
        model_spec = None
        for (endpoint_method, endpoint_pattern), model_name in self.endpoint_mappings.items():
            if method.upper() == endpoint_method and self._match_path(path, endpoint_pattern):
                model_spec = model_name
                break

        if not model_spec:
            # No mapping found, return original response
            logger.debug(f"No model mapping for {method} {path}")
            return response

        # Handle list responses
        if isinstance(model_spec, list):
            model_name = model_spec[0]
            model_class = self._get_model_class(model_name)

            if model_class and isinstance(response, list):
                try:
                    # Cast each item in the list
                    return [model_class.model_validate(item) for item in response]
                except Exception as e:
                    logger.warning(f"Failed to cast list response to {model_name}: {e}")
                    return response
            return response

        # Handle single model responses
        model_class = self._get_model_class(model_spec)
        if model_class:
            try:
                return model_class.model_validate(response)
            except Exception as e:
                logger.warning(f"Failed to cast response to {model_spec}: {e}")
                return response

        return response


# Singleton instance
_mapper_instance: Optional[ResponseMapper] = None


def get_response_mapper() -> ResponseMapper:
    """Get the singleton ResponseMapper instance.

    Returns:
        The ResponseMapper instance
    """
    global _mapper_instance
    if _mapper_instance is None:
        _mapper_instance = ResponseMapper()
    return _mapper_instance