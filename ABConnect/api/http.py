import logging
import requests

logger = logging.getLogger(__name__)

class RequestHandler:
    def __init__(self, token_storage):
        self.base_url = "https://portal.abconnect.co/api/"
        self.token_storage = token_storage

    def call(self, method, path, *, params=None, data=None, json=None, headers=None):
            headers = headers or {}
            token = self.token_storage.get_token()
            if token:
                access_token = token.get("access_token")
                headers.setdefault("Authorization", f"Bearer {access_token}")
            else:
                logger.error("No token available. Please log in or refresh the token.")
                return None

            url = f"{self.base_url}{path}"
            logger.debug(f"{method.upper()} {url}")

            response = requests.request(
                method=method.upper(),
                url=url,
                headers=headers,
                params=params,
                data=data,
                json=json
            )

            if not response.ok:
                logger.error(
                    f"HTTP {response.status_code} {method.upper()} {path}\n"
                    f"Headers: {response.headers}\n"
                    f"Response: {response.text}"
                )
            return response
