"""Documents models for ABConnect API."""

from typing import List, Optional, Union
from pydantic import Field
from .base import ABConnectBaseModel
from .enums import DocumentType


class DocumentUpdateModel(ABConnectBaseModel):
    """DocumentUpdateModel model"""

    file_name: Optional[str] = Field(None, alias="fileName")
    type_id: Optional[Union[int, DocumentType]] = Field(None, alias="typeId", description="Document type ID. See DocumentType enum for valid values.")
    shared: Optional[int] = Field(None)
    tags: Optional[List[str]] = Field(None)
    job_items: Optional[List[str]] = Field(None, alias="jobItems")


__all__ = ['DocumentUpdateModel']
