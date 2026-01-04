"""Users API endpoints.

Auto-generated from swagger.json specification.
Provides type-safe access to users/* endpoints.
"""

from ABConnect.api.endpoints.base import BaseEndpoint
from ABConnect.api.routes import SCHEMA


class UsersEndpoint(BaseEndpoint):
    """Users API endpoint operations.

    Handles all API operations for /api/users/* endpoints.
    Total endpoints: 5
    """

    api_path = "users"
    routes = SCHEMA["USERS"]

    def post_list(self, data: dict = None) -> dict:
        """POST /api/users/list

        Returns:
            dict: API response data
        """
        route = self.routes['LIST']
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def post_user(self, data: dict = None) -> dict:
        """POST /api/users/user

        Returns:
            dict: API response data
        """
        route = self.routes['USER']
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def put_user(self, data: dict = None) -> dict:
        """PUT /api/users/user

        Returns:
            dict: API response data
        """
        route = self.routes['USER_UPDATE']
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def get_roles(self) -> dict:
        """GET /api/users/roles

        Returns:
            dict: API response data
        """
        route = self.routes['ROLES']
        return self._make_request(route)

    def get_pocusers(self) -> dict:
        """GET /api/users/pocusers

        Returns:
            dict: API response data
        """
        route = self.routes['POCUSERS']
        return self._make_request(route)
