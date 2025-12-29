"""Shared models for ABConnect API."""

import logging
from typing import List, Optional, TYPE_CHECKING
from datetime import datetime
from datetime import date
from pydantic import Field
from .base import ABConnectBaseModel, CompanyRelatedModel, IdentifiedModel, JobRelatedModel, TimestampedModel
from .enums import RetransTimeZoneEnum, LabelType, PaymentType, LabelImageType, JobAccessLevel, CarrierAPI, HistoryCodeABCState, ListSortDirection, SortByField, SelectedOption, DocumentType

if TYPE_CHECKING:
    from .jobnote import JobTaskNote
    from .address import AddressDetails, PlannerAddress, SearchAddress, SoldToAddress
    from .contacts import PlannerContact
    from .jobparcelitems import ParcelItem

logger = logging.getLogger(__name__)


class ServiceBaseResponse(ABConnectBaseModel):
    """Standard success/error response used by many API endpoints.

    Common response format:
    - {'success': True} on success
    - {'success': False, 'errorMessage': '...'} on failure

    Example:
        response = api.job.post_freightproviders(job_id)
        response.raise_for_error()  # Raises if failed

        # Or check manually:
        if response:
            print("Success!")
        else:
            print(f"Failed: {response.error_message}")
    """

    success: Optional[bool] = Field(None)
    error_message: Optional[str] = Field(None, alias="errorMessage")

    def raise_for_error(self) -> None:
        """Raise ValueError if response indicates failure.

        Logs the error message before raising.

        Raises:
            ValueError: If success is False
        """
        if self.success is False:
            error_msg = self.error_message or "Unknown error"
            logger.error("API request failed: %s", error_msg)
            raise ValueError(error_msg)

    def __bool__(self) -> bool:
        """Allow using response in boolean context.

        Returns:
            True if success is True, False otherwise
        """
        return self.success is True

    def __repr__(self) -> str:
        if self.success:
            return "ServiceBaseResponse(success=True)"
        return f"ServiceBaseResponse(success=False, error_message={self.error_message!r})"


class ServiceWarningResponse(ServiceBaseResponse):
    """ServiceBaseResponse with additional warning message field.

    Extends ServiceBaseResponse to include a warning_message that may be
    present even on successful responses.
    """

    warning_message: Optional[str] = Field(None, alias="warningMessage")

    def log_warning_if_present(self) -> None:
        """Log warning message if present."""
        if self.warning_message:
            logger.warning("API response warning: %s", self.warning_message)

    def raise_for_error(self) -> None:
        """Raise ValueError if response indicates failure, log warnings.

        Also logs any warning message present in the response.

        Raises:
            ValueError: If success is False
        """
        self.log_warning_if_present()
        super().raise_for_error()

    def __repr__(self) -> str:
        parts = [f"success={self.success}"]
        if self.error_message:
            parts.append(f"error_message={self.error_message!r}")
        if self.warning_message:
            parts.append(f"warning_message={self.warning_message!r}")
        return f"ServiceWarningResponse({', '.join(parts)})"


class AccesorialCharges(ABConnectBaseModel):
    """AccesorialCharges model"""

    stairs: Optional[float] = Field(None)
    elevator: Optional[float] = Field(None)
    long_carry: Optional[float] = Field(None, alias="longCarry")
    certificate_of_insurance: Optional[float] = Field(None, alias="certificateOfInsurance")
    de_installation: Optional[float] = Field(None, alias="deInstallation")
    disassembly: Optional[float] = Field(None)
    time_specific: Optional[float] = Field(None, alias="timeSpecific")
    saturday: Optional[float] = Field(None)


class AutoCompleteValue(IdentifiedModel):
    """AutoCompleteValue model"""

    value: Optional[str] = Field(None)


class Base64File(ABConnectBaseModel):
    """Base64File model"""

    name: Optional[str] = Field(None)
    data: Optional[str] = Field(None)


class BaseTask(TimestampedModel):
    """BaseTask model"""

    id: Optional[int] = Field(None)
    job_id: Optional[str] = Field(None, alias="jobId")
    task_code: Optional[str] = Field(None, alias="taskCode")
    planned_start_date: Optional[datetime] = Field(None, alias="plannedStartDate")
    notes: Optional[List["JobTaskNote"]] = Field(None)
    work_time_logs: Optional[List["WorkTimeLog"]] = Field(None, alias="workTimeLogs")
    target_start_date: Optional[datetime] = Field(None, alias="targetStartDate")
    actual_end_date: Optional[datetime] = Field(None, alias="actualEndDate")


class BookShipmentSpecificParams(ABConnectBaseModel):
    """BookShipmentSpecificParams model"""

    label_type: Optional[LabelType] = Field(None, alias="labelType")
    payment_type: Optional[PaymentType] = Field(None, alias="paymentType")
    third_party_company_id: Optional[str] = Field(None, alias="thirdPartyCompanyId")
    label_image_type: Optional[LabelImageType] = Field(None, alias="labelImageType")
    fed_ex_express_freight_detail: Optional["ExpressFreightDetail"] = Field(None, alias="fedExExpressFreightDetail")


class CalendarItem(IdentifiedModel):
    """CalendarItem model"""

    name: Optional[str] = Field(None)
    quantity: Optional[int] = Field(None)
    length: Optional[float] = Field(None)
    width: Optional[float] = Field(None)
    height: Optional[float] = Field(None)
    weight: Optional[float] = Field(None)
    value: Optional[float] = Field(None)
    notes: Optional[str] = Field(None)
    noted_conditions: Optional[str] = Field(None, alias="notedConditions")
    customer_item_id: Optional[str] = Field(None, alias="customerItemId")


class CalendarNotes(TimestampedModel):
    """CalendarNotes model"""

    id: Optional[int] = Field(None)
    value: Optional[str] = Field(None)
    is_important: Optional[bool] = Field(None, alias="isImportant")
    is_completed: Optional[bool] = Field(None, alias="isCompleted")
    author: Optional[str] = Field(None)


