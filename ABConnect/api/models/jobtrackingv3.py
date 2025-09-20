"""Jobtrackingv3 models for ABConnect API."""

from typing import List, Optional
from pydantic import Field
from .base import ABConnectBaseModel

class JobTrackingResponseV3(ABConnectBaseModel):
    """JobTrackingResponseV3 model"""

    statuses: Optional[List[TrackingStatusV2]] = Field(None)
    carriers: Optional[List[CarrierInfo]] = Field(None)


__all__ = ['JobTrackingResponseV3']
