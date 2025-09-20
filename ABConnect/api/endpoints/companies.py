"""Companies API endpoints.

Auto-generated from swagger.json specification.
Provides type-safe access to /api/companies/* endpoints.
"""

from typing import Optional
from .base import BaseEndpoint


class CompaniesEndpoint(BaseEndpoint):
    """Companies API endpoint operations.
    
    Handles all API operations for /api/companies/* endpoints.
    Total endpoints: 29
    """
    
    api_path = "/api/companies"

    def get_get(self, id: str) -> dict:
        """GET /api/companies/{id}
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{id}"
        path = path.replace("{id}", id)
        return self._make_request("GET", path, **kwargs)
    def get_details(self, companyId: str) -> dict:
        """GET /api/companies/{companyId}/details
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{companyId}/details"
        path = path.replace("{companyId}", companyId)
        return self._make_request("GET", path, **kwargs)
    def get_availablebycurrentuser(self) -> dict:
        """GET /api/companies/availableByCurrentUser
        
        
        
        Returns:
            dict: API response data
        """
        path = "/availableByCurrentUser"
        return self._make_request("GET", path, **kwargs)
    def get_search(self, search_value: Optional[str] = None) -> dict:
        """GET /api/companies/search
        
        
        
        Returns:
            dict: API response data
        """
        path = "/search"
        kwargs = {}
        params = {}
        if search_value is not None:
            params["searchValue"] = search_value
        if params:
            kwargs["params"] = params
        return self._make_request("GET", path, **kwargs)
    def post_search_v2(self, data: dict = None) -> dict:
        """POST /api/companies/search/v2
        
        
        
        Returns:
            dict: API response data
        """
        path = "/search/v2"
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def post_list(self, data: dict = None) -> dict:
        """POST /api/companies/list
        
        
        
        Returns:
            dict: API response data
        """
        path = "/list"
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def post_simplelist(self, data: dict = None) -> dict:
        """POST /api/companies/simplelist
        
        
        
        Returns:
            dict: API response data
        """
        path = "/simplelist"
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def get_fulldetails(self, companyId: str) -> dict:
        """GET /api/companies/{companyId}/fulldetails
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{companyId}/fulldetails"
        path = path.replace("{companyId}", companyId)
        return self._make_request("GET", path, **kwargs)
    def put_fulldetails(self, companyId: str, data: dict = None) -> dict:
        """PUT /api/companies/{companyId}/fulldetails
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{companyId}/fulldetails"
        path = path.replace("{companyId}", companyId)
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("PUT", path, **kwargs)
    def post_fulldetails(self, data: dict = None) -> dict:
        """POST /api/companies/fulldetails
        
        
        
        Returns:
            dict: API response data
        """
        path = "/fulldetails"
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def get_infofromkey(self, key: Optional[str] = None) -> dict:
        """GET /api/companies/infoFromKey
        
        
        
        Returns:
            dict: API response data
        """
        path = "/infoFromKey"
        kwargs = {}
        params = {}
        if key is not None:
            params["key"] = key
        if params:
            kwargs["params"] = params
        return self._make_request("GET", path, **kwargs)
    def get_geosettings(self, companyId: str) -> dict:
        """GET /api/companies/{companyId}/geosettings
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{companyId}/geosettings"
        path = path.replace("{companyId}", companyId)
        return self._make_request("GET", path, **kwargs)
    def post_geosettings(self, companyId: str, data: dict = None) -> dict:
        """POST /api/companies/{companyId}/geosettings
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{companyId}/geosettings"
        path = path.replace("{companyId}", companyId)
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def get_geosettings(self, latitude: Optional[str] = None, longitude: Optional[str] = None, miles_radius: Optional[str] = None) -> dict:
        """GET /api/companies/geosettings
        
        
        
        Returns:
            dict: API response data
        """
        path = "/geosettings"
        kwargs = {}
        params = {}
        if latitude is not None:
            params["Latitude"] = latitude
        if longitude is not None:
            params["Longitude"] = longitude
        if miles_radius is not None:
            params["milesRadius"] = miles_radius
        if params:
            kwargs["params"] = params
        return self._make_request("GET", path, **kwargs)
    def post_filteredcustomers(self, data: dict = None) -> dict:
        """POST /api/companies/filteredCustomers
        
        
        
        Returns:
            dict: API response data
        """
        path = "/filteredCustomers"
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def get_carrieracounts(self, companyId: str) -> dict:
        """GET /api/companies/{companyId}/carrierAcounts
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{companyId}/carrierAcounts"
        path = path.replace("{companyId}", companyId)
        return self._make_request("GET", path, **kwargs)
    def post_carrieracounts(self, companyId: str, data: dict = None) -> dict:
        """POST /api/companies/{companyId}/carrierAcounts
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{companyId}/carrierAcounts"
        path = path.replace("{companyId}", companyId)
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def get_capabilities(self, companyId: str) -> dict:
        """GET /api/companies/{companyId}/capabilities
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{companyId}/capabilities"
        path = path.replace("{companyId}", companyId)
        return self._make_request("GET", path, **kwargs)
    def post_capabilities(self, companyId: str, data: dict = None) -> dict:
        """POST /api/companies/{companyId}/capabilities
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{companyId}/capabilities"
        path = path.replace("{companyId}", companyId)
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def get_packagingsettings(self, companyId: str) -> dict:
        """GET /api/companies/{companyId}/packagingsettings
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{companyId}/packagingsettings"
        path = path.replace("{companyId}", companyId)
        return self._make_request("GET", path, **kwargs)
    def post_packagingsettings(self, companyId: str, data: dict = None) -> dict:
        """POST /api/companies/{companyId}/packagingsettings
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{companyId}/packagingsettings"
        path = path.replace("{companyId}", companyId)
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def get_inheritedpackagingtariffs(self, companyId: str, inherit_from: Optional[str] = None) -> dict:
        """GET /api/companies/{companyId}/inheritedPackagingTariffs
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{companyId}/inheritedPackagingTariffs"
        path = path.replace("{companyId}", companyId)
        kwargs = {}
        params = {}
        if inherit_from is not None:
            params["inheritFrom"] = inherit_from
        if params:
            kwargs["params"] = params
        return self._make_request("GET", path, **kwargs)
    def get_packaginglabor(self, companyId: str) -> dict:
        """GET /api/companies/{companyId}/packaginglabor
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{companyId}/packaginglabor"
        path = path.replace("{companyId}", companyId)
        return self._make_request("GET", path, **kwargs)
    def post_packaginglabor(self, companyId: str, data: dict = None) -> dict:
        """POST /api/companies/{companyId}/packaginglabor
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{companyId}/packaginglabor"
        path = path.replace("{companyId}", companyId)
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def get_inheritedpackaginglabor(self, companyId: str, inherit_from: Optional[str] = None) -> dict:
        """GET /api/companies/{companyId}/inheritedpackaginglabor
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{companyId}/inheritedpackaginglabor"
        path = path.replace("{companyId}", companyId)
        kwargs = {}
        params = {}
        if inherit_from is not None:
            params["inheritFrom"] = inherit_from
        if params:
            kwargs["params"] = params
        return self._make_request("GET", path, **kwargs)
    def get_geoareacompanies(self) -> dict:
        """GET /api/companies/geoAreaCompanies
        
        
        
        Returns:
            dict: API response data
        """
        path = "/geoAreaCompanies"
        return self._make_request("GET", path, **kwargs)
    def get_brands(self) -> dict:
        """GET /api/companies/brands
        
        
        
        Returns:
            dict: API response data
        """
        path = "/brands"
        return self._make_request("GET", path, **kwargs)
    def get_brandstree(self) -> dict:
        """GET /api/companies/brandstree
        
        
        
        Returns:
            dict: API response data
        """
        path = "/brandstree"
        return self._make_request("GET", path, **kwargs)
    def get_franchiseeaddresses(self, companyId: str) -> dict:
        """GET /api/companies/{companyId}/franchiseeAddresses
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{companyId}/franchiseeAddresses"
        path = path.replace("{companyId}", companyId)
        return self._make_request("GET", path, **kwargs)
