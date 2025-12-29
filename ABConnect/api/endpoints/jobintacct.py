"""Jobintacct API endpoints.

Auto-generated from swagger.json specification.
Provides type-safe access to jobintacct/* endpoints.
"""

from ABConnect.api.endpoints.base import BaseEndpoint


class JobintacctEndpoint(BaseEndpoint):
    """Jobintacct API endpoint operations.
    
    Handles all API operations for /api/jobintacct/* endpoints.
    Total endpoints: 5
    """
    
    api_path = "jobintacct"

    def get_get(self, jobDisplayId: str) -> dict:
        """GET /api/jobintacct/{jobDisplayId}
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        kwargs = {}
        return self._make_request("GET", path, **kwargs)
    def post_post(self, jobDisplayId: str, data: dict = None) -> dict:
        """POST /api/jobintacct/{jobDisplayId}
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def post_draft(self, jobDisplayId: str, data: dict = None) -> dict:
        """POST /api/jobintacct/{jobDisplayId}/draft
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/draft"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def delete_delete(self, jobDisplayId: str, franchiseeId: str) -> dict:
        """DELETE /api/jobintacct/{jobDisplayId}/{franchiseeId}
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/{franchiseeId}"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        path = path.replace("{franchiseeId}", franchiseeId)
        kwargs = {}
        return self._make_request("DELETE", path, **kwargs)
    def post_applyrebate(self, jobDisplayId: str, data: dict = None) -> dict:
        """POST /api/jobintacct/{jobDisplayId}/applyRebate
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/applyRebate"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
