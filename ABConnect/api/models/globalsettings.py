"""Globalsettings models for ABConnect API."""

from __future__ import annotations
from typing import List, Optional
from datetime import datetime
from pydantic import Field
from .base import IdentifiedModel, JobRelatedModel

class CompanyHierarchyInfo(IdentifiedModel):
    """CompanyHierarchyInfo model"""

    name: Optional[str] = Field(None)
    code: Optional[str] = Field(None)
    children: Optional[List[CompanyHierarchyInfo]] = Field(None)


class SelectApproveInsuranceResult(JobRelatedModel):
    """SelectApproveInsuranceResult model"""

    job_display_id: Optional[int] = Field(None, alias="jobDisplayId")
    franchisee: Optional[str] = Field(None)
    customer_name: Optional[str] = Field(None, alias="customerName")
    job_status: Optional[str] = Field(None, alias="jobStatus")
    booked_date: Optional[datetime] = Field(None, alias="bookedDate")
    total_weight: Optional[float] = Field(None, alias="totalWeight")
    insured_value: Optional[float] = Field(None, alias="insuredValue")
    transportation: Optional[str] = Field(None)
    total_amount: Optional[float] = Field(None, alias="totalAmount")
    is_ins_approved: Optional[int] = Field(None, alias="isInsApproved")


__all__ = ['CompanyHierarchyInfo', 'SelectApproveInsuranceResult']
