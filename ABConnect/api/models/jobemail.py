"""Jobemail models for ABConnect API."""

from typing import Optional
from pydantic import Field
from .base import ABConnectBaseModel

class SendDocumentEmailModel(ABConnectBaseModel):
    """SendDocumentEmailModel model"""

    to: str = Field(..., min_length=1)
    document_id: Optional[int] = Field(None, alias="documentId")


__all__ = ['SendDocumentEmailModel']
