"""Documents API endpoints.

Auto-generated from swagger.json specification.
Provides type-safe access to documents/* endpoints.
"""

import mimetypes
from typing import Optional, Union, BinaryIO, List
from pathlib import Path

from ABConnect.api.endpoints.base import BaseEndpoint
from ABConnect.api import models
from ABConnect.api.routes import SCHEMA


class DocumentsEndpoint(BaseEndpoint):
    """Documents API endpoint operations.

    Handles all API operations for /api/documents/* endpoints.
    Total endpoints: 6
    """

    api_path = "documents"
    routes = SCHEMA["DOCUMENTS"]

    def thumbnail(self, docPath: str) -> Union[dict, bytes]:
        """GET /api/documents/get/thumbnail/{docPath}

        Get a thumbnail of a document. Returns binary image data for image thumbnails,
        or JSON response data for other cases.

        Args:
            docPath: Path to the document

        Returns:
            Union[dict, bytes]: Binary image data for thumbnails, or JSON response data
        """
        route = SCHEMA["DOCUMENTS"]["THUMBNAIL"]
        route.params = {"docPath": docPath}
        kwargs = {}
        return self._make_request(route, **kwargs)

    def get(self, docPath: str) -> Union[dict, bytes]:
        """GET /api/documents/get/{docPath}

        Download a document. Returns binary data for files like PDFs, images, etc.,
        or JSON response data for other cases.

        Args:
            docPath: Path to the document

        Returns:
            Binary document data (e.g., PDF bytes, image bytes),

        Example:
            >>> # Download a PDF document
            >>> pdf_bytes = client.docs.get("path/to/document.pdf")
            >>> with open("downloaded.pdf", "wb") as f:
            ...     f.write(pdf_bytes)
        """
        route = SCHEMA["DOCUMENTS"]["GET"]
        route.params = {"docPath": docPath}
        kwargs = {}
        return self._make_request(route, **kwargs)

    def list(
        self,
        job_display_id: Optional[str] = None,
        item_id: Optional[str] = None,
        rfq_id: Optional[str] = None,
    ) -> dict:
        """GET /api/documents/list



        Returns:
            dict: API response data
        """
        route = SCHEMA["DOCUMENTS"]["LIST"]
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
        return self._make_request(route, **kwargs)

    def post(self, data: dict = None) -> dict:
        """POST /api/documents



        Returns:
            dict: API response data
        """
        route = SCHEMA["DOCUMENTS"]["POST"]
        
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)
    def update(self, docId: str, data: dict = None) -> dict:
        """PUT /api/documents/update/{docId}

        Returns:
            dict: API response data
        """
        route = self.routes["UPDATE"]
        route.params = {"docId": docId}
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def put_hide(self, docId: str) -> dict:
        """PUT /api/documents/hide/{docId}

        Returns:
            dict: API response data
        """
        route = self.routes["HIDE"]
        route.params = {"docId": docId}
        return self._make_request(route)

    def upload_item_photo(
        self,
        job_display_id: str,
        file_path: Union[str, Path, BinaryIO],
        item_id: str,
        filename: Optional[str] = None,
        shared: bool = True,
    ) -> dict:
        """Upload an item photo using the documents endpoint.

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
            ...     item_id="00000000-0000-0000-0000-000000000001",
            ...     job_display_id="2000000"
            ... )
        """
        # Create upload model with item photo settings

        upload_data = models.ItemPhotoUploadRequest(
            job_display_id=job_display_id,
            document_type=6,
            document_type_description="Item Photo",
            shared=28 if shared else 0,
            job_items=[str(item_id)],
        )

        if isinstance(file_path, (str, Path)):
            file_path = Path(file_path)
            if not filename:
                filename = file_path.name
            with open(file_path, "rb") as f:
                file_content = f.read()
        else:
            file_content = file_path.read()
            if not filename:
                filename = getattr(file_path, "name", "item_photo.jpg")

        # Prepare multipart form data
        files = {"file": (filename, file_content, "image/jpeg")}

        # Convert model to form data using aliases
        form_data = upload_data.model_dump(by_alias=True, exclude_none=True)

        path = f"/{self.api_path}/"

        return self._r.upload_file(path=path, files=files, data=form_data)

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

        # Handle the files dict format expected by existing code
        responses = []
        for field_name, file_tuple in files.items():
            filename, content, content_type = file_tuple

            # Create upload model
            upload_data = models.ItemPhotoUploadRequest(
                job_display_id=jobid,
                document_type=6,  # 6 for Item_Photo
                document_type_description="Item Photo",
                shared=28,  # Default shared value
                job_items=[str(itemid)],
            )

            # Prepare request
            files_data = {field_name: (filename, content, content_type)}
            form_data = upload_data.model_dump(by_alias=True, exclude_none=True)

            response = self._r.upload_file(path=f"/{self.api_path}/", files=files_data, data=form_data)
            responses.append(response)

        return responses[0] if len(responses) == 1 else responses

    @staticmethod
    def _resolve_document_type(
        document_type: Union[str, int, models.DocumentType],
    ) -> models.DocumentType:
        """Resolve document_type to a DocumentType enum.

        Args:
            document_type: Can be:
                - DocumentType enum value
                - int (enum value)
                - str like "commercial invoice", "COMMERCIAL_INVOICE", "Commercial Invoice"

        Returns:
            DocumentType enum value

        Raises:
            ValueError: If string doesn't match any DocumentType name
        """
        if isinstance(document_type, models.DocumentType):
            return document_type.value
        if isinstance(document_type, int):
            return models.DocumentType(document_type).value
        if isinstance(document_type, str):
            # Convert "commercial invoice" -> "COMMERCIAL_INVOICE"
            normalized = (
                document_type.strip().upper().replace(" ", "_").replace("-", "_")
            )
            try:
                return models.DocumentType[normalized].value
            except KeyError:
                valid_names = [dt.name for dt in models.DocumentType]
                raise ValueError(
                    f"Unknown document type: '{document_type}'. "
                    f"Valid types: {', '.join(valid_names)}"
                )
        raise TypeError(
            f"document_type must be str, int, or DocumentType, got {type(document_type)}"
        )

    def upload_doc(
        self,
        job_display_id: int,
        filename: str,
        data: BinaryIO,
        document_type: Union[str, int, models.DocumentType],
        shared: int = 28,
        rfq_id: Optional[int] = None,
        content_type: Optional[str] = None,
    ) -> models.DocumentUploadResponse:
        """Upload a document of any type using the DocumentType enum.

        This convenience function validates the request using Pydantic models
        and returns a validated response model.

        Args:
            file_path: Path to the file or file-like object
            job_display_id: Job display ID (integer, e.g., 2000000)
            document_type: Document type - accepts:
                - DocumentType enum (e.g., DocumentType.BOL)
                - int (e.g., 4 for BOL)
                - str (e.g., "commercial invoice", "COMMERCIAL_INVOICE", "Commercial-Invoice")
            item_ids: Optional list of item UUIDs to associate with the document
            filename: Optional custom filename (inferred from path if not provided)
            shared: Sharing level (0=private, 28=shared). Defaults to 28.
            rfq_id: Optional RFQ ID if applicable
            content_type: Optional MIME type (auto-detected if not provided)

        Returns:
            DocumentUploadResponse: Validated response model

        Example:
            >>> from ABConnect import models
            >>> # Upload using enum
            >>> response = client.docs.upload_doc(
            ...     file_path="/path/to/bol.pdf",
            ...     job_display_id=2000000,
            ...     document_type=models.DocumentType.BOL,
            ... )

            >>> # Upload using string (flexible formats)
            >>> response = client.docs.upload_doc(
            ...     file_path="/path/to/invoice.pdf",
            ...     job_display_id=2000000,
            ...     document_type="commercial invoice",
            ... )

            >>> # Upload using int
            >>> response = client.docs.upload_doc(
            ...     file_path="/path/to/list.pdf",
            ...     job_display_id=2000000,
            ...     document_type=11,  # PACKING_LIST
            ... )
        """
        # Resolve document_type to enum
        resolved_type = self._resolve_document_type(document_type)

        # Build and validate request model
        request_data = {
            "job_display_id": job_display_id,
            "document_type": resolved_type,
            "shared": shared,
        }
        # if item_ids:
        #     request_data["job_items"] = item_ids
        if rfq_id is not None:
            request_data["rfq_id"] = rfq_id

        upload_request = models.DocumentUploadRequest.model_validate(request_data)
        files = {"file": (filename, data, content_type)}
        form_data = upload_request.model_dump(by_alias=True, exclude_none=True)

        # Make the upload request
        path = f"/{self.api_path}/"
        raw_response = self._r.upload_file(path=path, files=files, data=form_data)

        # Validate response with Pydantic model
        return models.DocumentUploadResponse.model_validate(raw_response)
