"""Document upload models for ABConnect API."""

from typing import List, Optional, Union
from pydantic import BaseModel, Field
from .base import ABConnectBaseModel
from .enums import DocumentType




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


class DocumentUploadRequest(BaseModel):
    """Request model for uploading documents of any type.

    Note: The file itself is NOT part of this model. Files must be passed
    separately to the upload method as multipart form data::

        files = {"file": (filename, content, mime_type)}
        data = request.model_dump(by_alias=True, exclude_none=True)
        response = requests.post(url, files=files, data=data)

    Example:
        >>> from ABConnect import models
        >>> request = DocumentUploadRequest(
        ...     job_display_id=2000000,
        ...     document_type=models.DocumentType.BOL,
        ...     shared=28,
        ...     job_items=["550e8400-e29b-41d4-a716-446655440001"]
        ... )
    """

    job_display_id: int = Field(..., alias="JobDisplayId", description="The job display ID (e.g., 2000000)")
    document_type: Union[int, DocumentType] = Field(..., alias="DocumentType", description="Document type ID. See DocumentType enum.")
    document_type_description: Optional[str] = Field(None, alias="DocumentTypeDescription", description="Document type description (auto-set from enum if not provided)")
    shared: int = Field(28, alias="Shared", description="Sharing level bitmask (any int, e.g., 0=private, 28=shared)")
    job_items: Optional[List[str]] = Field(None, alias="JobItems", description="List of item UUIDs to associate with document")
    rfq_id: Optional[int] = Field(None, alias="RfqId", description="RFQ ID if applicable")

    class Config:
        populate_by_name = True

    def model_post_init(self, __context) -> None:
        """Auto-populate document_type_description from enum if not provided."""
        if self.document_type_description is None and isinstance(self.document_type, DocumentType):
            # Convert enum name to title case with spaces
            self.document_type_description = self.document_type.name.replace("_", " ").title()


# Alias for item photo uploads (same structure, document_type=6 by convention)
ItemPhotoUploadRequest = DocumentUploadRequest

class DocumentUploadResponse(ABConnectBaseModel):
    """Response model for document upload."""

    success: Optional[bool] = Field(None, description="Whether the upload was successful")
    successfully: Optional[bool] = Field(None, description="Whether the upload completed successfully")
    uploaded_files: Optional[List[UploadedFile]] = Field(None, alias="uploadedFiles", description="List of uploaded files")
    message: Optional[str] = Field(None, description="Response message")
    id: Optional[int] = Field(None, description="Document ID if single file uploaded")
    file_name: Optional[str] = Field(None, alias="fileName", description="Filename if single file uploaded")
    amazon_exception: Optional[bool] = Field(None, alias="amazonException", description="Whether an Amazon S3 exception occurred")
    amazon_error_message: Optional[str] = Field(None, alias="amazonErrorMessage", description="Amazon S3 error message if any")
    amazon_error_code: Optional[str] = Field(None, alias="amazonErrorCode", description="Amazon S3 error code if any")
    document_details: Optional[dict] = Field(None, alias="documentDetails", description="Detailed document information")


__all__ = [
    'ItemPhotoUploadRequest',
    'UploadedFile',
    'ItemPhotoUploadResponse',
    'DocumentUploadRequest',
    'DocumentUploadResponse',
]