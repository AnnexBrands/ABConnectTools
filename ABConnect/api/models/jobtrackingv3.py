"""Jobtrackingv3 models for ABConnect API."""

from __future__ import annotations
from typing import List, Optional
from pydantic import Field
from .base import ABConnectBaseModel
from .shared import TrackingStatusV2, CarrierInfo

class JobTrackingResponseV3(ABConnectBaseModel):
    """JobTrackingResponseV3 model"""

    statuses: Optional[List[TrackingStatusV2]] = Field(None)
    carriers: Optional[List[CarrierInfo]] = Field(None)


__all__ = ['JobTrackingResponseV3']
