"""Contact models for ABConnect API."""

from typing import Optional
from .base import ABConnectBaseModel, ContactType


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
    contactType: Optional[ContactType] = None
    isActive: bool = True