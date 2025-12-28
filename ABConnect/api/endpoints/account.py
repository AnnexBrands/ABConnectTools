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
        route = self.routes["register"]
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route.method, route, **kwargs)
    def post_sendconfirmation(self, data: dict = None) -> dict:
        """POST /api/account/sendConfirmation
        
        
        
        Returns:
            dict: API response data
        """
        path = "/sendConfirmation"
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def post_confirm(self, data: dict = None) -> dict:
        """POST /api/account/confirm
        
        
        
        Returns:
            dict: API response data
        """
        path = "/confirm"
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def post_forgot(self, data: dict = None) -> dict:
        """
            Initiate a forgot-username or forgot-password request.

            Sends a recovery request to the server, which will trigger either a username reminder
            email or a password-reset link, depending on the value of ``forgot_type``.

            Parameters
            ----------
            request_model : ForgotLoginModel
                The payload containing the user's identifier and the type of recovery requested.
                
                Required fields depend on the recovery type:
                - For ``ForgotType.USERNAME``: ``email`` is typically required.
                - For ``ForgotType.PASSWORD``: ``user_name`` is typically required.
                
                Example::
                
                    ForgotLoginModel(
                        user_name="training",
                        email="abconnect@annexbrands.com",
                        forgot_type=ForgotType.USERNAME
                    )

            Returns
            -------
            ServiceBaseResponse
                Standardized API response wrapper containing:
                - ``success``: bool indicating whether the request was accepted
                - ``message``: str with a human-readable status or error description
                - ``data``: optional additional payload (often None for this endpoint)
                - ``errors``: optional list of validation or server errors

                On success, a recovery email/link is queued for delivery.

            Raises
            ------
            API-specific exceptions
                May raise network, timeout, validation, or server-error exceptions depending
                on the underlying ``abapi`` client implementation.

            Examples
            --------
            >>> request = ForgotLoginModel(
            ...     user_name="training",
            ...     email="abconnect@annexbrands.com",
            ...     forgot_type=ForgotType.USERNAME
            ... )
            >>> response = abapi.account.post_forgot(request)
            >>> print(response.success)   # True if the request was processed
            >>> print(response.message)   # e.g., "Username recovery email sent"
        """
        route = self.routes["POST_FORGOT"]
        return self._make_request(route.method, route, json=data)
    def get_verifyresettoken(self, username: Optional[str] = None, token: Optional[str] = None) -> dict:
        """GET /api/account/verifyresettoken
        
        
        
        Returns:
            dict: API response data
        """
        path = "/verifyresettoken"
        kwargs = {}
        params = {}
        if username is not None:
            params["username"] = username
        if token is not None:
            params["token"] = token
        if params:
            kwargs["params"] = params
        return self._make_request("GET", path, **kwargs)
    def post_resetpassword(self, data: dict = None) -> dict:
        """POST /api/account/resetpassword
        
        
        
        Returns:
            dict: API response data
        """
        path = "/resetpassword"
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def get_profile(self) -> Dict[str, Any]:
        """Get current user profile information.
        
        Returns:
            User profile with contact info, company details, and payment sources.
        """
        return self._make_request("GET", "profile")
    def post_setpassword(self, data: dict = None) -> dict:
        """POST /api/account/setpassword
        
        
        
        Returns:
            dict: API response data
        """
        path = "/setpassword"
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def put_paymentsource(self, sourceId: str, data: dict = None) -> dict:
        """PUT /api/account/paymentsource/{sourceId}
        
        
        
        Returns:
            dict: API response data
        """
        path = "/paymentsource/{sourceId}"
        path = path.replace("{sourceId}", sourceId)
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("PUT", path, **kwargs)
    def delete_paymentsource(self, sourceId: str) -> dict:
        """DELETE /api/account/paymentsource/{sourceId}
        
        
        
        Returns:
            dict: API response data
        """
        path = "/paymentsource/{sourceId}"
        path = path.replace("{sourceId}", sourceId)
        kwargs = {}
        return self._make_request("DELETE", path, **kwargs)
