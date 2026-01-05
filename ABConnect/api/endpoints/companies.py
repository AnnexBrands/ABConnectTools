"""Companies API endpoints.

Auto-generated from swagger.json specification.
Provides type-safe access to companies/* endpoints.
"""

from typing import List, Optional, Union
from ABConnect.api.endpoints.base import BaseEndpoint
from ABConnect.api import models
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
        self, code_or_id: str, details: str = "full", cast: bool = False, **kwargs
    ) -> dict:
        """Convenience method to get company by code or ID.

        Args:
            code_or_id: Company code (e.g., '16023SC') or UUID
            details: Level of detail - 'short', 'full' (default), or 'details'
            cast: If True, cast response to Pydantic model
            **kwargs: Additional query parameters

        Returns:
            Company data as Pydantic model (if cast=True) or dict
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

    def get_by_id(self, id: str) -> models.CompanySimple:
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

    def get_details(self, companyId: str) -> dict:
        """GET /api/companies/{companyId}/details

        Returns:
            dict: API response data
        """
        route = self.routes['GET_DETAILS']
        route.params = {"companyId": companyId}
        return self._make_request(route)

    def get_availablebycurrentuser(self) -> List[dict]:
        """GET /api/companies/availableByCurrentUser

        Returns companies available to the current user.

        Returns:
            List[dict]: List of Company objects
        """
        route = self.routes['GET_AVAILABLE_BY_CURRENT_USER']
        return self._make_request(route)

    def get_search(self, search_value: Optional[str] = None) -> List[dict]:
        """GET /api/companies/search

        Search for companies by value.

        Args:
            search_value: Optional search term

        Returns:
            List[dict]: List of matching companies
        """
        route = self.routes['GET_SEARCH']
        if search_value is not None:
            route.params = {"searchValue": search_value}
        return self._make_request(route)

    def post_search_v2(self, data: dict = None) -> List[dict]:
        """POST /api/companies/search/v2

        Returns:
            dict: API response data
        """
        route = self.routes['POST_SEARCH_V2']
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def post_list(self, data: dict = None) -> dict:
        """POST /api/companies/list

        Returns:
            dict: API response data
        """
        route = self.routes['POST_LIST']
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def post_simplelist(self, data: dict = None) -> dict:
        """POST /api/companies/simplelist

        Returns:
            dict: API response data
        """
        route = self.routes['POST_SIMPLELIST']
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def get_fulldetails(self, companyId: str) -> dict:
        """GET /api/companies/{companyId}/fulldetails

        Returns:
            dict: API response data
        """
        route = self.routes['GET_FULLDETAILS']
        route.params = {"companyId": companyId}
        return self._make_request(route)

    def put_fulldetails(self, companyId: str, data: dict = None) -> dict:
        """PUT /api/companies/{companyId}/fulldetails

        Returns:
            dict: API response data
        """
        route = self.routes['PUT_FULLDETAILS']
        route.params = {"companyId": companyId}
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def get_search_carrier_accounts(
        self, current_company_id: Optional[str] = None, query: Optional[str] = None
    ) -> List[dict]:
        """GET /api/companies/search/carrier-accounts

        Search for carrier accounts.

        Args:
            current_company_id: Optional company ID filter
            query: Optional search query

        Returns:
            List[dict]: List of carrier account info
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

    def post_fulldetails(self, data: dict = None) -> dict:
        """POST /api/companies/fulldetails

        Returns:
            dict: API response data
        """
        route = self.routes['POST_FULLDETAILS']
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def get_infofromkey(self, key: Optional[str] = None) -> dict:
        """GET /api/companies/infoFromKey

        Returns:
            dict: API response data
        """
        route = self.routes['GET_INFO_FROM_KEY']
        if key is not None:
            route.params = {"key": key}
        return self._make_request(route)

    def get_geosettings(self, companyId: str) -> dict:
        """GET /api/companies/{companyId}/geosettings

        Returns:
            dict: API response data
        """
        route = self.routes['POST_GEOSETTINGS']
        route.params = {"companyId": companyId}
        return self._make_request("GET", route)

    def post_geosettings(self, companyId: str, data: dict = None) -> dict:
        """POST /api/companies/{companyId}/geosettings

        Returns:
            dict: API response data
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
    ) -> List[dict]:
        """GET /api/companies/geosettings

        Search for geo settings by location.

        Args:
            latitude: Optional latitude
            longitude: Optional longitude
            miles_radius: Optional radius in miles

        Returns:
            List[dict]: List of geo settings
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

    def post_filteredcustomers(self, data: dict = None) -> dict:
        """POST /api/companies/filteredCustomers

        Returns:
            dict: API response data
        """
        route = self.routes['POST_FILTERED_CUSTOMERS']
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def get_carrieracounts(self, companyId: str) -> dict:
        """GET /api/companies/{companyId}/carrierAcounts

        Returns:
            dict: API response data
        """
        route = self.routes['GET_CARRIER_ACOUNTS']
        route.params = {"companyId": companyId}
        return self._make_request(route)

    def post_carrieracounts(self, companyId: str, data: dict = None) -> dict:
        """POST /api/companies/{companyId}/carrierAcounts

        Returns:
            dict: API response data
        """
        route = self.routes['POST_CARRIER_ACOUNTS']
        route.params = {"companyId": companyId}
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def get_capabilities(self, companyId: str) -> dict:
        """GET /api/companies/{companyId}/capabilities

        Returns:
            dict: API response data
        """
        route = self.routes['GET_CAPABILITIES']
        route.params = {"companyId": companyId}
        return self._make_request(route)

    def post_capabilities(self, companyId: str, data: dict = None) -> dict:
        """POST /api/companies/{companyId}/capabilities

        Returns:
            dict: API response data
        """
        route = self.routes['POST_CAPABILITIES']
        route.params = {"companyId": companyId}
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def get_packagingsettings(self, companyId: str) -> dict:
        """GET /api/companies/{companyId}/packagingsettings

        Returns:
            dict: API response data
        """
        route = self.routes['GET_PACKAGINGSETTINGS']
        route.params = {"companyId": companyId}
        return self._make_request(route)

    def post_packagingsettings(self, companyId: str, data: dict = None) -> dict:
        """POST /api/companies/{companyId}/packagingsettings

        Returns:
            dict: API response data
        """
        route = self.routes['POST_PACKAGINGSETTINGS']
        route.params = {"companyId": companyId}
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def get_inheritedpackagingtariffs(
        self, companyId: str, inherit_from: Optional[str] = None
    ) -> dict:
        """GET /api/companies/{companyId}/inheritedPackagingTariffs

        Returns:
            dict: API response data
        """
        route = self.routes['GET_INHERITED_PACKAGING_TARIFFS']
        route.params = {"companyId": companyId}
        if inherit_from is not None:
            route.params["inheritFrom"] = inherit_from
        return self._make_request(route)

    def get_packaginglabor(self, companyId: str) -> dict:
        """GET /api/companies/{companyId}/packaginglabor

        Returns:
            dict: API response data
        """
        route = self.routes['GET_PACKAGINGLABOR']
        route.params = {"companyId": companyId}
        return self._make_request(route)

    def post_packaginglabor(self, companyId: str, data: dict = None) -> dict:
        """POST /api/companies/{companyId}/packaginglabor

        Returns:
            dict: API response data
        """
        route = self.routes['POST_PACKAGINGLABOR']
        route.params = {"companyId": companyId}
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def get_inheritedpackaginglabor(
        self, companyId: str, inherit_from: Optional[str] = None
    ) -> dict:
        """GET /api/companies/{companyId}/inheritedpackaginglabor

        Returns:
            dict: API response data
        """
        route = self.routes['GET_INHERITEDPACKAGINGLABOR']
        route.params = {"companyId": companyId}
        if inherit_from is not None:
            route.params["inheritFrom"] = inherit_from
        return self._make_request(route)

    def get_geoareacompanies(self) -> dict:
        """GET /api/companies/geoAreaCompanies

        Returns list of geo area companies.

        Returns:
            dict: List of companies with geo area info
        """
        route = self.routes['GET_GEO_AREA_COMPANIES']
        return self._make_request(route)

    def get_brands(self) -> List[dict]:
        """GET /api/companies/brands

        Returns list of company brands.
        """
        route = self.routes['GET_BRANDS']
        return self._make_request(route)

    def get_brandstree(self) -> dict:
        """GET /api/companies/brandstree

        Returns the company brands in tree structure.

        Returns:
            dict: Tree structure of company brands
        """
        route = self.routes['GET_BRANDSTREE']
        return self._make_request(route)

    def get_franchiseeaddresses(self, companyId: str) -> List[dict]:
        """GET /api/companies/{companyId}/franchiseeAddresses

        Returns:
            dict: API response data
        """
        route = self.routes['GET_FRANCHISEE_ADDRESSES']
        route.params = {"companyId": companyId}
        return self._make_request(route)
