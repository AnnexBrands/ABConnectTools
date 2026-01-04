"""Job Form API endpoints.

Auto-generated from swagger.json specification.

Note: The generic form endpoint was removed in API version 709.
- OLD: GET /api/job/{jobDisplayId}/form/{formid}
- NEW: Multiple specific form endpoints (see methods below)
"""

from typing import List, Dict, Any
from ABConnect.api.endpoints.base import BaseEndpoint
from ABConnect.api.routes import SCHEMA


class JobFormEndpoint(BaseEndpoint):
    """JobForm API endpoint operations."""

    api_path = "job"
    routes = SCHEMA["JOB"]

    def get_form_shipments(self, jobDisplayId: str) -> List[Dict[str, Any]]:
        """GET /api/job/{jobDisplayId}/form/shipments"""
        route = self.routes['GET_FORM_SHIPMENTS']
        route.params = {"jobDisplayId": jobDisplayId}
        return self._make_request(route)

    def get_form_address_label(self, jobDisplayId: str) -> bytes:
        """GET /api/job/{jobDisplayId}/form/address-label"""
        route = self.routes['GET_FORM_ADDRESS_LABEL']
        route.params = {"jobDisplayId": jobDisplayId}
        return self._make_request(route)

    def get_form_bill_of_lading(
        self,
        jobDisplayId: str,
        shipment_plan_id: str,
        provider_option_index: int = 0
    ) -> bytes:
        """GET /api/job/{jobDisplayId}/form/bill-of-lading"""
        route = self.routes['GET_FORM_BILL_OF_LADING']
        route.params = {
            "jobDisplayId": jobDisplayId,
            "shipmentPlanId": shipment_plan_id,
            "providerOptionIndex": provider_option_index
        }
        return self._make_request(route)

    def get_form_credit_card_authorization(self, jobDisplayId: str) -> bytes:
        """GET /api/job/{jobDisplayId}/form/credit-card-authorization"""
        route = self.routes['GET_FORM_CREDIT_CARD_AUTHORIZATION']
        route.params = {"jobDisplayId": jobDisplayId}
        return self._make_request(route)

    def get_form_customer_quote(self, jobDisplayId: str) -> bytes:
        """GET /api/job/{jobDisplayId}/form/customer-quote"""
        route = self.routes['GET_FORM_CUSTOMER_QUOTE']
        route.params = {"jobDisplayId": jobDisplayId}
        return self._make_request(route)

    def get_form_invoice(self, jobDisplayId: str) -> bytes:
        """GET /api/job/{jobDisplayId}/form/invoice"""
        route = self.routes['GET_FORM_INVOICE']
        route.params = {"jobDisplayId": jobDisplayId}
        return self._make_request(route)

    def get_form_invoice_editable(self, jobDisplayId: str) -> Dict[str, Any]:
        """GET /api/job/{jobDisplayId}/form/invoice/editable"""
        route = self.routes['GET_FORM_INVOICE_EDITABLE']
        route.params = {"jobDisplayId": jobDisplayId}
        return self._make_request(route)

    def get_form_item_labels(self, jobDisplayId: str) -> bytes:
        """GET /api/job/{jobDisplayId}/form/item-labels"""
        route = self.routes['GET_FORM_ITEM_LABELS']
        route.params = {"jobDisplayId": jobDisplayId}
        return self._make_request(route)

    def get_form_operations(self, jobDisplayId: str, ops_type: int = 0) -> bytes:
        """GET /api/job/{jobDisplayId}/form/operations"""
        route = self.routes['GET_FORM_OPERATIONS']
        route.params = {"jobDisplayId": jobDisplayId, "type": ops_type}
        return self._make_request(route)

    def get_form_packaging_labels(self, jobDisplayId: str) -> bytes:
        """GET /api/job/{jobDisplayId}/form/packaging-labels"""
        route = self.routes['GET_FORM_PACKAGING_LABELS']
        route.params = {"jobDisplayId": jobDisplayId}
        return self._make_request(route)

    def get_form_packaging_specification(self, jobDisplayId: str) -> bytes:
        """GET /api/job/{jobDisplayId}/form/packaging-specification"""
        route = self.routes['GET_FORM_PACKAGING_SPECIFICATION']
        route.params = {"jobDisplayId": jobDisplayId}
        return self._make_request(route)

    def get_form_packing_slip(self, jobDisplayId: str) -> bytes:
        """GET /api/job/{jobDisplayId}/form/packing-slip"""
        route = self.routes['GET_FORM_PACKING_SLIP']
        route.params = {"jobDisplayId": jobDisplayId}
        return self._make_request(route)

    def get_form_quick_sale(self, jobDisplayId: str) -> bytes:
        """GET /api/job/{jobDisplayId}/form/quick-sale"""
        route = self.routes['GET_FORM_QUICK_SALE']
        route.params = {"jobDisplayId": jobDisplayId}
        return self._make_request(route)

    def get_form_usar(self, jobDisplayId: str) -> bytes:
        """GET /api/job/{jobDisplayId}/form/usar"""
        route = self.routes['GET_FORM_USAR']
        route.params = {"jobDisplayId": jobDisplayId}
        return self._make_request(route)

    def get_form_usar_editable(self, jobDisplayId: str) -> Dict[str, Any]:
        """GET /api/job/{jobDisplayId}/form/usar/editable"""
        route = self.routes['GET_FORM_USAR_EDITABLE']
        route.params = {"jobDisplayId": jobDisplayId}
        return self._make_request(route)
