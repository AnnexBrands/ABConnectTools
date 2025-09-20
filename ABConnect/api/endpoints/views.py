"""Views API endpoints.

Auto-generated from swagger.json specification.
Provides type-safe access to views/* endpoints.
"""

from .base import BaseEndpoint


class ViewsEndpoint(BaseEndpoint):
    """Views API endpoint operations.
    
    Handles all API operations for /api/views/* endpoints.
    Total endpoints: 8
    """
    
    api_path = "views"

    def get_all(self) -> dict:
        """GET /api/views/all
        
        
        
        Returns:
            dict: API response data
        """
        path = "/all"
        kwargs = {}
        return self._make_request("GET", path, **kwargs)
    def get_get(self, viewId: str) -> dict:
        """GET /api/views/{viewId}
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{viewId}"
        path = path.replace("{viewId}", viewId)
        kwargs = {}
        return self._make_request("GET", path, **kwargs)
    def delete_delete(self, viewId: str) -> dict:
        """DELETE /api/views/{viewId}
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{viewId}"
        path = path.replace("{viewId}", viewId)
        kwargs = {}
        return self._make_request("DELETE", path, **kwargs)
    def get_accessinfo(self, viewId: str) -> dict:
        """GET /api/views/{viewId}/accessinfo
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{viewId}/accessinfo"
        path = path.replace("{viewId}", viewId)
        kwargs = {}
        return self._make_request("GET", path, **kwargs)
    def post_post(self, data: dict = None) -> dict:
        """POST /api/views
        
        
        
        Returns:
            dict: API response data
        """
        path = "/"
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def put_access(self, viewId: str, data: dict = None) -> dict:
        """PUT /api/views/{viewId}/access
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{viewId}/access"
        path = path.replace("{viewId}", viewId)
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("PUT", path, **kwargs)
    def get_datasetsps(self) -> dict:
        """GET /api/views/datasetsps
        
        
        
        Returns:
            dict: API response data
        """
        path = "/datasetsps"
        kwargs = {}
        return self._make_request("GET", path, **kwargs)
    def get_datasetsp(self, spName: str) -> dict:
        """GET /api/views/datasetsp/{spName}
        
        
        
        Returns:
            dict: API response data
        """
        path = "/datasetsp/{spName}"
        path = path.replace("{spName}", spName)
        kwargs = {}
        return self._make_request("GET", path, **kwargs)
