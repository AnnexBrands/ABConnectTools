"""Shipment API endpoints.

Auto-generated from swagger.json specification.
Provides type-safe access to shipment/* endpoints.
"""

from typing import Optional
from .base import BaseEndpoint
# Model imports disabled
    # Model imports disabled


class ShipmentEndpoint(BaseEndpoint):
    """Shipment API endpoint operations.
    
    Handles all API operations for /api/shipment/* endpoints.
    Total endpoints: 3
    """
    
    api_path = "shipment"

    def get_get(self, franchisee_id: Optional[str] = None, provider_id: Optional[str] = None, pro_number: Optional[str] = None) -> dict:
        """GET /api/shipment
        
        
        
        Returns:
            dict: API response data
        """
        path = "/"
        kwargs = {}
        params = {}
        if franchisee_id is not None:
            params["franchiseeId"] = franchisee_id
        if provider_id is not None:
            params["providerId"] = provider_id
        if pro_number is not None:
            params["proNumber"] = pro_number
        if params:
            kwargs["params"] = params
        return self._make_request("GET", path, **kwargs)
    def get_accessorials(self) -> dict:
        """GET /api/shipment/accessorials
        
        
        
        Returns:
            dict: API response data
        """
        path = "/accessorials"
        kwargs = {}
        return self._make_request("GET", path, **kwargs)
    def get_document(self, docId: str, franchisee_id: Optional[str] = None) -> dict:
        """GET /api/shipment/document/{docId}
        
        
        
        Returns:
            dict: API response data
        """
        path = "/document/{docId}"
        path = path.replace("{docId}", docId)
        kwargs = {}
        params = {}
        if franchisee_id is not None:
            params["franchiseeId"] = franchisee_id
        if params:
            kwargs["params"] = params
        return self._make_request("GET", path, **kwargs)
