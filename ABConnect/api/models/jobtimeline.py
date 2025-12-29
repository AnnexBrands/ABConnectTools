"""Jobtimeline models for ABConnect API."""

from typing import List, Optional, Union, TYPE_CHECKING
from datetime import datetime
from pydantic import Field
from .base import ABConnectBaseModel, IdentifiedModel, TimestampedModel

# Import models needed for forward reference resolution
from .shared import (
    InitialNoteModel, WorkTimeLog, LookupItem, BaseTask,
    UpdateDateModel, UpdateTruckModel, SimpleTaskModel, CarrierTaskModel,
    InTheFieldTaskModel, TimeLogModel, TaskTruckInfo
)

if TYPE_CHECKING:
    from .jobnote import JobTaskNote
    from .jobonhold import OnHoldDetails

class BaseTaskModel(TimestampedModel):
    """BaseTaskModel model"""

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


class CarrierTask(TimestampedModel):
    """CarrierTask model"""

    id: Optional[int] = Field(None)
    job_id: Optional[str] = Field(None, alias="jobId")
    task_code: Optional[str] = Field(None, alias="taskCode")
    planned_start_date: Optional[datetime] = Field(None, alias="plannedStartDate")
    notes: Optional[List["JobTaskNote"]] = Field(None)
    work_time_logs: Optional[List["WorkTimeLog"]] = Field(None, alias="workTimeLogs")
    scheduled_date: Optional[datetime] = Field(None, alias="scheduledDate")
    pickup_completed_date: Optional[datetime] = Field(None, alias="pickupCompletedDate")
    delivery_completed_date: Optional[datetime] = Field(None, alias="deliveryCompletedDate")
    expected_delivery_date: Optional[datetime] = Field(None, alias="expectedDeliveryDate")
    target_start_date: Optional[datetime] = Field(None, alias="targetStartDate")
    actual_end_date: Optional[datetime] = Field(None, alias="actualEndDate")


class CompanyListItem(IdentifiedModel):
    """CompanyListItem model"""

    code: Optional[str] = Field(None)
    name: Optional[str] = Field(None)
    type_id: Optional[str] = Field(None, alias="typeId")


class DeleteTaskResponse(ABConnectBaseModel):
    """DeleteTaskResponse model"""

    success: Optional[bool] = Field(None)
    error_message: Optional[str] = Field(None, alias="errorMessage")
    job_sub_management_status: Optional["LookupItem"] = Field(None, alias="jobSubManagementStatus")


class SaveResponseModel(ABConnectBaseModel):
    """SaveResponseModel model"""

    success: Optional[bool] = Field(None)
    error_message: Optional[str] = Field(None, alias="errorMessage")
    task_exists: Optional[bool] = Field(None, alias="taskExists")
    task: Optional["BaseTask"] = Field(None)
    email_log_id: Optional[int] = Field(None, alias="emailLogId")
    job_sub_management_status: Optional["LookupItem"] = Field(None, alias="jobSubManagementStatus")


class TimelineResponse(ABConnectBaseModel):
    """TimelineResponse model"""

    success: Optional[bool] = Field(None)
    error_message: Optional[str] = Field(None, alias="errorMessage")
    tasks: Optional[List["BaseTask"]] = Field(None)
    on_holds: Optional[List["OnHoldDetails"]] = Field(None, alias="onHolds")
    days_per_sla: Optional[int] = Field(None, alias="daysPerSla")
    delivery_service_done_by: Optional[str] = Field(None, alias="deliveryServiceDoneBy")
    job_sub_management_status: Optional["LookupItem"] = Field(None, alias="jobSubManagementStatus")
    job_booked_date: Optional[datetime] = Field(None, alias="jobBookedDate")


class UpdateTaskModel(ABConnectBaseModel):
    """UpdateTaskModel model"""

    truck_id: Optional["UpdateTruckModel"] = Field(None, alias="truckId")
    planned_start_date: Optional["UpdateDateModel"] = Field(None, alias="plannedStartDate")
    preferred_start_date: Optional["UpdateDateModel"] = Field(None, alias="preferredStartDate")
    planned_end_date: Optional["UpdateDateModel"] = Field(None, alias="plannedEndDate")
    preferred_end_date: Optional["UpdateDateModel"] = Field(None, alias="preferredEndDate")


# Union type for timeline task input - accepts any task model variant
# The POST /api/job/{jobDisplayId}/timeline endpoint is polymorphic and can accept
# BaseTaskModel, SimpleTaskModel, CarrierTaskModel, or InTheFieldTaskModel
TimelineTaskInput = Union[SimpleTaskModel, CarrierTaskModel, InTheFieldTaskModel, BaseTaskModel]


__all__ = ['BaseTaskModel', 'CarrierTask', 'CompanyListItem', 'DeleteTaskResponse', 'SaveResponseModel', 'TimelineResponse', 'UpdateTaskModel', 'TimelineTaskInput']
