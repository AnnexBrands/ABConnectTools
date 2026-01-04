"""Base models and common patterns for ABConnect API.

This module provides base classes that capture common patterns
found across the 293 swagger schemas.
"""

from datetime import datetime
from typing import Any, Dict, List, Optional, Union, TypeVar, Type
from enum import Enum
from pydantic import BaseModel, Field, ConfigDict, validator, TypeAdapter


T = TypeVar('T', bound='ABConnectBaseModel')


class ABConnectBaseModel(BaseModel):
    """Base class for all ABConnect API models.

    Provides common configuration and utilities.
    """
    model_config = ConfigDict(
        extra="forbid",  # Forbid extra fields from API responses (schemas may evolve)
        populate_by_name=True,
        str_strip_whitespace=True,
        validate_assignment=True,
        use_enum_values=True
    )

    @classmethod
    def check(cls: Type[T], data: Union[Dict[str, Any], List[Dict[str, Any]], T, List[T]], exclude_unset: bool = True) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
        """Validate data and return as dict(s) with proper aliasing and JSON serialization.

        This method validates incoming data against the model schema and returns
        it as a dict (or list of dicts) suitable for API requests. All special types
        (datetime, UUID, etc.) are automatically serialized to JSON-compatible formats.

        Args:
            data: Data to validate - can be:
                - Single dict
                - List of dicts
                - Single model instance
                - List of model instances
            exclude_unset: If True (default), only include fields that were explicitly
                provided in the input data. If False, include all fields with their
                default values.

        Returns:
            Validated data as dict(s) with:
            - camelCase field names (by_alias=True)
            - JSON-serializable values (mode='json') - datetime as ISO strings, etc.
            - Only fields that were actually provided (exclude_unset=True by default)

        Raises:
            ValidationError: If data doesn't match the model schema

        Example:
            # Only sends fields that were provided, datetime serialized to ISO string
            data = {"ratesKey": "abc", "shipOutDate": datetime.now()}
            SetRateModel.check(data)  # {"ratesKey": "abc", "shipOutDate": "2025-10-19T..."}
            # carrierAccountId and active are NOT included (weren't provided)

            # To include all fields with defaults:
            SetRateModel.check(data, exclude_unset=False)
        """
        # Handle list of items
        if isinstance(data, list):
            adapter = TypeAdapter(List[cls])
            validated = adapter.validate_python(data)
            return [item.model_dump(by_alias=True, exclude_none=True, exclude_unset=exclude_unset, mode='json') for item in validated]

        # Handle single item (dict or model instance)
        validated = cls.model_validate(data)
        return validated.model_dump(by_alias=True, exclude_none=True, exclude_unset=exclude_unset, mode='json')

    def json(self) -> Dict[str, Any]:
        """Return the model data as a JSON-serializable dict with camelCase keys."""
        return self.model_dump(by_alias=True, exclude_none=True, mode='json')
    
    def __repr__(self) -> str:
            """Return a pretty, indented, one-field-per-line representation."""
            # Get all fields that are set (exclude_none=True removes Nones)
            fields = self.model_dump(exclude_none=True, by_alias=True)

            if not fields:
                return f"{self.__class__.__name__}()"

            lines = [f"{self.__class__.__name__}("]
            for key, value in fields.items():
                # Indent and format each field
                repr_value = repr(value)
                # Multi-line values (like nested models) get extra indentation
                if "\n" in repr_value:
                    indented = "\n    ".join(repr_value.split("\n"))
                    lines.append(f"    {key}={indented},")
                else:
                    lines.append(f"    {key}={repr_value},")
            lines.append(")")

            return "\n".join(lines)

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