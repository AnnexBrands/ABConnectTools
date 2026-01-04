"""Lookup API endpoints.

Auto-generated from swagger.json specification.
Provides type-safe access to lookup/* endpoints.
"""

from typing import List, Optional
from ABConnect.api.endpoints.base import BaseEndpoint
from ABConnect.api.routes import SCHEMA


class LookupEndpoint(BaseEndpoint):
    """Lookup API endpoint operations.

    Handles all API operations for /api/lookup/* endpoints.
    Total endpoints: 15
    """

    api_path = "lookup"
    routes = SCHEMA["LOOKUP"]

    def get_lookup_value(self, masterConstantKey: str, valueId: str) -> dict:
        """GET /api/lookup/{masterConstantKey}/{valueId}

        Returns:
            dict: API response data
        """
        route = self.routes['GET']
        route.params = {"masterConstantKey": masterConstantKey, "valueId": valueId}
        return self._make_request(route)

    def get_countries(self) -> List[dict]:
        """GET /api/lookup/countries

        Returns list of country codes.

        Returns:
            List[dict]: List of country code objects
        """
        route = self.routes['COUNTRIES']
        return self._make_request(route)

    def get_resetmasterconstantcache(self) -> dict:
        """GET /api/lookup/resetMasterConstantCache

        Returns:
            dict: API response data
        """
        route = self.routes['RESET_MASTER_CONSTANT_CACHE']
        return self._make_request(route)

    def get_accesskeys(self) -> List[dict]:
        """GET /api/lookup/accessKeys

        Returns list of access keys.

        Returns:
            List[dict]: List of access key lookup values
        """
        route = self.routes['ACCESS_KEYS']
        return self._make_request(route)

    def get_accesskey(self, accessKey: str) -> dict:
        """GET /api/lookup/accessKey/{accessKey}

        Returns:
            dict: API response data
        """
        route = self.routes['ACCESS_KEY']
        route.params = {"accessKey": accessKey}
        return self._make_request(route)

    def get_documenttypes(self, document_source: Optional[str] = None) -> List[dict]:
        """GET /api/lookup/documentTypes

        Returns list of document types.

        Args:
            document_source: Optional document source filter

        Returns:
            List[dict]: List of document type lookup values
        """
        route = self.routes['DOCUMENT_TYPES']
        if document_source is not None:
            route.params = {"documentSource": document_source}
        return self._make_request(route)

    def get_items(self, job_display_id: Optional[str] = None, job_item_id: Optional[str] = None) -> dict:
        """GET /api/lookup/items

        Returns:
            dict: API response data
        """
        route = self.routes['ITEMS']
        params = {}
        if job_display_id is not None:
            params["jobDisplayId"] = job_display_id
        if job_item_id is not None:
            params["jobItemId"] = job_item_id
        if params:
            route.params = params
        return self._make_request(route)

    def get_refercategory(self) -> dict:
        """GET /api/lookup/referCategory

        Returns:
            dict: API response data
        """
        route = self.routes['REFER_CATEGORY']
        return self._make_request(route)

    def get_refercategoryheirachy(self) -> dict:
        """GET /api/lookup/referCategoryHeirachy

        Returns:
            dict: API response data
        """
        route = self.routes['REFER_CATEGORY_HEIRACHY']
        return self._make_request(route)

    def get_ppccampaigns(self) -> dict:
        """GET /api/lookup/PPCCampaigns

        Returns:
            dict: API response data
        """
        route = self.routes['PPCCAMPAIGNS']
        return self._make_request(route)

    def get_parcelpackagetypes(self) -> List[dict]:
        """GET /api/lookup/parcelPackageTypes

        Returns list of parcel package types.

        Returns:
            List[dict]: List of parcel package type lookup values
        """
        route = self.routes['PARCEL_PACKAGE_TYPES']
        return self._make_request(route)

    def get_comoninsurance(self) -> dict:
        """GET /api/lookup/comonInsurance

        Returns:
            dict: API response data
        """
        route = self.routes['COMON_INSURANCE']
        return self._make_request(route)

    def get_contacttypes(self) -> List[dict]:
        """GET /api/lookup/contactTypes

        Returns list of contact types.

        Returns:
            List[dict]: List of contact type entities
        """
        route = self.routes['CONTACT_TYPES']
        return self._make_request(route)

    def get_densityclassmap(self, carrier_api: Optional[str] = None) -> List[dict]:
        """GET /api/lookup/densityClassMap

        Returns density class map.

        Args:
            carrier_api: Optional carrier API filter

        Returns:
            List[dict]: List of density class map values
        """
        route = self.routes['DENSITY_CLASS_MAP']
        if carrier_api is not None:
            route.params = {"carrierApi": carrier_api}
        return self._make_request(route)
