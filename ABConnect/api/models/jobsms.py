"""Jobsms models for ABConnect API."""

from typing import List, Optional
from pydantic import Field
from .base import ABConnectBaseModel


class SendSMSModel(ABConnectBaseModel):
    """SendSMSModel model"""

    phone: Optional[str] = Field(None)
    body: Optional[str] = Field(None)


class MarkSmsAsReadModel(ABConnectBaseModel):
    """Model for marking SMS messages as read.

    .. versionadded:: 709
    """

    sms_ids: Optional[List[int]] = Field(None, alias="smsIds", description="List of SMS IDs to mark as read")


__all__ = ['MarkSmsAsReadModel', 'SendSMSModel']
