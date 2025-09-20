"""Job API endpoints.

Auto-generated from swagger.json specification.
Provides type-safe access to job/* endpoints.
"""

from typing import List, Optional
from .base import BaseEndpoint
try:
    from ..models import CarrierTask, CompanyListItem, DeleteTaskResponse, ExtendedOnHoldInfo, FormsShipmentPlan, JobCarrierRatesModel, JobParcelAddOn, JobTaskNote, OnHoldDetails, OnHoldNoteDetails, OnHoldUser, Packaging, ParcelItemWithMaterials, ParcelItemWithPackage, PricedFreightProvider, QuoteRequestDisplayInfo, QuoteRequestStatus, ResolveJobOnHoldResponse, SaveOnHoldResponse, SaveResponseModel, ServiceBaseResponse, ShipmentOriginDestination, ShipmentTrackingDetails, TimelineResponse
except ImportError:
    # Models not available, will return dict responses
    pass


class JobEndpoint(BaseEndpoint):
    """Job API endpoint operations.
    
    Handles all API operations for /api/job/* endpoints.
    Total endpoints: 81
    """
    
    api_path = "job"

    def post_book(self, jobDisplayId: str) -> dict:
        """POST /api/job/{jobDisplayId}/book
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/book"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        kwargs = {}
        return self._make_request("POST", path, **kwargs)
    def get_get(self, jobDisplayId: str) -> dict:
        """GET /api/job/{jobDisplayId}
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        kwargs = {}
        return self._make_request("GET", path, **kwargs)
    def get_search(self, job_display_id: Optional[str] = None) -> dict:
        """GET /api/job/search
        
        
        
        Returns:
            dict: API response data
        """
        path = "/search"
        kwargs = {}
        params = {}
        if job_display_id is not None:
            params["jobDisplayId"] = job_display_id
        if params:
            kwargs["params"] = params
        return self._make_request("GET", path, **kwargs)
    def post_searchbydetails(self, data: dict = None) -> dict:
        """POST /api/job/searchByDetails
        
        
        
        Returns:
            dict: API response data
        """
        path = "/searchByDetails"
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def get_calendaritems(self, jobDisplayId: str) -> dict:
        """GET /api/job/{jobDisplayId}/calendaritems
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/calendaritems"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        kwargs = {}
        return self._make_request("GET", path, **kwargs)
    def put_save(self, data: dict = None) -> dict:
        """PUT /api/job/save
        
        
        
        Returns:
            dict: API response data
        """
        path = "/save"
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("PUT", path, **kwargs)
    def post_post(self, data: dict = None) -> dict:
        """POST /api/job
        
        
        
        Returns:
            dict: API response data
        """
        path = "/"
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def get_feedback(self, jobDisplayId: str) -> dict:
        """GET /api/job/feedback/{jobDisplayId}
        
        
        
        Returns:
            dict: API response data
        """
        path = "/feedback/{jobDisplayId}"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        kwargs = {}
        return self._make_request("GET", path, **kwargs)
    def post_feedback(self, jobDisplayId: str, data: dict = None) -> dict:
        """POST /api/job/feedback/{jobDisplayId}
        
        
        
        Returns:
            dict: API response data
        """
        path = "/feedback/{jobDisplayId}"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def post_transfer(self, jobDisplayId: str, data: dict = None) -> dict:
        """POST /api/job/transfer/{jobDisplayId}
        
        
        
        Returns:
            dict: API response data
        """
        path = "/transfer/{jobDisplayId}"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def post_freightitems(self, jobDisplayId: str, data: dict = None) -> dict:
        """POST /api/job/{jobDisplayId}/freightitems
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/freightitems"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def get_submanagementstatus(self, jobDisplayId: str) -> dict:
        """GET /api/job/{jobDisplayId}/submanagementstatus
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/submanagementstatus"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        kwargs = {}
        return self._make_request("GET", path, **kwargs)
    def post_item_notes(self, jobDisplayId: str, data: dict = None) -> dict:
        """POST /api/job/{jobDisplayId}/item/notes
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/item/notes"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def post_changeagent(self, jobDisplayId: str, data: dict = None) -> dict:
        """POST /api/job/{jobDisplayId}/changeAgent
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/changeAgent"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def get_updatepageconfig(self, jobDisplayId: str) -> dict:
        """GET /api/job/{jobDisplayId}/updatePageConfig
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/updatePageConfig"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        kwargs = {}
        return self._make_request("GET", path, **kwargs)
    def get_price(self, jobDisplayId: str) -> dict:
        """GET /api/job/{jobDisplayId}/price
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/price"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        kwargs = {}
        return self._make_request("GET", path, **kwargs)
    def get_jobaccesslevel(self, job_display_id: Optional[str] = None, job_item_id: Optional[str] = None) -> dict:
        """GET /api/job/jobAccessLevel
        
        
        
        Returns:
            dict: API response data
        """
        path = "/jobAccessLevel"
        kwargs = {}
        params = {}
        if job_display_id is not None:
            params["jobDisplayId"] = job_display_id
        if job_item_id is not None:
            params["jobItemId"] = job_item_id
        if params:
            kwargs["params"] = params
        return self._make_request("GET", path, **kwargs)
    def get_documentconfig(self) -> dict:
        """GET /api/job/documentConfig
        
        
        
        Returns:
            dict: API response data
        """
        path = "/documentConfig"
        kwargs = {}
        return self._make_request("GET", path, **kwargs)
    def get_packagingcontainers(self, jobDisplayId: str) -> List[Packaging]:
        """GET /api/job/{jobDisplayId}/packagingcontainers
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/packagingcontainers"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        kwargs = {}
        return self._make_request("GET", path, **kwargs)
    def post_email_senddocument(self, jobDisplayId: str, data: dict = None) -> dict:
        """POST /api/job/{jobDisplayId}/email/senddocument
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/email/senddocument"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def post_email(self, jobDisplayId: str, data: dict = None) -> dict:
        """POST /api/job/{jobDisplayId}/email
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/email"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def post_email_createtransactionalemail(self, jobDisplayId: str) -> dict:
        """POST /api/job/{jobDisplayId}/email/createtransactionalemail
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/email/createtransactionalemail"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        kwargs = {}
        return self._make_request("POST", path, **kwargs)
    def post_email_send(self, jobDisplayId: str, emailTemplateGuid: str) -> dict:
        """POST /api/job/{jobDisplayId}/email/{emailTemplateGuid}/send
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/email/{emailTemplateGuid}/send"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        path = path.replace("{emailTemplateGuid}", emailTemplateGuid)
        kwargs = {}
        return self._make_request("POST", path, **kwargs)
    def get_form_shipments(self, jobDisplayId: str) -> List[FormsShipmentPlan]:
        """GET /api/job/{jobDisplayId}/form/shipments
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/form/shipments"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        kwargs = {}
        return self._make_request("GET", path, **kwargs)
    def get_form(self, jobDisplayId: str, formid: str, type: Optional[str] = None, shipment_plan_id: Optional[str] = None) -> dict:
        """GET /api/job/{jobDisplayId}/form/{formid}
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/form/{formid}"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        path = path.replace("{formid}", formid)
        kwargs = {}
        params = {}
        if type is not None:
            params["type"] = type
        if shipment_plan_id is not None:
            params["shipmentPlanID"] = shipment_plan_id
        if params:
            kwargs["params"] = params
        return self._make_request("GET", path, **kwargs)
    def post_freightproviders(self, jobDisplayId: str, data: dict = None) -> ServiceBaseResponse:
        """POST /api/job/{jobDisplayId}/freightproviders
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/freightproviders"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def get_freightproviders(self, jobDisplayId: str, provider_indexes: Optional[str] = None, shipment_types: Optional[str] = None, only_active: Optional[str] = None) -> List[PricedFreightProvider]:
        """GET /api/job/{jobDisplayId}/freightproviders
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/freightproviders"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        kwargs = {}
        params = {}
        if provider_indexes is not None:
            params["ProviderIndexes"] = provider_indexes
        if shipment_types is not None:
            params["ShipmentTypes"] = shipment_types
        if only_active is not None:
            params["OnlyActive"] = only_active
        if params:
            kwargs["params"] = params
        return self._make_request("GET", path, **kwargs)
    def post_freightproviders_ratequote(self, jobDisplayId: str, optionIndex: str, data: dict = None) -> ServiceBaseResponse:
        """POST /api/job/{jobDisplayId}/freightproviders/{optionIndex}/ratequote
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/freightproviders/{optionIndex}/ratequote"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        path = path.replace("{optionIndex}", optionIndex)
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def get_note(self, jobDisplayId: str, category: Optional[str] = None, task_code: Optional[str] = None) -> List[JobTaskNote]:
        """GET /api/job/{jobDisplayId}/note
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/note"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        kwargs = {}
        params = {}
        if category is not None:
            params["category"] = category
        if task_code is not None:
            params["taskCode"] = task_code
        if params:
            kwargs["params"] = params
        return self._make_request("GET", path, **kwargs)
    def post_note(self, jobDisplayId: str, data: dict = None) -> JobTaskNote:
        """POST /api/job/{jobDisplayId}/note
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/note"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def get_note(self, jobDisplayId: str, id: str) -> JobTaskNote:
        """GET /api/job/{jobDisplayId}/note/{id}
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/note/{id}"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        path = path.replace("{id}", id)
        kwargs = {}
        return self._make_request("GET", path, **kwargs)
    def put_note(self, jobDisplayId: str, id: str, data: dict = None) -> dict:
        """PUT /api/job/{jobDisplayId}/note/{id}
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/note/{id}"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        path = path.replace("{id}", id)
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("PUT", path, **kwargs)
    def get_onhold(self, jobDisplayId: str) -> List[ExtendedOnHoldInfo]:
        """GET /api/job/{jobDisplayId}/onhold
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/onhold"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        kwargs = {}
        return self._make_request("GET", path, **kwargs)
    def post_onhold(self, jobDisplayId: str, data: dict = None) -> SaveOnHoldResponse:
        """POST /api/job/{jobDisplayId}/onhold
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/onhold"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def delete_onhold(self, jobDisplayId: str) -> dict:
        """DELETE /api/job/{jobDisplayId}/onhold
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/onhold"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        kwargs = {}
        return self._make_request("DELETE", path, **kwargs)
    def get_onhold(self, jobDisplayId: str, id: str) -> OnHoldDetails:
        """GET /api/job/{jobDisplayId}/onhold/{id}
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/onhold/{id}"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        path = path.replace("{id}", id)
        kwargs = {}
        return self._make_request("GET", path, **kwargs)
    def put_onhold(self, jobDisplayId: str, onHoldId: str, data: dict = None) -> SaveOnHoldResponse:
        """PUT /api/job/{jobDisplayId}/onhold/{onHoldId}
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/onhold/{onHoldId}"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        path = path.replace("{onHoldId}", onHoldId)
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("PUT", path, **kwargs)
    def put_onhold_resolve(self, jobDisplayId: str, onHoldId: str, data: dict = None) -> ResolveJobOnHoldResponse:
        """PUT /api/job/{jobDisplayId}/onhold/{onHoldId}/resolve
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/onhold/{onHoldId}/resolve"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        path = path.replace("{onHoldId}", onHoldId)
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("PUT", path, **kwargs)
    def post_onhold_comment(self, jobDisplayId: str, onHoldId: str, data: dict = None) -> OnHoldNoteDetails:
        """POST /api/job/{jobDisplayId}/onhold/{onHoldId}/comment
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/onhold/{onHoldId}/comment"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        path = path.replace("{onHoldId}", onHoldId)
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def get_onhold_followupusers(self, jobDisplayId: str) -> List[OnHoldUser]:
        """GET /api/job/{jobDisplayId}/onhold/followupusers
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/onhold/followupusers"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        kwargs = {}
        return self._make_request("GET", path, **kwargs)
    def get_onhold_followupuser(self, jobDisplayId: str, contactId: str) -> OnHoldUser:
        """GET /api/job/{jobDisplayId}/onhold/followupuser/{contactId}
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/onhold/followupuser/{contactId}"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        path = path.replace("{contactId}", contactId)
        kwargs = {}
        return self._make_request("GET", path, **kwargs)
    def put_onhold_dates(self, jobDisplayId: str, onHoldId: str, data: dict = None) -> ResolveJobOnHoldResponse:
        """PUT /api/job/{jobDisplayId}/onhold/{onHoldId}/dates
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/onhold/{onHoldId}/dates"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        path = path.replace("{onHoldId}", onHoldId)
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("PUT", path, **kwargs)
    def get_parcelitems(self, jobDisplayId: str) -> List[ParcelItemWithPackage]:
        """GET /api/job/{jobDisplayId}/parcelitems
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/parcelitems"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        kwargs = {}
        return self._make_request("GET", path, **kwargs)
    def post_parcelitems(self, jobDisplayId: str, data: dict = None) -> List[ParcelItemWithPackage]:
        """POST /api/job/{jobDisplayId}/parcelitems
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/parcelitems"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def get_parcel_items_with_materials(self, jobDisplayId: str) -> List[ParcelItemWithMaterials]:
        """GET /api/job/{jobDisplayId}/parcel-items-with-materials
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/parcel-items-with-materials"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        kwargs = {}
        return self._make_request("GET", path, **kwargs)
    def delete_parcelitems(self, jobDisplayId: str, parcelItemId: str) -> dict:
        """DELETE /api/job/{jobDisplayId}/parcelitems/{parcelItemId}
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/parcelitems/{parcelItemId}"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        path = path.replace("{parcelItemId}", parcelItemId)
        kwargs = {}
        return self._make_request("DELETE", path, **kwargs)
    def get_payment_create(self, jobDisplayId: str) -> dict:
        """GET /api/job/{jobDisplayId}/payment/create
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/payment/create"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        kwargs = {}
        return self._make_request("GET", path, **kwargs)
    def post_payment_achpaymentsession(self, jobDisplayId: str) -> dict:
        """POST /api/job/{jobDisplayId}/payment/ACHPaymentSession
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/payment/ACHPaymentSession"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        kwargs = {}
        return self._make_request("POST", path, **kwargs)
    def post_payment_achcredittransfer(self, jobDisplayId: str) -> dict:
        """POST /api/job/{jobDisplayId}/payment/ACHCreditTransfer
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/payment/ACHCreditTransfer"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        kwargs = {}
        return self._make_request("POST", path, **kwargs)
    def get_payment(self, jobDisplayId: str, job_sub_key: Optional[str] = None) -> dict:
        """GET /api/job/{jobDisplayId}/payment
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/payment"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        kwargs = {}
        params = {}
        if job_sub_key is not None:
            params["jobSubKey"] = job_sub_key
        if params:
            kwargs["params"] = params
        return self._make_request("GET", path, **kwargs)
    def post_payment_attachcustomerbank(self, jobDisplayId: str, data: dict = None) -> dict:
        """POST /api/job/{jobDisplayId}/payment/attachCustomerBank
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/payment/attachCustomerBank"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def post_payment_verifyjobachsource(self, jobDisplayId: str, data: dict = None) -> dict:
        """POST /api/job/{jobDisplayId}/payment/verifyJobACHSource
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/payment/verifyJobACHSource"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def post_payment_canceljobachverification(self, jobDisplayId: str) -> dict:
        """POST /api/job/{jobDisplayId}/payment/cancelJobACHVerification
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/payment/cancelJobACHVerification"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        kwargs = {}
        return self._make_request("POST", path, **kwargs)
    def get_payment_sources(self, jobDisplayId: str) -> dict:
        """GET /api/job/{jobDisplayId}/payment/sources
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/payment/sources"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        kwargs = {}
        return self._make_request("GET", path, **kwargs)
    def post_payment_bysource(self, jobDisplayId: str, data: dict = None) -> dict:
        """POST /api/job/{jobDisplayId}/payment/bysource
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/payment/bysource"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def post_payment_banksource(self, jobDisplayId: str, data: dict = None) -> dict:
        """POST /api/job/{jobDisplayId}/payment/banksource
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/payment/banksource"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def get_rfq(self, jobDisplayId: str, rfq_service_type: Optional[str] = None) -> List[QuoteRequestDisplayInfo]:
        """GET /api/job/{jobDisplayId}/rfq
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/rfq"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        kwargs = {}
        params = {}
        if rfq_service_type is not None:
            params["rfqServiceType"] = rfq_service_type
        if params:
            kwargs["params"] = params
        return self._make_request("GET", path, **kwargs)
    def get_rfq_statusof_forcompany(self, jobDisplayId: str, rfqServiceType: str, companyId: str) -> QuoteRequestStatus:
        """GET /api/job/{jobDisplayId}/rfq/statusof/{rfqServiceType}/forcompany/{companyId}
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/rfq/statusof/{rfqServiceType}/forcompany/{companyId}"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        path = path.replace("{rfqServiceType}", rfqServiceType)
        path = path.replace("{companyId}", companyId)
        kwargs = {}
        return self._make_request("GET", path, **kwargs)
    def post_shipment_book(self, jobDisplayId: str, data: dict = None) -> dict:
        """POST /api/job/{jobDisplayId}/shipment/book
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/shipment/book"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def delete_shipment(self, jobDisplayId: str, data: dict = None) -> dict:
        """DELETE /api/job/{jobDisplayId}/shipment
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/shipment"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("DELETE", path, **kwargs)
    def get_shipment_ratequotes(self, jobDisplayId: str, ship_out_date: Optional[str] = None, rates_sources: Optional[str] = None, settings_key: Optional[str] = None) -> JobCarrierRatesModel:
        """GET /api/job/{jobDisplayId}/shipment/ratequotes
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/shipment/ratequotes"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        kwargs = {}
        params = {}
        if ship_out_date is not None:
            params["ShipOutDate"] = ship_out_date
        if rates_sources is not None:
            params["RatesSources"] = rates_sources
        if settings_key is not None:
            params["SettingsKey"] = settings_key
        if params:
            kwargs["params"] = params
        return self._make_request("GET", path, **kwargs)
    def post_shipment_ratequotes(self, jobDisplayId: str, data: dict = None) -> JobCarrierRatesModel:
        """POST /api/job/{jobDisplayId}/shipment/ratequotes
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/shipment/ratequotes"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def get_shipment_origindestination(self, jobDisplayId: str) -> ShipmentOriginDestination:
        """GET /api/job/{jobDisplayId}/shipment/origindestination
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/shipment/origindestination"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        kwargs = {}
        return self._make_request("GET", path, **kwargs)
    def get_shipment_accessorials(self, jobDisplayId: str) -> List[JobParcelAddOn]:
        """GET /api/job/{jobDisplayId}/shipment/accessorials
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/shipment/accessorials"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        kwargs = {}
        return self._make_request("GET", path, **kwargs)
    def post_shipment_accessorial(self, jobDisplayId: str, data: dict = None) -> dict:
        """POST /api/job/{jobDisplayId}/shipment/accessorial
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/shipment/accessorial"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def delete_shipment_accessorial(self, jobDisplayId: str, addOnId: str) -> dict:
        """DELETE /api/job/{jobDisplayId}/shipment/accessorial/{addOnId}
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/shipment/accessorial/{addOnId}"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        path = path.replace("{addOnId}", addOnId)
        kwargs = {}
        return self._make_request("DELETE", path, **kwargs)
    def get_shipment_ratesstate(self, jobDisplayId: str) -> dict:
        """GET /api/job/{jobDisplayId}/shipment/ratesstate
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/shipment/ratesstate"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        kwargs = {}
        return self._make_request("GET", path, **kwargs)
    def get_shipment_exportdata(self, jobDisplayId: str) -> dict:
        """GET /api/job/{jobDisplayId}/shipment/exportdata
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/shipment/exportdata"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        kwargs = {}
        return self._make_request("GET", path, **kwargs)
    def post_shipment_exportdata(self, jobDisplayId: str, data: dict = None) -> dict:
        """POST /api/job/{jobDisplayId}/shipment/exportdata
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/shipment/exportdata"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def get_sms(self, jobDisplayId: str) -> dict:
        """GET /api/job/{jobDisplayId}/sms
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/sms"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        kwargs = {}
        return self._make_request("GET", path, **kwargs)
    def post_sms(self, jobDisplayId: str, data: dict = None) -> dict:
        """POST /api/job/{jobDisplayId}/sms
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/sms"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def get_sms_templatebased(self, jobDisplayId: str, templateId: str) -> dict:
        """GET /api/job/{jobDisplayId}/sms/templatebased/{templateId}
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/sms/templatebased/{templateId}"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        path = path.replace("{templateId}", templateId)
        kwargs = {}
        return self._make_request("GET", path, **kwargs)
    def post_status_quote(self, jobDisplayId: str) -> dict:
        """POST /api/job/{jobDisplayId}/status/quote
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/status/quote"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        kwargs = {}
        return self._make_request("POST", path, **kwargs)
    def get_timeline(self, jobDisplayId: str) -> TimelineResponse:
        """GET /api/job/{jobDisplayId}/timeline
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/timeline"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        kwargs = {}
        return self._make_request("GET", path, **kwargs)
    def post_timeline(self, jobDisplayId: str, create_email: Optional[str] = None, data: dict = None) -> SaveResponseModel:
        """POST /api/job/{jobDisplayId}/timeline
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/timeline"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        kwargs = {}
        params = {}
        if create_email is not None:
            params["createEmail"] = create_email
        if params:
            kwargs["params"] = params
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def patch_timeline(self, jobDisplayId: str, timelineTaskId: str, data: dict = None) -> dict:
        """PATCH /api/job/{jobDisplayId}/timeline/{timelineTaskId}
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/timeline/{timelineTaskId}"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        path = path.replace("{timelineTaskId}", timelineTaskId)
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("PATCH", path, **kwargs)
    def delete_timeline(self, jobDisplayId: str, timelineTaskId: str) -> DeleteTaskResponse:
        """DELETE /api/job/{jobDisplayId}/timeline/{timelineTaskId}
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/timeline/{timelineTaskId}"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        path = path.replace("{timelineTaskId}", timelineTaskId)
        kwargs = {}
        return self._make_request("DELETE", path, **kwargs)
    def get_timeline(self, jobDisplayId: str, timelineTaskIdentifier: str) -> CarrierTask:
        """GET /api/job/{jobDisplayId}/timeline/{timelineTaskIdentifier}
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/timeline/{timelineTaskIdentifier}"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        path = path.replace("{timelineTaskIdentifier}", timelineTaskIdentifier)
        kwargs = {}
        return self._make_request("GET", path, **kwargs)
    def get_timeline_agent(self, jobDisplayId: str, taskCode: str) -> CompanyListItem:
        """GET /api/job/{jobDisplayId}/timeline/{taskCode}/agent
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/timeline/{taskCode}/agent"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        path = path.replace("{taskCode}", taskCode)
        kwargs = {}
        return self._make_request("GET", path, **kwargs)
    def get_tracking(self, jobDisplayId: str) -> dict:
        """GET /api/job/{jobDisplayId}/tracking
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/tracking"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        kwargs = {}
        return self._make_request("GET", path, **kwargs)
    def get_tracking_shipment(self, jobDisplayId: str, proNumber: str) -> ShipmentTrackingDetails:
        """GET /api/job/{jobDisplayId}/tracking/shipment/{proNumber}
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/tracking/shipment/{proNumber}"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        path = path.replace("{proNumber}", proNumber)
        kwargs = {}
        return self._make_request("GET", path, **kwargs)