class CalendarTask(TimestampedModel):
    """CalendarTask model"""

    id: Optional[int] = Field(None)
    job_id: Optional[str] = Field(None, alias="jobId")
    truck_id: Optional[int] = Field(None, alias="truckId")
    task_code: Optional[str] = Field(None, alias="taskCode")
    planned_start_date: Optional[datetime] = Field(None, alias="plannedStartDate")
    planned_end_date: Optional[datetime] = Field(None, alias="plannedEndDate")
    on_site_time_log: Optional["TimeLog"] = Field(None, alias="onSiteTimeLog")
    trip_time_log: Optional["TimeLog"] = Field(None, alias="tripTimeLog")
    completed_date: Optional[datetime] = Field(None, alias="completedDate")


class CarrierAccountInfo(IdentifiedModel):
    """CarrierAccountInfo model"""

    key: Optional[str] = Field(None)
    friendly_name: Optional[str] = Field(None, alias="friendlyName")


class CarrierInfo(ABConnectBaseModel):
    """CarrierInfo model"""

    name: Optional[str] = Field(None)
    tracking_number: Optional[str] = Field(None, alias="trackingNumber")
    tracking_url: Optional[str] = Field(None, alias="trackingUrl")
    eta: Optional[datetime] = Field(None)


class CarrierProviderMessage(ABConnectBaseModel):
    """CarrierProviderMessage model"""

    source_id: Optional[CarrierAPI] = Field(None, alias="sourceId")
    message: Optional[str] = Field(None)


class CarrierRateModel(ABConnectBaseModel):
    """CarrierRateModel model"""

    carrier_name: Optional[str] = Field(None, alias="carrierName")
    carrier_code: Optional[str] = Field(None, alias="carrierCode")
    used_carrier_account_info: Optional[CarrierAccountInfo] = Field(None, alias="usedCarrierAccountInfo")
    service_days: Optional[int] = Field(None, alias="serviceDays")
    price: Optional[float] = Field(None)
    accessorials: Optional[List[str]] = Field(None)


class CarrierTaskModel(TimestampedModel):
    """CarrierTaskModel model"""

    id: Optional[int] = Field(None)
    job_id: Optional[str] = Field(None, alias="jobId")
    task_code: str = Field(..., alias="taskCode", min_length=1)
    planned_start_date: Optional[datetime] = Field(None, alias="plannedStartDate")
    initial_note: Optional["InitialNoteModel"] = Field(None, alias="initialNote")
    work_time_logs: Optional[List["WorkTimeLog"]] = Field(None, alias="workTimeLogs")
    notes: Optional[List["JobTaskNote"]] = Field(None)
    scheduled_date: Optional[datetime] = Field(None, alias="scheduledDate")
    pickup_completed_date: Optional[datetime] = Field(None, alias="pickupCompletedDate")
    delivery_completed_date: Optional[datetime] = Field(None, alias="deliveryCompletedDate")
    expected_delivery_date: Optional[datetime] = Field(None, alias="expectedDeliveryDate")


class Commodity(ABConnectBaseModel):
    """Commodity model"""

    description: Optional[str] = Field(None)
    weight: float = Field(...)
    unit_price: float = Field(..., alias="unitPrice")
    country_id: Optional[str] = Field(None, alias="countryId")
    country_iata_code: Optional[str] = Field(None, alias="countryIataCode")
    quantity: float = Field(...)
    unit_of_measure: Optional[str] = Field(None, alias="unitOfMeasure")
    schedule_b_number: Optional[str] = Field(None, alias="scheduleBNumber")
    eccn: Optional[str] = Field(None)
    export_license_code: Optional[str] = Field(None, alias="exportLicenseCode")
    special_marks: Optional[str] = Field(None, alias="specialMarks")
    item_value: Optional[float] = Field(None, alias="itemValue")
    full_description: Optional[str] = Field(None, alias="fullDescription")


class CreatedTask(TimestampedModel):
    """CreatedTask model"""

    id: Optional[int] = Field(None)
    planned_start_date: Optional[datetime] = Field(None, alias="plannedStartDate")
    preferred_start_date: Optional[datetime] = Field(None, alias="preferredStartDate")
    planned_end_date: Optional[datetime] = Field(None, alias="plannedEndDate")
    preferred_end_date: Optional[datetime] = Field(None, alias="preferredEndDate")
    truck: Optional["TaskTruckInfo"] = Field(None)


class CustomerInfo(ABConnectBaseModel):
    """CustomerInfo model"""

    name: Optional[str] = Field(None)
    email: Optional[str] = Field(None)
    address: Optional["AddressDetails"] = Field(None)
    contact_display_id: Optional[str] = Field(None, alias="contactDisplayId")
    customer_id: Optional[str] = Field(None, alias="customerId")


class Details(ABConnectBaseModel):
    """Details model"""

    contact: Optional["PlannerContact"] = Field(None)
    address: Optional["PlannerAddress"] = Field(None)
    labor: Optional["PlannerLabor"] = Field(None)


class DocumentDetails(IdentifiedModel):
    """DocumentDetails model"""

    path: Optional[str] = Field(None)
    thumbnail_path: Optional[str] = Field(None, alias="thumbnailPath")
    description: Optional[str] = Field(None)
    type_name: Optional[str] = Field(None, alias="typeName")
    type_id: Optional[int] = Field(None, alias="typeId")
    file_name: Optional[str] = Field(None, alias="fileName")
    shared: Optional[JobAccessLevel] = Field(None)
    tags: Optional[List[str]] = Field(None)
    job_items: Optional[List[str]] = Field(None, alias="jobItems")

    def __repr__(self) -> str:
        try:
            type_str = DocumentType(self.type_id).name if self.type_id else None
        except ValueError:
            type_str = str(self.type_id)
        try:
            shared_str = JobAccessLevel(self.shared).name if self.shared is not None else None
        except ValueError:
            shared_str = str(self.shared)
        return f"DocumentDetails(id={self.id}, file_name={self.file_name!r}, type={type_str}, shared={shared_str})"


class EmailDetails(IdentifiedModel):
    """EmailDetails model"""

    email: Optional[str] = Field(None)
    invalid: Optional[bool] = Field(None)
    dont_spam: Optional[bool] = Field(None, alias="dontSpam")


class EstesAccountData(ABConnectBaseModel):
    """EstesAccountData model"""

    user_name: Optional[str] = Field(None, alias="userName", min_length=0, max_length=48)
    password: Optional[str] = Field(None, min_length=0, max_length=128)
    account: Optional[str] = Field(None, min_length=0, max_length=8)


