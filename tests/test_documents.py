"""Tests for Documents API endpoints and models."""

import pytest
import unittest
import tempfile
import os
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock, mock_open

from ABConnect.api.client import ABConnectAPI
from ABConnect.api.endpoints.documents import DocumentsEndpoint
from ABConnect.api.models.documents import DocumentUpdateModel
from ABConnect.api.models.document_upload import ItemPhotoUploadRequest


class TestDocumentModels:
    """Test the Documents Pydantic models."""

    def test_item_photo_upload_request_creation(self):
        """Test creating an ItemPhotoUploadRequest with all fields."""
        model = ItemPhotoUploadRequest(
            job_display_id="JOB-12345",
            document_type=6,
            document_type_description="Item Photo",
            shared=28,
            job_items=[123, 456],
            rfq_id=987
        )

        assert model.job_display_id == "JOB-12345"
        assert model.rfq_id == 987
        assert model.document_type == 6
        assert model.document_type_description == "Item Photo"
        assert model.shared == 28
        assert model.job_items == [123, 456]

    def test_item_photo_upload_request_aliases(self):
        """Test that aliases work correctly in serialization."""
        model = ItemPhotoUploadRequest(
            job_display_id="JOB-123",
            document_type=6,
            document_type_description="Item Photo",
            shared=28,
            job_items=[123]
        )

        serialized = model.model_dump(by_alias=True, exclude_none=True)
        expected = {
            "JobDisplayId": "JOB-123",
            "DocumentType": 6,
            "DocumentTypeDescription": "Item Photo",
            "Shared": 28,
            "JobItems": [123]
        }
        assert serialized == expected

    def test_document_update_model_creation(self):
        """Test creating a DocumentUpdateModel."""
        model = DocumentUpdateModel(
            file_name="updated_file.pdf",
            type_id=3,
            shared=1,
            tags=["updated", "final"],
            job_items=["item-123"]
        )

        assert model.file_name == "updated_file.pdf"
        assert model.type_id == 3
        assert model.shared == 1
        assert model.tags == ["updated", "final"]
        assert model.job_items == ["item-123"]


