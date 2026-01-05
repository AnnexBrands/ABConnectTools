"""Contacts models for ABConnect API."""

from typing import List, Optional, TYPE_CHECKING
from datetime import datetime
from pydantic import Field
from .base import ABConnectBaseModel, CompanyRelatedModel, IdentifiedModel, TimestampedModel
from .enums import ListSortDirection

# Runtime imports for forward reference resolution (avoid circular imports with deferred import)
from .address import Address, AddressDetails, FreightRateRequestAddressDetails
from .shared import PhoneDetails, EmailDetails, PageOrderedRequestModel, AutoCompleteValue
from .users import Users
from .companies import Company, ContactDetailsCompanyInfo

class BaseContactDetails(CompanyRelatedModel):
    """BaseContactDetails model"""

    contact_display_id: Optional[str] = Field(None, alias="contactDisplayId")
    contact_name: Optional[str] = Field(None, alias="contactName")
    job_title: Optional[str] = Field(None, alias="jobTitle")
    co_name: Optional[str] = Field(None, alias="coName")
    bol_note: Optional[str] = Field(None, alias="bolNote")
    contact_tax_id: Optional[str] = Field(None, alias="contactTaxId")
    company_display_id: Optional[str] = Field(None, alias="companyDisplayId")
    company_type: Optional[str] = Field(None, alias="companyType")
    company_inductry: Optional[str] = Field(None, alias="companyInductry")
    company_tax_id: Optional[str] = Field(None, alias="companyTaxId")
    company_payer_name: Optional[str] = Field(None, alias="companyPayerName")
    company_address1: Optional[str] = Field(None, alias="companyAddress1")
    company_address2: Optional[str] = Field(None, alias="companyAddress2")
    company_city: Optional[str] = Field(None, alias="companyCity")
    company_state: Optional[str] = Field(None, alias="companyState")
    company_country: Optional[str] = Field(None, alias="companyCountry")
    company_zip_code: Optional[str] = Field(None, alias="companyZipCode")
    company_latitude: Optional[float] = Field(None, alias="companyLatitude")
    company_longitude: Optional[float] = Field(None, alias="companyLongitude")


class CalendarContact(IdentifiedModel):
    """CalendarContact model"""

    contact_display_id: Optional[str] = Field(None, alias="contactDisplayId")
    company_id: Optional[str] = Field(None, alias="companyId")
    company_name: Optional[str] = Field(None, alias="companyName")
    bol_notes: Optional[str] = Field(None, alias="bolNotes")
    full_name: Optional[str] = Field(None, alias="fullName")


