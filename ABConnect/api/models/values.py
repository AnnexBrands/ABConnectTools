"""Values models for ABConnect API."""

from typing import Optional
from pydantic import Field
from .base import ABConnectBaseModel


class ValuesResponse(ABConnectBaseModel):
    """Response model for GET /Values endpoint.

    Contains configuration values for the current user/company context.
    """

    code: Optional[str] = Field(None)
    email_signature_template: Optional[str] = Field(None, alias="emailSignatureTemplate")
    portal_url: Optional[str] = Field(None, alias="portalUrl")
    stripe_success_url_format: Optional[str] = Field(None, alias="stripeSuccessUrlFormat")
    stripe_cancel_url_format: Optional[str] = Field(None, alias="stripeCancelUrlFormat")


__all__ = ['ValuesResponse']
