"""Views API endpoints.

Auto-generated from swagger.json specification.
Provides type-safe access to views/* endpoints.
"""

from ABConnect.api.endpoints.base import BaseEndpoint
from ABConnect.api.routes import SCHEMA


class ViewsEndpoint(BaseEndpoint):
    """Views API endpoint operations.

    Handles all API operations for /api/views/* endpoints.
    Total endpoints: 8
    """

    api_path = "views"
    routes = SCHEMA["VIEWS"]

    def get_all(self) -> dict:
        """GET /api/views/all

        Returns:
            dict: API response data
        """
        route = self.routes['ALL']
        return self._make_request(route)

    def get_get(self, viewId: str) -> dict:
        """GET /api/views/{viewId}

        Returns:
            dict: API response data
        """
        route = self.routes['GET']
        route.params = {"viewId": viewId}
        return self._make_request(route)

    def delete_delete(self, viewId: str) -> dict:
        """DELETE /api/views/{viewId}

        Returns:
            dict: API response data
        """
        route = self.routes['DELETE']
        route.params = {"viewId": viewId}
        return self._make_request(route)

    def get_accessinfo(self, viewId: str) -> dict:
        """GET /api/views/{viewId}/accessinfo

        Returns:
            dict: API response data
        """
        route = self.routes['ACCESSINFO']
        route.params = {"viewId": viewId}
        return self._make_request(route)

    def post_post(self, data: dict = None) -> dict:
        """POST /api/views

        Returns:
            dict: API response data
        """
        route = self.routes['POST']
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def put_access(self, viewId: str, data: dict = None) -> dict:
        """PUT /api/views/{viewId}/access

        Returns:
            dict: API response data
        """
        route = self.routes['PUT_ACCESS']
        route.params = {"viewId": viewId}
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def get_datasetsps(self) -> dict:
        """GET /api/views/datasetsps

        Returns:
            dict: API response data
        """
        route = self.routes['DATASETSPS']
        return self._make_request(route)

    def get_datasetsp(self, spName: str) -> dict:
        """GET /api/views/datasetsp/{spName}

        Returns:
            dict: API response data
        """
        route = self.routes['DATASETSP']
        route.params = {"spName": spName}
        return self._make_request(route)
