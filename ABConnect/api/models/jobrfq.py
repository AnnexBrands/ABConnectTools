"""Jobrfq models for ABConnect API."""

from __future__ import annotations
from typing import List, Optional, TYPE_CHECKING
from datetime import datetime
from pydantic import Field
from .base import ActiveModel
from .enums import ServiceType, SendEmailStatus
from .shared import QuoteRequestComment

if TYPE_CHECKING:
    from .address import AddressDetails
    from .companies import CommercialCapabilities

# QuoteRequestStatus is defined in enums as well
from .enums import QuoteRequestStatus

class QuoteRequestDisplayInfo(ActiveModel):
    """QuoteRequestDisplayInfo model"""

    request_id: Optional[int] = Field(None, alias="requestId")
    job_id: Optional[str] = Field(None, alias="jobId")
    company_id: Optional[str] = Field(None, alias="companyId")
    type: Optional[ServiceType] = Field(None)
    requested_amount: Optional[float] = Field(None, alias="requestedAmount")
    agent_amount: Optional[float] = Field(None, alias="agentAmount")
    final_amount: Optional[float] = Field(None, alias="finalAmount")
    message: Optional[str] = Field(None)
    due_date: Optional[datetime] = Field(None, alias="dueDate")
    job_service_start: Optional[datetime] = Field(None, alias="jobServiceStart")
    job_service_end: Optional[datetime] = Field(None, alias="jobServiceEnd")
    negotiable_price: Optional[bool] = Field(None, alias="negotiablePrice")
    status: Optional[QuoteRequestStatus] = Field(None)
    expedited: Optional[bool] = Field(None)
    notify_bidder: Optional[bool] = Field(None, alias="notifyBidder")
    agent_amount_job_state: Optional[str] = Field(None, alias="agentAmountJobState")
    company_code: Optional[str] = Field(None, alias="companyCode")
    agent_responded: Optional[bool] = Field(None, alias="agentResponded")
    sent_utc: Optional[datetime] = Field(None, alias="sentUtc")
    sent_by: Optional[str] = Field(None, alias="sentBy")
    comments: Optional[List[QuoteRequestComment]] = Field(None)
    company_name: Optional[str] = Field(None, alias="companyName")
    contact_name: Optional[str] = Field(None, alias="contactName")
    contact_phone: Optional[str] = Field(None, alias="contactPhone")
    contact_email: Optional[str] = Field(None, alias="contactEmail")
    address: Optional[AddressDetails] = Field(None)
    miles: Optional[float] = Field(None)
    commercial_capabilities: Optional[CommercialCapabilities] = Field(None, alias="commercialCapabilities")
    dont_use: Optional[bool] = Field(None, alias="dontUse")
    api_send_status: Optional[SendEmailStatus] = Field(None, alias="apiSendStatus")


__all__ = ['QuoteRequestDisplayInfo']
