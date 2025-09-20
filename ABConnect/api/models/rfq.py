"""Rfq models for ABConnect API."""

from typing import Optional
from pydantic import Field
from .base import ABConnectBaseModel

class AcceptModel(ABConnectBaseModel):
    """AcceptModel model"""

    agent_amount: Optional[float] = Field(None, alias="agentAmount")
    job_state: Optional[str] = Field(None, alias="jobState")


__all__ = ['AcceptModel']
