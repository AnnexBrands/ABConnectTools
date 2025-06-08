"""Job models for ABConnect API."""

from datetime import datetime
from typing import Any, Dict, List, Optional
from pydantic import Field
from .base import ABConnectBaseModel, JobStatus, TaskStatus
from .addresses import Address


class JobItem(ABConnectBaseModel):
    """Item within a job."""
    code: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    type: Optional[str] = None
    weight: Optional[float] = None
    dimensions: Optional[Dict[str, float]] = None
    value: Optional[float] = None
    quantity: Optional[int] = None
    currency: str = "USD"
    isHazmat: bool = False
    metadata: Dict[str, Any] = Field(default_factory=dict)


class JobTask(ABConnectBaseModel):
    """Task within a job."""
    jobId: Optional[str] = None
    type: Optional[str] = None
    status: Optional[TaskStatus] = None
    description: Optional[str] = None
    assignedTo: Optional[str] = None
    scheduledDate: Optional[datetime] = None
    completedDate: Optional[datetime] = None
    duration: Optional[int] = None
    notes: Optional[str] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)


class JobShipment(ABConnectBaseModel):
    """Shipment information within a job."""
    trackingNumber: Optional[str] = None
    carrier: Optional[str] = None
    service: Optional[str] = None
    estimatedDelivery: Optional[datetime] = None
    actualDelivery: Optional[datetime] = None
    status: Optional[str] = None
    weight: Optional[float] = None
    cost: Optional[float] = None


class JobPayment(ABConnectBaseModel):
    """Payment information within a job."""
    method: Optional[str] = None
    amount: Optional[float] = None
    currency: str = "USD"
    status: Optional[str] = None
    transactionId: Optional[str] = None
    processedDate: Optional[datetime] = None


class Job(ABConnectBaseModel):
    """Job model with nested entities."""
    displayId: Optional[str] = None
    code: Optional[str] = None
    type: Optional[str] = None
    status: Optional[JobStatus] = None
    customerId: Optional[str] = None
    customerName: Optional[str] = None
    vendorId: Optional[str] = None
    vendorName: Optional[str] = None
    
    # Addresses
    originAddress: Optional[Address] = None
    destinationAddress: Optional[Address] = None
    
    # Nested entities
    items: List[JobItem] = Field(default_factory=list)
    tasks: List[JobTask] = Field(default_factory=list)
    shipments: List[JobShipment] = Field(default_factory=list)
    payments: List[JobPayment] = Field(default_factory=list)
    
    # Dates
    scheduledDate: Optional[datetime] = None
    completedDate: Optional[datetime] = None
    
    # Totals
    totalWeight: Optional[float] = None
    totalValue: Optional[float] = None
    totalCost: Optional[float] = None
    
    # Additional fields
    notes: Optional[List[str]] = None  # API returns notes as a list
    metadata: Dict[str, Any] = Field(default_factory=dict)