class ExportPackingInfo(ABConnectBaseModel):
    """ExportPackingInfo model"""

    commodity: Optional[int] = Field(None)
    package_number: Optional[int] = Field(None, alias="packageNumber")
    amount_in_package: Optional[int] = Field(None, alias="amountInPackage")
    shipper_memo: Optional[str] = Field(None, alias="shipperMemo")
    special_marks: Optional[str] = Field(None, alias="specialMarks")


class ExportTotalCosts(ABConnectBaseModel):
    """ExportTotalCosts model"""

    discount: Optional[float] = Field(None)
    insurance: Optional[float] = Field(None)
    freight: Optional[float] = Field(None)
    packing: Optional[float] = Field(None)
    handling: Optional[float] = Field(None)
    other: Optional[float] = Field(None)


class ExpressFreightDetail(ABConnectBaseModel):
    """ExpressFreightDetail model"""

    booking_confirmation_number: Optional[str] = Field(None, alias="bookingConfirmationNumber")
    shippers_load_and_count: Optional[int] = Field(None, alias="shippersLoadAndCount")
    packing_list_enclosed: Optional[bool] = Field(None, alias="packingListEnclosed")


class FedExAccountData(ABConnectBaseModel):
    """FedExAccountData model"""

    key: Optional[str] = Field(None, min_length=0, max_length=48)
    password: Optional[str] = Field(None, min_length=0, max_length=32)
    account_number: Optional[str] = Field(None, alias="accountNumber", min_length=0, max_length=48)
    meter_number: Optional[str] = Field(None, alias="meterNumber", min_length=0, max_length=48)
    rest_api_accounts: Optional[List["FedExRestApiAccount"]] = Field(None, alias="restApiAccounts")


class FedExRestApiAccount(IdentifiedModel):
    """FedExRestApiAccount model"""

    friendly_name: Optional[str] = Field(None, alias="friendlyName", min_length=0, max_length=32)
    account_number: Optional[str] = Field(None, alias="accountNumber", min_length=0, max_length=48)
    client_id: Optional[str] = Field(None, alias="clientId", min_length=0, max_length=512)
    client_secret: Optional[str] = Field(None, alias="clientSecret", min_length=0, max_length=512)
    is_active: Optional[bool] = Field(None, alias="isActive")


class FedExSpecific(ABConnectBaseModel):
    """FedExSpecific model"""

    reason_for_export: Optional[str] = Field(None, alias="reasonForExport")
    special_instructions: Optional[str] = Field(None, alias="specialInstructions")
    payment_type: Optional[str] = Field(None, alias="paymentType")
    export_compliance_statement: Optional[str] = Field(None, alias="exportComplianceStatement")
    payment_terms: Optional[str] = Field(None, alias="paymentTerms")


class ForwardAirAccountData(ABConnectBaseModel):
    """ForwardAirAccountData model"""

    user_name: Optional[str] = Field(None, alias="userName", min_length=0, max_length=48)
    password: Optional[str] = Field(None, min_length=0, max_length=128)
    customer_id: Optional[str] = Field(None, alias="customerId", min_length=0, max_length=16)
    bill_to: Optional[str] = Field(None, alias="billTo", min_length=0, max_length=16)
    shipper_number: Optional[str] = Field(None, alias="shipperNumber", min_length=0, max_length=16)


class FranchiseeCarrierAccounts(ABConnectBaseModel):
    """FranchiseeCarrierAccounts model"""

    lmi_client_code: Optional[str] = Field(None, alias="lmiClientCode")
    use_flat_rates: Optional[bool] = Field(None, alias="useFlatRates")
    fed_ex: Optional[FedExAccountData] = Field(None, alias="fedEx")
    ups: Optional["UPSAccountData"] = Field(None)
    road_runner: Optional["RoadRunnerAccountData"] = Field(None, alias="roadRunner")
    pilot: Optional["PilotAccountData"] = Field(None)
    team_ww: Optional["TeamWWAccountData"] = Field(None, alias="teamWw")
    estes: Optional[EstesAccountData] = Field(None)
    forward_air: Optional[ForwardAirAccountData] = Field(None, alias="forwardAir")
    global_tranz: Optional["GlobalTranzAccountData"] = Field(None, alias="globalTranz")
    usps: Optional["USPSAccountData"] = Field(None)
    lmi_user_name: Optional[str] = Field(None, alias="lmiUserName")


class GlobalTranzAccountData(ABConnectBaseModel):
    """GlobalTranzAccountData model"""

    access_key: Optional[str] = Field(None, alias="accessKey", min_length=0, max_length=48)
    user_name: Optional[str] = Field(None, alias="userName", min_length=0, max_length=48)
    password: Optional[str] = Field(None, min_length=0, max_length=128)


class GroupingInfo(ABConnectBaseModel):
    """GroupingInfo model"""

    selector: Optional[str] = Field(None)
    desc: Optional[bool] = Field(None)
    group_interval: Optional[str] = Field(None, alias="groupInterval")
    is_expanded: Optional[bool] = Field(None, alias="isExpanded")


class HandlingUnitModel(ABConnectBaseModel):
    """HandlingUnitModel model"""

    quantity: int = Field(...)
    length: Optional[float] = Field(None)
    width: Optional[float] = Field(None)
    height: Optional[float] = Field(None)
    weight: float = Field(...)
    value: Optional[float] = Field(None)
    parcel_package_code: Optional[str] = Field(None, alias="parcelPackageCode")


class InTheFieldTaskModel(TimestampedModel):
    """InTheFieldTaskModel model"""

    id: Optional[int] = Field(None)
    job_id: Optional[str] = Field(None, alias="jobId")
    task_code: str = Field(..., alias="taskCode", min_length=1)
    planned_start_date: Optional[datetime] = Field(None, alias="plannedStartDate")
    initial_note: Optional["InitialNoteModel"] = Field(None, alias="initialNote")
    work_time_logs: Optional[List["WorkTimeLog"]] = Field(None, alias="workTimeLogs")
    notes: Optional[List["JobTaskNote"]] = Field(None)
    planned_end_date: Optional[datetime] = Field(None, alias="plannedEndDate")
    preferred_start_date: Optional[datetime] = Field(None, alias="preferredStartDate")
    preferred_end_date: Optional[datetime] = Field(None, alias="preferredEndDate")
    truck: Optional["TaskTruckInfo"] = Field(None)
    on_site_time_log: Optional["TimeLogModel"] = Field(None, alias="onSiteTimeLog")
    trip_time_log: Optional["TimeLogModel"] = Field(None, alias="tripTimeLog")
    completed_date: Optional[datetime] = Field(None, alias="completedDate")