class Contact(TimestampedModel):
    """Contact model"""

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
    parent_company_id: Optional[str] = Field(None, alias="parentCompanyId")
    user_id: Optional[str] = Field(None, alias="userId")
    payer_id: Optional[str] = Field(None, alias="payerId")
    cust_companyid: Optional[str] = Field(None, alias="custCompanyid")
    pu_business_status: Optional[str] = Field(None, alias="puBusinessStatus")
    del_business_status: Optional[str] = Field(None, alias="delBusinessStatus")
    pu_zone: Optional[float] = Field(None, alias="puZone")
    new_contact_id: Optional[int] = Field(None, alias="newContactId")
    contact_is_business: Optional[bool] = Field(None, alias="contactIsBusiness")
    contact_first_name: Optional[str] = Field(None, alias="contactFirstName")
    contact_last_name: Optional[str] = Field(None, alias="contactLastName")
    contact_full_name: Optional[str] = Field(None, alias="contactFullName")
    contact_phone: Optional[str] = Field(None, alias="contactPhone")
    contact_fax: Optional[str] = Field(None, alias="contactFax")
    customer_cell: Optional[str] = Field(None, alias="customerCell")
    contact_email_id: Optional[str] = Field(None, alias="contactEmailId")
    contact_type_id: Optional[int] = Field(None, alias="contactTypeId")
    refer_id: Optional[str] = Field(None, alias="referId")
    referred_name: Optional[str] = Field(None, alias="referredName")
    contact_dept: Optional[str] = Field(None, alias="contactDept")
    contact_assistant: Optional[str] = Field(None, alias="contactAssistant")
    contact_assistant_phone: Optional[str] = Field(None, alias="contactAssistantPhone")
    contact_home_phone: Optional[str] = Field(None, alias="contactHomePhone")
    contact_birth_date: Optional[datetime] = Field(None, alias="contactBirthDate")
    is_primary: Optional[bool] = Field(None, alias="isPrimary")
    is_prefered: Optional[bool] = Field(None, alias="isPrefered")
    referred_by: Optional[str] = Field(None, alias="referredBy")
    is_payer: Optional[bool] = Field(None, alias="isPayer")
    payer_name: Optional[str] = Field(None, alias="payerName")
    other_referral: Optional[str] = Field(None, alias="otherReferral")
    master_constant_id: Optional[str] = Field(None, alias="masterConstantId")
    company_name: Optional[str] = Field(None, alias="companyName")
    parent_company_name: Optional[str] = Field(None, alias="parentCompanyName")
    company_code: Optional[str] = Field(None, alias="companyCode")
    master_constant_value: Optional[str] = Field(None, alias="masterConstantValue")
    total_record: Optional[int] = Field(None, alias="totalRecord")
    industry_type: Optional[str] = Field(None, alias="industryType")
    contact_address: Optional["Address"] = Field(None, alias="contactAddress")
    contact_user: Optional["Users"] = Field(None, alias="contactUser")
    total_items: Optional[int] = Field(None, alias="totalItems")
    contact_web_site: Optional[str] = Field(None, alias="contactWebSite")
    is_global: Optional[bool] = Field(None, alias="isGlobal")
    user_name: Optional[str] = Field(None, alias="userName")
    is_access: Optional[str] = Field(None, alias="isAccess")
    contact_display_id: Optional[str] = Field(None, alias="contactDisplayId")
    company_display_id: Optional[str] = Field(None, alias="companyDisplayId")
    franchisee_name: Optional[str] = Field(None, alias="franchiseeName")
    contact_type: Optional[str] = Field(None, alias="contactType")
    created_user: Optional[str] = Field(None, alias="createdUser")
    mapping_locations: Optional[str] = Field(None, alias="mappingLocations")
    location_count: Optional[str] = Field(None, alias="locationCount")
    base_parent: Optional[str] = Field(None, alias="baseParent")


class ContactAddressDetails(IdentifiedModel):
    """ContactAddressDetails model"""

    is_active: Optional[bool] = Field(None, alias="isActive")
    deactivated_reason: Optional[str] = Field(None, alias="deactivatedReason")
    meta_data: Optional[str] = Field(None, alias="metaData")
    address: Optional["AddressDetails"] = Field(None)


class ContactAddressEditDetails(ContactAddressDetails):
    """ContactAddressEditDetails model - extends ContactAddressDetails with edit metadata."""

    editable: Optional[bool] = Field(None)
    detail_hash: Optional[str] = Field(None, alias="detailHash")


