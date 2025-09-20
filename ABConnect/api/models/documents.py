"""Documents models for ABConnect API."""

from typing import List, Optional
from pydantic import Field
from .base import ABConnectBaseModel

class DocumentUpdateModel(ABConnectBaseModel):
    """DocumentUpdateModel model"""

    file_name: Optional[str] = Field(None, alias="fileName")
    type_id: Optional[int] = Field(None, alias="typeId")
    shared: Optional[int] = Field(None)
    tags: Optional[List[str]] = Field(None)
    job_items: Optional[List[str]] = Field(None, alias="jobItems")


__all__ = ['DocumentUpdateModel']
