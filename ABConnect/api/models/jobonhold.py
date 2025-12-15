"""Jobonhold models for ABConnect API."""

from __future__ import annotations  # Enable forward references
from typing import List, Optional, TYPE_CHECKING
from datetime import datetime
from pydantic import Field
from .base import ABConnectBaseModel, IdentifiedModel, TimestampedModel

if TYPE_CHECKING:
    from .job import CreateScheduledJobEmailResponse

class ExtendedOnHoldInfo(IdentifiedModel):
    """ExtendedOnHoldInfo model"""

    responsible_party_type_id: Optional[str] = Field(None, alias="responsiblePartyTypeId")
    reason_id: Optional[str] = Field(None, alias="reasonId")
    responsible_party: Optional[str] = Field(None, alias="responsibleParty")
    reason: Optional[str] = Field(None)
    comment: Optional[str] = Field(None)
    start_date: Optional[datetime] = Field(None, alias="startDate")
    created_by: Optional[str] = Field(None, alias="createdBy")
    created_by_contact_id: Optional[int] = Field(None, alias="createdByContactId")
    created_by_job_relation: Optional[str] = Field(None, alias="createdByJobRelation")
    resolved_date: Optional[datetime] = Field(None, alias="resolvedDate")


class OnHoldDetails(IdentifiedModel):
    """OnHoldDetails model"""

    responsible_party_type_id: Optional[str] = Field(None, alias="responsiblePartyTypeId")
    reason_id: Optional[str] = Field(None, alias="reasonId")
    start_date: Optional[datetime] = Field(None, alias="startDate")
    next_step_id: Optional[str] = Field(None, alias="nextStepId")
    due_date: Optional[datetime] = Field(None, alias="dueDate")
    assigned_to_id: Optional[int] = Field(None, alias="assignedToId")
    resolved_date: Optional[datetime] = Field(None, alias="resolvedDate")
    resolved_code_id: Optional[str] = Field(None, alias="resolvedCodeId")
    is_active: Optional[bool] = Field(None, alias="isActive")
    created_by_contact_id: Optional[int] = Field(None, alias="createdByContactId")
    created_by_contact_name: Optional[str] = Field(None, alias="createdByContactName")
    notes: Optional[List[OnHoldNoteDetails]] = Field(None)
    responsible_party: Optional[str] = Field(None, alias="responsibleParty")
    reason: Optional[str] = Field(None)
    comment: Optional[str] = Field(None)


class OnHoldNoteDetails(TimestampedModel):
    """OnHoldNoteDetails model"""

    comment: Optional[str] = Field(None)


class OnHoldUser(ABConnectBaseModel):
    """OnHoldUser model"""

    contact_id: Optional[int] = Field(None, alias="contactId")
    full_name: Optional[str] = Field(None, alias="fullName")
    job_relation: Optional[str] = Field(None, alias="jobRelation")


class ResolveJobOnHoldResponse(ABConnectBaseModel):
    """ResolveJobOnHoldResponse model"""

    success: Optional[bool] = Field(None)
    error_message: Optional[str] = Field(None, alias="errorMessage")
    total_on_hold_days: Optional[int] = Field(None, alias="totalOnHoldDays")


class SaveOnHoldDatesModel(ABConnectBaseModel):
    """SaveOnHoldDatesModel model"""

    start_date: datetime = Field(..., alias="startDate")
    resolved_date: datetime = Field(..., alias="resolvedDate")


class SaveOnHoldRequest(ABConnectBaseModel):
    """SaveOnHoldRequest model"""

    responsible_party_type_id: str = Field(..., alias="responsiblePartyTypeId")
    reason_id: str = Field(..., alias="reasonId")
    comment: Optional[str] = Field(None, min_length=0, max_length=1024)
    next_step_id: Optional[str] = Field(None, alias="nextStepId")
    due_date: Optional[datetime] = Field(None, alias="dueDate")
    assigned_to_id: Optional[int] = Field(None, alias="assignedToId")
    resolved_date: Optional[datetime] = Field(None, alias="resolvedDate")
    resolved_code_id: Optional[str] = Field(None, alias="resolvedCodeId")
    start_date: Optional[datetime] = Field(None, alias="startDate")


class SaveOnHoldResponse(ABConnectBaseModel):
    """SaveOnHoldResponse model"""

    success: Optional[bool] = Field(None)
    error_message: Optional[str] = Field(None, alias="errorMessage")
    details: Optional[OnHoldDetails] = Field(None)
    follow_up_email_result: Optional[CreateScheduledJobEmailResponse] = Field(None, alias="followUpEmailResult")
    total_on_hold_days: Optional[int] = Field(None, alias="totalOnHoldDays")


__all__ = ['ExtendedOnHoldInfo', 'OnHoldDetails', 'OnHoldNoteDetails', 'OnHoldUser', 'ResolveJobOnHoldResponse', 'SaveOnHoldDatesModel', 'SaveOnHoldRequest', 'SaveOnHoldResponse']
