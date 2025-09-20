"""Users API endpoints.

Auto-generated from swagger.json specification.
Provides type-safe access to users/* endpoints.
"""

from .base import BaseEndpoint


class UsersEndpoint(BaseEndpoint):
    """Users API endpoint operations.
    
    Handles all API operations for /api/users/* endpoints.
    Total endpoints: 5
    """
    
    api_path = "users"

    def post_list(self, data: dict = None) -> dict:
        """POST /api/users/list
        
        
        
        Returns:
            dict: API response data
        """
        path = "/list"
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def post_user(self, data: dict = None) -> dict:
        """POST /api/users/user
        
        
        
        Returns:
            dict: API response data
        """
        path = "/user"
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def put_user(self, data: dict = None) -> dict:
        """PUT /api/users/user
        
        
        
        Returns:
            dict: API response data
        """
        path = "/user"
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("PUT", path, **kwargs)
    def get_roles(self) -> dict:
        """GET /api/users/roles
        
        
        
        Returns:
            dict: API response data
        """
        path = "/roles"
        kwargs = {}
        return self._make_request("GET", path, **kwargs)
    def get_pocusers(self) -> dict:
        """GET /api/users/pocusers
        
        
        
        Returns:
            dict: API response data
        """
        path = "/pocusers"
        kwargs = {}
        return self._make_request("GET", path, **kwargs)
