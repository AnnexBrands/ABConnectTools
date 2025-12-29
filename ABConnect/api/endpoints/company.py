"""Company API endpoints.

Auto-generated from swagger.json specification.
Provides type-safe access to company/* endpoints.

New in API version 709:
- /api/company/{companyId}/gridsettings (migrated from /api/dashboard/gridsettings)
- /api/company/{companyId}/material (new feature)
"""

from typing import List, Optional, Dict, Any
from ABConnect.api.endpoints.base import BaseEndpoint


class CompanyEndpoint(BaseEndpoint):
    """Company API endpoint operations.

    Handles all API operations for /api/company/* endpoints.
    Total endpoints: 22 (16 original + 6 new in v709)
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

    # =========================================================================
    # New endpoints in API version 709
    # =========================================================================

    def get_gridsettings(
        self, companyId: str, dashboard_type: Optional[str] = None
    ) -> Dict[str, Any]:
        """GET /api/company/{companyId}/gridsettings

        Get grid settings for a company dashboard.

        .. versionadded:: 709
            Replaces deprecated /api/dashboard/gridsettings endpoint.

        Args:
            companyId: Company UUID
            dashboard_type: Optional dashboard type filter

        Returns:
            dict: Grid settings data
        """
        path = f"/{companyId}/gridsettings"
        kwargs: Dict[str, Any] = {}
        params: Dict[str, Any] = {}
        if dashboard_type is not None:
            params["dashboardType"] = dashboard_type
        if params:
            kwargs["params"] = params
        return self._make_request("GET", path, **kwargs)

    def post_gridsettings(self, companyId: str, data: dict = None) -> Dict[str, Any]:
        """POST /api/company/{companyId}/gridsettings

        Save grid settings for a company dashboard.

        .. versionadded:: 709
            Replaces deprecated /api/dashboard/gridsettings endpoint.

        Args:
            companyId: Company UUID
            data: Grid settings data to save

        Returns:
            dict: Save response
        """
        path = f"/{companyId}/gridsettings"
        kwargs: Dict[str, Any] = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)

    def get_material(self, companyId: str) -> List[Dict[str, Any]]:
        """GET /api/company/{companyId}/material

        Get list of materials for a company.

        .. versionadded:: 709

        Args:
            companyId: Company UUID

        Returns:
            list: List of company materials
        """
        path = f"/{companyId}/material"
        return self._make_request("GET", path)

    def post_material(self, companyId: str, data: dict = None) -> Dict[str, Any]:
        """POST /api/company/{companyId}/material

        Create a new material for a company.

        .. versionadded:: 709

        Args:
            companyId: Company UUID
            data: Material data (SaveCompanyMaterialModel)

        Returns:
            dict: Created material data
        """
        path = f"/{companyId}/material"
        kwargs: Dict[str, Any] = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)

    def put_material(
        self, companyId: str, materialId: str, data: dict = None
    ) -> Dict[str, Any]:
        """PUT /api/company/{companyId}/material/{materialId}

        Update an existing company material.

        .. versionadded:: 709

        Args:
            companyId: Company UUID
            materialId: Material UUID to update
            data: Updated material data (SaveCompanyMaterialModel)

        Returns:
            dict: Updated material data
        """
        path = f"/{companyId}/material/{materialId}"
        kwargs: Dict[str, Any] = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("PUT", path, **kwargs)

    def delete_material(self, companyId: str, materialId: str) -> Dict[str, Any]:
        """DELETE /api/company/{companyId}/material/{materialId}

        Delete a company material.

        .. versionadded:: 709

        Args:
            companyId: Company UUID
            materialId: Material UUID to delete

        Returns:
            dict: Deletion response
        """
        path = f"/{companyId}/material/{materialId}"
        return self._make_request("DELETE", path)