class ContactDetailedInfo(IdentifiedModel):
    """ContactDetailedInfo model"""

    contact_display_id: Optional[str] = Field(None, alias="contactDisplayId")
    full_name: Optional[str] = Field(None, alias="fullName")
    contact_type_id: Optional[int] = Field(None, alias="contactTypeId")
    care_of: Optional[str] = Field(None, alias="careOf")
    bol_notes: Optional[str] = Field(None, alias="bolNotes")
    tax_id: Optional[str] = Field(None, alias="taxId")
    is_business: Optional[bool] = Field(None, alias="isBusiness")
    is_payer: Optional[bool] = Field(None, alias="isPayer")
    is_prefered: Optional[bool] = Field(None, alias="isPrefered")
    is_private: Optional[bool] = Field(None, alias="isPrivate")
    is_active: Optional[bool] = Field(None, alias="isActive")
    company_id: Optional[str] = Field(None, alias="companyId")
    root_contact_id: Optional[int] = Field(None, alias="rootContactId")
    owner_franchisee_id: Optional[str] = Field(None, alias="ownerFranchiseeId")
    company: Optional["Company"] = Field(None)
    legacy_guid: Optional[str] = Field(None, alias="legacyGuid")
    is_primary: Optional[bool] = Field(None, alias="isPrimary")
    assistant: Optional[str] = Field(None)
    department: Optional[str] = Field(None)
    web_site: Optional[str] = Field(None, alias="webSite")
    birth_date: Optional[datetime] = Field(None, alias="birthDate")
    job_title_id: Optional[int] = Field(None, alias="jobTitleId")
    job_title: Optional[str] = Field(None, alias="jobTitle")
    emails_list: Optional[List["ContactEmailEditDetails"]] = Field(None, alias="emailsList")
    phones_list: Optional[List["ContactPhoneEditDetails"]] = Field(None, alias="phonesList")
    addresses_list: Optional[List[ContactAddressEditDetails]] = Field(None, alias="addressesList")
    fax: Optional[str] = Field(None)
    primary_phone_detail: Optional["PhoneDetails"] = Field(None, alias="primaryPhoneDetail")
    primary_phone: Optional[str] = Field(None, alias="primaryPhone")
    primary_email_detail: Optional["EmailDetails"] = Field(None, alias="primaryEmailDetail")
    primary_email: Optional[str] = Field(None, alias="primaryEmail")
    primary_address_detail: Optional["AddressDetails"] = Field(None, alias="primaryAddressDetail")
    editable: Optional[bool] = Field(None)
    contact_details_company_info: Optional["ContactDetailsCompanyInfo"] = Field(None, alias="contactDetailsCompanyInfo")


class ContactDetails(IdentifiedModel):
    """ContactDetails model"""

    contact_display_id: Optional[str] = Field(None, alias="contactDisplayId")
    full_name: Optional[str] = Field(None, alias="fullName")
    contact_type_id: Optional[int] = Field(None, alias="contactTypeId")
    care_of: Optional[str] = Field(None, alias="careOf")
    bol_notes: Optional[str] = Field(None, alias="bolNotes")
    tax_id: Optional[str] = Field(None, alias="taxId")
    is_business: Optional[bool] = Field(None, alias="isBusiness")
    is_payer: Optional[bool] = Field(None, alias="isPayer")
    is_prefered: Optional[bool] = Field(None, alias="isPrefered")
    is_private: Optional[bool] = Field(None, alias="isPrivate")
    is_active: Optional[bool] = Field(None, alias="isActive")
    company_id: Optional[str] = Field(None, alias="companyId")
    root_contact_id: Optional[int] = Field(None, alias="rootContactId")
    owner_franchisee_id: Optional[str] = Field(None, alias="ownerFranchiseeId")
    company: Optional["Company"] = Field(None)
    legacy_guid: Optional[str] = Field(None, alias="legacyGuid")
    is_primary: Optional[bool] = Field(None, alias="isPrimary")
    assistant: Optional[str] = Field(None)
    department: Optional[str] = Field(None)
    web_site: Optional[str] = Field(None, alias="webSite")
    birth_date: Optional[datetime] = Field(None, alias="birthDate")
    job_title_id: Optional[int] = Field(None, alias="jobTitleId")
    job_title: Optional[str] = Field(None, alias="jobTitle")
    emails_list: Optional[List["ContactEmailDetails"]] = Field(None, alias="emailsList")
    phones_list: Optional[List["ContactPhoneDetails"]] = Field(None, alias="phonesList")
    addresses_list: Optional[List["ContactAddressDetails"]] = Field(None, alias="addressesList")
    fax: Optional[str] = Field(None)
    primary_phone_detail: Optional["PhoneDetails"] = Field(None, alias="primaryPhoneDetail")
    primary_phone: Optional[str] = Field(None, alias="primaryPhone")
    primary_email_detail: Optional["EmailDetails"] = Field(None, alias="primaryEmailDetail")
    primary_email: Optional[str] = Field(None, alias="primaryEmail")
    primary_address_detail: Optional["AddressDetails"] = Field(None, alias="primaryAddressDetail")
    editable: Optional[bool] = Field(None)
    is_empty: Optional[bool] = Field(None, alias="isEmpty")
    full_name_update_required: Optional[bool] = Field(None, alias="fullNameUpdateRequired")


