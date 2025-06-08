"""Company models for ABConnect API."""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from .base import ABConnectBaseModel
from .addresses import MainAddress, AddressData, OverridableAddressData


class CompanyBase(ABConnectBaseModel):
    """Base company model with fields common to all company responses."""
    code: Optional[str] = None
    name: Optional[str] = None
    parentCompanyId: Optional[str] = None
    
    # Common fields that appear in multiple responses
    companyTypeId: Optional[str] = Field(None, alias="companyTypeID")
    companyEmail: Optional[str] = None
    companyPhone: Optional[str] = None
    isActive: Optional[bool] = None


class CompanyBasic(CompanyBase):
    """Basic company model returned by /api/companies/{id}.
    
    This is the simplest company response with just the essential fields.
    """
    pass  # All fields inherited from CompanyBase


class CompanyInfo(CompanyBase):
    """Company info model used within other responses."""
    companyId: Optional[str] = None
    companyDisplayId: Optional[str] = None
    companyName: Optional[str] = None
    companyCode: Optional[str] = None
    thumbnailLogo: Optional[str] = None
    companyLogo: Optional[str] = None
    mapsMarkerImage: Optional[str] = None
    mainAddress: Optional[MainAddress] = None
    isThirdParty: Optional[bool] = None
    isHidden: Optional[bool] = None


class CompanyDetails(CompanyBase):
    """Detailed company model returned by /api/companies/{companyId}/details.
    
    This includes all fields from CompanyBase plus extensive additional details.
    """
    # User and contact information
    userId: Optional[str] = Field(None, alias="userID")
    contactName: Optional[str] = None
    contactPhone: Optional[str] = None
    primaryContactId: Optional[int] = None
    payerContactId: Optional[int] = None
    payerContactName: Optional[str] = None
    primaryCustomerName: Optional[str] = None
    contactInfo: Optional[str] = None
    
    # Company type and classification
    companyType: Optional[str] = None
    parentCompanyName: Optional[str] = None
    parentCompanyID: Optional[str] = None
    franchiseeName: Optional[str] = None
    
    # Contact details
    companyFax: Optional[str] = None
    companyWebSite: Optional[str] = None
    companyCell: Optional[str] = None
    customerCell: Optional[str] = None
    
    # Business information
    industryType: Optional[str] = None
    industryTypeName: Optional[str] = None
    taxId: Optional[str] = None
    companyDisplayID: Optional[str] = None
    
    # Logos and branding
    companyLogo: Optional[str] = None
    letterHeadLogo: Optional[str] = None
    thumbnailLogo: Optional[str] = None
    mapsMarkerImage: Optional[str] = None
    colorTheme: Optional[str] = None
    
    # Settings and preferences
    parcelOnly: Optional[bool] = None
    isThirdParty: Optional[bool] = None
    isGlobal: Optional[bool] = None
    isQbUser: Optional[bool] = None
    skipIntacct: Optional[bool] = None
    isAccess: Optional[bool] = None
    isPrefered: Optional[bool] = None
    isHide: Optional[bool] = None
    isDontUse: Optional[bool] = None
    
    # Codes and references
    pzCode: Optional[str] = None
    referralCode: Optional[str] = None
    
    # Pricing and insurance
    franchiseeMaturityType: Optional[str] = None
    pricingToUse: Optional[str] = None
    insuranceType: Optional[str] = None
    wholeSaleMarkup: Optional[float] = None
    baseMarkup: Optional[float] = None
    mediumMarkup: Optional[float] = None
    highMarkup: Optional[float] = None
    companyInsurancePricing: Optional[float] = None
    companyServicePricing: Optional[float] = None
    companyTaxPricing: Optional[float] = None
    
    # Carrier and account management
    accountManagerFranchiseeId: Optional[str] = None
    accountManagerFranchiseeName: Optional[str] = None
    carrierAccountsSourceCompanyId: Optional[str] = None
    carrierAccountsSourceCompanyName: Optional[str] = None
    
    # API settings
    autoPriceAPIEnableEmails: Optional[bool] = None
    autoPriceAPIEnableSMSs: Optional[bool] = None
    
    # Capabilities and statistics
    commercialCapabilities: Optional[int] = None
    totalJobs: Optional[int] = None
    totalJobsRevenue: Optional[float] = None
    totalSales: Optional[int] = None
    totalSalesRevenue: Optional[float] = None
    
    # Address information
    mainAddress: Optional[MainAddress] = None
    addressData: Optional[AddressData] = None
    overridableAddressData: Optional[OverridableAddressData] = None
    companyInfo: Optional[CompanyInfo] = None
    
    # Legacy fields
    companyID: Optional[str] = None
    addressID: Optional[int] = None
    address: Optional[str] = None
    address1: Optional[str] = None
    address2: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    stateCode: Optional[str] = None
    countryName: Optional[str] = None
    countryCode: Optional[str] = None
    countryID: Optional[str] = None
    zipCode: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    
    # Metadata
    totalRows: Optional[int] = None
    depth: Optional[int] = None
    miles: Optional[float] = None
    createdUser: Optional[str] = None
    createdDate: Optional[datetime] = None
    createdBy: Optional[str] = None
    modifiedDate: Optional[datetime] = None
    modifiedBy: Optional[str] = None
    
    # Other fields
    result: Optional[str] = None
    addressMappingID: Optional[int] = None
    contactID: Optional[int] = None
    mappingLocations: Optional[str] = None
    locationCount: Optional[int] = None
    baseParent: Optional[str] = None
    copyMaterialFrom: Optional[str] = None


# Company Full Details Models (for /api/companies/{companyId}/fulldetails)

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


class CompanyPricing(BaseModel):
    """Company pricing model."""
    transportationCharge: Optional[TransportationCharge] = None
    transportationMarkups: Optional[MarkupRates] = None
    carrierFreightMarkups: Optional[MarkupRates] = None


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


class CompanyFullDetails(CompanyBase):
    """Full company details returned by /api/companies/{companyId}/fulldetails.
    
    This inherits from CompanyBase but overrides the ID field and adds sections.
    """
    id: Optional[str] = None  # This endpoint returns id at root level
    details: Optional[CompanyDetailsSection] = None
    preferences: Optional[CompanyPreferences] = None
    capabilities: Optional[int] = None
    address: Optional[MainAddress] = None
    pricing: Optional[CompanyPricing] = None
    insurance: Optional[CompanyInsurance] = None
    readOnlyAccess: Optional[bool] = None