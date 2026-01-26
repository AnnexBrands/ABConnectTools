"""Companies API endpoints.

Auto-generated from swagger.json specification.
Provides type-safe access to companies/* endpoints.
"""

from typing import List, Optional, Union
from ABConnect.api.endpoints.base import BaseEndpoint
from ABConnect.api import models
from ABConnect.api.models import (
    CompanySimple,
    CompanyDetails,
    CompanyInfo,
    CompanyAddressInfo,
    CompanyBrandTreeNode,
    CompanyGeoAreaCompanies,
    SearchCompanyResponse,
    SaveGeoSettingModel,
    PackagingTariffSettings,
    PackagingLaborSettings,
    FranchiseeCarrierAccounts,
    CarrierAccountInfo,
    ServiceBaseResponse,
)
from ABConnect.api.models.enums import CommercialCapabilities
from ABConnect.api.routes import SCHEMA


import logging
logger = logging.getLogger(__name__)

class CompaniesEndpoint(BaseEndpoint):
    """Companies API endpoint operations.

    Handles all API operations for /api/companies/* endpoints.
    Total endpoints: 30
    """

    api_path = "companies"
    routes = SCHEMA["COMPANIES"]

    def get(
        self, code_or_id: str, details: str = "full", **kwargs
    ) -> Union[CompanySimple, CompanyDetails]:
        """Convenience method to get company by code or ID.

        Args:
            code_or_id: Company code (e.g., '16023SC') or UUID
            details: Level of detail - 'short', 'full' (default), or 'details'
            **kwargs: Additional query parameters

        Returns:
            CompanySimple (if details='short') or CompanyDetails (if details='full' or 'details')
        """
        logger.info("Fetching company with code or ID: %s", code_or_id)
        company_uuid = self.get_cache(code_or_id)

        if details == "short":
            route = self.routes['GET']
            route.params = {"id": company_uuid}
            return self._make_request(route, **kwargs)
        elif details == "details":
            route = self.routes['GET_DETAILS']
            route.params = {"companyId": company_uuid}
            return self._make_request(route, **kwargs)
        else:  # full
            route = self.routes['GET_FULLDETAILS']
            route.params = {"companyId": company_uuid}
            return self._make_request(route, **kwargs)

    def get_by_id(self, id: str) -> CompanySimple:
        """GET /api/companies/{id}

        Retrieves company by ID.

        Args:
            id: Company ID (GUID string)

        Returns:
            CompanySimple: Typed company model
        """
        route = self.routes['GET']
        route.params = {"id": id}
        return self._make_request(route)

    def get_details(self, companyId: str) -> CompanyDetails:
        """GET /api/companies/{companyId}/details

        Returns:
            CompanyDetails: Company details model
        """
        route = self.routes['GET_DETAILS']
        route.params = {"companyId": companyId}
        return self._make_request(route)

    def get_availablebycurrentuser(self) -> List[CompanySimple]:
        """GET /api/companies/availableByCurrentUser

        Returns companies available to the current user.

        Returns:
            List[CompanySimple]: List of CompanySimple objects
        """
        route = self.routes['GET_AVAILABLE_BY_CURRENT_USER']
        return self._make_request(route)

    def get_search(self, search_value: Optional[str] = None) -> List[SearchCompanyResponse]:
        """GET /api/companies/search

        Search for companies by value.

        Args:
            search_value: Optional search term

        Returns:
            List[SearchCompanyResponse]: List of matching companies
        """
        route = self.routes['GET_SEARCH']
        if search_value is not None:
            route.params = {"searchValue": search_value}
        return self._make_request(route)

    def post_search_v2(self, data: dict = None) -> List[SearchCompanyResponse]:
        """POST /api/companies/search/v2

        Returns:
            List[SearchCompanyResponse]: List of matching companies
        """
        route = self.routes['POST_SEARCH_V2']
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def post_list(self, data: dict = None) -> ServiceBaseResponse:
        """POST /api/companies/list

        Returns:
            ServiceBaseResponse: API response
        """
        route = self.routes['POST_LIST']
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def post_simplelist(self, data: dict = None) -> ServiceBaseResponse:
        """POST /api/companies/simplelist

        Returns:
            ServiceBaseResponse: API response
        """
        route = self.routes['POST_SIMPLELIST']
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def get_fulldetails(self, companyId: str) -> CompanyDetails:
        """GET /api/companies/{companyId}/fulldetails

        Returns:
            CompanyDetails: Full company details
        """
        route = self.routes['GET_FULLDETAILS']
        route.params = {"companyId": companyId}
        return self._make_request(route)

    def put_fulldetails(self, companyId: str, data: dict = None) -> CompanyDetails:
        """PUT /api/companies/{companyId}/fulldetails

        Returns:
            CompanyDetails: Updated company details
        """
        route = self.routes['PUT_FULLDETAILS']
        route.params = {"companyId": companyId}
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def get_search_carrier_accounts(
        self, current_company_id: Optional[str] = None, query: Optional[str] = None
    ) -> List[CarrierAccountInfo]:
        """GET /api/companies/search/carrier-accounts

        Search for carrier accounts.

        Args:
            current_company_id: Optional company ID filter
            query: Optional search query

        Returns:
            List[CarrierAccountInfo]: List of carrier account info
        """
        route = self.routes['GET_SEARCH_CARRIER_ACCOUNTS']
        params = {}
        if current_company_id is not None:
            params["currentCompanyId"] = current_company_id
        if query is not None:
            params["query"] = query
        if params:
            route.params = params
        return self._make_request(route)

    def post_fulldetails(self, data: dict = None) -> ServiceBaseResponse:
        """POST /api/companies/fulldetails

        Returns:
            ServiceBaseResponse: API response
        """
        route = self.routes['POST_FULLDETAILS']
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def get_infofromkey(self, key: Optional[str] = None) -> CompanyInfo:
        """GET /api/companies/infoFromKey

        Returns:
            CompanyInfo: Company info from key
        """
        route = self.routes['GET_INFO_FROM_KEY']
        if key is not None:
            route.params = {"key": key}
        return self._make_request(route)

    def get_geosettings(self, companyId: str) -> List[SaveGeoSettingModel]:
        """GET /api/companies/{companyId}/geosettings

        Returns:
            List[SaveGeoSettingModel]: Geo settings for the company
        """
        route = self.routes['GET_COMPANY_GEOSETTINGS']
        route.params = {"companyId": companyId}
        return self._make_request(route)

    def post_geosettings(self, companyId: str, data: dict = None) -> ServiceBaseResponse:
        """POST /api/companies/{companyId}/geosettings

        Returns:
            ServiceBaseResponse: API response
        """
        route = self.routes['POST_GEOSETTINGS']
        route.params = {"companyId": companyId}
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def get_geosettings_search(
        self,
        latitude: Optional[str] = None,
        longitude: Optional[str] = None,
        miles_radius: Optional[str] = None,
    ) -> List[SaveGeoSettingModel]:
        """GET /api/companies/geosettings

        Search for geo settings by location.

        Args:
            latitude: Optional latitude
            longitude: Optional longitude
            miles_radius: Optional radius in miles

        Returns:
            List[SaveGeoSettingModel]: List of geo settings
        """
        route = self.routes['GET_GEOSETTINGS']
        params = {}
        if latitude is not None:
            params["Latitude"] = latitude
        if longitude is not None:
            params["Longitude"] = longitude
        if miles_radius is not None:
            params["milesRadius"] = miles_radius
        if params:
            route.params = params
        return self._make_request(route)

    def post_filteredcustomers(self, data: dict = None) -> ServiceBaseResponse:
        """POST /api/companies/filteredCustomers

        Returns:
            ServiceBaseResponse: API response
        """
        route = self.routes['POST_FILTERED_CUSTOMERS']
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def get_carrieracounts(self, companyId: str) -> FranchiseeCarrierAccounts:
        """GET /api/companies/{companyId}/carrierAcounts

        Returns:
            FranchiseeCarrierAccounts: Carrier account information
        """
        route = self.routes['GET_CARRIER_ACOUNTS']
        route.params = {"companyId": companyId}
        return self._make_request(route)

    def post_carrieracounts(self, companyId: str, data: dict = None) -> ServiceBaseResponse:
        """POST /api/companies/{companyId}/carrierAcounts

        Returns:
            ServiceBaseResponse: API response
        """
        route = self.routes['POST_CARRIER_ACOUNTS']
        route.params = {"companyId": companyId}
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def get_capabilities(self, companyId: str) -> CommercialCapabilities:
        """GET /api/companies/{companyId}/capabilities

        Returns:
            CommercialCapabilities: Company commercial capabilities
        """
        route = self.routes['GET_CAPABILITIES']
        route.params = {"companyId": companyId}
        return self._make_request(route)

    def post_capabilities(self, companyId: str, data: dict = None) -> ServiceBaseResponse:
        """POST /api/companies/{companyId}/capabilities

        Returns:
            ServiceBaseResponse: API response
        """
        route = self.routes['POST_CAPABILITIES']
        route.params = {"companyId": companyId}
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def get_packagingsettings(self, companyId: str) -> PackagingTariffSettings:
        """GET /api/companies/{companyId}/packagingsettings

        Returns:
            PackagingTariffSettings: Packaging tariff settings
        """
        route = self.routes['GET_PACKAGINGSETTINGS']
        route.params = {"companyId": companyId}
        return self._make_request(route)

    def post_packagingsettings(self, companyId: str, data: dict = None) -> ServiceBaseResponse:
        """POST /api/companies/{companyId}/packagingsettings

        Returns:
            ServiceBaseResponse: API response
        """
        route = self.routes['POST_PACKAGINGSETTINGS']
        route.params = {"companyId": companyId}
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def get_inheritedpackagingtariffs(
        self, companyId: str, inherit_from: Optional[str] = None
    ) -> PackagingTariffSettings:
        """GET /api/companies/{companyId}/inheritedPackagingTariffs

        Returns:
            PackagingTariffSettings: Inherited packaging tariff settings
        """
        route = self.routes['GET_INHERITED_PACKAGING_TARIFFS']
        route.params = {"companyId": companyId}
        if inherit_from is not None:
            route.params["inheritFrom"] = inherit_from
        return self._make_request(route)

    def get_packaginglabor(self, companyId: str) -> PackagingLaborSettings:
        """GET /api/companies/{companyId}/packaginglabor

        Returns:
            PackagingLaborSettings: Packaging labor settings
        """
        route = self.routes['GET_PACKAGINGLABOR']
        route.params = {"companyId": companyId}
        return self._make_request(route)

    def post_packaginglabor(self, companyId: str, data: dict = None) -> ServiceBaseResponse:
        """POST /api/companies/{companyId}/packaginglabor

        Returns:
            ServiceBaseResponse: API response
        """
        route = self.routes['POST_PACKAGINGLABOR']
        route.params = {"companyId": companyId}
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def get_inheritedpackaginglabor(
        self, companyId: str, inherit_from: Optional[str] = None
    ) -> PackagingLaborSettings:
        """GET /api/companies/{companyId}/inheritedpackaginglabor

        Returns:
            PackagingLaborSettings: Inherited packaging labor settings
        """
        route = self.routes['GET_INHERITEDPACKAGINGLABOR']
        route.params = {"companyId": companyId}
        if inherit_from is not None:
            route.params["inheritFrom"] = inherit_from
        return self._make_request(route)

    def get_geoareacompanies(self) -> List[CompanyGeoAreaCompanies]:
        """GET /api/companies/geoAreaCompanies

        Returns list of geo area companies.

        Returns:
            List[CompanyGeoAreaCompanies]: List of companies with geo area info
        """
        route = self.routes['GET_GEO_AREA_COMPANIES']
        return self._make_request(route)

    def get_brands(self) -> List[CompanyBrandTreeNode]:
        """GET /api/companies/brands

        Returns list of company brands.

        Returns:
            List[CompanyBrandTreeNode]: List of company brands
        """
        route = self.routes['GET_BRANDS']
        return self._make_request(route)

    def get_brandstree(self) -> List[CompanyBrandTreeNode]:
        """GET /api/companies/brandstree

        Returns the company brands in tree structure.

        Returns:
            List[CompanyBrandTreeNode]: Tree structure of company brands
        """
        route = self.routes['GET_BRANDSTREE']
        return self._make_request(route)

    def get_franchiseeaddresses(self, companyId: str) -> List[CompanyAddressInfo]:
        """GET /api/companies/{companyId}/franchiseeAddresses

        Returns:
            List[CompanyAddressInfo]: List of franchisee addresses
        """
        route = self.routes['GET_FRANCHISEE_ADDRESSES']
        route.params = {"companyId": companyId}
        return self._make_request(route)