class ContactEmailDetails(IdentifiedModel):
    """ContactEmailDetails model"""

    is_active: Optional[bool] = Field(None, alias="isActive")
    deactivated_reason: Optional[str] = Field(None, alias="deactivatedReason")
    meta_data: Optional[str] = Field(None, alias="metaData")
    email: Optional["EmailDetails"] = Field(None)


class ContactEmailEditDetails(ContactEmailDetails):
    """ContactEmailEditDetails model - extends ContactEmailDetails with edit metadata."""

    editable: Optional[bool] = Field(None)
    detail_hash: Optional[str] = Field(None, alias="detailHash")


class ContactHistoryPricePerPound(ABConnectBaseModel):
    """ContactHistoryPricePerPound model"""

    weight: Optional[float] = Field(None)
    amount: Optional[float] = Field(None)
    job_type: Optional[int] = Field(None, alias="jobType")
    booked_or_completed: Optional[bool] = Field(None, alias="bookedOrCompleted")


class ContactHistoryRevenueSum(TimestampedModel):
    """ContactHistoryRevenueSum model"""

    created_date_str_internal: Optional[str] = Field(None, alias="createdDateStrInternal")
    booked_completed_revenue: Optional[float] = Field(None, alias="bookedCompletedRevenue")
    quoted_estimate_revenue: Optional[float] = Field(None, alias="quotedEstimateRevenue")
    booked_completed_job_count: Optional[int] = Field(None, alias="bookedCompletedJobCount")
    quoted_estimate_job_count: Optional[int] = Field(None, alias="quotedEstimateJobCount")


class ContactPhoneDetails(IdentifiedModel):
    """ContactPhoneDetails model"""

    is_active: Optional[bool] = Field(None, alias="isActive")
    deactivated_reason: Optional[str] = Field(None, alias="deactivatedReason")
    meta_data: Optional[str] = Field(None, alias="metaData")
    phone: Optional["PhoneDetails"] = Field(None)


class ContactPhoneEditDetails(ContactPhoneDetails):
    """ContactPhoneEditDetails model - extends ContactPhoneDetails with edit metadata."""

    editable: Optional[bool] = Field(None)
    detail_hash: Optional[str] = Field(None, alias="detailHash")


class ContactPrimaryDetails(CompanyRelatedModel):
    """ContactPrimaryDetails model"""

    full_name: Optional[str] = Field(None, alias="fullName")
    email: Optional[str] = Field(None)
    phone: Optional[str] = Field(None)
    cell_phone: Optional[str] = Field(None, alias="cellPhone")
    fax: Optional[str] = Field(None)
    address: Optional["AddressDetails"] = Field(None)
    company: Optional["Company"] = Field(None)


class MergeContactsSearchRequestModel(ABConnectBaseModel):
    """MergeContactsSearchRequestModel model"""

    main_search_request: "MergeContactsSearchRequestParameters" = Field(..., alias="mainSearchRequest")
    load_options: "PageOrderedRequestModel" = Field(..., alias="loadOptions")


class MergeContactsSearchRequestParameters(CompanyRelatedModel):
    """MergeContactsSearchRequestParameters model"""

    contact_display_id: Optional[int] = Field(None, alias="contactDisplayId")
    full_name: Optional[str] = Field(None, alias="fullName")
    company_code: Optional[str] = Field(None, alias="companyCode")
    email: Optional[str] = Field(None)
    phone: Optional[str] = Field(None)
    company_display_id: Optional[int] = Field(None, alias="companyDisplayId")


class PlannerContact(IdentifiedModel):
    """PlannerContact model"""

    full_name: Optional[str] = Field(None, alias="fullName")
    company_name: Optional[str] = Field(None, alias="companyName")


