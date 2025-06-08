"""User models for ABConnect API."""

from datetime import datetime
from typing import List, Optional
from pydantic import Field
from .base import ABConnectBaseModel


class User(ABConnectBaseModel):
    """User model."""
    username: Optional[str] = None
    email: Optional[str] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    role: Optional[str] = None
    permissions: List[str] = Field(default_factory=list)
    companyId: Optional[str] = None
    isActive: bool = True
    lastLogin: Optional[datetime] = None