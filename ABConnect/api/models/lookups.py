"""Lookup models for ABConnect API."""

from typing import Any, Dict, Optional
from enum import Enum
from pydantic import BaseModel


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
    id: str
    value: str
    description: Optional[str] = None
    isActive: bool = True
    sortOrder: Optional[int] = None
    metadata: Optional[Dict[str, Any]] = None