class InitialNoteModel(JobRelatedModel):
    """InitialNoteModel model"""

    comments: str = Field(..., min_length=1, max_length=8000)
    due_date: Optional[date] = Field(None, alias="dueDate")
    is_important: Optional[bool] = Field(None, alias="isImportant")
    is_completed: Optional[bool] = Field(None, alias="isCompleted")
    send_notification: Optional[bool] = Field(None, alias="sendNotification")


class InsuranceOption(ABConnectBaseModel):
    """InsuranceOption model"""

    insurance_slab_id: Optional[str] = Field(None, alias="insuranceSlabId")
    option: Optional[SelectedOption] = Field(None)
    sell_price: Optional[float] = Field(None, alias="sellPrice")


class ItemTotals(ABConnectBaseModel):
    """ItemTotals model"""

    max_length: Optional[float] = Field(None, alias="maxLength")
    max_width: Optional[float] = Field(None, alias="maxWidth")
    max_height: Optional[float] = Field(None, alias="maxHeight")
    weight: Optional[float] = Field(None)
    value: Optional[float] = Field(None)
    cubic_feet: Optional[float] = Field(None, alias="cubicFeet")


class Items(TimestampedModel):
    """Items model"""

    item_id: Optional[str] = Field(None, alias="itemId")
    item_length: Optional[float] = Field(None, alias="itemLength")
    item_width: Optional[float] = Field(None, alias="itemWidth")
    item_height: Optional[float] = Field(None, alias="itemHeight")
    item_weight: Optional[float] = Field(None, alias="itemWeight")
    item_value: Optional[float] = Field(None, alias="itemValue")
    net_cubic_feet: Optional[float] = Field(None, alias="netCubicFeet")
    company_id: Optional[str] = Field(None, alias="companyId")
    company_name: Optional[str] = Field(None, alias="companyName")
    item_sequence_no: Optional[int] = Field(None, alias="itemSequenceNo")
    item_name: Optional[str] = Field(None, alias="itemName")
    item_description: Optional[str] = Field(None, alias="itemDescription")
    schedule_b: Optional[str] = Field(None, alias="scheduleB")
    eccn: Optional[str] = Field(None)
    item_notes: Optional[str] = Field(None, alias="itemNotes")
    is_prepacked: Optional[bool] = Field(None, alias="isPrepacked")
    item_active: Optional[bool] = Field(None, alias="itemActive")
    item_public: Optional[bool] = Field(None, alias="itemPublic")
    c_pack_id: Optional[str] = Field(None, alias="cPackId")
    job_display_id: Optional[str] = Field(None, alias="jobDisplayId")
    job_item_id: Optional[str] = Field(None, alias="jobItemId")
    original_job_item_id: Optional[str] = Field(None, alias="originalJobItemId")
    job_id: Optional[str] = Field(None, alias="jobId")
    quantity: Optional[int] = Field(None)
    original_qty: Optional[int] = Field(None, alias="originalQty")
    job_freight_id: Optional[str] = Field(None, alias="jobFreightId")
    nmfc_item: Optional[str] = Field(None, alias="nmfcItem")
    nmfc_sub: Optional[str] = Field(None, alias="nmfcSub")
    nmfc_sub_class: Optional[str] = Field(None, alias="nmfcSubClass")
    job_item_pkd_length: Optional[float] = Field(None, alias="jobItemPkdLength")
    job_item_pkd_width: Optional[float] = Field(None, alias="jobItemPkdWidth")
    job_item_pkd_height: Optional[float] = Field(None, alias="jobItemPkdHeight")
    job_item_pkd_weight: Optional[float] = Field(None, alias="jobItemPkdWeight")
    is_fill_percent_changed: Optional[bool] = Field(None, alias="isFillPercentChanged")
    c_fill_id: Optional[int] = Field(None, alias="cFillId")
    container_id: Optional[int] = Field(None, alias="containerId")
    labor_hrs: Optional[float] = Field(None, alias="laborHrs")
    labor_charge: Optional[float] = Field(None, alias="laborCharge")
    user_id: Optional[str] = Field(None, alias="userId")
    is_fill_changed: Optional[bool] = Field(None, alias="isFillChanged")
    is_container_changed: Optional[bool] = Field(None, alias="isContainerChanged")
    is_valid_container: Optional[bool] = Field(None, alias="isValidContainer")
    is_valid_fill: Optional[bool] = Field(None, alias="isValidFill")
    inches_to_add: Optional[float] = Field(None, alias="inchesToAdd")
    container_thickness: Optional[float] = Field(None, alias="containerThickness")
    is_inch_to_add_changed: Optional[bool] = Field(None, alias="isInchToAddChanged")
    total_pcs: Optional[float] = Field(None, alias="totalPcs")
    description_of_products: Optional[str] = Field(None, alias="descriptionOfProducts")
    total_items: Optional[int] = Field(None, alias="totalItems")
    auto_pack_off: Optional[bool] = Field(None, alias="autoPackOff")
    c_pack_value: Optional[str] = Field(None, alias="cPackValue")
    c_fill_value: Optional[str] = Field(None, alias="cFillValue")
    container_type: Optional[str] = Field(None, alias="containerType")
    job_item_fill_percent: Optional[float] = Field(None, alias="jobItemFillPercent")
    container_weight: Optional[float] = Field(None, alias="containerWeight")
    fill_weight: Optional[float] = Field(None, alias="fillWeight")
    material_weight: Optional[float] = Field(None, alias="materialWeight")
    job_item_pkd_value: Optional[float] = Field(None, alias="jobItemPkdValue")
    total_packed_value: Optional[float] = Field(None, alias="totalPackedValue")
    total_weight: Optional[float] = Field(None, alias="totalWeight")
    stc: Optional[str] = Field(None)
    materials: Optional[List["MasterMaterials"]] = Field(None)
    material_total_cost: Optional[float] = Field(None, alias="materialTotalCost")
    is_access: Optional[str] = Field(None, alias="isAccess")
    job_item_parcel_value: Optional[float] = Field(None, alias="jobItemParcelValue")
    total_labor_charge: Optional[float] = Field(None, alias="totalLaborCharge")
    gross_cubic_feet: Optional[float] = Field(None, alias="grossCubicFeet")
    row_number: Optional[int] = Field(None, alias="rowNumber")
    noted_conditions: Optional[str] = Field(None, alias="notedConditions")
    job_item_notes: Optional[str] = Field(None, alias="jobItemNotes")
    customer_item_id: Optional[str] = Field(None, alias="customerItemId")
    document_exists: Optional[bool] = Field(None, alias="documentExists")
    force_crate: Optional[bool] = Field(None, alias="forceCrate")
    auto_pack_failed: Optional[bool] = Field(None, alias="autoPackFailed")
    do_not_tip: Optional[bool] = Field(None, alias="doNotTip", description="Do not tip flag (v709)")
    commodity_id: Optional[int] = Field(None, alias="commodityId", description="Commodity ID for HS code (v709)")
    longest_dimension: Optional[float] = Field(None, alias="longestDimension")
    second_dimension: Optional[float] = Field(None, alias="secondDimension")
    pkd_girth: Optional[float] = Field(None, alias="pkdGirth")
    pkd_length_plus_girth: Optional[float] = Field(None, alias="pkdLengthPlusGirth")
    requested_parcel_packagings: Optional[List["RequestedParcelPackaging"]] = Field(None, alias="requestedParcelPackagings")
    parcel_package_type_id: Optional[int] = Field(None, alias="parcelPackageTypeId")
    transportation_length: Optional[int] = Field(None, alias="transportationLength")
    transportation_width: Optional[int] = Field(None, alias="transportationWidth")
    transportation_height: Optional[int] = Field(None, alias="transportationHeight")
    transportation_weight: Optional[float] = Field(None, alias="transportationWeight")
    ceiling_transportation_weight: Optional[int] = Field(None, alias="ceilingTransportationWeight")


