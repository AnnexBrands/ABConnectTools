"""Jobnote models for ABConnect API."""

from typing import Optional
from datetime import datetime
from datetime import date
from pydantic import Field
from .base import JobRelatedModel, TimestampedModel

class JobTaskNote(TimestampedModel):
    """JobTaskNote model"""

    id: Optional[int] = Field(None)
    comment: Optional[str] = Field(None)
    is_important: Optional[bool] = Field(None, alias="isImportant")
    is_completed: Optional[bool] = Field(None, alias="isCompleted")
    author: Optional[str] = Field(None)
    modifiy_date: Optional[datetime] = Field(None, alias="modifiyDate")


class TaskNoteModel(JobRelatedModel):
    """TaskNoteModel model"""

    comments: str = Field(..., min_length=1, max_length=8000)
    due_date: Optional[date] = Field(None, alias="dueDate")
    is_important: Optional[bool] = Field(None, alias="isImportant")
    is_completed: Optional[bool] = Field(None, alias="isCompleted")
    send_notification: Optional[bool] = Field(None, alias="sendNotification")
    task_code: str = Field(..., alias="taskCode", min_length=1)


__all__ = ['JobTaskNote', 'TaskNoteModel']
