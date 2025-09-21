"""Document upload models for ABConnect API."""

from typing import List, Optional, BinaryIO, Tuple, Any
from pydantic import BaseModel, Field
from .base import ABConnectBaseModel


class ItemPhotoUploadRequest(BaseModel):
    """Request model for uploading item photos."""

    job_display_id: int = Field(..., alias="JobDisplayId", description="The job display ID (e.g., 2000000)")
    document_type: int = Field(..., alias="DocumentType", description="Document type ID (6 for Item_Photo)")
    document_type_description: str = Field(..., alias="DocumentTypeDescription", description="Document type description")
    shared: int = Field(28, alias="Shared", description="Sharing level")
    job_items: List[str] = Field(..., alias="JobItems", description="List of item UUIDs")
    rfq_id: Optional[int] = Field(None, alias="RfqId", description="RFQ ID if applicable")

    class Config:
        populate_by_name = True


class UploadedFile(ABConnectBaseModel):
    """Model for an uploaded file in the response."""

    id: int = Field(..., description="File ID")
    file_name: str = Field(..., alias="fileName", description="Name of the uploaded file")
    file_size: int = Field(..., alias="fileSize", description="Size of the file in bytes")
    document_type: str = Field(..., alias="documentType", description="Type of document")
    item_id: int = Field(..., alias="itemId", description="Associated item ID")
    thumbnail_url: str = Field(..., alias="thumbnailUrl", description="URL to the thumbnail")


class ItemPhotoUploadResponse(ABConnectBaseModel):
    """Response model for item photo upload."""

    success: bool = Field(..., description="Whether the upload was successful")
    uploaded_files: List[UploadedFile] = Field(..., alias="uploadedFiles", description="List of uploaded files")
    message: str = Field(..., description="Response message")


__all__ = ['ItemPhotoUploadRequest', 'UploadedFile', 'ItemPhotoUploadResponse']