class SearchContactEntityResult(CompanyRelatedModel):
    """SearchContactEntityResult model"""

    contact_id: Optional[int] = Field(None, alias="contactId")
    customer_cell: Optional[str] = Field(None, alias="customerCell")
    contact_display_id: Optional[str] = Field(None, alias="contactDisplayId")
    contact_full_name: Optional[str] = Field(None, alias="contactFullName")
    contact_phone: Optional[str] = Field(None, alias="contactPhone")
    contact_home_phone: Optional[str] = Field(None, alias="contactHomePhone")
    contact_email: Optional[str] = Field(None, alias="contactEmail")
    master_constant_value: Optional[str] = Field(None, alias="masterConstantValue")
    contact_dept: Optional[str] = Field(None, alias="contactDept")
    address1: Optional[str] = Field(None)
    address2: Optional[str] = Field(None)
    city: Optional[str] = Field(None)
    state: Optional[str] = Field(None)
    zip_code: Optional[str] = Field(None, alias="zipCode")
    country_name: Optional[str] = Field(None, alias="countryName")
    company_code: Optional[str] = Field(None, alias="companyCode")
    company_display_id: Optional[str] = Field(None, alias="companyDisplayId")
    is_prefered: Optional[bool] = Field(None, alias="isPrefered")
    industry_type: Optional[str] = Field(None, alias="industryType")
    total_records: Optional[int] = Field(None, alias="totalRecords")


class SearchContactRequest(CompanyRelatedModel):
    """SearchContactRequest model"""

    page_index: Optional[int] = Field(None, alias="pageIndex")
    page_size: Optional[int] = Field(None, alias="pageSize")
    total_count: Optional[int] = Field(None, alias="totalCount")
    sorting_by: Optional[str] = Field(None, alias="sortingBy")
    sorting_direction: Optional[ListSortDirection] = Field(None, alias="sortingDirection")
    full_name: Optional[str] = Field(None, alias="fullName")
    company_display_id: Optional[str] = Field(None, alias="companyDisplayId")
    contact_display_id: Optional[str] = Field(None, alias="contactDisplayId")
    company_code: Optional[str] = Field(None, alias="companyCode")
    email: Optional[str] = Field(None)
    phone: Optional[str] = Field(None)
    city: Optional[str] = Field(None)
    state: Optional[str] = Field(None)
    zip_code: Optional[str] = Field(None, alias="zipCode")
    user_id: Optional[str] = Field(None, alias="userId")
    type: Optional[str] = Field(None)


class ShipmentContactAddressDetails(CompanyRelatedModel):
    """ShipmentContactAddressDetails model"""

    contact_name: Optional[str] = Field(None, alias="contactName")
    phone_number: Optional[str] = Field(None, alias="phoneNumber")
    email_address: Optional[str] = Field(None, alias="emailAddress")
    address: Optional["AddressDetails"] = Field(None)
    tax_ids: Optional[List["AutoCompleteValue"]] = Field(None, alias="taxIds")


class ShipmentContactDetails(CompanyRelatedModel):
    """ShipmentContactDetails model"""

    contact_name: Optional[str] = Field(None, alias="contactName")
    phone_number: Optional[str] = Field(None, alias="phoneNumber")
    email_address: Optional[str] = Field(None, alias="emailAddress")
    tax_id: Optional[str] = Field(None, alias="taxId")
    address: Optional["FreightRateRequestAddressDetails"] = Field(None)
    is_empty: Optional[bool] = Field(None, alias="isEmpty")


class ContactUser(ABConnectBaseModel):
    """ContactUser model for GET /contacts/user response."""

    full_name: Optional[str] = Field(None, alias="fullName")
    company_id: Optional[str] = Field(None, alias="companyId")
    company_name: Optional[str] = Field(None, alias="companyName")


__all__ = ['BaseContactDetails', 'CalendarContact', 'Contact', 'ContactAddressDetails', 'ContactAddressEditDetails', 'ContactDetailedInfo', 'ContactDetails', 'ContactEmailDetails', 'ContactEmailEditDetails', 'ContactHistoryPricePerPound', 'ContactHistoryRevenueSum', 'ContactPhoneDetails', 'ContactPhoneEditDetails', 'ContactPrimaryDetails', 'ContactUser', 'MergeContactsSearchRequestModel', 'MergeContactsSearchRequestParameters', 'PlannerContact', 'SearchContactEntityResult', 'SearchContactRequest', 'ShipmentContactAddressDetails', 'ShipmentContactDetails']

# Rebuild models to resolve forward references within this module
Contact.model_rebuild()
ContactDetailedInfo.model_rebuild()
ContactDetails.model_rebuild()
ContactPrimaryDetails.model_rebuild()
ShipmentContactAddressDetails.model_rebuild()
ShipmentContactDetails.model_rebuild()
