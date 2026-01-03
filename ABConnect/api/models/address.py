"""Address models for ABConnect API."""

from typing import Optional, TYPE_CHECKING
from pydantic import Field
from .base import ABConnectBaseModel, CompanyRelatedModel, IdentifiedModel, TimestampedModel
from .enums import PropertyType

# Runtime imports for forward reference resolution
from .shared import LatLng, StringOverridable

if TYPE_CHECKING:
    from .contacts import Contact

class Address(TimestampedModel):
    """Address model"""

    company_id: Optional[str] = Field(None, alias="companyId")
    address_id: Optional[str] = Field(None, alias="addressId")
    address1: Optional[str] = Field(None)
    address2: Optional[str] = Field(None)
    city: Optional[str] = Field(None)
    state: Optional[str] = Field(None)
    state_code: Optional[str] = Field(None, alias="stateCode")
    country_name: Optional[str] = Field(None, alias="countryName")
    country_code: Optional[str] = Field(None, alias="countryCode")
    country_id: Optional[str] = Field(None, alias="countryId")
    zip_code: Optional[str] = Field(None, alias="zipCode")
    is_active: Optional[bool] = Field(None, alias="isActive")
    latitude: Optional[str] = Field(None)
    longitude: Optional[str] = Field(None)
    result: Optional[str] = Field(None)
    address_mapping_id: Optional[str] = Field(None, alias="addressMappingId")
    contact_id: Optional[str] = Field(None, alias="contactId")
    user_id: Optional[str] = Field(None, alias="userId")
    primary_customer_name: Optional[str] = Field(None, alias="primaryCustomerName")
    contact_info: Optional["Contact"] = Field(None, alias="contactInfo")
    address: Optional[str] = Field(None)


class AddressData(ABConnectBaseModel):
    """AddressData model"""

    company: Optional[str] = Field(None)
    first_last_name: Optional[str] = Field(None, alias="firstLastName")
    address_line1: Optional[str] = Field(None, alias="addressLine1")
    address_line2: Optional[str] = Field(None, alias="addressLine2")
    contact_bol_note: Optional[str] = Field(None, alias="contactBOLNote")  # API uses uppercase BOL
    city: Optional[str] = Field(None)
    state: Optional[str] = Field(None)
    state_code: Optional[str] = Field(None, alias="stateCode")
    zip_code: Optional[str] = Field(None, alias="zipCode")
    country_name: Optional[str] = Field(None, alias="countryName")
    property_type: Optional[str] = Field(None, alias="propertyType")
    full_city_line: Optional[str] = Field(None, alias="fullCityLine")
    phone: Optional[str] = Field(None)
    cell_phone: Optional[str] = Field(None, alias="cellPhone")
    fax: Optional[str] = Field(None)
    email: Optional[str] = Field(None)
    address_line2_visible: Optional[bool] = Field(None, alias="addressLine2Visible")
    company_visible: Optional[bool] = Field(None, alias="companyVisible")
    country_name_visible: Optional[bool] = Field(None, alias="countryNameVisible")
    phone_visible: Optional[bool] = Field(None, alias="phoneVisible")
    email_visible: Optional[bool] = Field(None, alias="emailVisible")
    full_address_line: Optional[str] = Field(None, alias="fullAddressLine")
    full_address: Optional[str] = Field(None, alias="fullAddress")
    country_id: Optional[str] = Field(None, alias="countryId")


class AddressDetails(IdentifiedModel):
    """AddressDetails model"""

    address1: Optional[str] = Field(None)
    address2: Optional[str] = Field(None)
    city: Optional[str] = Field(None)
    state: Optional[str] = Field(None)
    zip_code: Optional[str] = Field(None, alias="zipCode")
    is_valid: Optional[bool] = Field(None, alias="isValid")
    dont_validate: Optional[bool] = Field(None, alias="dontValidate")
    property_type: Optional[PropertyType] = Field(None, alias="propertyType")
    address1_value: Optional[str] = Field(None, alias="address1Value")
    address2_value: Optional[str] = Field(None, alias="address2Value")
    country_name: Optional[str] = Field(None, alias="countryName")
    country_code: Optional[str] = Field(None, alias="countryCode")
    country_id: Optional[str] = Field(None, alias="countryId")
    latitude: Optional[float] = Field(None)
    longitude: Optional[float] = Field(None)
    full_city_line: Optional[str] = Field(None, alias="fullCityLine")
    coordinates: Optional["LatLng"] = Field(None)
    country_skip_zip_code_verification: Optional[bool] = Field(None, alias="countrySkipZipCodeVerification")
    zip_code_resolving_failed: Optional[bool] = Field(None, alias="zipCodeResolvingFailed")


class AddressDetailsMergePreviewDataItem(ABConnectBaseModel):
    """AddressDetailsMergePreviewDataItem model"""

    data: Optional[AddressDetails] = Field(None)
    label: Optional[str] = Field(None)
    is_base_contact_item: Optional[bool] = Field(None, alias="isBaseContactItem")


