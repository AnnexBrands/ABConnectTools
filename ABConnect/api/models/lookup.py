"""Lookup models for ABConnect API."""

from typing import Any, Dict, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field, field_validator
from .base import IdentifiedModel


class LookupKeys(str, Enum):
    """Available lookup keys."""
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


class LookupValue(BaseModel):
    """Lookup value model."""
    id: Optional[int]
    value: Optional[str] = None  # Some lookups use 'value'
    name: Optional[str] = None   # Some lookups use 'name'
    description: Optional[str] = None
    is_active: Optional[bool] = Field(True, alias="isActive")
    sort_order: Optional[int] = Field(None, alias="sortOrder")
    metadata: Optional[Dict[str, Any]] = None
    
    # @field_validator('id', mode='before')
    # @classmethod
    # def convert_id_to_string(cls, v):
    #     """Convert ID to string if it's an integer."""
    #     if isinstance(v, int):
    #         return str(v)
    #     return v
    
    @property
    def display_value(self) -> str:
        """Get the display value (prefers 'value' over 'name')."""
        return self.value or self.name or ""


class ContactTypeEntity(IdentifiedModel):
    """ContactTypeEntity model"""

    value: Optional[str] = Field(None)


class CountryCodeDto(IdentifiedModel):
    """CountryCodeDto model"""

    name: Optional[str] = Field(None)
    iata_code: Optional[str] = Field(None, alias="iataCode")


class LookupDocumentType(BaseModel):
    """Document type lookup model for GET /lookup/documentTypes response."""

    name: Optional[str] = Field(None, description="Document type name")
    value: Optional[int] = Field(None, description="Document type ID")
    document_source: Optional[int] = Field(None, alias="documentSource", description="Document source ID")


class GuidSequentialRangeValue(BaseModel):
    """Density class map lookup model for GET /lookup/densityClassMap response."""

    range_end: Optional[float] = Field(None, alias="rangeEnd", description="Range end value")
    value: Optional[str] = Field(None, description="GUID value")


class LookupAccessKey(BaseModel):
    """Access key lookup model for GET /lookup/accessKeys response."""

    access_key: Optional[str] = Field(None, alias="accessKey", description="Access key GUID")
    friendly_name: Optional[str] = Field(None, alias="friendlyName", description="Friendly name")


__all__ = ['LookupKeys', 'LookupValue', 'LookupDocumentType', 'LookupAccessKey', 'GuidSequentialRangeValue', 'ContactTypeEntity', 'CountryCodeDto']
