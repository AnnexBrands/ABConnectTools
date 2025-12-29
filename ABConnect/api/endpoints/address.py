"""Address API endpoints.

Auto-generated from swagger.json specification.
Provides type-safe access to address/* endpoints.
"""

from typing import Optional
from ABConnect.api.endpoints.base import BaseEndpoint


class AddressEndpoint(BaseEndpoint):
    """Address API endpoint operations.
    
    Handles all API operations for /api/address/* endpoints.
    Total endpoints: 4
    """
    
    api_path = "address"

    def get_isvalid(self, line1: Optional[str] = None, city: Optional[str] = None, state: Optional[str] = None, zip: Optional[str] = None) -> dict:
        """GET /api/address/isvalid
        
        
        
        Returns:
            dict: API response data
        """
        path = "/isvalid"
        kwargs = {}
        params = {}
        if line1 is not None:
            params["Line1"] = line1
        if city is not None:
            params["City"] = city
        if state is not None:
            params["State"] = state
        if zip is not None:
            params["Zip"] = zip
        if params:
            kwargs["params"] = params
        return self._make_request("GET", path, **kwargs)
    def post_validated(self, addressId: str, data: dict = None) -> dict:
        """POST /api/address/{addressId}/validated
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{addressId}/validated"
        path = path.replace("{addressId}", addressId)
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def post_avoidvalidation(self, addressId: str) -> dict:
        """POST /api/address/{addressId}/avoidValidation
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{addressId}/avoidValidation"
        path = path.replace("{addressId}", addressId)
        kwargs = {}
        return self._make_request("POST", path, **kwargs)
    def get_propertytype(self, address1: Optional[str] = None, address2: Optional[str] = None, city: Optional[str] = None, state: Optional[str] = None, zip_code: Optional[str] = None) -> dict:
        """GET /api/address/propertytype
        
        
        
        Returns:
            dict: API response data
        """
        path = "/propertytype"
        kwargs = {}
        params = {}
        if address1 is not None:
            params["Address1"] = address1
        if address2 is not None:
            params["Address2"] = address2
        if city is not None:
            params["City"] = city
        if state is not None:
            params["State"] = state
        if zip_code is not None:
            params["ZipCode"] = zip_code
        if params:
            kwargs["params"] = params
        return self._make_request("GET", path, **kwargs)
