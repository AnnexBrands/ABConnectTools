"""Shipment API endpoints.

Auto-generated from swagger.json specification.
Provides type-safe access to shipment/* endpoints.
"""

from typing import Optional
from ABConnect.api.endpoints.base import BaseEndpoint
from ABConnect.api.routes import SCHEMA


class ShipmentEndpoint(BaseEndpoint):
    """Shipment API endpoint operations.

    Handles all API operations for /api/shipment/* endpoints.
    Total endpoints: 3
    """

    api_path = "shipment"
    routes = SCHEMA["SHIPMENT"]

    def get_get(self, franchisee_id: Optional[str] = None, provider_id: Optional[str] = None, pro_number: Optional[str] = None) -> dict:
        """GET /api/shipment

        Returns:
            dict: API response data
        """
        route = self.routes['GET']
        params = {}
        if franchisee_id is not None:
            params["franchiseeId"] = franchisee_id
        if provider_id is not None:
            params["providerId"] = provider_id
        if pro_number is not None:
            params["proNumber"] = pro_number
        if params:
            route.params = params
        return self._make_request(route)

    def get_accessorials(self) -> dict:
        """GET /api/shipment/accessorials

        Returns:
            dict: API response data
        """
        route = self.routes['ACCESSORIALS']
        return self._make_request(route)

    def get_document(self, docId: str, franchisee_id: Optional[str] = None) -> dict:
        """GET /api/shipment/document/{docId}

        Returns:
            dict: API response data
        """
        route = self.routes['DOCUMENT']
        route.params = {"docId": docId}
        if franchisee_id is not None:
            route.params["franchiseeId"] = franchisee_id
        return self._make_request(route)
