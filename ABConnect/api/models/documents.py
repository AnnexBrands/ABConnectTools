"""Document models for ABConnect API."""

from typing import Any, Dict, List, Optional
from pydantic import Field
from .base import ABConnectBaseModel


class Document(ABConnectBaseModel):
    """Document model."""
    name: Optional[str] = None
    type: Optional[str] = None
    size: Optional[int] = None
    mimeType: Optional[str] = None
    url: Optional[str] = None
    jobId: Optional[str] = None
    uploadedBy: Optional[str] = None
    tags: List[str] = Field(default_factory=list)
    metadata: Dict[str, Any] = Field(default_factory=dict)