class TestDocumentsEndpoint:
    """Test the DocumentsEndpoint class."""

    def setup_method(self):
        """Set up test fixtures."""
        self.api = ABConnectAPI()
        self.docs_endpoint = self.api.documents

    @patch('ABConnect.api.endpoints.documents.DocumentsEndpoint._make_request')
    def test_get_list(self, mock_request):
        """Test the get_list method."""
        mock_request.return_value = {"data": []}

        result = self.docs_endpoint.get_list(job_display_id="JOB-123")

        mock_request.assert_called_once_with("GET", "/list", params={"jobDisplayId": "JOB-123"})
        assert result == {"data": []}

    @patch('ABConnect.api.endpoints.documents.DocumentsEndpoint._make_request')
    def test_get_list_with_item_id(self, mock_request):
        """Test get_list with item_id parameter."""
        mock_request.return_value = {"data": []}

        result = self.docs_endpoint.get_list(item_id="item-456")

        mock_request.assert_called_once_with("GET", "/list", params={"itemId": "item-456"})

    @patch.object(DocumentsEndpoint, '_r')
    @patch('builtins.open', new_callable=mock_open, read_data=b"fake_image_data")
    def test_upload_item_photo_with_file_path(self, mock_file, mock_request_handler):
        """Test upload_item_photo with file path."""
        mock_request_handler.upload_file.return_value = {"success": True, "doc_id": 123}

        # Create a temporary file path
        with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as tmp_file:
            tmp_file_path = tmp_file.name

        try:
            result = self.docs_endpoint.upload_item_photo(
                file_path=tmp_file_path,
                item_id="item-789",
                job_display_id="JOB-456",
                shared=True
            )

            # Verify the upload_file was called correctly
            mock_request_handler.upload_file.assert_called_once()
            call_args = mock_request_handler.upload_file.call_args
            assert call_args[1]['path'] == "/api/documents/"
            assert 'files' in call_args[1]
            assert 'data' in call_args[1]

            # Check the form data
            form_data = call_args[1]['data']
            assert form_data['JobDisplayId'] == "JOB-456"
            assert form_data['DocumentType'] == 6
            assert form_data['DocumentTypeDescription'] == "Item Photo"
            assert form_data['Shared'] == 28
            assert form_data['JobItems'] == [789]  # Should be converted to int

        finally:
            if os.path.exists(tmp_file_path):
                os.unlink(tmp_file_path)

    @patch.object(DocumentsEndpoint, '_r')
    def test_upload_item_photo_with_file_object(self, mock_request_handler):
        """Test upload_item_photo with file-like object."""
        mock_request_handler.upload_file.return_value = {"success": True, "doc_id": 456}

        # Create a mock file object
        mock_file = MagicMock()
        mock_file.read.return_value = b"fake_image_data"
        mock_file.name = "test_photo.jpg"

        result = self.docs_endpoint.upload_item_photo(
            file_path=mock_file,
            item_id="item-999",
            shared=False
        )

        # Verify the upload_file was called
        mock_request_handler.upload_file.assert_called_once()
        call_args = mock_request_handler.upload_file.call_args

        # Check form data
        form_data = call_args[1]['data']
        assert form_data['Shared'] == 0
        assert form_data['JobItems'] == [999]  # Should be converted to int

    @patch.object(DocumentsEndpoint, '_r')
    def test_upload_item_photos_backward_compatibility(self, mock_request_handler):
        """Test upload_item_photos backward compatibility method."""
        mock_request_handler.upload_file.return_value = {"success": True, "doc_id": 789}

        files = {
            'img1': ('photo1.jpg', b'fake_image_data_1', 'image/jpeg'),
            'img2': ('photo2.jpg', b'fake_image_data_2', 'image/jpeg')
        }

        result = self.docs_endpoint.upload_item_photos(
            jobid=2000000,
            itemid=1,
            files=files
        )

        # Should be called twice (once for each file)
        assert mock_request_handler.upload_file.call_count == 2

        # Check the first call
        first_call = mock_request_handler.upload_file.call_args_list[0]
        assert first_call[1]['path'] == "/api/documents/"
        form_data = first_call[1]['data']
        assert form_data['JobDisplayId'] == "JOB-2000000"
        assert form_data['JobItems'] == [1]

    def test_docs_alias_exists(self):
        """Test that the docs alias exists and points to documents."""
        api = ABConnectAPI()
        assert hasattr(api, 'docs')
        assert api.docs is api.documents
        assert isinstance(api.docs, DocumentsEndpoint)

    @patch('ABConnect.api.endpoints.documents.DocumentsEndpoint._make_request')
    def test_put_update(self, mock_request):
        """Test the put_update method."""
        mock_request.return_value = {"success": True}

        update_data = DocumentUpdateModel(
            file_name="new_name.pdf",
            shared=1
        )

        result = self.docs_endpoint.put_update(
            "123",
            update_data.model_dump(by_alias=True)
        )

        mock_request.assert_called_once_with(
            "PUT",
            "/update/123",
            json={'fileName': 'new_name.pdf', 'shared': 1}
        )

    @patch('ABConnect.api.endpoints.documents.DocumentsEndpoint._make_request')
    def test_put_hide(self, mock_request):
        """Test the put_hide method."""
        mock_request.return_value = {"success": True}

        result = self.docs_endpoint.put_hide("456")

        mock_request.assert_called_once_with("PUT", "/hide/456")

    @patch('ABConnect.api.endpoints.documents.DocumentsEndpoint._make_request')
    def test_get_get_with_pdf_returns_bytes(self, mock_request):
        """Test that get_get returns bytes for PDF documents."""
        # Simulate binary PDF content
        pdf_bytes = b'%PDF-1.4\n%\xe2\xe3\xcf\xd3\n'
        mock_request.return_value = pdf_bytes

        result = self.docs_endpoint.get_get("path/to/document.pdf")

        mock_request.assert_called_once_with("GET", "/get/path/to/document.pdf")
        assert isinstance(result, bytes)
        assert result == pdf_bytes

    @patch('ABConnect.api.endpoints.documents.DocumentsEndpoint._make_request')
    def test_get_get_with_json_returns_dict(self, mock_request):
        """Test that get_get can still return JSON when applicable."""
        json_response = {"success": True, "message": "Document retrieved"}
        mock_request.return_value = json_response

        result = self.docs_endpoint.get_get("path/to/metadata")

        mock_request.assert_called_once_with("GET", "/get/path/to/metadata")
        assert isinstance(result, dict)
        assert result == json_response

    @patch('ABConnect.api.endpoints.documents.DocumentsEndpoint._make_request')
    def test_get_get_thumbnail_returns_bytes(self, mock_request):
        """Test that get_get_thumbnail returns bytes for image thumbnails."""
        # Simulate image bytes
        image_bytes = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR'
        mock_request.return_value = image_bytes

        result = self.docs_endpoint.get_get_thumbnail("path/to/image.jpg")

        mock_request.assert_called_once_with("GET", "/get/thumbnail/path/to/image.jpg")
        assert isinstance(result, bytes)
        assert result == image_bytes


class TestDocumentsIntegration:
    """Integration tests for the Documents API."""

    def setup_method(self):
        """Set up test fixtures."""
        self.api = ABConnectAPI()

    def test_documents_endpoint_available(self):
        """Test that documents endpoint is available on API client."""
        assert hasattr(self.api, 'documents')
        assert isinstance(self.api.documents, DocumentsEndpoint)

    def test_docs_alias_available(self):
        """Test that docs alias is available on API client."""
        assert hasattr(self.api, 'docs')
        assert self.api.docs is self.api.documents

    def test_endpoint_methods_exist(self):
        """Test that all expected methods exist on the endpoint."""
        docs = self.api.docs

        # Auto-generated methods
        assert hasattr(docs, 'get_list')
        assert hasattr(docs, 'get_get')
        assert hasattr(docs, 'get_get_thumbnail')
        assert hasattr(docs, 'post_post')
        assert hasattr(docs, 'put_update')
        assert hasattr(docs, 'put_hide')

        # Custom convenience methods
        assert hasattr(docs, 'upload_item_photo')
        assert hasattr(docs, 'upload_item_photos')

    def test_model_imports_available(self):
        """Test that model classes can be imported."""
        from ABConnect.api.models.documents import DocumentUpdateModel
        from ABConnect.api.models.document_upload import ItemPhotoUploadRequest

        # Test that we can instantiate the models
        update_model = DocumentUpdateModel()
        upload_model = ItemPhotoUploadRequest(
            job_display_id="TEST",
            document_type=6,
            document_type_description="Test",
            job_items=[1]
        )

        assert upload_model is not None
        assert update_model is not None


if __name__ == "__main__":
    pytest.main([__file__])