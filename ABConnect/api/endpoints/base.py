"""Enhanced base endpoint class for schema-first API endpoints.

This class provides the foundation for all API endpoint implementations,
maintaining request handler inheritance while adding type safety and
integration with auto-generated Pydantic models.
"""

from typing import Any, Optional
import requests
from ABConnect.config import get_config


class BaseEndpoint:
    """Enhanced base class for all API endpoints.

    Maintains request handler inheritance while adding support for
    type-safe operations with Pydantic models.
    """

    _r = None
    api_path: str = ""  # Relative path without /api/ prefix

    def __init__(self):
        """Initialize endpoint instance."""
        if self._r is None:
            raise RuntimeError(
                "Request handler not set. Call BaseEndpoint.set_request_handler() first."
            )

    @classmethod
    def set_request_handler(cls, handler):
        """Set the HTTP request handler for all endpoints.

        This class method sets the request handler that will be used by all
        endpoint instances. It should be called once during API client
        initialization.

        Args:
            handler: The HTTP request handler callable. Should accept
                (method, path, **kwargs) and return the API response.

        Example:
            >>> from ABConnect.api.http_client import RequestHandler
            >>> handler = RequestHandler(base_url='https://api.example.com')
            >>> BaseEndpoint.set_request_handler(handler)
        """
        cls._r = handler

    def _make_request(
        self,
        method: str,
        path: str,
        operation_id: Optional[str] = None,
        cast_response: bool = True,
        validate_request: bool = True,
        **kwargs,
    ):
        """Make HTTP request using the shared request handler.

        Args:
            method: HTTP method (GET, POST, PUT, DELETE, etc.)
            path: API path (will be prefixed with api_path if relative)
            operation_id: Optional swagger operation ID for response casting
            cast_response: Whether to cast response to Pydantic model
            validate_request: Whether to validate request data against Pydantic model.
                Defaults to True. Set to False to skip validation for edge cases.
            **kwargs: Additional arguments for the request

        Returns:
            API response data (cast to Pydantic model if available)

        Raises:
            pydantic.ValidationError: If validate_request=True and request data
                doesn't match the expected model schema
        """
        # Build relative path (RequestHandler will add base URL with /api/)
        if path.startswith("/"):
            # Remove leading slash for relative path
            path = path.lstrip("/")

        # Combine with api_path (without /api/ prefix)
        if self.api_path:
            full_path = f"{self.api_path.strip('/')}/{path}"
        else:
            full_path = path

        # Validate request data if present and validation is enabled
        if validate_request and 'json' in kwargs and kwargs['json'] is not None:
            kwargs['json'] = self._validate_request(
                kwargs['json'], method, f"/api/{full_path}"
            )

        # Make the API call
        response = self._r.call(method, full_path, **kwargs)

        # Cast response to Pydantic model if requested
        if cast_response:
            return self._cast_response(
                response, method, f"/api/api/{full_path}", operation_id
            )

        return response

    def _validate_request(
        self,
        data: Any,
        method: str,
        full_path: str,
    ) -> Any:
        """Validate request data against appropriate Pydantic model.

        Uses ABConnectBaseModel.check() for validation, which validates
        the data and returns it as a JSON-serializable dict with proper
        camelCase field aliases.

        Args:
            data: Raw request data (dict or list)
            method: HTTP method
            full_path: Full API path including /api/ prefix

        Returns:
            Validated and transformed data

        Raises:
            pydantic.ValidationError: If data doesn't match the model schema
        """
        try:
            from ..request_mapper import get_request_mapper

            mapper = get_request_mapper()
            return mapper.validate_request(data, method, full_path)
        except ImportError as e:
            # If request mapper not available, pass through unchanged
            import logging

            logging.debug(f"Failed to import request_mapper: {e}")
            return data

    def _cast_response(
        self,
        response: Any,
        method: str,
        full_path: str,
        operation_id: Optional[str] = None,
    ) -> dict:
        """Cast response to appropriate Pydantic model.

        Args:
            response: Raw API response
            method: HTTP method
            full_path: Full API path including /api/ prefix
            operation_id: Optional operation ID

        Returns:
            Typed model instance or original response
        """
        try:
            from ..response_mapper import get_response_mapper

            mapper = get_response_mapper()
            return mapper.cast_response(response, method, full_path, operation_id)
        except ImportError as e:
            # If response mapper not available, return raw response
            import logging

            logging.debug(f"Failed to import response_mapper: {e}")
            return response

    @staticmethod
    def get_cache(key: str) -> Optional[str]:
        """Get cached data from cache service.

        Args:
            key: Cache key to retrieve

        Returns:
            Cached value or None if not found
        """
        cache_url = "https://tasks.abconnect.co/cache/%s"
        headers = {"x-api-key": get_config("ABC_CLIENT_SECRET")}
        result = requests.get(cache_url % key, headers=headers).text
        if result:
            return result
        return None
