"""Lookup models for ABConnect API."""

from typing import Any, Dict, Optional, Union
from enum import Enum
from pydantic import BaseModel, field_validator


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
    id: Union[str, int]  # Can be either string or int
    value: Optional[str] = None  # Some lookups use 'value'
    name: Optional[str] = None   # Some lookups use 'name'
    description: Optional[str] = None
    isActive: Optional[bool] = True
    sortOrder: Optional[int] = None
    metadata: Optional[Dict[str, Any]] = None
    
    @field_validator('id', mode='before')
    @classmethod
    def convert_id_to_string(cls, v):
        """Convert ID to string if it's an integer."""
        if isinstance(v, int):
            return str(v)
        return v
    
    @property
    def display_value(self) -> str:
        """Get the display value (prefers 'value' over 'name')."""
        return self.value or self.name or ""