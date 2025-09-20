"""Lookup API endpoints.

Auto-generated from swagger.json specification.
Provides type-safe access to /api/lookup/* endpoints.
"""

from typing import Optional
from .base import BaseEndpoint


class LookupEndpoint(BaseEndpoint):
    """Lookup API endpoint operations.
    
    Handles all API operations for /api/lookup/* endpoints.
    Total endpoints: 14
    """
    
    api_path = "/api/lookup"

    def get_get(self, masterConstantKey: str) -> dict:
        """GET /api/lookup/{masterConstantKey}
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{masterConstantKey}"
        path = path.replace("{masterConstantKey}", masterConstantKey)
        return self._make_request("GET", path, **kwargs)
    def get_get(self, masterConstantKey: str, valueId: str) -> dict:
        """GET /api/lookup/{masterConstantKey}/{valueId}
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{masterConstantKey}/{valueId}"
        path = path.replace("{masterConstantKey}", masterConstantKey)
        path = path.replace("{valueId}", valueId)
        return self._make_request("GET", path, **kwargs)
    def get_countries(self) -> dict:
        """GET /api/lookup/countries
        
        
        
        Returns:
            dict: API response data
        """
        path = "/countries"
        return self._make_request("GET", path, **kwargs)
    def get_resetmasterconstantcache(self) -> dict:
        """GET /api/lookup/resetMasterConstantCache
        
        
        
        Returns:
            dict: API response data
        """
        path = "/resetMasterConstantCache"
        return self._make_request("GET", path, **kwargs)
    def get_accesskeys(self) -> dict:
        """GET /api/lookup/accessKeys
        
        
        
        Returns:
            dict: API response data
        """
        path = "/accessKeys"
        return self._make_request("GET", path, **kwargs)
    def get_accesskey(self, accessKey: str) -> dict:
        """GET /api/lookup/accessKey/{accessKey}
        
        
        
        Returns:
            dict: API response data
        """
        path = "/accessKey/{accessKey}"
        path = path.replace("{accessKey}", accessKey)
        return self._make_request("GET", path, **kwargs)
    def get_documenttypes(self, document_source: Optional[str] = None) -> dict:
        """GET /api/lookup/documentTypes
        
        
        
        Returns:
            dict: API response data
        """
        path = "/documentTypes"
        kwargs = {}
        params = {}
        if document_source is not None:
            params["documentSource"] = document_source
        if params:
            kwargs["params"] = params
        return self._make_request("GET", path, **kwargs)
    def get_items(self, job_display_id: Optional[str] = None, job_item_id: Optional[str] = None) -> dict:
        """GET /api/lookup/items
        
        
        
        Returns:
            dict: API response data
        """
        path = "/items"
        kwargs = {}
        params = {}
        if job_display_id is not None:
            params["jobDisplayId"] = job_display_id
        if job_item_id is not None:
            params["jobItemId"] = job_item_id
        if params:
            kwargs["params"] = params
        return self._make_request("GET", path, **kwargs)
    def get_refercategory(self) -> dict:
        """GET /api/lookup/referCategory
        
        
        
        Returns:
            dict: API response data
        """
        path = "/referCategory"
        return self._make_request("GET", path, **kwargs)
    def get_refercategoryheirachy(self) -> dict:
        """GET /api/lookup/referCategoryHeirachy
        
        
        
        Returns:
            dict: API response data
        """
        path = "/referCategoryHeirachy"
        return self._make_request("GET", path, **kwargs)
    def get_ppccampaigns(self) -> dict:
        """GET /api/lookup/PPCCampaigns
        
        
        
        Returns:
            dict: API response data
        """
        path = "/PPCCampaigns"
        return self._make_request("GET", path, **kwargs)
    def get_parcelpackagetypes(self) -> dict:
        """GET /api/lookup/parcelPackageTypes
        
        
        
        Returns:
            dict: API response data
        """
        path = "/parcelPackageTypes"
        return self._make_request("GET", path, **kwargs)
    def get_comoninsurance(self) -> dict:
        """GET /api/lookup/comonInsurance
        
        
        
        Returns:
            dict: API response data
        """
        path = "/comonInsurance"
        return self._make_request("GET", path, **kwargs)
    def get_contacttypes(self) -> dict:
        """GET /api/lookup/contactTypes
        
        
        
        Returns:
            dict: API response data
        """
        path = "/contactTypes"
        return self._make_request("GET", path, **kwargs)
