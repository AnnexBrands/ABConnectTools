"""Jobtimeline models for ABConnect API."""

from typing import Annotated, List, Optional, Union
from datetime import datetime
from pydantic import Discriminator, Field, Tag
from .base import ABConnectBaseModel, IdentifiedModel
from .shared import (
    LookupItem, BaseTask, InTheFieldTaskModel, SimpleTaskModel,
    PickupTask, PackagingTask, StorageTask,
    UpdateDateModel, UpdateTruckModel, CarrierTaskModel,
)
from .jobonhold import OnHoldDetails


def _task_discriminator(data):
    """Discriminator function for timeline task types based on taskCode."""
    tc = data.get("taskCode") if isinstance(data, dict) else getattr(data, "task_code", None)
    return {"PU": "PU", "PK": "PK", "ST": "ST", "CP": "CP"}.get(tc, tc)


TimelineTask = Annotated[
    Union[
        Annotated[PickupTask, Tag("PU")],
        Annotated[PackagingTask, Tag("PK")],
        Annotated[StorageTask, Tag("ST")],
        Annotated[CarrierTaskModel, Tag("CP")],
    ],
    Discriminator(_task_discriminator),
]

# Backward compatibility alias
CarrierTask = CarrierTaskModel
BaseTaskModel = CarrierTaskModel


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
    task: Optional[TimelineTask] = Field(None)
    email_log_id: Optional[int] = Field(None, alias="emailLogId")
    job_sub_management_status: Optional["LookupItem"] = Field(None, alias="jobSubManagementStatus")


class TimelineResponse(ABConnectBaseModel):
    """TimelineResponse model"""

    success: Optional[bool] = Field(None)
    error_message: Optional[str] = Field(None, alias="errorMessage")
    tasks: Optional[List[TimelineTask]] = Field(None)
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


# Union type for timeline task input
TimelineTaskInput = Union[PickupTask, PackagingTask, StorageTask, CarrierTaskModel]


__all__ = ['BaseTaskModel', 'CarrierTask', 'CompanyListItem', 'DeleteTaskResponse', 'SaveResponseModel', 'TimelineResponse', 'TimelineTask', 'TimelineTaskInput', 'UpdateTaskModel']
