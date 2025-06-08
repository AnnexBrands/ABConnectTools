"""Form models for ABConnect API."""

from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field
from .base import ABConnectBaseModel


class FormField(BaseModel):
    """Form field definition."""
    name: str
    type: str
    label: Optional[str] = None
    required: bool = False
    defaultValue: Optional[Any] = None
    options: Optional[List[str]] = None
    validation: Optional[Dict[str, Any]] = None


class Form(ABConnectBaseModel):
    """Form/Template model."""
    name: Optional[str] = None
    type: Optional[str] = None
    version: Optional[str] = None
    fields: List[FormField] = Field(default_factory=list)
    isActive: bool = True
    metadata: Dict[str, Any] = Field(default_factory=dict)