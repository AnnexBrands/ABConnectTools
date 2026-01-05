"""Dashboard models for ABConnect API."""

from typing import List, Optional
from datetime import datetime
from pydantic import Field
from .base import ABConnectBaseModel, CompanyRelatedModel, JobRelatedModel
from .shared import JToken
from .enums import DashboardType

class GridSettingsEntity(ABConnectBaseModel):
    """GridSettingsEntity model"""

    range_months: Optional[List[JToken]] = Field(None, alias="rangeMonths")
    columns: Optional[List[JToken]] = Field(None)


class InboundNewDashboardItem(CompanyRelatedModel):
    """InboundNewDashboardItem model"""

    job_id: Optional[str] = Field(None, alias="jobId")
    job_display_id: Optional[int] = Field(None, alias="jobDisplayId")
    current_job_status: Optional[str] = Field(None, alias="currentJobStatus")
    unread_inbound_exists: Optional[bool] = Field(None, alias="unreadInboundExists")
    important_note_exists: Optional[bool] = Field(None, alias="importantNoteExists")
    usar_signed: Optional[bool] = Field(None, alias="usarSigned")
    payment_state: Optional[int] = Field(None, alias="paymentState")
    action_required: Optional[bool] = Field(None, alias="actionRequired")
    rfq_state: Optional[int] = Field(None, alias="rfqState")
    is_quick_sale: Optional[bool] = Field(None, alias="isQuickSale")
    intacct_status: Optional[str] = Field(None, alias="intacctStatus")
    pickup_agent_company: Optional[str] = Field(None, alias="pickupAgentCompany")
    pickup_city: Optional[str] = Field(None, alias="pickupCity")
    pickup_zip: Optional[str] = Field(None, alias="pickupZip")
    dest_city: Optional[str] = Field(None, alias="destCity")
    dest_zip: Optional[str] = Field(None, alias="destZip")
    pickup_date: Optional[datetime] = Field(None, alias="pickupDate")
    franchisee: Optional[str] = Field(None)
    customer_name: Optional[str] = Field(None, alias="customerName")
    pick_up_zone: Optional[int] = Field(None, alias="pickUpZone")
    job_price: Optional[float] = Field(None, alias="jobPrice")
    other_ref_no: Optional[str] = Field(None, alias="otherRefNo")
    created_by: Optional[str] = Field(None, alias="createdBy")
    sales_rep: Optional[str] = Field(None, alias="salesRep")
    number_of_men: Optional[int] = Field(None, alias="numberOfMen")
    trip_time: Optional[float] = Field(None, alias="tripTime")
    on_site_time: Optional[float] = Field(None, alias="onSiteTime")
    follow_up_pipeline_id: Optional[str] = Field(None, alias="followUpPipelineId")
    follow_up_heat_id: Optional[str] = Field(None, alias="followUpHeatId")
    follow_up_due_date: Optional[datetime] = Field(None, alias="followUpDueDate")
    is_job_on_hold: Optional[bool] = Field(None, alias="isJobOnHold")


class IncrementJobStatusInputModel(JobRelatedModel):
    """IncrementJobStatusInputModel model"""

    client_date_time: Optional[datetime] = Field(None, alias="clientDateTime")


class IncrementJobStatusResponseModel(ABConnectBaseModel):
    """IncrementJobStatusResponseModel model"""

    message: Optional[str] = Field(None)
    can_undo: Optional[bool] = Field(None, alias="canUndo")
    intact_send_required: Optional[bool] = Field(None, alias="intactSendRequired")


