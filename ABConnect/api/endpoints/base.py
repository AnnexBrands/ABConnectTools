"""Enhanced base endpoint class for schema-first API endpoints.

This class provides the foundation for all API endpoint implementations,
maintaining request handler inheritance while adding type safety and
integration with auto-generated Pydantic models.
"""

from ABConnect.config import get_config
from ABConnect.api.routes import Route
from ABConnect.api.request_mapper import get_request_mapper
from ABConnect.api.response_mapper import get_response_mapper

import requests
from typing import Any, Optional, TYPE_CHECKING, overload
import logging
logger = logging.getLogger(__name__)

if TYPE_CHECKING:
    from pydantic import BaseModel


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
        cls._r = handler

    def _make_request(
        self,
        method: str,
        path: str | Route,
        **kwargs,
    ):
        """Make HTTP request using the shared request handler.

        Supports both legacy (method, path) style and new Route-based style.

        Args:
            method: HTTP method (ignored if path is a Route)
            path: API path string or Route object
            operation_id: Optional swagger operation ID for response casting
            cast_response: Whether to cast response to Pydantic model
            validate_request: Whether to validate request data against Pydantic model
            **kwargs: Path parameters (for Route) or request options

        Returns:
            API response data (cast to Pydantic model if available)
        """
        if isinstance(path, Route):
            data = kwargs.get("json")
            if path.request_model:
                kwargs["json"] = self._validate_route(path, data)
                    
            response = self._r.call(
                path.method,
                path.url,
                **kwargs,
            )
            return self._cast_response(
                response, response_model=path.response_model
            )

        else:
            if path.startswith("/"):
                path = path.lstrip("/")

            if self.api_path:
                full_path = f"{self.api_path.strip('/')}/{path}"
            else:
                full_path = path

            if "json" in kwargs and kwargs["json"] is not None:
                kwargs["json"] = self._validate_request(
                    kwargs["json"], method, f"/api/{full_path}"
                )
        
            response = self._r.call(method, full_path, **kwargs)


            return self._cast_response(
                response, method, f"/api/api/{full_path}"
            )

    def _validate_route(self, route: Route, data: Any) -> Any:
        """Validate request data against Route's request model.

        Args:
            route: Route object
            data: Pydantic model or json

        Returns:
            validated json

        Raises:
            pydantic.ValidationError: If data doesn't match the model schema
        """
        mapper = get_request_mapper()
        data = mapper.check(data, route.request_model)
        return data
        

    def _validate_request(
        self,
        data: Any,
        method: str,
        full_path: str
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
            

            mapper = get_request_mapper()
            return mapper.validate_request(data, method, full_path)
        except ImportError as e:
            logger.error(f"Failed calling request model validate: {e}")
            return data

    def _cast_response(
        self,
        response: Any,
        method: Optional[str] = None,
        full_path: Optional[str] = None,
        response_model: Optional[str] = None,
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
        # Skip casting for binary responses
        if isinstance(response, bytes):
            return response

        try:
            mapper = get_response_mapper()

            if response_model:
                return mapper.cast_response(response, response_model=response_model)
            else:
                return mapper.cast_response(response, method=method, full_path=full_path)
        except ImportError as e:
            # If response mapper not available, return raw response
            logger.error(f"Failed to import response_mapper: {e}")
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
        upper_key = str(key).upper()
        result = requests.get(cache_url % upper_key, headers=headers).text
        if result:
            return result
        return None