class JToken(ABConnectBaseModel):
    """JToken model"""
    pass


class LaborCharges(ABConnectBaseModel):
    """LaborCharges model"""

    cost: Optional[float] = Field(None)
    charge: Optional[float] = Field(None)


class LastObtainNFM(ABConnectBaseModel):
    """LastObtainNFM model"""

    from_zip: Optional[str] = Field(None, alias="fromZip")
    to_zip: Optional[str] = Field(None, alias="toZip")
    item_weight: Optional[float] = Field(None, alias="itemWeight")
    services: Optional[List[str]] = Field(None)
    parcel_items: Optional[List["ObtainNFMParcelItem"]] = Field(None, alias="parcelItems")
    parcel_services: Optional[List["ObtainNFMParcelService"]] = Field(None, alias="parcelServices")
    ship_out_date: Optional[datetime] = Field(None, alias="shipOutDate")


class LatLng(ABConnectBaseModel):
    """LatLng model"""

    latitude: Optional[float] = Field(None)
    longitude: Optional[float] = Field(None)


class LookupItem(IdentifiedModel):
    """LookupItem model"""

    name: Optional[str] = Field(None)


class MasterMaterials(TimestampedModel):
    """MasterMaterials model"""

    job_id: Optional[str] = Field(None, alias="jobId")
    job_pack_material_id: Optional[str] = Field(None, alias="jobPackMaterialId")
    material_id: Optional[int] = Field(None, alias="materialId")
    mateial_master_id: Optional[str] = Field(None, alias="mateialMasterId")
    material_quantity: Optional[float] = Field(None, alias="materialQuantity")
    material_name: Optional[str] = Field(None, alias="materialName")
    material_description: Optional[str] = Field(None, alias="materialDescription")
    material_code: Optional[str] = Field(None, alias="materialCode")
    material_type: Optional[str] = Field(None, alias="materialType")
    material_unit: Optional[str] = Field(None, alias="materialUnit")
    material_weight: Optional[float] = Field(None, alias="materialWeight")
    material_length: Optional[float] = Field(None, alias="materialLength")
    material_width: Optional[float] = Field(None, alias="materialWidth")
    material_height: Optional[float] = Field(None, alias="materialHeight")
    material_cost: Optional[float] = Field(None, alias="materialCost")
    material_price: Optional[float] = Field(None, alias="materialPrice")
    material_waste_factor: Optional[float] = Field(None, alias="materialWasteFactor")
    material_total_cost: Optional[float] = Field(None, alias="materialTotalCost")
    material_total_weight: Optional[float] = Field(None, alias="materialTotalWeight")
    item_id: Optional[str] = Field(None, alias="itemId")
    quantity_actual: Optional[float] = Field(None, alias="quantityActual")
    is_automatic: Optional[bool] = Field(None, alias="isAutomatic")
    waste: Optional[float] = Field(None)
    price: Optional[float] = Field(None)
    is_edited: Optional[bool] = Field(None, alias="isEdited")
    item_name: Optional[str] = Field(None, alias="itemName")
    item_description: Optional[str] = Field(None, alias="itemDescription")
    item_notes: Optional[str] = Field(None, alias="itemNotes")
    job_item_id: Optional[str] = Field(None, alias="jobItemId")
    company_id: Optional[str] = Field(None, alias="companyId")
    is_active: Optional[bool] = Field(None, alias="isActive")


class NameValueEntity(ABConnectBaseModel):
    """NameValueEntity model"""

    name: Optional[str] = Field(None)
    value: Optional[str] = Field(None)


class ObtainNFMParcelItem(ABConnectBaseModel):
    """ObtainNFMParcelItem model"""

    width: Optional[float] = Field(None)
    length: Optional[float] = Field(None)
    height: Optional[float] = Field(None)
    parcel_package_type_id: Optional[int] = Field(None, alias="parcelPackageTypeId")
    qty: Optional[int] = Field(None)
    weight: Optional[float] = Field(None)
    parcel_value: Optional[float] = Field(None, alias="parcelValue")


class ObtainNFMParcelService(IdentifiedModel):
    """ObtainNFMParcelService model"""

    params: Optional[List[NameValueEntity]] = Field(None)


class OnlinePaymentSettings(ABConnectBaseModel):
    """OnlinePaymentSettings model"""

    credit_card_surcharge: Optional[float] = Field(None, alias="creditCardSurcharge")
    stripe_connected: Optional[bool] = Field(None, alias="stripeConnected")