class InhouseNewDashboardItem(CompanyRelatedModel):
    """InhouseNewDashboardItem model"""

    job_id: Optional[str] = Field(None, alias="jobId")
    job_display_id: Optional[int] = Field(None, alias="jobDisplayId")
    is_quick_sale: Optional[bool] = Field(None, alias="isQuickSale")
    current_job_status: Optional[str] = Field(None, alias="currentJobStatus")
    intacct_status: Optional[str] = Field(None, alias="intacctStatus")
    franchisee: Optional[str] = Field(None)
    origin_city: Optional[str] = Field(None, alias="originCity")
    dest_city: Optional[str] = Field(None, alias="destCity")
    dest_zip: Optional[str] = Field(None, alias="destZip")
    pickup_date: Optional[datetime] = Field(None, alias="pickupDate")
    customer_name: Optional[str] = Field(None, alias="customerName")
    other_ref_no: Optional[str] = Field(None, alias="otherRefNo")
    created_by: Optional[str] = Field(None, alias="createdBy")
    sales_rep: Optional[str] = Field(None, alias="salesRep")
    days_inhouse: Optional[int] = Field(None, alias="daysInhouse")
    ship_out_by: Optional[datetime] = Field(None, alias="shipOutBy")
    eta: Optional[datetime] = Field(None)
    delivery_dead_line: Optional[datetime] = Field(None, alias="deliveryDeadLine")
    job_price: Optional[float] = Field(None, alias="jobPrice")
    carrier_name: Optional[str] = Field(None, alias="carrierName")
    unread_inbound_exists: Optional[bool] = Field(None, alias="unreadInboundExists")
    follow_up_pipeline_id: Optional[str] = Field(None, alias="followUpPipelineId")
    follow_up_heat_id: Optional[str] = Field(None, alias="followUpHeatId")
    follow_up_due_date: Optional[datetime] = Field(None, alias="followUpDueDate")
    is_job_on_hold: Optional[bool] = Field(None, alias="isJobOnHold")
    labor_hrs: Optional[str] = Field(None, alias="laborHrs")


class LocalDeliveriesNewDashboardItem(JobRelatedModel):
    """LocalDeliveriesNewDashboardItem model"""

    job_display_id: Optional[int] = Field(None, alias="jobDisplayId")
    current_job_status: Optional[str] = Field(None, alias="currentJobStatus")
    intacct_status: Optional[str] = Field(None, alias="intacctStatus")
    delivery_zone: Optional[int] = Field(None, alias="deliveryZone")
    delivery_contact: Optional[str] = Field(None, alias="deliveryContact")
    delivery_company: Optional[str] = Field(None, alias="deliveryCompany")
    dest_city: Optional[str] = Field(None, alias="destCity")
    dest_zip: Optional[str] = Field(None, alias="destZip")
    delivery_scheduled_start: Optional[datetime] = Field(None, alias="deliveryScheduledStart")
    delivery_scheduled_end: Optional[datetime] = Field(None, alias="deliveryScheduledEnd")
    delivery_complete: Optional[str] = Field(None, alias="deliveryComplete")
    note: Optional[str] = Field(None)
    pro_num: Optional[str] = Field(None, alias="proNum")
    transportation_state: Optional[int] = Field(None, alias="transportationState")
    transportation_state_description: Optional[str] = Field(None, alias="transportationStateDescription")
    number_of_men: Optional[int] = Field(None, alias="numberOfMen")
    trip_time: Optional[float] = Field(None, alias="tripTime")
    on_site_time: Optional[float] = Field(None, alias="onSiteTime")
    unread_inbound_exists: Optional[bool] = Field(None, alias="unreadInboundExists")
    important_note_exists: Optional[bool] = Field(None, alias="importantNoteExists")
    usar_signed: Optional[bool] = Field(None, alias="usarSigned")
    payment_state: Optional[int] = Field(None, alias="paymentState")
    sales_rep: Optional[str] = Field(None, alias="salesRep")


