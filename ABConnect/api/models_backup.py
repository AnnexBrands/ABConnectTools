"""Response models for API data structures.

This module provides data models and type definitions for API responses,
enabling better type checking and autocomplete support.
"""

from datetime import datetime
from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field, ConfigDict


class LookupKeys(str, Enum):
    JOBINTACCTSTATUS = " JobIntacctStatus"
    BASISTYPES = "BasisTypes"
    CANCELLEDTYPES = "CancelledTypes"
    CFILLTYPE = "CFillType"
    COMMODITYCATEGORY = "CommodityCategory"
    COMPANYTYPES = "CompanyTypes"
    CONTACTTYPES = "ContactTypes"
    CONTAINERTYPE = "ContainerType"
    CPACKTYPE = "CPackType"
    CREDITCARDTYPES = "CreditCardTypes"
    DOCUMENTTAGS = "DocumentTags"
    FOLLOWUPHEATOPTION = "FollowupHeatOption"
    FOLLOWUPPIPELINEOPTION = "FollowupPipelineOption"
    FRANCHISEETYPES = "FranchiseeTypes"
    FREIGHTCLASS = "FreightClass"
    FREIGHTTYPES = "FreightTypes"
    INDUSTRYTYPES = "IndustryTypes"
    INSURANCEOPTION = "InsuranceOption"
    INSURANCETYPE = "InsuranceType"
    ITEMNOTEDCONDITIONS = "ItemNotedConditions"
    ITEMTYPES = "ItemTypes"
    JOBMANAGEMENT = "Job Management Status"
    JOBMGMTTYPES = "JobMgmtTypes"
    JOBNOTECATEGORY = "JobNoteCategory"
    JOBSSTATUSTYPES = "JobsStatusTypes"
    JOBTYPE = "JobType"
    ONHOLDNEXTSTEP = "OnHoldNextStep"
    ONHOLDREASON = "OnHoldReason"
    ONHOLDRECOLVEDCODE = "OnHoldRecolvedCode"
    PAYMENTSTATUSES = "PaymentStatuses"
    PRICINGTOUSE = "PricingToUse"
    QBJOBTRANSTYPE = "QBJobTransType"
    QBWSTRANSTYPE = "QBWSTransType"
    RESPONSIBILITYPARTY = "ResponsibilityParty"
    ROOMTYPES = "RoomTypes"
    TRANSRULES = "TransRules"
    TRANSTYPES = "TransTypes"
    YESNO = "YesNo"


class CompanyType(str, Enum):
    """Valid company types from ABC API."""

    AGENT = "Agent"
    CARRIER = "Carrier"
    CORPORATE = "Corporate"
    CUSTOMER = "Customer"
    FRANCHISEE = "Franchisee"
    NATIONAL_ACCOUNT = "National Account"
    TERMINAL = "Terminal"
    VENDOR = "Vendor"


# Company type ID mapping for reference
COMPANY_TYPE_IDS = {
    "Agent": "697cc861-d271-4baf-8cbb-2eb055a1005a",
    "Carrier": "88a541e1-456e-4e6e-b445-af75311b694f",
    "Corporate": "8ec06e36-7e6a-4ed6-a27c-7cc0c13a7292",
    "Customer": "8e809044-8d69-4618-9533-265d7e71db13",
    "Franchisee": "e7f85166-34cf-429b-805d-261b44cb0c04",
    "National Account": "27654fb3-9507-e811-8f3f-00155d426802",
    "Terminal": "65d232c9-3031-4682-83b5-594da868d9dd",
    "Vendor": "4176c2d7-b7ae-ec11-822e-a4aa13c701a3",
}


class JobStatus(str, Enum):
    """Job status enumeration."""

    DRAFT = "draft"
    PENDING = "pending"
    ACTIVE = "active"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"
    FAILED = "failed"


