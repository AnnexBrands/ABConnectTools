"""Twiliowebhook models for ABConnect API."""

from typing import Optional
from pydantic import Field
from .base import ABConnectBaseModel

class TwilioSmsStatusCallback(ABConnectBaseModel):
    """TwilioSmsStatusCallback model"""

    message_status: Optional[str] = Field(None, alias="messageStatus")
    message_sid: Optional[str] = Field(None, alias="messageSid")


__all__ = ['TwilioSmsStatusCallback']