class OutboundNewDashboardItem(CompanyRelatedModel):
    """OutboundNewDashboardItem model"""

    job_id: Optional[str] = Field(None, alias="jobId")
    job_display_id: Optional[int] = Field(None, alias="jobDisplayId")
    is_quick_sale: Optional[bool] = Field(None, alias="isQuickSale")
    current_job_status: Optional[str] = Field(None, alias="currentJobStatus")
    intacct_status: Optional[str] = Field(None, alias="intacctStatus")
    franchisee: Optional[str] = Field(None)
    dest_city: Optional[str] = Field(None, alias="destCity")
    dest_zip: Optional[str] = Field(None, alias="destZip")
    pickup_date: Optional[datetime] = Field(None, alias="pickupDate")
    total_days: Optional[int] = Field(None, alias="totalDays")
    delivery_dead_line: Optional[datetime] = Field(None, alias="deliveryDeadLine")
    days_to_del_dead_line: Optional[int] = Field(None, alias="daysToDelDeadLine")
    carrier_name: Optional[str] = Field(None, alias="carrierName")
    eta: Optional[datetime] = Field(None)
    customer_name: Optional[str] = Field(None, alias="customerName")
    job_price: Optional[float] = Field(None, alias="jobPrice")
    pro_num: Optional[str] = Field(None, alias="proNum")
    transportation_state: Optional[int] = Field(None, alias="transportationState")
    transportation_state_description: Optional[str] = Field(None, alias="transportationStateDescription")
    other_ref_no: Optional[str] = Field(None, alias="otherRefNo")
    created_by: Optional[str] = Field(None, alias="createdBy")
    sales_rep: Optional[str] = Field(None, alias="salesRep")
    unread_inbound_exists: Optional[bool] = Field(None, alias="unreadInboundExists")
    follow_up_pipeline_id: Optional[str] = Field(None, alias="followUpPipelineId")
    follow_up_heat_id: Optional[str] = Field(None, alias="followUpHeatId")
    follow_up_due_date: Optional[datetime] = Field(None, alias="followUpDueDate")
    is_job_on_hold: Optional[bool] = Field(None, alias="isJobOnHold")
    shipped: Optional[datetime] = Field(None)


class RecentEstimatesNewDashboardItem(CompanyRelatedModel):
    """RecentEstimatesNewDashboardItem model"""

    job_id: Optional[str] = Field(None, alias="jobId")
    job_display_id: Optional[int] = Field(None, alias="jobDisplayId")
    job_status_id: Optional[str] = Field(None, alias="jobStatusId")
    current_job_status: Optional[str] = Field(None, alias="currentJobStatus")
    customer_name: Optional[str] = Field(None, alias="customerName")
    sales_rep: Optional[str] = Field(None, alias="salesRep")
    item: Optional[str] = Field(None)
    franchisee: Optional[str] = Field(None)
    job_price: Optional[float] = Field(None, alias="jobPrice")
    quoted_date: Optional[datetime] = Field(None, alias="quotedDate")
    other_ref_no: Optional[str] = Field(None, alias="otherRefNo")
    created_by: Optional[str] = Field(None, alias="createdBy")
    rfq_state: Optional[int] = Field(None, alias="rfqState")


class SaveGridSettingsModel(CompanyRelatedModel):
    """SaveGridSettingsModel model"""

    dashboard_type: DashboardType = Field(..., alias="dashboardType")
    settings: GridSettingsEntity = Field(...)


class UndoIncrementJobStatusInputModel(JobRelatedModel):
    """UndoIncrementJobStatusInputModel model"""
    pass


class DashboardResponse(ABConnectBaseModel):
    """Dashboard response model for GET /dashboard."""

    data: Optional[List[dict]] = Field(default_factory=list, description="Dashboard data items")


__all__ = ['DashboardResponse', 'GridSettingsEntity', 'InboundNewDashboardItem', 'IncrementJobStatusInputModel', 'IncrementJobStatusResponseModel', 'InhouseNewDashboardItem', 'LocalDeliveriesNewDashboardItem', 'OutboundNewDashboardItem', 'RecentEstimatesNewDashboardItem', 'SaveGridSettingsModel', 'UndoIncrementJobStatusInputModel']
