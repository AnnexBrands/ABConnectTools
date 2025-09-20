"""Jobintacct models for ABConnect API."""

from typing import Optional
from datetime import datetime
from pydantic import Field
from .base import ABConnectBaseModel

class CreateJobIntacctModel(ABConnectBaseModel):
    """CreateJobIntacctModel model"""

    invoice_term: str = Field(..., alias="invoiceTerm", min_length=1)
    freight_acct: str = Field(..., alias="freightAcct", min_length=1)
    invoice_descr: str = Field(..., alias="invoiceDescr", min_length=1)
    franchisee_id: str = Field(..., alias="franchiseeId")
    invoice_date: Optional[datetime] = Field(None, alias="invoiceDate")
    po_num: Optional[str] = Field(None, alias="poNum")


__all__ = ['CreateJobIntacctModel']
