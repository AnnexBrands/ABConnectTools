"""Enhanced base endpoint class for schema-first API endpoints.

This class provides the foundation for all API endpoint implementations,
maintaining request handler inheritance while adding type safety and
integration with auto-generated Pydantic models.
"""

from ABConnect.config import get_config
from ABConnect.api.routes import Route
from ABConnect.api import models

import re
import requests
from typing import Any, Optional, TYPE_CHECKING, Tuple
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

    def _validate_request(self, route: Route, kwargs: dict) -> None:
        if "json" not in kwargs:
            return
        
        data = kwargs["json"]
        if model := getattr(models, route.request_model, None) is None:
            raise ValueError(
                f"Endpoint {route.method} {route.path} received a JSON body "
                f"but no request_model is defined. Remove the json= argument "
                f"or define a request_model for this route."
            )
        kwargs["json"] = model.model_validate(data)

    def _parse_type_string(self, type_str: str) -> Tuple[bool, str]:
        """Parse a type string to detect List[...] wrapper.

        Args:
            type_str: Type string like 'DocumentDetails' or 'List[DocumentDetails]'

        Returns:
            Tuple of (is_list, inner_model_name)
        """
        # Match List[ModelName] pattern
        list_match = re.match(r'^List\[(\w+)\]$', type_str)
        if list_match:
            return (True, list_match.group(1))
        return (False, type_str)

    def _validate_response(self, response: requests.Response, response_model: Optional[str]) -> Any:
        """Validate and cast API response to Pydantic model if specified.

        Args:
            response: Raw HTTP response
            response_model: Response model name (required - errors should not pass silently)

        Returns:
            Cast model instance, bytes, or original response data

        Raises:
            ValueError: If response_model is None - all endpoints must define a response model
        """
        if response_model == "bytes":
            return response.content

        if response_model is None:
            raise ValueError("All endpoints must define a response_model.")

        is_list, model_name = self._parse_type_string(response_model)

        # Handle primitive types (str, int, etc.) - return as-is
        if model_name == "str":
            return response if not is_list else list(response)

        model_class = getattr(models, model_name)

        if is_list:
            return [model_class.model_validate(item) for item in response]
        else:
            return model_class.model_validate(response)

    def _make_request(self, route: Route, **kwargs):
        """Make HTTP request using the shared request handler.


        Args:
            route: Route object defining the API endpoint
            **kwargs: Path parameters (for Route) or request options

        Returns:
            API response data (cast to Pydantic model if available)
        """
        self._validate_request(route, kwargs)
            
        if route.params:
            kwargs["params"] = route.params

        response = self._r.call(
            route.method,
            route.url,
            **kwargs,
        )
        return self._validate_response(
            response, response_model=route.response_model
        )


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
