"""Job models for ABConnect API."""

from typing import Any, Dict, List, Optional, TYPE_CHECKING
from datetime import datetime
from pydantic import Field
from .base import ABConnectBaseModel, IdentifiedModel, JobRelatedModel, TimestampedModel
from .enums import JobAccessLevel, ServiceType, JobContactType, JobType

if TYPE_CHECKING:
    from .shared import (
        CalendarTask, DocumentDetails, CalendarNotes, CalendarItem,
        EmailDetails, PhoneDetails, AddressDetails,
        Commodity, ExportPackingInfo, ExportTotalCosts, SoldToDetails,
        USPSSpecific, FedExSpecific, UPSSpecific,
        InitialNoteModel, Items, ServiceInfo, SortByModel,
        SearchCustomerInfo
    )
    from .contacts import ContactDetails

class BaseInfoCalendarJob(JobRelatedModel):
    """BaseInfoCalendarJob model"""

    agent_id: Optional[str] = Field(None, alias="agentId")
    job_display_id: Optional[int] = Field(None, alias="jobDisplayId")
    address_id: Optional[int] = Field(None, alias="addressId")
    calendar_task: Optional["CalendarTask"] = Field(None, alias="calendarTask")


class CalendarJob(JobRelatedModel):
    """CalendarJob model"""

    agent_id: Optional[str] = Field(None, alias="agentId")
    job_display_id: Optional[int] = Field(None, alias="jobDisplayId")
    address_id: Optional[int] = Field(None, alias="addressId")
    contact_id: Optional[int] = Field(None, alias="contactId")
    calendar_task: Optional["CalendarTask"] = Field(None, alias="calendarTask")
    documents: Optional[List["DocumentDetails"]] = Field(None)
    notes: Optional[List["CalendarNotes"]] = Field(None)
    items: Optional[List["CalendarItem"]] = Field(None)
    contact_email: Optional[str] = Field(None, alias="contactEmail")
    contact_phone: Optional[str] = Field(None, alias="contactPhone")
    access_level: Optional[JobAccessLevel] = Field(None, alias="accessLevel")
    unread_sms_count: Optional[int] = Field(None, alias="unreadSMSCount", description="Unread SMS count (v709)")


class ChangeJobAgentRequest(ABConnectBaseModel):
    """ChangeJobAgentRequest model"""

    service_type: Optional[ServiceType] = Field(None, alias="serviceType")
    agent_id: Optional[str] = Field(None, alias="agentId")
    recalculate_price: Optional[bool] = Field(None, alias="recalculatePrice")
    apply_rebate: Optional[bool] = Field(None, alias="applyRebate")


class CreateScheduledJobEmailResponse(ABConnectBaseModel):
    """CreateScheduledJobEmailResponse model"""

    success: Optional[bool] = Field(None)
    error_message: Optional[str] = Field(None, alias="errorMessage")
    email_sent: Optional[bool] = Field(None, alias="emailSent")


class FeedbackSaveModel(ABConnectBaseModel):
    """FeedbackSaveModel model"""

    feedback_id: Optional[str] = Field(None, alias="feedbackId")
    cancel_job: Optional[bool] = Field(None, alias="cancelJob")


class FreightShimpment(TimestampedModel):
    """FreightShimpment model

    Note: API returns jobID, jobFreightID, itemID (capital ID) but we accept both formats.
    """

    item_id: Optional[str] = Field(None, validation_alias="itemID", serialization_alias="itemId")
    item_length: Optional[float] = Field(None, alias="itemLength")
    item_width: Optional[float] = Field(None, alias="itemWidth")
    item_height: Optional[float] = Field(None, alias="itemHeight")
    item_weight: Optional[float] = Field(None, alias="itemWeight")
    item_value: Optional[float] = Field(None, alias="itemValue")
    longest_dimension: Optional[float] = Field(None, alias="longestDimension")
    transportation_length: Optional[int] = Field(None, alias="transportationLength")
    transportation_width: Optional[int] = Field(None, alias="transportationWidth")
    transportation_height: Optional[int] = Field(None, alias="transportationHeight")
    ceiling_transportation_weight: Optional[int] = Field(None, alias="ceilingTransportationWeight")
    net_cubic_feet: Optional[float] = Field(None, alias="netCubicFeet")
    job_id: Optional[str] = Field(None, validation_alias="jobID", serialization_alias="jobId")
    quantity: Optional[int] = Field(None)
    freight_item_id: Optional[str] = Field(None, alias="freightItemId")
    freight_item_class_id: Optional[str] = Field(None, alias="freightItemClassId")
    cube: Optional[float] = Field(None)
    job_freight_id: Optional[str] = Field(None, validation_alias="jobFreightID", serialization_alias="jobFreightId")
    freight_description: Optional[str] = Field(None, alias="freightDescription")
    freight_item_value: Optional[str] = Field(None, alias="freightItemValue")
    freight_item_class: Optional[str] = Field(None, alias="freightItemClass")
    job_display_id: Optional[str] = Field(None, alias="jobDisplayId")
    nmfc_item: Optional[str] = Field(None, alias="nmfcItem")
    total_weight: Optional[float] = Field(None, alias="totalWeight")
    job_freight_report: Optional[str] = Field(None, alias="jobFreightReport")
    bol_description: Optional[str] = Field(None, alias="bolDescription")


