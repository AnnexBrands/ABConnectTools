"""Response models for API data structures.

This module provides data models and type definitions for API responses,
organized by swagger tags for better structure and maintainability.
"""

# Import all models for backward compatibility
from .base import (
    ABConnectBaseModel,
    CompanyType,
    COMPANY_TYPE_IDS,
    JobStatus,
    TaskStatus,
    ContactType,
    MODEL_REGISTRY,
    get_model_class,
    parse_response
)

from .addresses import (
    AddressCoordinates,
    AddressBase,
    Address,
    MainAddress,
    AddressData,
    OverridableValue,
    OverridableAddressData
)

from .companies import (
    CompanyBase,
    CompanyBasic,
    CompanyInfo,
    CompanyDetails,
    CompanyDetailsSection,
    CompanyPreferences,
    CompanyPricing,
    CompanyInsurance,
    CompanyFullDetails,
    FileUpload,
    TransportationCharge,
    MarkupRates,
    InsuranceOption
)

from .contacts import Contact

from .jobs import (
    JobItem,
    JobTask,
    JobShipment,
    JobPayment,
    Job
)

from .users import User

from .documents import Document

from .forms import FormField, Form

from .lookups import LookupKeys, LookupValue

from .responses import PaginatedResponse, ErrorResponse

# Make all imports available at package level
__all__ = [
    # Base models and enums
    'ABConnectBaseModel',
    'CompanyType',
    'COMPANY_TYPE_IDS',
    'JobStatus',
    'TaskStatus',
    'ContactType',
    
    # Address models
    'AddressCoordinates',
    'AddressBase',
    'Address',
    'MainAddress',
    'AddressData',
    'OverridableValue',
    'OverridableAddressData',
    
    # Company models
    'CompanyBase',
    'CompanyBasic',
    'CompanyInfo',
    'CompanyDetails',
    'CompanyDetailsSection',
    'CompanyPreferences',
    'CompanyPricing',
    'CompanyInsurance',
    'CompanyFullDetails',
    'FileUpload',
    'TransportationCharge',
    'MarkupRates',
    'InsuranceOption',
    
    # Contact models
    'Contact',
    
    # Job models
    'JobItem',
    'JobTask',
    'JobShipment',
    'JobPayment',
    'Job',
    
    # User models
    'User',
    
    # Document models
    'Document',
    
    # Form models
    'FormField',
    'Form',
    
    # Lookup models
    'LookupKeys',
    'LookupValue',
    
    # Response models
    'PaginatedResponse',
    'ErrorResponse',
    
    # Utility functions
    'MODEL_REGISTRY',
    'get_model_class',
    'parse_response'
]