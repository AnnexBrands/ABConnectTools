"""Shipment models for ABConnect API."""

from typing import List, Optional
from datetime import datetime
from pydantic import Field
from .base import ABConnectBaseModel

class ShipmentDetails(ABConnectBaseModel):
    """ShipmentDetails model"""

    pro_number: Optional[str] = Field(None, alias="proNumber")
    used_api: Optional[CarrierAPI] = Field(None, alias="usedApi")
    history_provider_name: Optional[str] = Field(None, alias="historyProviderName")
    history_statuses: Optional[List[ShippingHistoryStatus]] = Field(None, alias="historyStatuses")
    weight: Optional[WeightInfo] = Field(None)
    job_weight: Optional[WeightInfo] = Field(None, alias="jobWeight")
    successfully: Optional[bool] = Field(None)
    error_message: Optional[str] = Field(None, alias="errorMessage")
    multiple_shipments: Optional[bool] = Field(None, alias="multipleShipments")
    packages: Optional[List[ShippingPackageInfo]] = Field(None)
    estimated_delivery: Optional[datetime] = Field(None, alias="estimatedDelivery")


class ShippingDocument(ABConnectBaseModel):
    """ShippingDocument model"""

    success: Optional[bool] = Field(None)
    error_message: Optional[str] = Field(None, alias="errorMessage")
    document_bytes: Optional[str] = Field(None, alias="documentBytes")
    document_type: Optional[str] = Field(None, alias="documentType")
    file_name: Optional[str] = Field(None, alias="fileName")


__all__ = ['ShipmentDetails', 'ShippingDocument']
