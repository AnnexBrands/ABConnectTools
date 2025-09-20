"""Jobsms models for ABConnect API."""

from typing import Optional
from pydantic import Field
from .base import ABConnectBaseModel

class SendSMSModel(ABConnectBaseModel):
    """SendSMSModel model"""

    phone: Optional[str] = Field(None)
    body: Optional[str] = Field(None)


__all__ = ['SendSMSModel']
