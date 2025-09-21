"""Smstemplate API endpoints.

Auto-generated from swagger.json specification.
Provides type-safe access to SmsTemplate/* endpoints.
"""

from typing import Optional, Union
from .base import BaseEndpoint
from ..utils import resolve_company_id_param


class SmstemplateEndpoint(BaseEndpoint):
    """Smstemplate API endpoint operations.
    
    Handles all API operations for /api/SmsTemplate/* endpoints.
    Total endpoints: 6
    """
    
    api_path = "SmsTemplate"

    def get_notificationtokens(self) -> dict:
        """GET /api/SmsTemplate/notificationTokens
        
        
        
        Returns:
            dict: API response data
        """
        path = "/notificationTokens"
        kwargs = {}
        return self._make_request("GET", path, **kwargs)
    def get_jobstatuses(self) -> dict:
        """GET /api/SmsTemplate/jobStatuses
        
        
        
        Returns:
            dict: API response data
        """
        path = "/jobStatuses"
        kwargs = {}
        return self._make_request("GET", path, **kwargs)
    def get_list(self, company_id: Optional[str] = None) -> dict:
        """GET /api/SmsTemplate/list

        Raw API method - use list() convenience method instead.

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

    def list(self, company: Optional[Union[str, None]] = None) -> dict:
        """Get SMS templates for a company.

        Convenience method that accepts company code or ID.

        Args:
            company: Company code (e.g., 'LIVE') or UUID. If None, lists all accessible templates.

        Returns:
            List of SMS templates for the company

        Examples:
            # List templates by company code
            templates = api.sms_template.list('LIVE')

            # List templates by company UUID
            templates = api.sms_template.list('cf8085ed-b2f2-e611-9f52-00155d426802')

            # List all accessible templates
            templates = api.sms_template.list()
        """
        path = "/list"
        kwargs = {}

        # Resolve company parameter to companyId
        params = resolve_company_id_param(company, self)
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
        kwargs = {}
        return self._make_request("GET", path, **kwargs)
    def delete_delete(self, templateId: str) -> dict:
        """DELETE /api/SmsTemplate/{templateId}
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{templateId}"
        path = path.replace("{templateId}", templateId)
        kwargs = {}
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