class TaskStatus(str, Enum):
    """Task status enumeration."""

    PENDING = "pending"
    SCHEDULED = "scheduled"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class ABConnectBaseModel(BaseModel):
    """Base class for all API models."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Optional[str] = None
    created: Optional[datetime] = None
    modified: Optional[datetime] = None


class Address(ABConnectBaseModel):
    """Address model."""

    line1: Optional[str] = None
    line2: Optional[str] = None
    line3: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zip: Optional[str] = None
    country: Optional[str] = None
    type: Optional[str] = None
    isValid: Optional[bool] = None


class Contact(ABConnectBaseModel):
    """Contact model."""

    firstName: Optional[str] = None
    lastName: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    mobile: Optional[str] = None
    title: Optional[str] = None
    department: Optional[str] = None
    companyId: Optional[str] = None
    isActive: bool = True


class CompanyBasic(ABConnectBaseModel):
    """Basic company model returned by /api/companies/{id}."""

    code: Optional[str] = None
    name: Optional[str] = None
    parentCompanyId: Optional[str] = None


class AddressCoordinates(BaseModel):
    """Coordinate model for addresses."""
    
    latitude: Optional[float] = None
    longitude: Optional[float] = None


class MainAddress(BaseModel):
    """Main address model with extended fields."""
    
    id: Optional[int] = None
    isValid: Optional[bool] = None
    dontValidate: Optional[bool] = None
    propertyType: Optional[str] = None
    address1Value: Optional[str] = None
    address2Value: Optional[str] = None
    countryName: Optional[str] = None
    countryCode: Optional[str] = None
    countryId: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    fullCityLine: Optional[str] = None
    coordinates: Optional[AddressCoordinates] = None
    address1: Optional[str] = None
    address2: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zipCode: Optional[str] = None


class AddressData(BaseModel):
    """Address data model for company details."""
    
    company: Optional[str] = None
    firstLastName: Optional[str] = None
    addressLine1: Optional[str] = None
    addressLine2: Optional[str] = None
    contactBOLNote: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    stateCode: Optional[str] = None
    zipCode: Optional[str] = None
    countryName: Optional[str] = None
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


class CompanyInfo(BaseModel):
    """Company info model for details response."""
    
    companyId: Optional[str] = None
    companyTypeId: Optional[str] = None
    companyDisplayId: Optional[str] = None
    companyName: Optional[str] = None
    companyCode: Optional[str] = None
    companyEmail: Optional[str] = None
    companyPhone: Optional[str] = None
    thumbnailLogo: Optional[str] = None
    companyLogo: Optional[str] = None
    mapsMarkerImage: Optional[str] = None
    mainAddress: Optional[MainAddress] = None
    isThirdParty: Optional[bool] = None
    isActive: Optional[bool] = None
    isHidden: Optional[bool] = None


class CompanyDetails(ABConnectBaseModel):
    """Detailed company model returned by /api/companies/{companyId}/details."""
    
    userId: Optional[str] = None
    companyName: Optional[str] = None
    contactName: Optional[str] = None
    contactPhone: Optional[str] = None
    companyType: Optional[str] = None
    parcelOnly: Optional[bool] = None
    isThirdParty: Optional[bool] = None
    companyCode: Optional[str] = None
    parentCompanyName: Optional[str] = None
    companyTypeID: Optional[str] = None
    parentCompanyID: Optional[str] = None
    companyPhone: Optional[str] = None
    companyEmail: Optional[str] = None
    companyFax: Optional[str] = None
    companyWebSite: Optional[str] = None
    industryType: Optional[str] = None
    industryTypeName: Optional[str] = None
    taxId: Optional[str] = None
    customerCell: Optional[str] = None
    companyCell: Optional[str] = None
    pzCode: Optional[str] = None
    referralCode: Optional[str] = None
    companyLogo: Optional[str] = None
    letterHeadLogo: Optional[str] = None
    thumbnailLogo: Optional[str] = None
    mapsMarkerImage: Optional[str] = None
    colorTheme: Optional[str] = None
    franchiseeMaturityType: Optional[str] = None
    pricingToUse: Optional[str] = None
    totalRows: Optional[int] = None
    address: Optional[str] = None
    companyInsurancePricing: Optional[float] = None
    companyServicePricing: Optional[float] = None
    companyTaxPricing: Optional[float] = None
    wholeSaleMarkup: Optional[float] = None
    baseMarkup: Optional[float] = None
    mediumMarkup: Optional[float] = None
    highMarkup: Optional[float] = None
    miles: Optional[float] = None
    insuranceType: Optional[str] = None
    isGlobal: Optional[bool] = None
    isQbUser: Optional[bool] = None
    skipIntacct: Optional[bool] = None
    isAccess: Optional[bool] = None
    companyDisplayID: Optional[str] = None
    depth: Optional[int] = None
    franchiseeName: Optional[str] = None
    isPrefered: Optional[bool] = None
    createdUser: Optional[str] = None
    mappingLocations: Optional[str] = None
    locationCount: Optional[int] = None
    baseParent: Optional[str] = None
    copyMaterialFrom: Optional[str] = None
    isHide: Optional[bool] = None
    isDontUse: Optional[bool] = None
    mainAddress: Optional[MainAddress] = None
    accountManagerFranchiseeId: Optional[str] = None
    accountManagerFranchiseeName: Optional[str] = None
    carrierAccountsSourceCompanyId: Optional[str] = None
    carrierAccountsSourceCompanyName: Optional[str] = None
    autoPriceAPIEnableEmails: Optional[bool] = None
    autoPriceAPIEnableSMSs: Optional[bool] = None
    commercialCapabilities: Optional[int] = None
    primaryContactId: Optional[int] = None
    payerContactId: Optional[int] = None
    payerContactName: Optional[str] = None
    totalJobs: Optional[int] = None
    totalJobsRevenue: Optional[float] = None
    totalSales: Optional[int] = None
    totalSalesRevenue: Optional[float] = None
    addressData: Optional[AddressData] = None
    overridableAddressData: Optional[OverridableAddressData] = None
    companyInfo: Optional[CompanyInfo] = None
    companyID: Optional[str] = None
    addressID: Optional[int] = None
    address1: Optional[str] = None
    address2: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    stateCode: Optional[str] = None
    countryName: Optional[str] = None
    countryCode: Optional[str] = None
    countryID: Optional[str] = None
    zipCode: Optional[str] = None
    isActive: Optional[bool] = None
    createdDate: Optional[datetime] = None
    createdBy: Optional[str] = None
    modifiedDate: Optional[datetime] = None
    modifiedBy: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    result: Optional[str] = None
    addressMappingID: Optional[int] = None
    contactID: Optional[int] = None
    userID: Optional[str] = None
    primaryCustomerName: Optional[str] = None
    contactInfo: Optional[str] = None


class Company(ABConnectBaseModel):
    """Company model - comprehensive version."""

    code: Optional[str] = None
    name: Optional[str] = None
    type: Optional[CompanyType] = None
    parentCompanyId: Optional[str] = None
    parentCompanyName: Optional[str] = None
    companyTypeId: Optional[str] = None
    companyDisplayId: Optional[str] = None
    taxId: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    website: Optional[str] = None
    addresses: List[Address] = Field(default_factory=list)
    contacts: List[Contact] = Field(default_factory=list)
    isActive: bool = True
    isHidden: bool = False
    isGlobal: bool = False
    metadata: Dict[str, Any] = Field(default_factory=dict)


# Company Full Details Models

class FileUpload(BaseModel):
    """File upload model for logos."""
    
    filePath: Optional[str] = None
    newFile: Optional[str] = None


class CompanyDetailsSection(BaseModel):
    """Details section of company full details."""
    
    displayId: Optional[str] = None
    name: Optional[str] = None
    taxId: Optional[str] = None
    code: Optional[str] = None
    parentId: Optional[str] = None
    franchiseeId: Optional[str] = None
    companyTypeId: Optional[str] = None
    industryTypeId: Optional[str] = None
    cellPhone: Optional[str] = None
    phone: Optional[str] = None
    fax: Optional[str] = None
    email: Optional[str] = None
    website: Optional[str] = None
    isActive: Optional[bool] = None
    isHidden: Optional[bool] = None
    isGlobal: Optional[bool] = None
    isNotUsed: Optional[bool] = None
    isPreferred: Optional[bool] = None
    payerContactId: Optional[int] = None
    payerContactName: Optional[str] = None


class CompanyPreferences(BaseModel):
    """Company preferences model."""
    
    companyHeaderLogo: Optional[FileUpload] = None
    thumbnailLogo: Optional[FileUpload] = None
    letterHeadLogo: Optional[FileUpload] = None
    mapsMarker: Optional[FileUpload] = None
    isQbUser: Optional[bool] = None
    skipIntacct: Optional[bool] = None
    pricingToUse: Optional[str] = None
    pzCode: Optional[str] = None
    insuranceTypeId: Optional[str] = None
    franchiseeMaturityTypeId: Optional[str] = None
    isCompanyUsedAsCarrierSource: Optional[bool] = None
    carrierAccountsSourceCompanyId: Optional[str] = None
    carrierAccountsSourceCompanyName: Optional[str] = None
    accountManagerFranchiseeId: Optional[str] = None
    accountManagerFranchiseeName: Optional[str] = None
    autoPriceAPIEnableEmails: Optional[bool] = None
    autoPriceAPIEnableSMSs: Optional[bool] = None
    copyMaterials: Optional[int] = None


class TransportationCharge(BaseModel):
    """Transportation charge model."""
    
    baseTripFee: Optional[float] = None
    baseTripMile: Optional[float] = None
    extraFee: Optional[float] = None
    fuelSurcharge: Optional[float] = None


class MarkupRates(BaseModel):
    """Markup rates model."""
    
    wholeSale: Optional[float] = None
    base: Optional[float] = None
    medium: Optional[float] = None
    high: Optional[float] = None


class LaborCharge(BaseModel):
    """Labor charge model."""
    
    cost: Optional[float] = None
    charge: Optional[float] = None


class AccesorialCharge(BaseModel):
    """Accesorial charge model."""
    
    stairs: Optional[float] = None
    elevator: Optional[float] = None
    longCarry: Optional[float] = None
    certificateOfInsurance: Optional[float] = None
    deInstallation: Optional[float] = None
    disassembly: Optional[float] = None
    timeSpecific: Optional[float] = None
    saturday: Optional[float] = None


class Royalties(BaseModel):
    """Royalties model."""
    
    franchisee: Optional[float] = None
    national: Optional[float] = None
    local: Optional[float] = None


class PaymentSettings(BaseModel):
    """Payment settings model."""
    
    creditCardSurcharge: Optional[float] = None
    stripeConnected: Optional[bool] = None


class CompanyPricing(BaseModel):
    """Company pricing model."""
    
    transportationCharge: Optional[TransportationCharge] = None
    transportationMarkups: Optional[MarkupRates] = None
    carrierFreightMarkups: Optional[MarkupRates] = None
    carrierOtherMarkups: Optional[MarkupRates] = None
    materialMarkups: Optional[MarkupRates] = None
    laborCharge: Optional[LaborCharge] = None
    accesorialCharge: Optional[AccesorialCharge] = None
    royalties: Optional[Royalties] = None
    paymentSettings: Optional[PaymentSettings] = None


class InsuranceOption(BaseModel):
    """Insurance option model."""
    
    insuranceSlabId: Optional[str] = None
    option: Optional[int] = None
    sellPrice: Optional[float] = None


class CompanyInsurance(BaseModel):
    """Company insurance model."""
    
    isp: Optional[InsuranceOption] = None
    nsp: Optional[InsuranceOption] = None
    ltl: Optional[InsuranceOption] = None


class FinalMileTariffItem(BaseModel):
    """Final mile tariff item model."""
    
    groupId: Optional[str] = None
    from_: Optional[float] = Field(None, alias="from")
    to: Optional[float] = None
    toCurb: Optional[float] = None
    intoGarage: Optional[float] = None
    roomOfChoice: Optional[float] = None
    whiteGlove: Optional[float] = None
    deleteGroup: Optional[bool] = None


class TaxSettings(BaseModel):
    """Tax settings model."""
    
    isTaxable: Optional[bool] = None
    taxPercent: Optional[float] = None


class CompanyTaxes(BaseModel):
    """Company taxes model."""
    
    deliveryService: Optional[TaxSettings] = None
    insurance: Optional[TaxSettings] = None
    pickupService: Optional[TaxSettings] = None
    services: Optional[TaxSettings] = None
    transportationService: Optional[TaxSettings] = None
    packagingMaterial: Optional[TaxSettings] = None
    packagingLabor: Optional[TaxSettings] = None


class CompanyFullDetails(ABConnectBaseModel):
    """Full company details returned by /api/companies/{companyId}/fulldetails."""
    
    details: Optional[CompanyDetailsSection] = None
    preferences: Optional[CompanyPreferences] = None
    capabilities: Optional[int] = None
    address: Optional[MainAddress] = None
    accountInformation: Optional[Dict[str, Any]] = None  # Complex nested structure
    pricing: Optional[CompanyPricing] = None
    insurance: Optional[CompanyInsurance] = None
    finalMileTariff: Optional[List[FinalMileTariffItem]] = None
    taxes: Optional[CompanyTaxes] = None
    readOnlyAccess: Optional[bool] = None


class Item(ABConnectBaseModel):
    """Item/Product model."""

    code: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    type: Optional[str] = None
    weight: Optional[float] = None
    dimensions: Optional[Dict[str, float]] = None
    value: Optional[float] = None
    currency: str = "USD"
    isHazmat: bool = False
    metadata: Dict[str, Any] = Field(default_factory=dict)


class Task(ABConnectBaseModel):
    """Task model."""

    jobId: Optional[str] = None
    type: Optional[str] = None
    status: Optional[TaskStatus] = None
    description: Optional[str] = None
    assignedTo: Optional[str] = None
    scheduledDate: Optional[datetime] = None
    completedDate: Optional[datetime] = None
    duration: Optional[int] = None
    notes: Optional[str] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)


class Job(ABConnectBaseModel):
    """Job model."""

    code: Optional[str] = None
    type: Optional[str] = None
    status: Optional[JobStatus] = None
    customerId: Optional[str] = None
    vendorId: Optional[str] = None
    originAddress: Optional[Address] = None
    destinationAddress: Optional[Address] = None
    items: List[Item] = Field(default_factory=list)
    tasks: List[Task] = Field(default_factory=list)
    scheduledDate: Optional[datetime] = None
    completedDate: Optional[datetime] = None
    totalWeight: Optional[float] = None
    totalValue: Optional[float] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)


class User(ABConnectBaseModel):
    """User model."""

    username: Optional[str] = None
    email: Optional[str] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    role: Optional[str] = None
    permissions: List[str] = Field(default_factory=list)
    isActive: bool = True
    lastLogin: Optional[datetime] = None


class Document(ABConnectBaseModel):
    """Document model."""

    name: Optional[str] = None
    type: Optional[str] = None
    size: Optional[int] = None
    mimeType: Optional[str] = None
    url: Optional[str] = None
    jobId: Optional[str] = None
    uploadedBy: Optional[str] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)


class Form(ABConnectBaseModel):
    """Form/Template model."""

    name: Optional[str] = None
    type: Optional[str] = None
    version: Optional[str] = None
    fields: List[Dict[str, Any]] = Field(default_factory=list)
    isActive: bool = True
    metadata: Dict[str, Any] = Field(default_factory=dict)


# Response wrapper models


class PaginatedResponse(BaseModel):
    """Paginated response wrapper."""

    model_config = ConfigDict(extra="allow")

    data: List[Any] = Field(default_factory=list)
    page: int = 1
    per_page: int = 50
    total: int = 0
    total_pages: int = 0
    has_next: bool = False
    has_prev: bool = False

    @classmethod
    def from_dict(
        cls, data: Dict[str, Any], item_class: Optional[type] = None
    ) -> "PaginatedResponse":
        """Create paginated response from dictionary.

        Args:
            data: Response dictionary
            item_class: Optional class to convert items to

        Returns:
            PaginatedResponse instance
        """
        # Extract pagination metadata
        page = data.get("page", 1)
        per_page = data.get("per_page", data.get("perPage", 50))
        total = data.get("total", 0)
        total_pages = data.get("total_pages", data.get("totalPages", 0))
        has_next = data.get("has_next", data.get("hasNext", False))
        has_prev = data.get("has_prev", data.get("hasPrev", False))

        # Extract data items
        items = data.get("data", data.get("items", data.get("results", [])))

        # Convert items to model instances if class provided
        if item_class and hasattr(item_class, "model_validate"):
            parsed_items = [item_class.model_validate(item) for item in items]
        else:
            parsed_items = items

        return cls(
            data=parsed_items,
            page=page,
            per_page=per_page,
            total=total,
            total_pages=total_pages,
            has_next=has_next,
            has_prev=has_prev,
        )


class ErrorResponse(BaseModel):
    """Error response model."""

    error: str
    message: str
    code: Optional[str] = None
    details: Optional[Dict[str, Any]] = None
    timestamp: Optional[datetime] = Field(default_factory=datetime.now)


# Model registry for dynamic model lookup
MODEL_REGISTRY = {
    "address": Address,
    "addresses": Address,
    "company": Company,
    "companies": Company,
    "contact": Contact,
    "contacts": Contact,
    "item": Item,
    "items": Item,
    "job": Job,
    "jobs": Job,
    "task": Task,
    "tasks": Task,
    "user": User,
    "users": User,
    "document": Document,
    "documents": Document,
    "form": Form,
    "forms": Form,
}


def get_model_class(resource_name: str) -> Optional[type]:
    """Get model class for a resource name.

    Args:
        resource_name: Name of the resource

    Returns:
        Model class or None if not found
    """
    return MODEL_REGISTRY.get(resource_name.lower())


def parse_response(data: Any, resource_name: Optional[str] = None) -> Any:
    """Parse API response into model instances.

    Args:
        data: Response data (dict or list)
        resource_name: Optional resource name for model lookup

    Returns:
        Parsed response (model instance, list of instances, or original data)
    """
    if not data:
        return data

    # Get model class if resource name provided
    model_class = get_model_class(resource_name) if resource_name else None

    # Handle list responses
    if isinstance(data, list):
        if model_class and hasattr(model_class, "model_validate"):
            return [model_class.model_validate(item) for item in data]
        return data

    # Handle dict responses
    if isinstance(data, dict):
        # Check if it's a paginated response
        if any(key in data for key in ["data", "items", "results"]):
            return PaginatedResponse.from_dict(data, model_class)

        # Check if it's an error response
        if "error" in data:
            return ErrorResponse.model_validate(data)

        # Try to convert to model instance
        if model_class and hasattr(model_class, "model_validate"):
            return model_class.model_validate(data)

    return data
