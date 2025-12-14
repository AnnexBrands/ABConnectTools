"""Dashboard API endpoints.

Auto-generated from swagger.json specification.
Provides type-safe access to dashboard/* endpoints.

Note: Some endpoints were removed in API version 709:
- /api/dashboard/gridsettings -> Use /api/company/{companyId}/gridsettings
- /api/dashboard/incrementjobstatus -> Use /api/job/{jobDisplayId}/timeline/incrementjobstatus
- /api/dashboard/undoincrementjobstatus -> Use /api/job/{jobDisplayId}/timeline/undoincrementjobstatus
"""

import warnings
from typing import List, Optional
from .base import BaseEndpoint


class DashboardEndpoint(BaseEndpoint):
    """Dashboard API endpoint operations.
    
    Handles all API operations for /api/dashboard/* endpoints.
    Total endpoints: 13
    """
    
    api_path = "dashboard"

    def get_get(self, view_id: Optional[str] = None, company_id: Optional[str] = None) -> dict:
        """GET /api/dashboard
        
        
        
        Returns:
            dict: API response data
        """
        path = "/"
        kwargs = {}
        params = {}
        if view_id is not None:
            params["viewId"] = view_id
        if company_id is not None:
            params["companyId"] = company_id
        if params:
            kwargs["params"] = params
        return self._make_request("GET", path, **kwargs)
    def get_gridviewstate(self, id: str) -> dict:
        """GET /api/dashboard/gridviewstate/{id}
        
        
        
        Returns:
            dict: API response data
        """
        path = "/gridviewstate/{id}"
        path = path.replace("{id}", id)
        kwargs = {}
        return self._make_request("GET", path, **kwargs)
    def post_gridviewstate(self, id: str, data: dict = None) -> dict:
        """POST /api/dashboard/gridviewstate/{id}
        
        
        
        Returns:
            dict: API response data
        """
        path = "/gridviewstate/{id}"
        path = path.replace("{id}", id)
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def get_gridviews(self, company_id: Optional[str] = None) -> dict:
        """GET /api/dashboard/gridviews
        
        
        
        Returns:
            dict: API response data
        """
        path = "/gridviews"
        kwargs = {}
        params = {}
        if company_id is not None:
            params["companyId"] = company_id
        if params:
            kwargs["params"] = params
        return self._make_request("GET", path, **kwargs)
    def post_inbound(self, company_id: Optional[str] = None, data: dict = None) -> List[dict]:
        """POST /api/dashboard/inbound
        
        
        
        Returns:
            dict: API response data
        """
        path = "/inbound"
        kwargs = {}
        params = {}
        if company_id is not None:
            params["companyId"] = company_id
        if params:
            kwargs["params"] = params
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def post_recentestimates(self, company_id: Optional[str] = None, data: dict = None) -> List[dict]:
        """POST /api/dashboard/recentestimates
        
        
        
        Returns:
            dict: API response data
        """
        path = "/recentestimates"
        kwargs = {}
        params = {}
        if company_id is not None:
            params["companyId"] = company_id
        if params:
            kwargs["params"] = params
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def post_inhouse(self, company_id: Optional[str] = None, data: dict = None) -> List[dict]:
        """POST /api/dashboard/inhouse
        
        
        
        Returns:
            dict: API response data
        """
        path = "/inhouse"
        kwargs = {}
        params = {}
        if company_id is not None:
            params["companyId"] = company_id
        if params:
            kwargs["params"] = params
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def post_outbound(self, company_id: Optional[str] = None, data: dict = None) -> List[dict]:
        """POST /api/dashboard/outbound
        
        
        
        Returns:
            dict: API response data
        """
        path = "/outbound"
        kwargs = {}
        params = {}
        if company_id is not None:
            params["companyId"] = company_id
        if params:
            kwargs["params"] = params
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def post_local_deliveries(self, company_id: Optional[str] = None, data: dict = None) -> List[dict]:
        """POST /api/dashboard/local-deliveries
        
        
        
        Returns:
            dict: API response data
        """
        path = "/local-deliveries"
        kwargs = {}
        params = {}
        if company_id is not None:
            params["companyId"] = company_id
        if params:
            kwargs["params"] = params
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def post_incrementjobstatus(self, data: dict = None) -> dict:
        """POST /api/dashboard/incrementjobstatus

        .. deprecated:: 709
            This endpoint was removed in API version 709.
            Use :meth:`ABConnect.api.endpoints.jobs.timeline.JobTimelineEndpoint.post_incrementjobstatus`
            at ``/api/job/{jobDisplayId}/timeline/incrementjobstatus`` instead.

        Returns:
            dict: API response data
        """
        warnings.warn(
            "post_incrementjobstatus() is deprecated since API v709. "
            "Use api.jobs.timeline.post_incrementjobstatus(jobDisplayId, data) instead.",
            DeprecationWarning,
            stacklevel=2
        )
        path = "/incrementjobstatus"
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)

    def post_undoincrementjobstatus(self, data: dict = None) -> dict:
        """POST /api/dashboard/undoincrementjobstatus

        .. deprecated:: 709
            This endpoint was removed in API version 709.
            Use :meth:`ABConnect.api.endpoints.jobs.timeline.JobTimelineEndpoint.post_undoincrementjobstatus`
            at ``/api/job/{jobDisplayId}/timeline/undoincrementjobstatus`` instead.

        Returns:
            dict: API response data
        """
        warnings.warn(
            "post_undoincrementjobstatus() is deprecated since API v709. "
            "Use api.jobs.timeline.post_undoincrementjobstatus(jobDisplayId, data) instead.",
            DeprecationWarning,
            stacklevel=2
        )
        path = "/undoincrementjobstatus"
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)

    def get_gridsettings(self, company_id: Optional[str] = None, dashboard_type: Optional[str] = None) -> dict:
        """GET /api/dashboard/gridsettings

        .. deprecated:: 709
            This endpoint was removed in API version 709.
            Use :meth:`ABConnect.api.endpoints.company.CompanyEndpoint.get_gridsettings`
            at ``/api/company/{companyId}/gridsettings`` instead.

        Returns:
            dict: API response data
        """
        warnings.warn(
            "get_gridsettings() is deprecated since API v709. "
            "Use api.company.get_gridsettings(companyId) instead.",
            DeprecationWarning,
            stacklevel=2
        )
        path = "/gridsettings"
        kwargs = {}
        params = {}
        if company_id is not None:
            params["companyId"] = company_id
        if dashboard_type is not None:
            params["dashboardType"] = dashboard_type
        if params:
            kwargs["params"] = params
        return self._make_request("GET", path, **kwargs)

    def post_gridsettings(self, data: dict = None) -> dict:
        """POST /api/dashboard/gridsettings

        .. deprecated:: 709
            This endpoint was removed in API version 709.
            Use :meth:`ABConnect.api.endpoints.company.CompanyEndpoint.post_gridsettings`
            at ``/api/company/{companyId}/gridsettings`` instead.

        Returns:
            dict: API response data
        """
        warnings.warn(
            "post_gridsettings() is deprecated since API v709. "
            "Use api.company.post_gridsettings(companyId, data) instead.",
            DeprecationWarning,
            stacklevel=2
        )
        path = "/gridsettings"
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
