"""Jobpayment models for ABConnect API."""

from typing import List, Optional
from pydantic import Field
from .base import ABConnectBaseModel, IdentifiedModel
from .shared import CustomerInfo

class AttachCustomerBankModel(ABConnectBaseModel):
    """AttachCustomerBankModel model"""

    bank_token_id: Optional[str] = Field(None, alias="bankTokenId")
    customer_info: Optional[CustomerInfo] = Field(None, alias="customerInfo")


class PaymentSourceDetails(IdentifiedModel):
    """PaymentSourceDetails model"""

    friendly_name: Optional[str] = Field(None, alias="friendlyName")
    bank_name: Optional[str] = Field(None, alias="bankName")
    account_number: Optional[str] = Field(None, alias="accountNumber")
    bank_id: Optional[str] = Field(None, alias="bankId")


class VerifyBankAccountRequest(ABConnectBaseModel):
    """VerifyBankAccountRequest model"""

    values: Optional[List[int]] = Field(None)


__all__ = ['AttachCustomerBankModel', 'PaymentSourceDetails', 'VerifyBankAccountRequest']
