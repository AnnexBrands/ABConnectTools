"""Rfq API endpoints.

Auto-generated from swagger.json specification.
Provides type-safe access to rfq/* endpoints.
"""

from typing import Optional
from ABConnect.api.endpoints.base import BaseEndpoint


class RfqEndpoint(BaseEndpoint):
    """Rfq API endpoint operations.
    
    Handles all API operations for /api/rfq/* endpoints.
    Total endpoints: 7
    """
    
    api_path = "rfq"

    def get_get(self, rfqId: str) -> dict:
        """GET /api/rfq/{rfqId}
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{rfqId}"
        path = path.replace("{rfqId}", rfqId)
        kwargs = {}
        return self._make_request("GET", path, **kwargs)
    def post_accept(self, rfqId: str, data: dict = None) -> dict:
        """POST /api/rfq/{rfqId}/accept
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{rfqId}/accept"
        path = path.replace("{rfqId}", rfqId)
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def post_decline(self, rfqId: str) -> dict:
        """POST /api/rfq/{rfqId}/decline
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{rfqId}/decline"
        path = path.replace("{rfqId}", rfqId)
        kwargs = {}
        return self._make_request("POST", path, **kwargs)
    def post_cancel(self, rfqId: str) -> dict:
        """POST /api/rfq/{rfqId}/cancel
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{rfqId}/cancel"
        path = path.replace("{rfqId}", rfqId)
        kwargs = {}
        return self._make_request("POST", path, **kwargs)
    def post_acceptwinner(self, rfqId: str, final_amount: Optional[str] = None) -> dict:
        """POST /api/rfq/{rfqId}/acceptwinner
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{rfqId}/acceptwinner"
        path = path.replace("{rfqId}", rfqId)
        kwargs = {}
        params = {}
        if final_amount is not None:
            params["finalAmount"] = final_amount
        if params:
            kwargs["params"] = params
        return self._make_request("POST", path, **kwargs)
    def post_comment(self, rfqId: str, data: dict = None) -> dict:
        """POST /api/rfq/{rfqId}/comment
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{rfqId}/comment"
        path = path.replace("{rfqId}", rfqId)
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def get_forjob(self, jobId: str, company_id: Optional[str] = None) -> dict:
        """GET /api/rfq/forjob/{jobId}
        
        
        
        Returns:
            dict: API response data
        """
        path = "/forjob/{jobId}"
        path = path.replace("{jobId}", jobId)
        kwargs = {}
        params = {}
        if company_id is not None:
            params["companyId"] = company_id
        if params:
            kwargs["params"] = params
        return self._make_request("GET", path, **kwargs)
