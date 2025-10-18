"""Companies API endpoints.

Auto-generated from swagger.json specification.
Provides type-safe access to companies/* endpoints.
"""

from typing import List, Optional, Union
from .base import BaseEndpoint
from ..utils import resolve_company_identifier
from ..models.companies import (
    Company,
    CompanyDetails,
    SearchCompanyResponse,
    SearchCompanyDataSourceLoadOptions,
    SearchCompanyModel,
    TagBoxDataSourceLoadOptions,
    WebApiDataSourceLoadOptions,
    SaveGeoSettingModel,
    UpdateCarrierAccountsModel,
    PackagingLaborSettings,
    PackagingTariffSettings
)


class CompaniesEndpoint(BaseEndpoint):
    """Companies API endpoint operations.

    Handles all API operations for /api/companies/* endpoints.
    Total endpoints: 30
    """

    api_path = "companies"

    def get(self, code_or_id: str, details: str = "full", cast: bool = False, **kwargs) -> dict:
        """Convenience method to get company by code or ID.

        Args:
            code_or_id: Company code (e.g., '16023SC') or UUID
            details: Level of detail - 'short', 'full' (default), or 'details'
            cast: If True, cast response to Pydantic model
            **kwargs: Additional query parameters

        Returns:
            Company data as Pydantic model (if cast=True) or dict

        Examples:
            # Get by code with full details (default)
            company = api.companies.get('16023SC')

            # Get by ID with short details
            company = api.companies.get('23493e85-a92e-e711-9f52-00155d426802', details='short')

            # Get by code with specific details endpoint
            company = api.companies.get('16023SC', details='details')
        """
        # Use DRY helper to resolve company code/ID to UUID
        company_uuid = resolve_company_identifier(code_or_id, self)

        # Use appropriate endpoint based on detail level
        # Pass cast_response parameter to enable model casting
        kwargs['cast_response'] = cast

        if details == 'short':
            return self._make_request("GET", f"/{company_uuid}", **kwargs)
        elif details == 'details':
            return self._make_request("GET", f"/{company_uuid}/details", **kwargs)
        else:  # full
            return self._make_request("GET", f"/{company_uuid}/fulldetails", **kwargs)

    def get_get(self, id: str) -> dict:
        """GET /api/companies/{id}
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{id}"
        path = path.replace("{id}", id)
        kwargs = {}
        return self._make_request("GET", path, **kwargs)
    def get_details(self, companyId: str) -> dict:
        """GET /api/companies/{companyId}/details
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{companyId}/details"
        path = path.replace("{companyId}", companyId)
        kwargs = {}
        return self._make_request("GET", path, **kwargs)
    def get_availablebycurrentuser(self) -> dict:
        """GET /api/companies/availableByCurrentUser
        
        
        
        Returns:
            dict: API response data
        """
        path = "/availableByCurrentUser"
        kwargs = {}
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
    def post_search_v2(self, data: dict = None) -> List[dict]:
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
        kwargs = {}
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
    def get_search_carrier_accounts(self, current_company_id: Optional[str] = None, query: Optional[str] = None) -> dict:
        """GET /api/companies/search/carrier-accounts
        
        
        
        Returns:
            dict: API response data
        """
        path = "/search/carrier-accounts"
        kwargs = {}
        params = {}
        if current_company_id is not None:
            params["currentCompanyId"] = current_company_id
        if query is not None:
            params["query"] = query
        if params:
            kwargs["params"] = params
        return self._make_request("GET", path, **kwargs)
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
        kwargs = {}
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
        kwargs = {}
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
        kwargs = {}
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
        kwargs = {}
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
        kwargs = {}
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
        kwargs = {}
        return self._make_request("GET", path, **kwargs)
    def get_brands(self) -> dict:
        """GET /api/companies/brands
        
        
        
        Returns:
            dict: API response data
        """
        path = "/brands"
        kwargs = {}
        return self._make_request("GET", path, **kwargs)
    def get_brandstree(self) -> dict:
        """GET /api/companies/brandstree
        
        
        
        Returns:
            dict: API response data
        """
        path = "/brandstree"
        kwargs = {}
        return self._make_request("GET", path, **kwargs)
    def get_franchiseeaddresses(self, companyId: str) -> List[dict]:
        """GET /api/companies/{companyId}/franchiseeAddresses
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{companyId}/franchiseeAddresses"
        path = path.replace("{companyId}", companyId)
        kwargs = {}
        return self._make_request("GET", path, **kwargs)
