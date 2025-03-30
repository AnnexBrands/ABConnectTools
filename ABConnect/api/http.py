import logging
import requests
from typing import BinaryIO, Mapping, Tuple, Union, Optional
from ABConnect.exceptions import RequestError, NotLoggedInError

logger = logging.getLogger(__name__)

RequestsFileSpecTuple = Tuple[
    Optional[str], BinaryIO, Optional[str]
]  # (filename, fileobj, content_type)
RequestsFiles = Mapping[str, Union[RequestsFileSpecTuple, BinaryIO]]


class RequestHandler:
    """Handles HTTP requests to the ABConnect API."""

    def __init__(self, token_storage):
        self.base_url = "https://portal.abconnect.co/api/"
        self.token_storage = token_storage

    def _get_auth_headers(self):
        """Helper method to get authorization headers."""
        headers = {}
        token = self.token_storage.get_token()
        if token:
            access_token = token.get("access_token")
            headers["Authorization"] = f"Bearer {access_token}"
            return headers
        else:
            raise NotLoggedInError("No access token found. Please log in first.")

    def _handle_response(self, response, raw=False, raise_for_status=True):
        """Helper method to process the response."""
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
                f"Response was not valid JSON. Status: {response.status_code}. Content: {response.text[:100]}..."
            )
            raise RequestError(
                response.status_code,
                "Response content was not valid JSON.",
                response=response,
            )

    def raise_for_status(self, response):
        """Raise an exception if the response status code indicates an error."""
        if not (200 <= response.status_code < 300):
            try:
                error_info = response.json()
                error_message = error_info.get("message", response.text)
            except ValueError:
                error_message = response.text

            raise RequestError(response.status_code, error_message, response=response)

    def call(
        self,
        method,
        path,
        *,
        params=None,
        data=None,
        json=None,
        headers=None,
        raw=False,
        raise_for_status=True,
    ):
        request_headers = self._get_auth_headers()
        if headers:
            request_headers.update(headers)

        url = f"{self.base_url}{path}"
        logger.debug(f"{method.upper()} {url}")

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

    def upload_file(
        self,
        path: str,
        files: RequestsFiles,
        *,
        data: Optional[dict] = None,
        params: Optional[dict] = None,
        headers: Optional[dict] = None,
        raw: bool = False,
        raise_for_status: bool = True,
    ):
        """Uploads a file to the specified API path using POST."""
        request_headers = self._get_auth_headers()
        if headers:
            request_headers.update(headers)

        url = f"{self.base_url}{path}"
        method = "POST"
        logger.debug(f"{method.upper()} {url} (File Upload)")

        response = requests.request(
            method=method,
            url=url,
            headers=request_headers,
            params=params,
            data=data,
            files=files,
        )

        return self._handle_response(response, raw, raise_for_status)
