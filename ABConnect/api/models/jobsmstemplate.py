"""Jobsmstemplate models for ABConnect API."""

from typing import List, Optional
from pydantic import Field
from .base import ABConnectBaseModel, IdentifiedModel


class NotificationToken(ABConnectBaseModel):
    """Individual notification token for SMS templates."""

    notification_token_id: Optional[int] = Field(None, alias="notificationTokenID")
    notification_token: Optional[str] = Field(None, alias="notificationToken")


class NotificationTokenGroup(ABConnectBaseModel):
    """Group of notification tokens for SMS templates."""

    group_name: Optional[str] = Field(None, alias="groupName")
    tokens: Optional[List[NotificationToken]] = Field(None)


class SmsJobStatus(ABConnectBaseModel):
    """Job status option for SMS template configuration."""

    key: Optional[str] = Field(None)
    name: Optional[str] = Field(None)
    value: Optional[str] = Field(None)


class SmsTemplateModel(IdentifiedModel):
    """SmsTemplateModel model"""

    name: Optional[str] = Field(None, min_length=0, max_length=500)
    message: Optional[str] = Field(None, min_length=0, max_length=1024)
    is_active: Optional[bool] = Field(None, alias="isActive")
    send_automatically: Optional[bool] = Field(None, alias="sendAutomatically")
    company_id: Optional[str] = Field(None, alias="companyId")
    job_statuses: Optional[List[str]] = Field(None, alias="jobStatuses")
    job_autosend_statuses: Optional[List[str]] = Field(None, alias="jobAutosendStatuses")


__all__ = ['NotificationToken', 'NotificationTokenGroup', 'SmsJobStatus', 'SmsTemplateModel']
