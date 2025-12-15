"""Carriererrormessage models for ABConnect API."""

from __future__ import annotations
from typing import Optional
from pydantic import Field
from .base import FullAuditModel
from .enums import CarrierAPI

class CarrierErrorMessage(FullAuditModel):
    """CarrierErrorMessage model"""

    rate_source: Optional[CarrierAPI] = Field(None, alias="rateSource")
    code: Optional[str] = Field(None)
    message: Optional[str] = Field(None)


__all__ = ['CarrierErrorMessage']
