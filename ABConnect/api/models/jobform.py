"""Jobform models for ABConnect API."""

from typing import Optional
from pydantic import Field
from .base import JobRelatedModel

class FormsShipmentPlan(JobRelatedModel):
    """FormsShipmentPlan model"""

    job_shipment_id: Optional[str] = Field(None, alias="jobShipmentId")
    from_address_id: Optional[int] = Field(None, alias="fromAddressId")
    to_address_id: Optional[int] = Field(None, alias="toAddressId")
    provider_id: Optional[str] = Field(None, alias="providerId")
    sequence_no: Optional[int] = Field(None, alias="sequenceNo")
    from_location_company_name: Optional[str] = Field(None, alias="fromLocationCompanyName")
    to_location_company_name: Optional[str] = Field(None, alias="toLocationCompanyName")
    transport_type: Optional[str] = Field(None, alias="transportType")
    provider_company_name: Optional[str] = Field(None, alias="providerCompanyName")
    option_index: Optional[int] = Field(None, alias="optionIndex")


__all__ = ['FormsShipmentPlan']