class PackagingLaborHours(IdentifiedModel):
    """PackagingLaborHours model"""

    condition_json: Optional[str] = Field(None, alias="conditionJson")
    filter_expression_json: Optional[str] = Field(None, alias="filterExpressionJson")
    hours: Optional[float] = Field(None)


class PageOrderedRequestModel(ABConnectBaseModel):
    """PageOrderedRequestModel model"""

    page_number: int = Field(..., alias="pageNumber")
    page_size: int = Field(..., alias="pageSize")
    sorting_by: Optional[str] = Field(None, alias="sortingBy")
    sorting_direction: Optional[ListSortDirection] = Field(None, alias="sortingDirection")


class PhoneDetails(IdentifiedModel):
    """PhoneDetails model"""

    phone: Optional[str] = Field(None)


class PickupLaborHoursRule(IdentifiedModel):
    """PickupLaborHoursRule model"""

    condition_json: Optional[str] = Field(None, alias="conditionJson")
    filter_expression_json: Optional[str] = Field(None, alias="filterExpressionJson")
    labor_count: Optional[int] = Field(None, alias="laborCount")
    trip_hours: Optional[float] = Field(None, alias="tripHours")
    on_site_hours: Optional[float] = Field(None, alias="onSiteHours")


class PilotAccountData(ABConnectBaseModel):
    """PilotAccountData model"""

    location_id: Optional[int] = Field(None, alias="locationId")
    tariff_header_id: Optional[int] = Field(None, alias="tariffHeaderId")
    user_name: Optional[str] = Field(None, alias="userName", min_length=0, max_length=48)
    password: Optional[str] = Field(None, min_length=0, max_length=128)
    address_id: Optional[int] = Field(None, alias="addressId")
    control_station: Optional[str] = Field(None, alias="controlStation", min_length=0, max_length=32)


class PlannerLabor(ABConnectBaseModel):
    """PlannerLabor model"""

    labor_count: Optional[int] = Field(None, alias="laborCount")
    trip_hours: Optional[float] = Field(None, alias="tripHours")
    on_site_hours: Optional[float] = Field(None, alias="onSiteHours")


class QuoteRequestComment(ABConnectBaseModel):
    """QuoteRequestComment model"""

    message: Optional[str] = Field(None)
    created_utc: Optional[datetime] = Field(None, alias="createdUtc")
    author: Optional[str] = Field(None)
    made_by_me: Optional[bool] = Field(None, alias="madeByMe")


class RequestedParcelPackaging(ABConnectBaseModel):
    """RequestedParcelPackaging model"""

    parcel_package_id: Optional[int] = Field(None, alias="parcelPackageId")
    package_code: Optional[str] = Field(None, alias="packageCode")
    carrier: Optional[CarrierAPI] = Field(None)
    weight: Optional[float] = Field(None)
    length: Optional[float] = Field(None)
    width: Optional[float] = Field(None)
    height: Optional[float] = Field(None)


class RoadRunnerAccountData(ABConnectBaseModel):
    """RoadRunnerAccountData model"""

    user_name: Optional[str] = Field(None, alias="userName", min_length=0, max_length=48)
    password: Optional[str] = Field(None, min_length=0, max_length=128)
    app_id: Optional[str] = Field(None, alias="appId", min_length=0, max_length=48)
    api_key: Optional[str] = Field(None, alias="apiKey", min_length=0, max_length=48)


class RoyaltiesCharges(ABConnectBaseModel):
    """RoyaltiesCharges model"""

    franchisee: Optional[float] = Field(None)
    national: Optional[float] = Field(None)
    local: Optional[float] = Field(None)


class SearchCustomerInfo(CompanyRelatedModel):
    """SearchCustomerInfo model"""

    full_name: Optional[str] = Field(None, alias="fullName")
    address: Optional["SearchAddress"] = Field(None)


class ServiceInfo(ABConnectBaseModel):
    """ServiceInfo model"""

    accessorials: Optional[List[str]] = Field(None)
    date: Optional[str] = Field(None)
    done_by: Optional[str] = Field(None, alias="doneBy")


class ServicePricingsMarkup(ABConnectBaseModel):
    """ServicePricingsMarkup model"""

    whole_sale: Optional[float] = Field(None, alias="wholeSale")
    base: Optional[float] = Field(None)
    medium: Optional[float] = Field(None)
    high: Optional[float] = Field(None)


class ShipmentTrackingDocument(ABConnectBaseModel):
    """ShipmentTrackingDocument model"""

    document_id: Optional[str] = Field(None, alias="documentId")
    document_path: Optional[str] = Field(None, alias="documentPath")
    document_description: Optional[str] = Field(None, alias="documentDescription")
    error_message: Optional[str] = Field(None, alias="errorMessage")


class ShippingHistoryStatus(ABConnectBaseModel):
    """ShippingHistoryStatus model"""

    city: Optional[str] = Field(None)
    state: Optional[str] = Field(None)
    country_code: Optional[str] = Field(None, alias="countryCode")
    country: Optional[str] = Field(None)
    display_status_message: Optional[str] = Field(None, alias="displayStatusMessage")
    internal_status_code: Optional[HistoryCodeABCState] = Field(None, alias="internalStatusCode")
    status_date: Optional[datetime] = Field(None, alias="statusDate")
    time_zone: Optional[RetransTimeZoneEnum] = Field(None, alias="timeZone")
    status_message: Optional[str] = Field(None, alias="statusMessage")
    reason_message: Optional[str] = Field(None, alias="reasonMessage")
    status_code: Optional[str] = Field(None, alias="statusCode")
    status_type: Optional[str] = Field(None, alias="statusType")
    location: Optional[str] = Field(None)


class ShippingPackageInfo(ABConnectBaseModel):
    """ShippingPackageInfo model"""

    tracking_number: Optional[str] = Field(None, alias="trackingNumber")
    weight: Optional["WeightInfo"] = Field(None)


class SimplePriceTariff(IdentifiedModel):
    """SimplePriceTariff model"""

    condition_json: Optional[str] = Field(None, alias="conditionJson")
    filter_expression_json: Optional[str] = Field(None, alias="filterExpressionJson")
    name: Optional[str] = Field(None)
    price: Optional[float] = Field(None)


