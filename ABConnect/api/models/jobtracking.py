"""Jobtracking models for ABConnect API."""

from typing import List, Optional
from pydantic import Field
from .base import ABConnectBaseModel

class ShipmentTrackingDetails(ABConnectBaseModel):
    """ShipmentTrackingDetails model"""

    shipment_details: Optional[ShipmentDetails] = Field(None, alias="shipmentDetails")
    documents: Optional[List[ShipmentTrackingDocument]] = Field(None)


__all__ = ['ShipmentTrackingDetails']
