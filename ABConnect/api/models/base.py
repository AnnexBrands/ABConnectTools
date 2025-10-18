"""Base models and common patterns for ABConnect API.

This module provides base classes that capture common patterns
found across the 293 swagger schemas.
"""

from datetime import datetime
from typing import Any, Dict, List, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field, ConfigDict, validator


class ABConnectBaseModel(BaseModel):
    """Base class for all ABConnect API models.

    Provides common configuration and utilities.
    """
    model_config = ConfigDict(
        extra="forbid",  # Strict mode for generated models
        populate_by_name=True,
        str_strip_whitespace=True,
        validate_assignment=True,
        use_enum_values=True
    )


class IdentifiedModel(ABConnectBaseModel):
    """Base for models with ID fields (63 schemas have 'id')."""
    id: Optional[Union[str, int]] = Field(None, description="Unique identifier")


class TimestampedModel(ABConnectBaseModel):
    """Base for models with timestamp fields.
    
    Used by models with created/modified tracking:
    - createdDate: 21 schemas
    - modifiedDate: 18 schemas  
    - createdBy: 17 schemas
    - modifiedBy: 10 schemas
    """
    created_date: Optional[datetime] = Field(None, alias="createdDate", description="Creation timestamp")
    modified_date: Optional[datetime] = Field(None, alias="modifiedDate", description="Last modification timestamp")
    created_by: Optional[str] = Field(None, alias="createdBy", description="Creator identifier")
    modified_by: Optional[str] = Field(None, alias="modifiedBy", description="Last modifier identifier")


class ActiveModel(ABConnectBaseModel):
    """Base for models with isActive field (30 schemas)."""
    is_active: Optional[bool] = Field(None, alias="isActive", description="Whether the record is active")


class CompanyRelatedModel(ABConnectBaseModel):
    """Base for models related to companies.
    
    Used by models with company associations:
    - companyId: 23 schemas
    - companyName: 30 schemas
    """
    company_id: Optional[str] = Field(None, alias="companyId", description="Associated company ID")
    company_name: Optional[str] = Field(None, alias="companyName", description="Associated company name")


class JobRelatedModel(ABConnectBaseModel):
    """Base for models related to jobs.
    
    Used by models with job associations:
    - jobId: 20 schemas
    - jobID: 13 schemas (legacy)
    """
    job_id: Optional[str] = Field(None, alias="jobId", description="Associated job ID")


class FullAuditModel(IdentifiedModel, TimestampedModel, ActiveModel):
    """Complete audit model with ID, timestamps, and active status.
    
    For models that need full audit trail tracking.
    """
    pass


class CompanyAuditModel(FullAuditModel, CompanyRelatedModel):
    """Company-related model with full audit trail."""
    pass


class JobAuditModel(FullAuditModel, JobRelatedModel):
    """Job-related model with full audit trail."""
    pass


# ==============================================================================
# UTILITIES
# ==============================================================================

def to_pascal_case(snake_str: str) -> str:
    """Convert snake_case to PascalCase."""
    return ''.join(word.capitalize() for word in snake_str.split('_'))


def to_snake_case(camel_str: str) -> str:
    """Convert camelCase/PascalCase to snake_case."""
    import re
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', camel_str)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


# Export all base classes
__all__ = [
    'ABConnectBaseModel',
    'IdentifiedModel', 
    'TimestampedModel',
    'ActiveModel',
    'CompanyRelatedModel',
    'JobRelatedModel', 
    'FullAuditModel',
    'CompanyAuditModel',
    'JobAuditModel',
    'to_pascal_case',
    'to_snake_case'
]