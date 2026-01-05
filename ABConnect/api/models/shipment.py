"""Shipment models for ABConnect API."""

from __future__ import annotations
from typing import List, Optional
from datetime import datetime
from pydantic import Field
from .base import ABConnectBaseModel
from .enums import CarrierAPI
from .shared import ShippingHistoryStatus, WeightInfo, ShippingPackageInfo


class ParcelAddOnRadioOption(ABConnectBaseModel):
    """Radio button option for parcel add-on configuration."""

    description: Optional[str] = Field(None)
    code: Optional[str] = Field(None)


class ParcelAddOnOptionsGroup(ABConnectBaseModel):
    """Options group for parcel add-on with radio button choices."""

    key: Optional[str] = Field(None)
    type: Optional[int] = Field(None)
    radio_button_options: Optional[List[ParcelAddOnRadioOption]] = Field(
        None, alias="radioButtonOptions"
    )


class ParcelAddOn(ABConnectBaseModel):
    """Available parcel add-on/accessorial from GET /shipment/accessorials.

    This represents the catalog of available accessorials that can be
    applied to a shipment. Note: This is different from JobParcelAddOn
    which represents an add-on that has been applied to a specific job.
    """

    unique_id: Optional[str] = Field(None, alias="uniqueId")
    name: Optional[str] = Field(None)
    description: Optional[str] = Field(None)
    price: Optional[str] = Field(None)
    options: Optional[List[ParcelAddOnOptionsGroup]] = Field(None)
    source_apis: Optional[List[CarrierAPI]] = Field(None, alias="sourceAPIs")


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


__all__ = ['ParcelAddOn', 'ParcelAddOnOptionsGroup', 'ParcelAddOnRadioOption', 'ShipmentDetails', 'ShippingDocument']
