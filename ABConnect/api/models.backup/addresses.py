"""Address models for ABConnect API."""

from typing import Optional
from pydantic import BaseModel
from .base import ABConnectBaseModel


class AddressCoordinates(BaseModel):
    """Coordinate model for addresses."""
    latitude: Optional[float] = None
    longitude: Optional[float] = None


class AddressBase(BaseModel):
    """Base address model with common fields."""
    address1: Optional[str] = None
    address2: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zipCode: Optional[str] = None
    countryCode: Optional[str] = None
    countryName: Optional[str] = None


class Address(AddressBase, ABConnectBaseModel):
    """Standard address model."""
    line1: Optional[str] = None  # Alias for address1
    line2: Optional[str] = None  # Alias for address2
    line3: Optional[str] = None
    zip: Optional[str] = None  # Alias for zipCode
    country: Optional[str] = None  # Alias for countryCode
    type: Optional[str] = None
    isValid: Optional[bool] = None


class MainAddress(AddressBase):
    """Main address model with extended fields."""
    id: Optional[int] = None
    isValid: Optional[bool] = None
    dontValidate: Optional[bool] = None
    propertyType: Optional[str] = None
    address1Value: Optional[str] = None
    address2Value: Optional[str] = None
    countryId: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    fullCityLine: Optional[str] = None
    coordinates: Optional[AddressCoordinates] = None


class AddressData(AddressBase):
    """Address data model for company details."""
    company: Optional[str] = None
    firstLastName: Optional[str] = None
    addressLine1: Optional[str] = None
    addressLine2: Optional[str] = None
    contactBOLNote: Optional[str] = None
    stateCode: Optional[str] = None
    propertyType: Optional[str] = None
    fullCityLine: Optional[str] = None
    phone: Optional[str] = None
    cellPhone: Optional[str] = None
    fax: Optional[str] = None
    email: Optional[str] = None
    addressLine2Visible: Optional[bool] = None
    companyVisible: Optional[bool] = None
    countryNameVisible: Optional[bool] = None
    phoneVisible: Optional[bool] = None
    emailVisible: Optional[bool] = None
    fullAddressLine: Optional[str] = None
    fullAddress: Optional[str] = None
    countryId: Optional[str] = None


class OverridableValue(BaseModel):
    """Model for overridable values in company details."""
    defaultValue: Optional[str] = None
    overrideValue: Optional[str] = None
    forceEmpty: Optional[bool] = None
    value: Optional[str] = None


class OverridableAddressData(BaseModel):
    """Overridable address data model."""
    company: Optional[OverridableValue] = None
    firstLastName: Optional[OverridableValue] = None
    addressLine1: Optional[OverridableValue] = None
    addressLine2: Optional[OverridableValue] = None
    city: Optional[OverridableValue] = None
    state: Optional[OverridableValue] = None
    zipCode: Optional[OverridableValue] = None
    phone: Optional[OverridableValue] = None
    email: Optional[OverridableValue] = None
    fullAddressLine: Optional[str] = None
    fullAddress: Optional[OverridableValue] = None
    fullCityLine: Optional[OverridableValue] = None