"""Tests for HTTP client request handler and response handling."""

import pytest
from unittest.mock import Mock, MagicMock
import requests

from ABConnect.api.http_client import RequestHandler
from ABConnect.exceptions import RequestError, NotLoggedInError


class TestRequestHandlerBinaryContent:
    """Test the RequestHandler binary content handling."""

    def setup_method(self):
        """Set up test fixtures."""
        # Create a mock token storage
        self.mock_token_storage = Mock()
        self.mock_token_storage.get_token.return_value = {
            "access_token": "test_token_12345"
        }
        self.handler = RequestHandler(self.mock_token_storage)

    def test_handle_response_pdf_content(self):
        """Test that PDF content is returned as bytes."""
        # Create a mock response with PDF content
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.headers = {'Content-Type': 'application/pdf'}
        mock_response.content = b'%PDF-1.4 fake pdf content'

        result = self.handler._handle_response(mock_response, raw=False)

        assert isinstance(result, bytes)
        assert result == b'%PDF-1.4 fake pdf content'

    def test_handle_response_image_content(self):
        """Test that image content is returned as bytes."""
        # Test various image types
        image_types = [
            'image/jpeg',
            'image/png',
            'image/gif',
            'image/webp'
        ]

        for content_type in image_types:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.headers = {'Content-Type': content_type}
            mock_response.content = b'\x89PNG\r\n\x1a\n fake image data'

            result = self.handler._handle_response(mock_response, raw=False)

            assert isinstance(result, bytes), f"Failed for {content_type}"
            assert result == b'\x89PNG\r\n\x1a\n fake image data'

    def test_handle_response_zip_content(self):
        """Test that ZIP archive content is returned as bytes."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.headers = {'Content-Type': 'application/zip'}
        mock_response.content = b'PK\x03\x04 fake zip content'

        result = self.handler._handle_response(mock_response, raw=False)

        assert isinstance(result, bytes)
        assert result == b'PK\x03\x04 fake zip content'

    def test_handle_response_octet_stream(self):
        """Test that octet-stream content is returned as bytes."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.headers = {'Content-Type': 'application/octet-stream'}
        mock_response.content = b'arbitrary binary data'

        result = self.handler._handle_response(mock_response, raw=False)

        assert isinstance(result, bytes)
        assert result == b'arbitrary binary data'

    def test_handle_response_json_content(self):
        """Test that JSON content is still parsed correctly."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.headers = {'Content-Type': 'application/json'}
        mock_response.json.return_value = {"status": "success", "data": [1, 2, 3]}

        result = self.handler._handle_response(mock_response, raw=False)

        assert isinstance(result, dict)
        assert result == {"status": "success", "data": [1, 2, 3]}

    def test_handle_response_json_without_content_type(self):
        """Test that responses without Content-Type still try JSON parsing."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.headers = {}
        mock_response.json.return_value = {"status": "success"}

        result = self.handler._handle_response(mock_response, raw=False)

        assert isinstance(result, dict)
        assert result == {"status": "success"}

    def test_handle_response_invalid_json_raises_error(self):
        """Test that invalid JSON still raises RequestError."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.headers = {'Content-Type': 'application/json'}
        mock_response.json.side_effect = requests.exceptions.JSONDecodeError("error", "doc", 0)
        mock_response.text = "invalid json content"

        with pytest.raises(RequestError) as exc_info:
            self.handler._handle_response(mock_response, raw=False)

        assert exc_info.value.status_code == 200
        assert "not valid JSON" in str(exc_info.value)

    def test_handle_response_raw_returns_response_object(self):
        """Test that raw=True returns the response object unchanged."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.headers = {'Content-Type': 'application/pdf'}
        mock_response.content = b'pdf content'

        result = self.handler._handle_response(mock_response, raw=True)

        assert result is mock_response

    def test_handle_response_204_returns_none(self):
        """Test that 204 status code returns None."""
        mock_response = Mock()
        mock_response.status_code = 204
        mock_response.headers = {'Content-Type': 'application/json'}

        result = self.handler._handle_response(mock_response, raw=False)

        assert result is None

    def test_handle_response_pdf_with_charset(self):
        """Test that Content-Type with charset parameter is handled correctly."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.headers = {'Content-Type': 'application/pdf; charset=utf-8'}
        mock_response.content = b'%PDF-1.4 content'

        result = self.handler._handle_response(mock_response, raw=False)

        assert isinstance(result, bytes)
        assert result == b'%PDF-1.4 content'

    def test_handle_response_error_status(self):
        """Test that error status codes raise RequestError."""
        mock_response = Mock()
        mock_response.status_code = 404
        mock_response.headers = {'Content-Type': 'application/json'}
        mock_response.json.return_value = {"message": "Not found"}
        mock_response.text = '{"message": "Not found"}'

        with pytest.raises(RequestError) as exc_info:
            self.handler._handle_response(mock_response, raw=False, raise_for_status=True)

        assert exc_info.value.status_code == 404


class TestRequestHandlerAuth:
    """Test the RequestHandler authentication."""

    def test_get_auth_headers_with_token(self):
        """Test that auth headers are created when token exists."""
        mock_token_storage = Mock()
        mock_token_storage.get_token.return_value = {
            "access_token": "test_token_abc123"
        }
        handler = RequestHandler(mock_token_storage)

        headers = handler._get_auth_headers()

        assert headers == {"Authorization": "Bearer test_token_abc123"}

    def test_get_auth_headers_without_token(self):
        """Test that NotLoggedInError is raised when no token exists."""
        mock_token_storage = Mock()
        mock_token_storage.get_token.return_value = None
        handler = RequestHandler(mock_token_storage)

        with pytest.raises(NotLoggedInError) as exc_info:
            handler._get_auth_headers()

        assert "No access token found" in str(exc_info.value)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
