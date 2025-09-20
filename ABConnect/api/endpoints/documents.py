"""Documents API endpoints.

Auto-generated from swagger.json specification.
Provides type-safe access to documents/* endpoints.
"""

from typing import Optional
from .base import BaseEndpoint


class DocumentsEndpoint(BaseEndpoint):
    """Documents API endpoint operations.
    
    Handles all API operations for /api/documents/* endpoints.
    Total endpoints: 6
    """
    
    api_path = "documents"

    def get_get_thumbnail(self, docPath: str) -> dict:
        """GET /api/documents/get/thumbnail/{docPath}
        
        
        
        Returns:
            dict: API response data
        """
        path = "/get/thumbnail/{docPath}"
        path = path.replace("{docPath}", docPath)
        kwargs = {}
        return self._make_request("GET", path, **kwargs)
    def get_get(self, docPath: str) -> dict:
        """GET /api/documents/get/{docPath}
        
        
        
        Returns:
            dict: API response data
        """
        path = "/get/{docPath}"
        path = path.replace("{docPath}", docPath)
        kwargs = {}
        return self._make_request("GET", path, **kwargs)
    def get_list(self, job_display_id: Optional[str] = None, item_id: Optional[str] = None, rfq_id: Optional[str] = None) -> dict:
        """GET /api/documents/list
        
        
        
        Returns:
            dict: API response data
        """
        path = "/list"
        kwargs = {}
        params = {}
        if job_display_id is not None:
            params["jobDisplayId"] = job_display_id
        if item_id is not None:
            params["itemId"] = item_id
        if rfq_id is not None:
            params["rfqId"] = rfq_id
        if params:
            kwargs["params"] = params
        return self._make_request("GET", path, **kwargs)
    def post_post(self, data: dict = None) -> dict:
        """POST /api/documents
        
        
        
        Returns:
            dict: API response data
        """
        path = "/"
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def put_update(self, docId: str, data: dict = None) -> dict:
        """PUT /api/documents/update/{docId}
        
        
        
        Returns:
            dict: API response data
        """
        path = "/update/{docId}"
        path = path.replace("{docId}", docId)
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("PUT", path, **kwargs)
    def put_hide(self, docId: str) -> dict:
        """PUT /api/documents/hide/{docId}
        
        
        
        Returns:
            dict: API response data
        """
        path = "/hide/{docId}"
        path = path.replace("{docId}", docId)
        kwargs = {}
        return self._make_request("PUT", path, **kwargs)
