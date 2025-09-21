"""Enhanced Documents API endpoints with Pydantic models.

This module provides enhanced document upload functionality using Pydantic models
while maintaining backward compatibility with the original dict-based interface.
"""

from typing import List, Tuple, BinaryIO, Optional, Dict, Any, Union
from ..models.document_upload import ItemPhotoUploadRequest, ItemPhotoUploadResponse
from ...common import DocType
from .documents import DocumentsEndpoint


class DocumentsEnhancedEndpoint(DocumentsEndpoint):
    """Enhanced Documents endpoint with Pydantic model support.

    Extends the auto-generated DocumentsEndpoint to provide additional
    functionality with type-safe Pydantic models.
    """

    def upload_item_photos_v2(
        self,
        jobid: str,
        itemid: int,
        files: List[Tuple[str, BinaryIO]],
        rfqid: Optional[int] = None,
        return_model: bool = True
    ) -> Union[ItemPhotoUploadResponse, Dict[str, Any]]:
        """Upload photos for a specific item in a job using Pydantic models.

        This is the enhanced version that uses Pydantic models for type safety.
        Set return_model=False for backward compatibility to get a dict response.

        Args:
            jobid: The job display ID (e.g., 'JOB-2024-001')
            itemid: The ID of the item within the job
            files: List of tuples containing photo files (field_name, file_object)
            rfqid: Optional RFQ ID if applicable
            return_model: If True, returns Pydantic model; if False, returns dict

        Returns:
            ItemPhotoUploadResponse model or dict depending on return_model parameter

        Example:
            >>> endpoint = DocumentsEnhancedEndpoint()
            >>> photo_files = []
            >>> for photo_path in ['front.jpg', 'back.jpg']:
            ...     f = open(photo_path, 'rb')
            ...     photo_files.append(('files[]', f))
            >>>
            >>> # Get Pydantic model response
            >>> response = endpoint.upload_item_photos_v2(
            ...     jobid='JOB-2024-001',
            ...     itemid=12345,
            ...     files=photo_files
            ... )
            >>> print(f"Uploaded {len(response.uploaded_files)} photos")
            >>> for file in response.uploaded_files:
            ...     print(f"  - {file.file_name}: {file.file_size} bytes")
        """
        # Create the request model
        request = ItemPhotoUploadRequest(
            job_display_id=jobid,
            document_type=DocType.Item_Photo.value,
            document_type_description=DocType.Item_Photo.fmt,
            shared=28,
            job_items=[itemid],
            rfq_id=rfqid
        )

        # Convert model to dict for the API call
        data = request.model_dump(by_alias=True, exclude_none=True)

        # Make the upload request
        response_data = self._r.upload_file("documents", files=files, data=data)

        # Return as model or dict based on preference
        if return_model:
            return ItemPhotoUploadResponse.model_validate(response_data)
        return response_data

    def upload_item_photos(
        self,
        jobid: str,
        itemid: int,
        files: List[Tuple[str, BinaryIO]],
        rfqid: Optional[int] = None
    ) -> Dict[str, Any]:
        """Upload photos for a specific item in a job (backward compatible).

        This maintains backward compatibility with the original function signature
        and return type. It internally uses the v2 method with Pydantic models
        but returns a dict for compatibility.

        Args:
            jobid: The job display ID (e.g., 'JOB-2024-001')
            itemid: The ID of the item within the job
            files: List of tuples containing photo files
            rfqid: Optional RFQ ID if applicable

        Returns:
            dict: Upload response containing information about uploaded photos

        Note:
            This is a backward compatibility wrapper. For new code, consider
            using upload_item_photos_v2() with return_model=True for type safety.
        """
        return self.upload_item_photos_v2(
            jobid=jobid,
            itemid=itemid,
            files=files,
            rfqid=rfqid,
            return_model=False  # Return dict for backward compatibility
        )


# Helper function to migrate from dict to model
def dict_to_upload_response(response_dict: Dict[str, Any]) -> ItemPhotoUploadResponse:
    """Convert a dictionary response to ItemPhotoUploadResponse model.

    Args:
        response_dict: Dictionary response from the API

    Returns:
        ItemPhotoUploadResponse: Typed Pydantic model

    Example:
        >>> # Converting legacy dict response to model
        >>> dict_response = endpoint.upload_item_photos(...)  # Returns dict
        >>> model_response = dict_to_upload_response(dict_response)
        >>> # Now you have type-safe access
        >>> print(model_response.success)
    """
    return ItemPhotoUploadResponse.model_validate(response_dict)


# Helper function to convert model to dict if needed
def upload_response_to_dict(response: ItemPhotoUploadResponse) -> Dict[str, Any]:
    """Convert ItemPhotoUploadResponse model to dictionary.

    Args:
        response: Pydantic model response

    Returns:
        dict: Dictionary representation of the response

    Example:
        >>> # Converting model to dict for legacy code
        >>> model_response = endpoint.upload_item_photos_v2(...)  # Returns model
        >>> dict_response = upload_response_to_dict(model_response)
    """
    return response.model_dump(by_alias=True)