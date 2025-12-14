"""Partner models for API version 709.

New models for partner management.
"""

from typing import Optional
from pydantic import Field

from .base import ABConnectBaseModel


__all__ = [
    'Partner',
    'PartnerServiceResponse',
]


class Partner(ABConnectBaseModel):
    """Partner model representing a business partner.

    .. versionadded:: 709
    """

    id: int = Field(..., description="Partner ID")
    name: Optional[str] = Field(None, description="Partner name")


class PartnerServiceResponse(ABConnectBaseModel):
    """Service response wrapper for Partner operations.

    .. versionadded:: 709
    """

    success: bool = Field(False, description="Whether the operation was successful")
    error_message: Optional[str] = Field(None, alias="errorMessage", description="Error message if operation failed")
    data: Optional[Partner] = Field(None, description="Partner data")