class AddressIsValidResult(ABConnectBaseModel):
    """AddressIsValidResult model"""

    is_valid: Optional[bool] = Field(None, alias="isValid")
    dont_validate: Optional[bool] = Field(None, alias="dontValidate")
    country_id: Optional[str] = Field(None, alias="countryId")
    country_code: Optional[str] = Field(None, alias="countryCode")
    latitude: Optional[float] = Field(None)
    longitude: Optional[float] = Field(None)
    property_type: Optional[PropertyType] = Field(None, alias="propertyType")


class CalendarAddress(IdentifiedModel):
    """CalendarAddress model"""

    master_address_id: Optional[int] = Field(None, alias="masterAddressId")
    property_type: Optional[PropertyType] = Field(None, alias="propertyType")
    address1: Optional[str] = Field(None)
    address2: Optional[str] = Field(None)
    city: Optional[str] = Field(None)
    state: Optional[str] = Field(None)
    country_name: Optional[str] = Field(None, alias="countryName")
    country_code: Optional[str] = Field(None, alias="countryCode")
    zip_code: Optional[str] = Field(None, alias="zipCode")


class FreightRateRequestAddressDetails(ABConnectBaseModel):
    """FreightRateRequestAddressDetails model"""

    address_line1: Optional[str] = Field(None, alias="addressLine1")
    address_line2: Optional[str] = Field(None, alias="addressLine2")
    city: Optional[str] = Field(None)
    state: Optional[str] = Field(None)
    zip_code: Optional[str] = Field(None, alias="zipCode")
    country_id: Optional[str] = Field(None, alias="countryId")
    country_iata_code: Optional[str] = Field(None, alias="countryIataCode")
    alpha3_code: Optional[str] = Field(None, alias="alpha3Code")
    county_name: Optional[str] = Field(None, alias="countyName")
    is_metric_system: Optional[bool] = Field(None, alias="isMetricSystem")
    is_empty: Optional[bool] = Field(None, alias="isEmpty")


class OverridableAddressData(ABConnectBaseModel):
    """OverridableAddressData model"""

    company: Optional["StringOverridable"] = Field(None)
    first_last_name: Optional["StringOverridable"] = Field(None, alias="firstLastName")
    address_line1: Optional["StringOverridable"] = Field(None, alias="addressLine1")
    address_line2: Optional["StringOverridable"] = Field(None, alias="addressLine2")
    city: Optional["StringOverridable"] = Field(None)
    state: Optional["StringOverridable"] = Field(None)
    zip_code: Optional["StringOverridable"] = Field(None, alias="zipCode")
    phone: Optional["StringOverridable"] = Field(None)
    email: Optional["StringOverridable"] = Field(None)
    full_address_line: Optional[str] = Field(None, alias="fullAddressLine")
    full_address: Optional["StringOverridable"] = Field(None, alias="fullAddress")
    full_city_line: Optional["StringOverridable"] = Field(None, alias="fullCityLine")


class PlannerAddress(ABConnectBaseModel):
    """PlannerAddress model"""

    address1: Optional[str] = Field(None)
    address2: Optional[str] = Field(None)
    city: Optional[str] = Field(None)
    state: Optional[str] = Field(None)
    country_name: Optional[str] = Field(None, alias="countryName")
    zip_code: Optional[str] = Field(None, alias="zipCode")
    latitude: Optional[float] = Field(None)
    longitude: Optional[float] = Field(None)


class SaveValidatedRequest(CompanyRelatedModel):
    """SaveValidatedRequest model"""

    address_details: Optional[AddressDetails] = Field(None, alias="addressDetails")
    job_id: Optional[str] = Field(None, alias="jobId")
    address_mapping_id: Optional[int] = Field(None, alias="addressMappingId")


class SearchAddress(ABConnectBaseModel):
    """SearchAddress model"""

    city: Optional[str] = Field(None)
    state: Optional[str] = Field(None)
    zip_code: Optional[str] = Field(None, alias="zipCode")


class SoldToAddress(ABConnectBaseModel):
    """SoldToAddress model"""

    address_line1: Optional[str] = Field(None, alias="addressLine1")
    address_line2: Optional[str] = Field(None, alias="addressLine2")
    city: Optional[str] = Field(None)
    state: Optional[str] = Field(None)
    zip_code: Optional[str] = Field(None, alias="zipCode")
    country_id: Optional[str] = Field(None, alias="countryId")


__all__ = ['Address', 'AddressData', 'AddressDetails', 'AddressDetailsMergePreviewDataItem', 'AddressIsValidResult', 'CalendarAddress', 'FreightRateRequestAddressDetails', 'OverridableAddressData', 'PlannerAddress', 'SaveValidatedRequest', 'SearchAddress', 'SoldToAddress']
