"""Companysettings models for ABConnect API."""

from typing import Optional
from pydantic import Field
from .base import CompanyRelatedModel

class CompanySetupData(CompanyRelatedModel):
    """CompanySetupData model"""

    extra_tax_row: Optional[bool] = Field(None, alias="extraTaxRow")
    default_is_private_contact: Optional[bool] = Field(None, alias="defaultIsPrivateContact")
    skip_intacct: Optional[bool] = Field(None, alias="skipIntacct")
    auto_price_api_enable_emails: Optional[bool] = Field(None, alias="autoPriceApiEnableEmails")
    auto_price_api_enable_sm_ss: Optional[bool] = Field(None, alias="autoPriceApiEnableSmSs")


__all__ = ['CompanySetupData']
