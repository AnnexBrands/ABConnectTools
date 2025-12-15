"""Jobtracking models for ABConnect API."""

from __future__ import annotations
from typing import List, Optional, TYPE_CHECKING
from pydantic import Field
from .base import ABConnectBaseModel
from .shared import ShipmentTrackingDocument

if TYPE_CHECKING:
    from .shipment import ShipmentDetails

class ShipmentTrackingDetails(ABConnectBaseModel):
    """ShipmentTrackingDetails model"""

    shipment_details: Optional[ShipmentDetails] = Field(None, alias="shipmentDetails")
    documents: Optional[List[ShipmentTrackingDocument]] = Field(None)


__all__ = ['ShipmentTrackingDetails']
