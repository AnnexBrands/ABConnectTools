"""HTTP client for Catalog API.

Uses the same identity token as ACPortal but connects to catalog-api.abconnect.co.
"""

import logging
import requests
from typing import Optional

from ABConnect.exceptions import RequestError, NotLoggedInError
from ABConnect.config import Config

logger = logging.getLogger(__name__)


class CatalogRequestHandler:
    """Handles HTTP requests to the Catalog API.

    Shares token storage with ACPortal API (same identity server).
    """

    def __init__(self, token_storage):
        """Initialize the catalog request handler.

        Args:
            token_storage: Token storage instance (shared with ACPortal)
        """
        self.base_url = Config.get_catalog_base_url()
        self.token_storage = token_storage

    def _get_auth_headers(self):
        """Get authorization headers using shared token."""
        headers = {}
        token = self.token_storage.get_token()
        if token:
            access_token = token.get("access_token")
            headers["Authorization"] = f"Bearer {access_token}"
            return headers
        else:
            raise NotLoggedInError("No access token found. Please log in first.")

    def _handle_response(self, response, raw=False, raise_for_status=True):
        """Process the API response."""
        if raw:
            return response
        if raise_for_status:
            self.raise_for_status(response)

        if response.status_code == 204:
            return None

        try:
            return response.json()
        except requests.exceptions.JSONDecodeError:
            logger.warning(
                f"Response was not valid JSON. Status: {response.status_code}. "
                f"Content: {response.text[:100]}..."
            )
            raise RequestError(
                response.status_code,
                "Response content was not valid JSON.",
                response=response,
            )

    def raise_for_status(self, response):
        """Raise an exception if the response indicates an error."""
        if not (200 <= response.status_code < 300):
            try:
                error_info = response.json()
                error_message = error_info.get("detail", error_info.get("message", response.text))
            except ValueError:
                error_message = response.text

            raise RequestError(response.status_code, error_message, response=response)

    def call(
        self,
        method: str,
        path: str,
        *,
        params: Optional[dict] = None,
        data: Optional[dict] = None,
        json: Optional[dict] = None,
        headers: Optional[dict] = None,
        raw: bool = False,
        raise_for_status: bool = True,
    ):
        """Make an HTTP request to the Catalog API.

        Args:
            method: HTTP method (GET, POST, PUT, DELETE)
            path: API path (e.g., 'api/Catalog')
            params: Query parameters
            data: Form data
            json: JSON body
            headers: Additional headers
            raw: Return raw response object
            raise_for_status: Raise exception on error status

        Returns:
            API response data (dict, list, or None)
        """
        request_headers = self._get_auth_headers()
        if headers:
            request_headers.update(headers)

        # Ensure path doesn't start with /
        path = path.lstrip('/')
        url = f"{self.base_url}{path}"
        logger.debug(f"Catalog API: {method.upper()} {url}")

        response = requests.request(
            method=method.upper(),
            url=url,
            headers=request_headers,
            params=params,
            data=data,
            json=json,
        )

        return self._handle_response(
            response, raw=raw, raise_for_status=raise_for_status
        )
