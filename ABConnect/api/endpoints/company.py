"""Company API endpoints.

Auto-generated from swagger.json specification.
Provides type-safe access to company/* endpoints.
"""

from typing import List, Optional
from .base import BaseEndpoint
# Model imports disabled
    # Model imports disabled


class CompanyEndpoint(BaseEndpoint):
    """Company API endpoint operations.
    
    Handles all API operations for /api/company/* endpoints.
    Total endpoints: 16
    """
    
    api_path = "company"

    def get_calendar(self, companyId: str, date: str) -> dict:
        """GET /api/company/{companyId}/calendar/{date}
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{companyId}/calendar/{date}"
        path = path.replace("{companyId}", companyId)
        path = path.replace("{date}", date)
        kwargs = {}
        return self._make_request("GET", path, **kwargs)
    def get_calendar_baseinfo(self, companyId: str, date: str) -> dict:
        """GET /api/company/{companyId}/calendar/{date}/baseinfo
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{companyId}/calendar/{date}/baseinfo"
        path = path.replace("{companyId}", companyId)
        path = path.replace("{date}", date)
        kwargs = {}
        return self._make_request("GET", path, **kwargs)
    def get_calendar_startofday(self, companyId: str, date: str) -> dict:
        """GET /api/company/{companyId}/calendar/{date}/startofday
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{companyId}/calendar/{date}/startofday"
        path = path.replace("{companyId}", companyId)
        path = path.replace("{date}", date)
        kwargs = {}
        return self._make_request("GET", path, **kwargs)
    def get_calendar_endofday(self, companyId: str, date: str) -> dict:
        """GET /api/company/{companyId}/calendar/{date}/endofday
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{companyId}/calendar/{date}/endofday"
        path = path.replace("{companyId}", companyId)
        path = path.replace("{date}", date)
        kwargs = {}
        return self._make_request("GET", path, **kwargs)
    def get_accounts_stripe_connecturl(self, companyId: str, return_uri: Optional[str] = None) -> dict:
        """GET /api/company/{companyId}/accounts/stripe/connecturl
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{companyId}/accounts/stripe/connecturl"
        path = path.replace("{companyId}", companyId)
        kwargs = {}
        params = {}
        if return_uri is not None:
            params["returnUri"] = return_uri
        if params:
            kwargs["params"] = params
        return self._make_request("GET", path, **kwargs)
    def post_accounts_stripe_completeconnection(self, companyId: str, data: dict = None) -> dict:
        """POST /api/company/{companyId}/accounts/stripe/completeconnection
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{companyId}/accounts/stripe/completeconnection"
        path = path.replace("{companyId}", companyId)
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def delete_accounts_stripe(self, companyId: str) -> dict:
        """DELETE /api/company/{companyId}/accounts/stripe
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{companyId}/accounts/stripe"
        path = path.replace("{companyId}", companyId)
        kwargs = {}
        return self._make_request("DELETE", path, **kwargs)
    def get_setupdata(self, companyId: str) -> dict:
        """GET /api/company/{companyId}/setupdata
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{companyId}/setupdata"
        path = path.replace("{companyId}", companyId)
        kwargs = {}
        return self._make_request("GET", path, **kwargs)
    def get_containerthicknessinches(self, companyId: str) -> List[dict]:
        """GET /api/company/{companyId}/containerthicknessinches
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{companyId}/containerthicknessinches"
        path = path.replace("{companyId}", companyId)
        kwargs = {}
        return self._make_request("GET", path, **kwargs)
    def post_containerthicknessinches(self, companyId: str, data: dict = None) -> dict:
        """POST /api/company/{companyId}/containerthicknessinches
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{companyId}/containerthicknessinches"
        path = path.replace("{companyId}", companyId)
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def delete_containerthicknessinches(self, companyId: str, container_id: Optional[str] = None) -> dict:
        """DELETE /api/company/{companyId}/containerthicknessinches
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{companyId}/containerthicknessinches"
        path = path.replace("{companyId}", companyId)
        kwargs = {}
        params = {}
        if container_id is not None:
            params["containerId"] = container_id
        if params:
            kwargs["params"] = params
        return self._make_request("DELETE", path, **kwargs)
    def get_planner(self, companyId: str) -> List[dict]:
        """GET /api/company/{companyId}/planner
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{companyId}/planner"
        path = path.replace("{companyId}", companyId)
        kwargs = {}
        return self._make_request("GET", path, **kwargs)
    def get_truck(self, companyId: str, only_own_trucks: Optional[str] = None) -> List[dict]:
        """GET /api/company/{companyId}/truck
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{companyId}/truck"
        path = path.replace("{companyId}", companyId)
        kwargs = {}
        params = {}
        if only_own_trucks is not None:
            params["onlyOwnTrucks"] = only_own_trucks
        if params:
            kwargs["params"] = params
        return self._make_request("GET", path, **kwargs)
    def post_truck(self, companyId: str, data: dict = None) -> dict:
        """POST /api/company/{companyId}/truck
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{companyId}/truck"
        path = path.replace("{companyId}", companyId)
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def put_truck(self, companyId: str, truckId: str, data: dict = None) -> dict:
        """PUT /api/company/{companyId}/truck/{truckId}
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{companyId}/truck/{truckId}"
        path = path.replace("{companyId}", companyId)
        path = path.replace("{truckId}", truckId)
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("PUT", path, **kwargs)
    def delete_truck(self, companyId: str, truckId: str) -> dict:
        """DELETE /api/company/{companyId}/truck/{truckId}
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{companyId}/truck/{truckId}"
        path = path.replace("{companyId}", companyId)
        path = path.replace("{truckId}", truckId)
        kwargs = {}
        return self._make_request("DELETE", path, **kwargs)
