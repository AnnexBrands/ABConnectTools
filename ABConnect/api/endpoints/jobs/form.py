"""Job Form API endpoints.

Auto-generated from swagger.json specification.

Note: The generic form endpoint was removed in API version 709.
- OLD: GET /api/job/{jobDisplayId}/form/{formid}
- NEW: Multiple specific form endpoints (see methods below)
"""

import warnings
from typing import List, Optional, Dict, Any
from ABConnect.api.endpoints.base import BaseEndpoint


class JobFormEndpoint(BaseEndpoint):
    """JobForm API endpoint operations.

    - address-label: Address labels
    - bill-of-lading: Bill of lading document
    - credit-card-authorization: Credit card auth form
    - customer-quote: Customer quote document
    - invoice: Invoice (read-only)
    - invoice/editable: Invoice (editable)
    - item-labels: Item labels
    - operations: Operations form
    - packaging-labels: Packaging labels
    - packaging-specification: Packaging specs
    - packing-slip: Packing slip
    - quick-sale: Quick sale form
    - shipments: Shipments form (existing)
    - usar: USAR form (read-only)
    - usar/editable: USAR form (editable)
    """

    api_path = "job"

    def get_form_shipments(self, jobDisplayId: str) -> Dict[str, Any]:
        """GET /api/job/{jobDisplayId}/form/shipments

        Get shipments form for a job.

        Returns:
            Dict[str, Any]: API response data
        """
        path = f"/{jobDisplayId}/form/shipments"
        return self._make_request("GET", path)

    def get_form_address_label(self, jobDisplayId: str) -> Dict[str, Any]:
        """GET /api/job/{jobDisplayId}/form/address-label

        Get address labels form for a job.

        .. versionadded:: 709

        Args:
            jobDisplayId: Job display ID

        Returns:
            Dict[str, Any]: Address label form data
        """
        path = f"/{jobDisplayId}/form/address-label"
        return self._make_request("GET", path)

    def get_form_bill_of_lading(
        self,
        jobDisplayId: str,
        shipment_plan_id: str,
        provider_option_index: int = 0
    ) -> bytes:
        """GET /api/job/{jobDisplayId}/form/bill-of-lading

        Get bill of lading form (PDF) for a specific shipment plan.

        Args:
            jobDisplayId: Job display ID
            shipment_plan_id: Shipment plan UUID
            provider_option_index: Provider option index (default 0)

        Returns:
            bytes: Bill of lading PDF data
        """
        path = f"/{jobDisplayId}/form/bill-of-lading"
        params = {
            "shipmentPlanId": shipment_plan_id,
            "providerOptionIndex": provider_option_index
        }
        return self._make_request("GET", path, params=params)

    def get_form_credit_card_authorization(self, jobDisplayId: str) -> Dict[str, Any]:
        """GET /api/job/{jobDisplayId}/form/credit-card-authorization

        Get credit card authorization form for a job.

        .. versionadded:: 709

        Args:
            jobDisplayId: Job display ID

        Returns:
            Dict[str, Any]: Credit card authorization form data
        """
        path = f"/{jobDisplayId}/form/credit-card-authorization"
        return self._make_request("GET", path)

    def get_form_customer_quote(self, jobDisplayId: str) -> Dict[str, Any]:
        """GET /api/job/{jobDisplayId}/form/customer-quote

        Get customer quote form for a job.

        .. versionadded:: 709

        Args:
            jobDisplayId: Job display ID

        Returns:
            Dict[str, Any]: Customer quote form data
        """
        path = f"/{jobDisplayId}/form/customer-quote"
        return self._make_request("GET", path)

    def get_form_invoice(self, jobDisplayId: str) -> Dict[str, Any]:
        """GET /api/job/{jobDisplayId}/form/invoice

        Get invoice form for a job (read-only).

        .. versionadded:: 709

        Args:
            jobDisplayId: Job display ID

        Returns:
            Dict[str, Any]: Invoice form data
        """
        path = f"/{jobDisplayId}/form/invoice"
        return self._make_request("GET", path)

    def get_form_invoice_editable(self, jobDisplayId: str) -> Dict[str, Any]:
        """GET /api/job/{jobDisplayId}/form/invoice/editable

        Get editable invoice form for a job.

        .. versionadded:: 709

        Args:
            jobDisplayId: Job display ID

        Returns:
            Dict[str, Any]: Editable invoice form data
        """
        path = f"/{jobDisplayId}/form/invoice/editable"
        return self._make_request("GET", path)

    def get_form_item_labels(self, jobDisplayId: str) -> Dict[str, Any]:
        """GET /api/job/{jobDisplayId}/form/item-labels

        Get item labels form for a job.

        .. versionadded:: 709

        Args:
            jobDisplayId: Job display ID

        Returns:
            Dict[str, Any]: Item labels form data
        """
        path = f"/{jobDisplayId}/form/item-labels"
        return self._make_request("GET", path)

    def get_form_operations(self, jobDisplayId: str, ops_type: int = 0) -> Dict[str, Any]:
        """GET /api/job/{jobDisplayId}/form/operations

        Get operations form for a job.

        .. versionadded:: 709

        Args:
            jobDisplayId: Job display ID
            ops_type: Operations form type (0 or 1, see OperationsFormType enum)

        Returns:
            Dict[str, Any]: Operations form data
        """
        path = f"/{jobDisplayId}/form/operations"
        params = {"type": ops_type}
        return self._make_request("GET", path, params=params)

    def get_form_packaging_labels(self, jobDisplayId: str) -> Dict[str, Any]:
        """GET /api/job/{jobDisplayId}/form/packaging-labels

        Get packaging labels form for a job.

        .. versionadded:: 709

        Args:
            jobDisplayId: Job display ID

        Returns:
            Dict[str, Any]: Packaging labels form data
        """
        path = f"/{jobDisplayId}/form/packaging-labels"
        return self._make_request("GET", path)

    def get_form_packaging_specification(self, jobDisplayId: str) -> Dict[str, Any]:
        """GET /api/job/{jobDisplayId}/form/packaging-specification

        Get packaging specification form for a job.

        .. versionadded:: 709

        Args:
            jobDisplayId: Job display ID

        Returns:
            Dict[str, Any]: Packaging specification form data
        """
        path = f"/{jobDisplayId}/form/packaging-specification"
        return self._make_request("GET", path)

    def get_form_packing_slip(self, jobDisplayId: str) -> Dict[str, Any]:
        """GET /api/job/{jobDisplayId}/form/packing-slip

        Get packing slip form for a job.

        .. versionadded:: 709

        Args:
            jobDisplayId: Job display ID

        Returns:
            Dict[str, Any]: Packing slip form data
        """
        path = f"/{jobDisplayId}/form/packing-slip"
        return self._make_request("GET", path)

    def get_form_quick_sale(self, jobDisplayId: str) -> Dict[str, Any]:
        """GET /api/job/{jobDisplayId}/form/quick-sale

        Get quick sale form for a job.

        .. versionadded:: 709

        Args:
            jobDisplayId: Job display ID

        Returns:
            Dict[str, Any]: Quick sale form data
        """
        path = f"/{jobDisplayId}/form/quick-sale"
        return self._make_request("GET", path)

    def get_form_usar(self, jobDisplayId: str) -> Dict[str, Any]:
        """GET /api/job/{jobDisplayId}/form/usar

        Get USAR (Uniform Straight Bill of Lading and Receipt) form (read-only).

        .. versionadded:: 709

        Args:
            jobDisplayId: Job display ID

        Returns:
            Dict[str, Any]: USAR form data
        """
        path = f"/{jobDisplayId}/form/usar"
        return self._make_request("GET", path)

    def get_form_usar_editable(self, jobDisplayId: str) -> Dict[str, Any]:
        """GET /api/job/{jobDisplayId}/form/usar/editable

        Get editable USAR form for a job.

        .. versionadded:: 709

        Args:
            jobDisplayId: Job display ID

        Returns:
            Dict[str, Any]: Editable USAR form data
        """
        path = f"/{jobDisplayId}/form/usar/editable"
        return self._make_request("GET", path)
