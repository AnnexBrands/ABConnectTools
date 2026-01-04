"""Account API endpoints."""

from typing import Optional, Dict, Any

from ABConnect.api.endpoints.base import BaseEndpoint
from ABConnect.api.routes import SCHEMA


class AccountEndpoint(BaseEndpoint):
    """Used to manage user accounts, authentication, and profiles."""

    api_path = "account"
    routes = SCHEMA["ACCOUNT"]

    def post_register(self, data: dict = None) -> dict:
        """POST /api/account/register

        Returns:
            dict: API response data
        """
        route = self.routes["POST_REGISTER"]
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def post_sendconfirmation(self, data: dict = None) -> dict:
        """POST /api/account/sendConfirmation

        Returns:
            dict: API response data
        """
        route = self.routes["POST_SEND_CONFIRMATION"]
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def post_confirm(self, data: dict = None) -> dict:
        """POST /api/account/confirm

        Returns:
            dict: API response data
        """
        route = self.routes["POST_CONFIRM"]
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def post_forgot(self, data: dict = None) -> dict:
        """POST /api/account/forgot

        Initiate a forgot-username or forgot-password request.

        Returns:
            dict: API response data
        """
        route = self.routes["POST_FORGOT"]
        return self._make_request(route, json=data)

    def get_verifyresettoken(self, username: Optional[str] = None, token: Optional[str] = None) -> dict:
        """GET /api/account/verifyresettoken

        Returns:
            dict: API response data
        """
        route = self.routes["GET_VERIFYRESETTOKEN"]
        params = {}
        if username is not None:
            params["username"] = username
        if token is not None:
            params["token"] = token
        if params:
            route.params = params
        return self._make_request(route)

    def post_resetpassword(self, data: dict = None) -> dict:
        """POST /api/account/resetpassword

        Returns:
            dict: API response data
        """
        route = self.routes["POST_RESETPASSWORD"]
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def get_profile(self) -> Dict[str, Any]:
        """Get current user profile information.

        Returns:
            User profile with contact info, company details, and payment sources.
        """
        route = self.routes["GET_PROFILE"]
        return self._make_request(route)

    def post_setpassword(self, data: dict = None) -> dict:
        """POST /api/account/setpassword

        Returns:
            dict: API response data
        """
        route = self.routes["POST_SETPASSWORD"]
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def put_paymentsource(self, sourceId: str, data: dict = None) -> dict:
        """PUT /api/account/paymentsource/{sourceId}

        Returns:
            dict: API response data
        """
        route = self.routes["PUT_PAYMENTSOURCE"]
        route.params = {"sourceId": sourceId}
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def delete_paymentsource(self, sourceId: str) -> dict:
        """DELETE /api/account/paymentsource/{sourceId}

        Returns:
            dict: API response data
        """
        route = self.routes["DELETE_PAYMENTSOURCE"]
        route.params = {"sourceId": sourceId}
        return self._make_request(route)
