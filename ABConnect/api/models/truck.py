"""Truck models for ABConnect API."""

from typing import Optional
from pydantic import Field
from .base import ActiveModel, IdentifiedModel
from .shared import ServiceBaseResponse, ServiceWarningResponse  # noqa: F401 - re-exported


class SaveEntityResponse(IdentifiedModel, ServiceBaseResponse):
    """Response model for save operations that return an entity ID.

    Combines IdentifiedModel (id field) with ServiceBaseResponse (success/error).
    """
    pass


class SaveTruckRequest(ActiveModel):
    """SaveTruckRequest model"""

    name: Optional[str] = Field(None)
    length: Optional[float] = Field(None)
    width: Optional[float] = Field(None)
    height: Optional[float] = Field(None)
    max_weight: Optional[float] = Field(None, alias="maxWeight")
    price_per_mile: Optional[float] = Field(None, alias="pricePerMile")
    cubes_capacity: Optional[int] = Field(None, alias="cubesCapacity")
    shared_for_children: Optional[bool] = Field(None, alias="sharedForChildren")


class Truck(IdentifiedModel):
    """Truck model"""

    company_id: Optional[str] = Field(None, alias="companyId")
    name: Optional[str] = Field(None)
    length: Optional[float] = Field(None)
    width: Optional[float] = Field(None)
    height: Optional[float] = Field(None)
    max_weight: Optional[float] = Field(None, alias="maxWeight")
    price_per_mile: Optional[float] = Field(None, alias="pricePerMile")
    cubes_capacity: Optional[int] = Field(None, alias="cubesCapacity")
    is_active: Optional[bool] = Field(None, alias="isActive")
    shared_for_children: Optional[bool] = Field(None, alias="sharedForChildren")
    available_cubes: Optional[float] = Field(None, alias="availableCubes")


__all__ = ['SaveEntityResponse', 'SaveTruckRequest', 'ServiceWarningResponse', 'Truck']