class SimpleTaskModel(TimestampedModel):
    """SimpleTaskModel model"""

    id: Optional[int] = Field(None)
    job_id: Optional[str] = Field(None, alias="jobId")
    task_code: str = Field(..., alias="taskCode", min_length=1)
    planned_start_date: Optional[datetime] = Field(None, alias="plannedStartDate")
    initial_note: Optional[InitialNoteModel] = Field(None, alias="initialNote")
    work_time_logs: Optional[List["WorkTimeLog"]] = Field(None, alias="workTimeLogs")
    notes: Optional[List["JobTaskNote"]] = Field(None)
    time_log: Optional["TimeLogModel"] = Field(None, alias="timeLog")


class SoldToDetails(CompanyRelatedModel):
    """SoldToDetails model"""

    contact_name: Optional[str] = Field(None, alias="contactName")
    phone_number: Optional[str] = Field(None, alias="phoneNumber")
    email_address: Optional[str] = Field(None, alias="emailAddress")
    address: Optional["SoldToAddress"] = Field(None)
    tax_id: Optional[str] = Field(None, alias="taxId")


class SortBy(ABConnectBaseModel):
    """SortBy model"""

    sort_dir: bool = Field(..., alias="sortDir")
    sort_by_field: SortByField = Field(..., alias="sortByField")


class SortByModel(ABConnectBaseModel):
    """SortByModel model"""

    sort_dir: bool = Field(..., alias="sortDir")
    sort_by_field: SortByField = Field(..., alias="sortByField")


class SortingInfo(ABConnectBaseModel):
    """SortingInfo model"""

    selector: Optional[str] = Field(None)
    desc: Optional[bool] = Field(None)


class StoredProcedureColumn(ABConnectBaseModel):
    """StoredProcedureColumn model"""

    data_field: Optional[str] = Field(None, alias="dataField")
    data_type: Optional[str] = Field(None, alias="dataType")


class StringMergePreviewDataItem(ABConnectBaseModel):
    """StringMergePreviewDataItem model"""

    data: Optional[str] = Field(None)
    label: Optional[str] = Field(None)
    is_base_contact_item: Optional[bool] = Field(None, alias="isBaseContactItem")


class StringOverridable(ABConnectBaseModel):
    """StringOverridable model"""

    default_value: Optional[str] = Field(None, alias="defaultValue")
    override_value: Optional[str] = Field(None, alias="overrideValue")
    force_empty: Optional[bool] = Field(None, alias="forceEmpty")
    value: Optional[str] = Field(None)


class SummaryInfo(ABConnectBaseModel):
    """SummaryInfo model"""

    selector: Optional[str] = Field(None)
    summary_type: Optional[str] = Field(None, alias="summaryType")


class TaskTruckInfo(IdentifiedModel):
    """TaskTruckInfo model"""

    name: Optional[str] = Field(None)
    is_active: Optional[bool] = Field(None, alias="isActive")


class TaxOption(ABConnectBaseModel):
    """TaxOption model"""

    is_taxable: Optional[bool] = Field(None, alias="isTaxable")
    tax_percent: Optional[float] = Field(None, alias="taxPercent")


class TeamWWAccountData(ABConnectBaseModel):
    """TeamWWAccountData model"""

    api_key: Optional[str] = Field(None, alias="apiKey", min_length=0, max_length=48)


class TimeLog(IdentifiedModel):
    """TimeLog model"""

    start: Optional[datetime] = Field(None)
    end: Optional[datetime] = Field(None)
    pauses: Optional[List["TimeLogPause"]] = Field(None)


class TimeLogModel(IdentifiedModel):
    """TimeLogModel model"""

    start: Optional[datetime] = Field(None)
    end: Optional[datetime] = Field(None)
    pauses: Optional[List["TimeLogPauseModel"]] = Field(None)


class TimeLogPause(IdentifiedModel):
    """TimeLogPause model"""

    start: Optional[datetime] = Field(None)
    end: Optional[datetime] = Field(None)


class TimeLogPauseModel(IdentifiedModel):
    """TimeLogPauseModel model"""

    start: Optional[datetime] = Field(None)
    end: Optional[datetime] = Field(None)


class TimeSpan(ABConnectBaseModel):
    """TimeSpan model"""

    ticks: Optional[int] = Field(None)
    days: Optional[int] = Field(None)
    hours: Optional[int] = Field(None)
    milliseconds: Optional[int] = Field(None)
    minutes: Optional[int] = Field(None)
    seconds: Optional[int] = Field(None)
    total_days: Optional[float] = Field(None, alias="totalDays")
    total_hours: Optional[float] = Field(None, alias="totalHours")
    total_milliseconds: Optional[float] = Field(None, alias="totalMilliseconds")
    total_minutes: Optional[float] = Field(None, alias="totalMinutes")
    total_seconds: Optional[float] = Field(None, alias="totalSeconds")


class TrackingCarrierProps(ABConnectBaseModel):
    """TrackingCarrierProps model"""

    code: Optional[str] = Field(None)
    city: Optional[str] = Field(None)
    state: Optional[str] = Field(None)
    message: Optional[str] = Field(None)


class TrackingStatusV2(ABConnectBaseModel):
    """TrackingStatusV2 model"""

    date: Optional[datetime] = Field(None)
    code: Optional[str] = Field(None)
    message: Optional[str] = Field(None)
    priority: Optional[int] = Field(None)
    carrier_props: Optional[TrackingCarrierProps] = Field(None, alias="carrierProps")


class TransportationCharges(ABConnectBaseModel):
    """TransportationCharges model"""

    base_trip_fee: Optional[float] = Field(None, alias="baseTripFee")
    base_trip_mile: Optional[float] = Field(None, alias="baseTripMile")
    extra_fee: Optional[float] = Field(None, alias="extraFee")
    fuel_surcharge: Optional[float] = Field(None, alias="fuelSurcharge")


class TransportationRatesRequest(ABConnectBaseModel):
    """TransportationRatesRequest model"""

    ship_out_date: Optional[datetime] = Field(None, alias="shipOutDate")
    rates_sources: Optional[List[CarrierAPI]] = Field(None, alias="ratesSources")
    settings_key: Optional[str] = Field(None, alias="settingsKey")
    override_parcel_items: Optional[List["ParcelItem"]] = Field(None, alias="overrideParcelItems")


