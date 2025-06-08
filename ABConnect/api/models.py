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


class Company(ABConnectBaseModel):
    """Company model."""

    code: Optional[str] = None
    name: Optional[str] = None
    type: Optional[CompanyType] = None
    taxId: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    website: Optional[str] = None
    addresses: List[Address] = Field(default_factory=list)
    contacts: List[Contact] = Field(default_factory=list)
    isActive: bool = True
    metadata: Dict[str, Any] = Field(default_factory=dict)


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
