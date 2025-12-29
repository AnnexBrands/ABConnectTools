"""Note API endpoints.

Auto-generated from swagger.json specification.
Provides type-safe access to note/* endpoints.
"""

from typing import List, Optional
from ABConnect.api.endpoints.base import BaseEndpoint


class NoteEndpoint(BaseEndpoint):
    """Note API endpoint operations.
    
    Handles all API operations for /api/note/* endpoints.
    Total endpoints: 4
    """
    
    api_path = "note"

    def get_get(self, category: Optional[str] = None, job_id: Optional[str] = None, contact_id: Optional[str] = None, company_id: Optional[str] = None) -> List[dict]:
        """GET /api/note
        
        
        
        Returns:
            dict: API response data
        """
        path = "/"
        kwargs = {}
        params = {}
        if category is not None:
            params["category"] = category
        if job_id is not None:
            params["jobId"] = job_id
        if contact_id is not None:
            params["contactId"] = contact_id
        if company_id is not None:
            params["companyId"] = company_id
        if params:
            kwargs["params"] = params
        return self._make_request("GET", path, **kwargs)
    def post_post(self, data: dict = None) -> dict:
        """POST /api/note
        
        
        
        Returns:
            dict: API response data
        """
        path = "/"
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def put_put(self, id: str, data: dict = None) -> dict:
        """PUT /api/note/{id}
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{id}"
        path = path.replace("{id}", id)
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("PUT", path, **kwargs)
    def get_suggestusers(self, search_key: str = None, job_franchisee_id: Optional[str] = None, company_id: Optional[str] = None) -> List[dict]:
        """GET /api/note/suggestUsers
        
        
        
        Returns:
            dict: API response data
        """
        path = "/suggestUsers"
        kwargs = {}
        params = {}
        if search_key is not None:
            params["SearchKey"] = search_key
        if job_franchisee_id is not None:
            params["JobFranchiseeId"] = job_franchisee_id
        if company_id is not None:
            params["CompanyId"] = company_id
        if params:
            kwargs["params"] = params
        return self._make_request("GET", path, **kwargs)