class UPSAccountData(ABConnectBaseModel):
    """UPSAccountData model"""

    access_license_number: Optional[str] = Field(None, alias="accessLicenseNumber", min_length=0, max_length=48)
    user_name: Optional[str] = Field(None, alias="userName", min_length=0, max_length=48)
    password: Optional[str] = Field(None, min_length=0, max_length=128)
    shipper_number: Optional[str] = Field(None, alias="shipperNumber", min_length=0, max_length=48)
    client_id: Optional[str] = Field(None, alias="clientId", min_length=0, max_length=512)
    client_secret: Optional[str] = Field(None, alias="clientSecret", min_length=0, max_length=512)
    use_new_api: Optional[bool] = Field(None, alias="useNewApi")


class UPSSpecific(ABConnectBaseModel):
    """UPSSpecific model"""

    reason_for_export: Optional[str] = Field(None, alias="reasonForExport")
    shipper_memo: Optional[str] = Field(None, alias="shipperMemo")
    invoice_date: Optional[datetime] = Field(None, alias="invoiceDate")
    description_on_label: Optional[str] = Field(None, alias="descriptionOnLabel")


class USPSAccountData(ABConnectBaseModel):
    """USPSAccountData model"""

    account_number: Optional[str] = Field(None, alias="accountNumber", min_length=0, max_length=48)
    customer_registration_id: Optional[str] = Field(None, alias="customerRegistrationId", min_length=0, max_length=18)
    mailer_id: Optional[str] = Field(None, alias="mailerId", min_length=0, max_length=9)
    mailer_id_code: Optional[str] = Field(None, alias="mailerIdCode", min_length=0, max_length=9)
    client_id: Optional[str] = Field(None, alias="clientId", min_length=0, max_length=512)
    client_secret: Optional[str] = Field(None, alias="clientSecret", min_length=0, max_length=512)


class USPSSpecific(ABConnectBaseModel):
    """USPSSpecific model"""

    aesitn: Optional[str] = Field(None)
    content_comments: Optional[str] = Field(None, alias="contentComments")
    reason_for_export: Optional[str] = Field(None, alias="reasonForExport")


class UpdateDateModel(ABConnectBaseModel):
    """UpdateDateModel model"""

    value: Optional[datetime] = Field(None)


class UpdateTruckModel(ABConnectBaseModel):
    """UpdateTruckModel model"""

    value: Optional[int] = Field(None)


class WeightInfo(ABConnectBaseModel):
    """WeightInfo model"""

    pounds: Optional[float] = Field(None)
    original_weight: Optional[float] = Field(None, alias="originalWeight")
    original_weight_measure_unit: Optional[str] = Field(None, alias="originalWeightMeasureUnit")


class WorkTimeLog(IdentifiedModel):
    """WorkTimeLog model"""

    date: Optional[datetime] = Field(None)
    start_time: Optional[TimeSpan] = Field(None, alias="startTime")
    end_time: Optional[TimeSpan] = Field(None, alias="endTime")


class MaerskAccountData(ABConnectBaseModel):
    """Maersk carrier account data """

    location_id: Optional[int] = Field(None, alias="locationId", description="Location ID")
    tariff_header_id: Optional[int] = Field(None, alias="tariffHeaderId", description="Tariff header ID")
    user_name: Optional[str] = Field(None, alias="userName", max_length=48, description="Account username")
    password: Optional[str] = Field(None, max_length=128, description="Account password")
    address_id: Optional[int] = Field(None, alias="addressId", description="Address ID")
    control_station: Optional[str] = Field(None, alias="controlStation", max_length=32, description="Control station")


__all__ = ['AccesorialCharges', 'AutoCompleteValue', 'Base64File', 'BaseTask', 'BookShipmentSpecificParams', 'CalendarItem', 'CalendarNotes', 'CalendarTask', 'CarrierAccountInfo', 'CarrierInfo', 'CarrierProviderMessage', 'CarrierRateModel', 'CarrierTaskModel', 'Commodity', 'CreatedTask', 'CustomerInfo', 'Details', 'DocumentDetails', 'EmailDetails', 'EstesAccountData', 'ExportPackingInfo', 'ExportTotalCosts', 'ExpressFreightDetail', 'FedExAccountData', 'FedExRestApiAccount', 'FedExSpecific', 'ForwardAirAccountData', 'FranchiseeCarrierAccounts', 'GlobalTranzAccountData', 'GroupingInfo', 'HandlingUnitModel', 'InTheFieldTaskModel', 'InitialNoteModel', 'InsuranceOption', 'ItemTotals', 'Items', 'JToken', 'LaborCharges', 'LastObtainNFM', 'LatLng', 'LookupItem', 'MaerskAccountData', 'MasterMaterials', 'NameValueEntity', 'ObtainNFMParcelItem', 'ObtainNFMParcelService', 'OnlinePaymentSettings', 'PackagingLaborHours', 'PageOrderedRequestModel', 'PhoneDetails', 'PickupLaborHoursRule', 'PilotAccountData', 'PlannerLabor', 'QuoteRequestComment', 'RequestedParcelPackaging', 'RoadRunnerAccountData', 'RoyaltiesCharges', 'SearchCustomerInfo', 'ServiceBaseResponse', 'ServiceInfo', 'ServicePricingsMarkup', 'ServiceWarningResponse', 'ShipmentTrackingDocument', 'ShippingHistoryStatus', 'ShippingPackageInfo', 'SimplePriceTariff', 'SimpleTaskModel', 'SoldToDetails', 'SortBy', 'SortByModel', 'SortingInfo', 'StoredProcedureColumn', 'StringMergePreviewDataItem', 'StringOverridable', 'SummaryInfo', 'TaskTruckInfo', 'TaxOption', 'TeamWWAccountData', 'TimeLog', 'TimeLogModel', 'TimeLogPause', 'TimeLogPauseModel', 'TimeSpan', 'TrackingCarrierProps', 'TrackingStatusV2', 'TransportationCharges', 'TransportationRatesRequest', 'UPSAccountData', 'UPSSpecific', 'USPSAccountData', 'USPSSpecific', 'UpdateDateModel', 'UpdateTruckModel', 'WeightInfo', 'WorkTimeLog']
