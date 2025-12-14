"""Request mapper for validating API request data against Pydantic models.

This module provides mapping from API endpoints to their corresponding
Pydantic models, enabling automatic validation of request data before
sending to the API.
"""

from typing import Any, Dict, List, Optional, Type, Union
import importlib
import logging

logger = logging.getLogger(__name__)


class RequestMapper:
    """Maps and validates API request data using Pydantic models."""

    def __init__(self):
        """Initialize the request mapper with endpoint mappings."""
        self._model_cache: Dict[str, Type] = {}
        self._models_rebuilt = False

        # Load mappings from generated schema_mappings module
        from .schema_mappings import REQUEST_MAPPINGS
        self.endpoint_mappings = REQUEST_MAPPINGS

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

            logger.debug(f"Model {model_name} not found in models package")

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
        # Normalize paths
        actual_path = actual_path.rstrip('/')
        pattern = pattern.rstrip('/')

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
            # Non-placeholder parts must match exactly (case-insensitive for path segments)
            if actual.lower() != pattern_part.lower():
                return False

        return True

    def get_model_for_endpoint(
        self,
        method: str,
        path: str
    ) -> Optional[Type]:
        """Get the Pydantic model class for an endpoint.

        Args:
            method: HTTP method (GET, POST, etc.)
            path: API path

        Returns:
            Model class or None if no mapping found
        """
        method_upper = method.upper()

        # Find matching endpoint pattern
        for (endpoint_method, endpoint_pattern), model_name in self.endpoint_mappings.items():
            if method_upper == endpoint_method and self._match_path(path, endpoint_pattern):
                return self._get_model_class(model_name)

        return None

    def validate_request(
        self,
        data: Any,
        method: str,
        path: str
    ) -> Any:
        """Validate request data against the appropriate Pydantic model.

        Uses ABConnectBaseModel.check() for validation, which:
        - Validates data against the model schema
        - Returns JSON-serializable dict with camelCase aliases
        - Raises ValidationError if data doesn't match schema

        Args:
            data: The raw request data (dict or list)
            method: HTTP method (POST, PUT, etc.)
            path: API path

        Returns:
            Validated data as dict (transformed via model.check())

        Raises:
            pydantic.ValidationError: If data doesn't match the model schema
        """
        if data is None:
            return data

        # Find model for this endpoint
        model_class = self.get_model_for_endpoint(method, path)

        if not model_class:
            # No mapping found, pass through unchanged
            logger.debug(f"No request model mapping for {method} {path}")
            return data

        # Use the model's check() method for validation and transformation
        # This raises ValidationError on failure
        logger.debug(f"Validating {method} {path} request with {model_class.__name__}")
        return model_class.check(data)


# Singleton instance
_mapper_instance: Optional[RequestMapper] = None


def get_request_mapper() -> RequestMapper:
    """Get the singleton RequestMapper instance.

    Returns:
        The RequestMapper instance
    """
    global _mapper_instance
    if _mapper_instance is None:
        _mapper_instance = RequestMapper()
    return _mapper_instance
