"""Base endpoint class for Catalog API."""

from typing import Any, Dict, Optional


class BaseCatalogEndpoint:
    """Base class for Catalog API endpoints."""

    _handler = None
    api_path: str = ""  # e.g., "api/Catalog"

    def __init__(self):
        """Initialize endpoint instance."""
        if self._handler is None:
            raise RuntimeError(
                "Catalog request handler not set. "
                "Call BaseCatalogEndpoint.set_request_handler() first."
            )

    @classmethod
    def set_request_handler(cls, handler):
        """Set the HTTP request handler for all catalog endpoints.

        Args:
            handler: CatalogRequestHandler instance
        """
        cls._handler = handler

    def _make_request(
        self,
        method: str,
        path: str = "",
        **kwargs,
    ) -> Any:
        """Make HTTP request to the Catalog API.

        Args:
            method: HTTP method (GET, POST, PUT, DELETE)
            path: Additional path segment (appended to api_path)
            **kwargs: Additional arguments for the request

        Returns:
            API response data
        """
        # Build full path
        if path:
            full_path = f"{self.api_path}/{path.lstrip('/')}"
        else:
            full_path = self.api_path

        return self._handler.call(method, full_path, **kwargs)

    def _get(self, path: str = "", **kwargs) -> Any:
        """Make GET request."""
        return self._make_request("GET", path, **kwargs)

    def _post(self, path: str = "", **kwargs) -> Any:
        """Make POST request."""
        return self._make_request("POST", path, **kwargs)

    def _put(self, path: str = "", **kwargs) -> Any:
        """Make PUT request."""
        return self._make_request("PUT", path, **kwargs)

    def _delete(self, path: str = "", **kwargs) -> Any:
        """Make DELETE request."""
        return self._make_request("DELETE", path, **kwargs)
