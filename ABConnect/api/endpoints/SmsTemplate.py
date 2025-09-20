"""Smstemplate API endpoints.

Auto-generated from swagger.json specification.
Provides type-safe access to /api/SmsTemplate/* endpoints.
"""

from typing import Optional
from .base import BaseEndpoint


class SmstemplateEndpoint(BaseEndpoint):
    """Smstemplate API endpoint operations.
    
    Handles all API operations for /api/SmsTemplate/* endpoints.
    Total endpoints: 6
    """
    
    api_path = "/api/SmsTemplate"

    def get_notificationtokens(self) -> dict:
        """GET /api/SmsTemplate/notificationTokens
        
        
        
        Returns:
            dict: API response data
        """
        path = "/notificationTokens"
        return self._make_request("GET", path, **kwargs)
    def get_jobstatuses(self) -> dict:
        """GET /api/SmsTemplate/jobStatuses
        
        
        
        Returns:
            dict: API response data
        """
        path = "/jobStatuses"
        return self._make_request("GET", path, **kwargs)
    def get_list(self, company_id: Optional[str] = None) -> dict:
        """GET /api/SmsTemplate/list
        
        
        
        Returns:
            dict: API response data
        """
        path = "/list"
        kwargs = {}
        params = {}
        if company_id is not None:
            params["companyId"] = company_id
        if params:
            kwargs["params"] = params
        return self._make_request("GET", path, **kwargs)
    def get_get(self, templateId: str) -> dict:
        """GET /api/SmsTemplate/{templateId}
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{templateId}"
        path = path.replace("{templateId}", templateId)
        return self._make_request("GET", path, **kwargs)
    def delete_delete(self, templateId: str) -> dict:
        """DELETE /api/SmsTemplate/{templateId}
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{templateId}"
        path = path.replace("{templateId}", templateId)
        return self._make_request("DELETE", path, **kwargs)
    def post_save(self, data: dict = None) -> dict:
        """POST /api/SmsTemplate/save
        
        
        
        Returns:
            dict: API response data
        """
        path = "/save"
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
