"""Base models and enums for ABConnect API."""

from datetime import datetime
from typing import Any, Dict, List, Optional
from enum import Enum
from pydantic import BaseModel, Field, ConfigDict


class ABConnectBaseModel(BaseModel):
    """Base class for all API models."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Optional[str] = None
    created: Optional[datetime] = None
    modified: Optional[datetime] = None


# ==============================================================================
# COMMON ENUMS
# ==============================================================================

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


class ContactType(str, Enum):
    """Contact type enumeration."""
    PRIMARY = "primary"
    BILLING = "billing"
    SHIPPING = "shipping"
    TECHNICAL = "technical"
    OTHER = "other"


# ==============================================================================
# MODEL REGISTRY
# ==============================================================================

# This will be populated by importing modules
MODEL_REGISTRY = {}


def get_model_class(resource_name: str) -> Optional[type]:
    """Get model class for a resource name."""
    # Lazy import to avoid circular dependencies
    if not MODEL_REGISTRY:
        from .addresses import Address
        from .companies import CompanyBasic, CompanyDetails, CompanyFullDetails
        from .contacts import Contact
        from .jobs import Job, JobItem, JobTask, JobShipment, JobPayment
        from .users import User
        from .documents import Document
        from .forms import Form
        from .lookups import LookupValue
        
        MODEL_REGISTRY.update({
            # Address models
            "address": Address,
            "addresses": Address,
            
            # Company models
            "company": CompanyBasic,
            "companies": CompanyBasic,
            "company_details": CompanyDetails,
            "company_fulldetails": CompanyFullDetails,
            
            # Contact models
            "contact": Contact,
            "contacts": Contact,
            
            # Job models
            "job": Job,
            "jobs": Job,
            "job_item": JobItem,
            "job_task": JobTask,
            "job_shipment": JobShipment,
            "job_payment": JobPayment,
            
            # User models
            "user": User,
            "users": User,
            
            # Document models
            "document": Document,
            "documents": Document,
            
            # Form models
            "form": Form,
            "forms": Form,
            
            # Lookup models
            "lookup_value": LookupValue,
        })
    
    return MODEL_REGISTRY.get(resource_name.lower())


def parse_response(data: Any, resource_name: Optional[str] = None) -> Any:
    """Parse API response into model instances."""
    if not data:
        return data
    
    model_class = get_model_class(resource_name) if resource_name else None
    
    if isinstance(data, list):
        if model_class and hasattr(model_class, "model_validate"):
            return [model_class.model_validate(item) for item in data]
        return data
    
    if isinstance(data, dict):
        # Import here to avoid circular dependency
        from .responses import PaginatedResponse, ErrorResponse
        
        if any(key in data for key in ["data", "items", "results"]):
            return PaginatedResponse.from_dict(data, model_class)
        
        if "error" in data:
            return ErrorResponse.model_validate(data)
        
        if model_class and hasattr(model_class, "model_validate"):
            return model_class.model_validate(data)
    
    return data