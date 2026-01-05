"""Notifications models for ABConnect API."""

from typing import Optional
from pydantic import Field
from .base import ABConnectBaseModel


class NotificationsResponse(ABConnectBaseModel):
    """Response model for GET /notifications endpoint."""

    rfq_notification_exists: Optional[bool] = Field(None, alias="rfqNotificationExists")


__all__ = ['NotificationsResponse']
