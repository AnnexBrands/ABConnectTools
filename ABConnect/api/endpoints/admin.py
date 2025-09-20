"""Admin API endpoints.

Auto-generated from swagger.json specification.
Provides type-safe access to /api/admin/* endpoints.
"""

from typing import Optional
from .base import BaseEndpoint


class AdminEndpoint(BaseEndpoint):
    """Admin API endpoint operations.
    
    Handles all API operations for /api/admin/* endpoints.
    Total endpoints: 13
    """
    
    api_path = "/api/admin"

    def get_advancedsettings_all(self) -> dict:
        """GET /api/admin/advancedsettings/all
        
        
        
        Returns:
            dict: API response data
        """
        path = "/advancedsettings/all"
        return self._make_request("GET", path, **kwargs)
    def get_advancedsettings(self, id: str) -> dict:
        """GET /api/admin/advancedsettings/{id}
        
        
        
        Returns:
            dict: API response data
        """
        path = "/advancedsettings/{id}"
        path = path.replace("{id}", id)
        return self._make_request("GET", path, **kwargs)
    def delete_advancedsettings(self, id: str) -> dict:
        """DELETE /api/admin/advancedsettings/{id}
        
        
        
        Returns:
            dict: API response data
        """
        path = "/advancedsettings/{id}"
        path = path.replace("{id}", id)
        return self._make_request("DELETE", path, **kwargs)
    def post_advancedsettings(self, data: dict = None) -> dict:
        """POST /api/admin/advancedsettings
        
        
        
        Returns:
            dict: API response data
        """
        path = "/advancedsettings"
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def get_carriererrormessage_all(self) -> dict:
        """GET /api/admin/carriererrormessage/all
        
        
        
        Returns:
            dict: API response data
        """
        path = "/carriererrormessage/all"
        return self._make_request("GET", path, **kwargs)
    def post_carriererrormessage(self, data: dict = None) -> dict:
        """POST /api/admin/carriererrormessage
        
        
        
        Returns:
            dict: API response data
        """
        path = "/carriererrormessage"
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def get_globalsettings_companyhierarchy(self) -> dict:
        """GET /api/admin/globalsettings/companyhierarchy
        
        
        
        Returns:
            dict: API response data
        """
        path = "/globalsettings/companyhierarchy"
        return self._make_request("GET", path, **kwargs)
    def get_globalsettings_companyhierarchy_company(self, companyId: str) -> dict:
        """GET /api/admin/globalsettings/companyhierarchy/company/{companyId}
        
        
        
        Returns:
            dict: API response data
        """
        path = "/globalsettings/companyhierarchy/company/{companyId}"
        path = path.replace("{companyId}", companyId)
        return self._make_request("GET", path, **kwargs)
    def post_globalsettings_getinsuranceexceptions(self, data: dict = None) -> dict:
        """POST /api/admin/globalsettings/getinsuranceexceptions
        
        
        
        Returns:
            dict: API response data
        """
        path = "/globalsettings/getinsuranceexceptions"
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def post_globalsettings_approveinsuranceexception(self, job_id: Optional[str] = None) -> dict:
        """POST /api/admin/globalsettings/approveinsuranceexception
        
        
        
        Returns:
            dict: API response data
        """
        path = "/globalsettings/approveinsuranceexception"
        kwargs = {}
        params = {}
        if job_id is not None:
            params["JobId"] = job_id
        if params:
            kwargs["params"] = params
        return self._make_request("POST", path, **kwargs)
    def post_globalsettings_intacct(self, data: dict = None) -> dict:
        """POST /api/admin/globalsettings/intacct
        
        
        
        Returns:
            dict: API response data
        """
        path = "/globalsettings/intacct"
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def post_logbuffer_flush(self, data: dict = None) -> dict:
        """POST /api/admin/logbuffer/flush
        
        
        
        Returns:
            dict: API response data
        """
        path = "/logbuffer/flush"
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def post_logbuffer_flushall(self) -> dict:
        """POST /api/admin/logbuffer/flushAll
        
        
        
        Returns:
            dict: API response data
        """
        path = "/logbuffer/flushAll"
        return self._make_request("POST", path, **kwargs)
