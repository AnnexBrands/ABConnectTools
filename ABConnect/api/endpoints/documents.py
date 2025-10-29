"""Documents API endpoints.

Auto-generated from swagger.json specification.
Provides type-safe access to documents/* endpoints.
"""

from typing import Optional, Union, BinaryIO
from pathlib import Path
from ..models.documents import DocumentUpdateModel
from ..models.document_upload import ItemPhotoUploadRequest
from .base import BaseEndpoint


class DocumentsEndpoint(BaseEndpoint):
    """Documents API endpoint operations.
    
    Handles all API operations for /api/documents/* endpoints.
    Total endpoints: 6
    """
    
    api_path = "documents"

    def get_get_thumbnail(self, docPath: str) -> Union[dict, bytes]:
        """GET /api/documents/get/thumbnail/{docPath}

        Get a thumbnail of a document. Returns binary image data for image thumbnails,
        or JSON response data for other cases.

        Args:
            docPath: Path to the document

        Returns:
            Union[dict, bytes]: Binary image data for thumbnails, or JSON response data
        """
        path = "/get/thumbnail/{docPath}"
        path = path.replace("{docPath}", docPath)
        kwargs = {}
        return self._make_request("GET", path, **kwargs)

    def get_get(self, docPath: str) -> Union[dict, bytes]:
        """GET /api/documents/get/{docPath}

        Download a document. Returns binary data for files like PDFs, images, etc.,
        or JSON response data for other cases.

        Args:
            docPath: Path to the document

        Returns:
            Union[dict, bytes]: Binary document data (e.g., PDF bytes, image bytes),
                               or JSON response data

        Example:
            >>> # Download a PDF document
            >>> pdf_bytes = client.docs.get_get("path/to/document.pdf")
            >>> with open("downloaded.pdf", "wb") as f:
            ...     f.write(pdf_bytes)
        """
        path = "/get/{docPath}"
        path = path.replace("{docPath}", docPath)
        kwargs = {}
        return self._make_request("GET", path, **kwargs)
    def get_list(self, job_display_id: Optional[str] = None, item_id: Optional[str] = None, rfq_id: Optional[str] = None) -> dict:
        """GET /api/documents/list
        
        
        
        Returns:
            dict: API response data
        """
        path = "/list"
        kwargs = {}
        params = {}
        if job_display_id is not None:
            params["jobDisplayId"] = job_display_id
        if item_id is not None:
            params["itemId"] = item_id
        if rfq_id is not None:
            params["rfqId"] = rfq_id
        if params:
            kwargs["params"] = params
        return self._make_request("GET", path, **kwargs)
    def post_post(self, data: dict = None) -> dict:
        """POST /api/documents
        
        
        
        Returns:
            dict: API response data
        """
        path = "/"
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def put_update(self, docId: str, data: dict = None) -> dict:
        """PUT /api/documents/update/{docId}
        
        
        
        Returns:
            dict: API response data
        """
        path = "/update/{docId}"
        path = path.replace("{docId}", docId)
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("PUT", path, **kwargs)
    def put_hide(self, docId: str) -> dict:
        """PUT /api/documents/hide/{docId}



        Returns:
            dict: API response data
        """
        path = "/hide/{docId}"
        path = path.replace("{docId}", docId)
        kwargs = {}
        return self._make_request("PUT", path, **kwargs)

    def upload_item_photo(self,
                         file_path: Union[str, Path, BinaryIO],
                         item_id: str,
                         job_display_id: Optional[str] = None,
                         filename: Optional[str] = None,
                         shared: bool = True) -> dict:
        """Upload an item photo using the documents endpoint.

        Convenience method that uploads a file as an item photo using the Pydantic
        DocumentUploadModel for type safety and validation.

        Args:
            file_path: Path to the image file or file-like object
            item_id: Item ID to associate the photo with
            job_display_id: Optional job display ID
            filename: Optional custom filename (inferred from path if not provided)
            shared: Whether the photo should be shared (default: True)

        Returns:
            dict: API response from the upload

        Example:
            >>> # Upload a photo for item
            >>> response = client.docs.upload_item_photo(
            ...     file_path="/path/to/photo.jpg",
            ...     item_id="12345",
            ...     job_display_id="JOB-001"
            ... )
        """
        # Create upload model with item photo settings
        # Convert job_display_id to int if it's a string like "JOB-2000000"
        if isinstance(job_display_id, str) and job_display_id.startswith("JOB-"):
            job_display_id_int = int(job_display_id.replace("JOB-", ""))
        elif isinstance(job_display_id, str) and job_display_id.isdigit():
            job_display_id_int = int(job_display_id)
        else:
            job_display_id_int = job_display_id

        upload_data = ItemPhotoUploadRequest(
            job_display_id=job_display_id_int,
            document_type=6,  # 6 for Item_Photo according to existing model
            document_type_description="Item Photo",
            shared=28 if shared else 0,  # Use default shared value from model
            job_items=[str(item_id)]  # Keep as string UUID
        )

        # Handle file input
        if isinstance(file_path, (str, Path)):
            file_path = Path(file_path)
            if not filename:
                filename = file_path.name
            with open(file_path, 'rb') as f:
                file_content = f.read()
        else:
            # Assume it's a file-like object
            file_content = file_path.read()
            if not filename:
                filename = getattr(file_path, 'name', 'item_photo.jpg')

        # Prepare multipart form data
        files = {'file': (filename, file_content, 'image/jpeg')}

        # Convert model to form data using aliases
        form_data = upload_data.model_dump(by_alias=True, exclude_none=True)

        # Make the request with files and form data using upload_file
        # Note: upload_file expects "api/documents/" format which results in correct
        # URL: https://portal.abconnect.co/api/api/documents/ (double api is intentional)
        path = f"api/{self.api_path}/"
        return self._r.upload_file(
            path=path,
            files=files,
            data=form_data
        )

    def upload_item_photos(self, jobid: int, itemid: int, files: dict) -> dict:
        """Upload item photos (backward compatibility method).

        Maintains compatibility with existing code that expects this method signature.

        Args:
            jobid: Job ID number
            itemid: Item ID number
            files: Dictionary of files in format {'img1': (filename, content, content_type)}

        Returns:
            dict: API response from upload

        Example:
            >>> files = {'img1': ('photo.jpg', file_content, 'image/jpeg')}
            >>> response = client.docs.upload_item_photos(jobid=2000000, itemid=1, files=files)
        """
        # Convert to our expected format - jobid is already an int
        job_display_id_int = jobid
        item_id = str(itemid)  # Keep as string UUID

        # Handle the files dict format expected by existing code
        responses = []
        for field_name, file_tuple in files.items():
            filename, content, content_type = file_tuple

            # Create upload model
            upload_data = ItemPhotoUploadRequest(
                job_display_id=job_display_id_int,
                document_type=6,  # 6 for Item_Photo
                document_type_description="Item Photo",
                shared=28,  # Default shared value
                job_items=[item_id]
            )

            # Prepare request
            files_data = {field_name: (filename, content, content_type)}
            form_data = upload_data.model_dump(by_alias=True, exclude_none=True)

            # Note: upload_file expects "api/documents/" format for correct URL construction
            path = f"api/{self.api_path}/"
            response = self._r.upload_file(
                path=path,
                files=files_data,
                data=form_data
            )
            responses.append(response)

        return responses[0] if len(responses) == 1 else responses
