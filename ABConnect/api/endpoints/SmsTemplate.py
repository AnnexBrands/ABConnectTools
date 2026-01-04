"""Smstemplate API endpoints.

Auto-generated from swagger.json specification.
Provides type-safe access to SmsTemplate/* endpoints.
"""

from typing import List, Optional, Union
from ABConnect.api.endpoints.base import BaseEndpoint
from ABConnect.api.routes import SCHEMA


class SmstemplateEndpoint(BaseEndpoint):
    """Smstemplate API endpoint operations.

    Handles all API operations for /api/SmsTemplate/* endpoints.
    Total endpoints: 6
    """

    api_path = "SmsTemplate"
    routes = SCHEMA["SMSTEMPLATE"]

    def get_notificationtokens(self) -> dict:
        """GET /api/SmsTemplate/notificationTokens

        Returns available notification tokens for SMS templates.

        Returns:
            dict: Notification tokens
        """
        route = self.routes['NOTIFICATION_TOKENS']
        return self._make_request(route)

    def get_jobstatuses(self) -> dict:
        """GET /api/SmsTemplate/jobStatuses

        Returns available job statuses for SMS templates.

        Returns:
            dict: Job statuses
        """
        route = self.routes['JOB_STATUSES']
        return self._make_request(route)

    def get_list(self, company_id: Optional[str] = None) -> List[dict]:
        """GET /api/SmsTemplate/list

        Returns SMS templates, optionally filtered by company.

        Args:
            company_id: Optional company ID filter

        Returns:
            List[dict]: List of SMS templates
        """
        route = self.routes['LIST']
        if company_id is not None:
            route.params = {"companyId": company_id}
        return self._make_request(route)

    def list(self, company: Optional[Union[str, None]] = None) -> List[dict]:
        """Get SMS templates for a company.

        Convenience method that accepts company code or ID.

        Args:
            company: Company code (e.g., 'LIVE') or UUID. If None, lists all accessible templates.

        Returns:
            List of SMS templates for the company
        """
        route = self.routes['LIST']
        if company:
            route.params = {"companyId": self.get_cache(company)}
        return self._make_request(route)

    def get_get(self, templateId: str) -> dict:
        """GET /api/SmsTemplate/{templateId}

        Returns:
            dict: API response data
        """
        route = self.routes['GET']
        route.params = {"templateId": templateId}
        return self._make_request(route)

    def delete_delete(self, templateId: str) -> dict:
        """DELETE /api/SmsTemplate/{templateId}

        Returns:
            dict: API response data
        """
        route = self.routes['DELETE']
        route.params = {"templateId": templateId}
        return self._make_request(route)

    def post_save(self, data: dict = None) -> dict:
        """POST /api/SmsTemplate/save

        Returns:
            dict: API response data
        """
        route = self.routes['SAVE']
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)
