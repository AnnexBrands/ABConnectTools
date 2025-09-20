"""Jobsmstemplate models for ABConnect API."""

from typing import List, Optional
from pydantic import Field
from .base import IdentifiedModel

class SmsTemplateModel(IdentifiedModel):
    """SmsTemplateModel model"""

    name: Optional[str] = Field(None, min_length=0, max_length=500)
    message: Optional[str] = Field(None, min_length=0, max_length=1024)
    is_active: Optional[bool] = Field(None, alias="isActive")
    send_automatically: Optional[bool] = Field(None, alias="sendAutomatically")
    company_id: Optional[str] = Field(None, alias="companyId")
    job_statuses: Optional[List[str]] = Field(None, alias="jobStatuses")
    job_autosend_statuses: Optional[List[str]] = Field(None, alias="jobAutosendStatuses")


__all__ = ['SmsTemplateModel']
