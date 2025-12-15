"""Planner models for ABConnect API."""

from __future__ import annotations
from typing import Optional
from pydantic import Field
from .base import JobRelatedModel
from .shared import Details, ItemTotals, CreatedTask

class PlannerTask(JobRelatedModel):
    """PlannerTask model"""

    job_display_id: Optional[int] = Field(None, alias="jobDisplayId")
    task_code: Optional[str] = Field(None, alias="taskCode")
    status: Optional[str] = Field(None)
    agent_id: Optional[str] = Field(None, alias="agentId")
    pickup_details: Optional[Details] = Field(None, alias="pickupDetails")
    delivery_details: Optional[Details] = Field(None, alias="deliveryDetails")
    item_totals: Optional[ItemTotals] = Field(None, alias="itemTotals")
    created_task: Optional[CreatedTask] = Field(None, alias="createdTask")


__all__ = ['PlannerTask']
