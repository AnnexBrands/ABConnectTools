"""Account API endpoints.

Auto-generated from swagger.json specification.
Provides type-safe access to account/* endpoints.
"""

from typing import Optional
from .base import BaseEndpoint


class AccountEndpoint(BaseEndpoint):
    """Account API endpoint operations.
    
    Handles all API operations for /api/account/* endpoints.
    Total endpoints: 10
    """
    
    api_path = "account"

    def post_register(self, data: dict = None) -> dict:
        """POST /api/account/register
        
        
        
        Returns:
            dict: API response data
        """
        path = "/register"
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
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
        """POST /api/account/forgot
        
        
        
        Returns:
            dict: API response data
        """
        path = "/forgot"
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
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
    def get_profile(self) -> dict:
        """GET /api/account/profile
        
        
        
        Returns:
            dict: API response data
        """
        path = "/profile"
        kwargs = {}
        return self._make_request("GET", path, **kwargs)
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
