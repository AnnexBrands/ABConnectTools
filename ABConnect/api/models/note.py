"""Note models for ABConnect API."""

from __future__ import annotations
from typing import List, Optional
from datetime import datetime
from datetime import date
from pydantic import Field
from .base import CompanyRelatedModel, IdentifiedModel, TimestampedModel

class NoteModel(CompanyRelatedModel):
    """NoteModel model"""

    comments: str = Field(..., min_length=1, max_length=8000)
    due_date: Optional[date] = Field(None, alias="dueDate")
    is_important: Optional[bool] = Field(None, alias="isImportant")
    is_completed: Optional[bool] = Field(None, alias="isCompleted")
    job_id: Optional[str] = Field(None, alias="jobId")
    send_notification: Optional[bool] = Field(None, alias="sendNotification")
    category: str = Field(...)
    assigned_users: Optional[List[SuggestedContactEntity]] = Field(None, alias="assignedUsers")
    crm_contact_id: Optional[int] = Field(None, alias="crmContactId")
    is_global: Optional[bool] = Field(None, alias="isGlobal")
    is_shared: Optional[bool] = Field(None, alias="isShared")


class Notes(TimestampedModel):
    """Notes model"""

    note_id: Optional[int] = Field(None, alias="noteId")
    is_important: Optional[bool] = Field(None, alias="isImportant")
    comments: Optional[str] = Field(None)
    category: Optional[str] = Field(None)
    due_date: Optional[datetime] = Field(None, alias="dueDate")
    job_id: Optional[str] = Field(None, alias="jobId")
    crm_contact_id: Optional[int] = Field(None, alias="crmContactId")
    contact_id: Optional[str] = Field(None, alias="contactId")
    company_id: Optional[str] = Field(None, alias="companyId")
    user_id: Optional[str] = Field(None, alias="userId")
    importance: Optional[str] = Field(None)
    author: Optional[str] = Field(None)
    due_dates: Optional[str] = Field(None, alias="dueDates")
    category_name: Optional[str] = Field(None, alias="categoryName")
    modifiy_date: Optional[datetime] = Field(None, alias="modifiyDate")
    franchise_id: Optional[str] = Field(None, alias="franchiseId")
    is_completed: Optional[bool] = Field(None, alias="isCompleted")
    is_global: Optional[bool] = Field(None, alias="isGlobal")
    is_shared: Optional[bool] = Field(None, alias="isShared")
    assigned_contact_names: Optional[List[str]] = Field(None, alias="assignedContactNames")
    assigned_users: Optional[List[SuggestedContactEntity]] = Field(None, alias="assignedUsers")
    is_job_level: Optional[bool] = Field(None, alias="isJobLevel")


class SuggestedContactEntity(IdentifiedModel):
    """SuggestedContactEntity model"""

    full_name: Optional[str] = Field(None, alias="fullName")


__all__ = ['NoteModel', 'Notes', 'SuggestedContactEntity']