class JobContactDetails(IdentifiedModel):
    """JobContactDetails model"""

    contact: Optional["ContactDetails"] = Field(None)
    email: Optional["EmailDetails"] = Field(None)
    phone: Optional["PhoneDetails"] = Field(None)
    address: Optional["AddressDetails"] = Field(None)
    care_of: Optional[str] = Field(None, alias="careOf")
    legacy_guid: Optional[str] = Field(None, alias="legacyGuid")
    contact_email_mapping_id: Optional[int] = Field(None, alias="contactEmailMappingId")
    contact_phone_mapping_id: Optional[int] = Field(None, alias="contactPhoneMappingId")
    contact_address_mapping_id: Optional[int] = Field(None, alias="contactAddressMappingId")
    dragged_from: Optional[JobContactType] = Field(None, alias="draggedFrom")
    job_contact_type: Optional[JobContactType] = Field(None, alias="jobContactType")


class JobExportData(ABConnectBaseModel):
    """JobExportData model"""

    commodities: Optional[List["Commodity"]] = Field(None)
    packing_info: Optional[List["ExportPackingInfo"]] = Field(None, alias="packingInfo")
    customs_value: float = Field(..., alias="customsValue")
    invoice_number: Optional[str] = Field(None, alias="invoiceNumber")
    purchase_order_number: Optional[str] = Field(None, alias="purchaseOrderNumber")
    terms_of_sale: Optional[str] = Field(None, alias="termsOfSale")
    exporter_tax_id: Optional[str] = Field(None, alias="exporterTaxId")
    consignee_tax_id: Optional[str] = Field(None, alias="consigneeTaxId")
    total_costs: Optional["ExportTotalCosts"] = Field(None, alias="totalCosts")
    sold_to: Optional["SoldToDetails"] = Field(None, alias="soldTo")
    usps_specific: Optional["USPSSpecific"] = Field(None, alias="uspsSpecific")
    fed_ex_specific: Optional["FedExSpecific"] = Field(None, alias="fedExSpecific")
    ups_specific: Optional["UPSSpecific"] = Field(None, alias="upsSpecific")


class JobItemNotesData(ABConnectBaseModel):
    """JobItemNotesData model"""

    job_item_id: Optional[str] = Field(None, alias="jobItemId")
    noted_conditions: Optional[str] = Field(None, alias="notedConditions")
    job_item_notes: Optional[str] = Field(None, alias="jobItemNotes")


class JobSaveRequest(JobRelatedModel):
    """JobSaveRequest model"""

    changed_values: Optional[Dict[str, Any]] = Field(None, alias="changedValues")


class JobSaveRequestModel(ABConnectBaseModel):
    """JobSaveRequestModel model"""

    customer_contact: Optional[JobContactDetails] = Field(None, alias="customerContact")
    pickup_contact: Optional[JobContactDetails] = Field(None, alias="pickupContact")
    delivery_contact: Optional[JobContactDetails] = Field(None, alias="deliveryContact")
    items: Optional[List["Items"]] = Field(None)
    job_type: Optional[JobType] = Field(None, alias="jobType")
    pickup_service: Optional["ServiceInfo"] = Field(None, alias="pickupService")
    delivery_service: Optional["ServiceInfo"] = Field(None, alias="deliveryService")


class SearchJobFilter(ABConnectBaseModel):
    """SearchJobFilter model"""

    page_size: int = Field(..., alias="pageSize")
    page_no: int = Field(..., alias="pageNo")
    total_count: Optional[int] = Field(None, alias="totalCount")
    sort_by: "SortByModel" = Field(..., alias="sortBy")
    job_info: Optional["SearchJobInfo"] = Field(None, alias="jobInfo")
    customer_info: Optional["SearchCustomerInfo"] = Field(None, alias="customerInfo")
    pickup_info: Optional["SearchCustomerInfo"] = Field(None, alias="pickupInfo")
    delivery_info: Optional["SearchCustomerInfo"] = Field(None, alias="deliveryInfo")
    from_date: Optional[datetime] = Field(None, alias="fromDate")
    to_date: Optional[datetime] = Field(None, alias="toDate")
    is_default_search_type: Optional[bool] = Field(None, alias="isDefaultSearchType")


class SearchJobInfo(ABConnectBaseModel):
    """SearchJobInfo model"""

    job_display_id: Optional[str] = Field(None, alias="jobDisplayId")
    agent_code: Optional[str] = Field(None, alias="agentCode")
    other_ref_no: Optional[str] = Field(None, alias="otherRefNo")
    referred_by: Optional[str] = Field(None, alias="referredBy")
    item_name: Optional[str] = Field(None, alias="itemName")
    job_mgmt_status_name: Optional[str] = Field(None, alias="jobMgmtStatusName")
    status_name: Optional[str] = Field(None, alias="statusName")


class TransferModel(ABConnectBaseModel):
    """TransferModel model"""

    franchisee_id: Optional[str] = Field(None, alias="franchiseeId")


__all__ = ['BaseInfoCalendarJob', 'CalendarJob', 'ChangeJobAgentRequest', 'CreateScheduledJobEmailResponse', 'FeedbackSaveModel', 'FreightShimpment', 'JobContactDetails', 'JobExportData', 'JobItemNotesData', 'JobSaveRequest', 'JobSaveRequestModel', 'SearchJobFilter', 'SearchJobInfo', 'TransferModel']
