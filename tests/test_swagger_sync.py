"""Tests for swagger synchronization functionality."""

import pytest
import json
from pathlib import Path
from unittest.mock import patch, mock_open

from ABConnect.common import sync_swagger
from ABConnect.config import Config


class TestSwaggerSync:
    """Test swagger synchronization functionality."""
    
    def test_sync_swagger_updates_when_different(self):
        """Test that sync_swagger updates local file when remote differs."""
        remote_data = {"openapi": "3.0.1", "info": {"title": "Test", "version": "v2"}}
        local_data = {"openapi": "3.0.1", "info": {"title": "Test", "version": "v1"}}
        
        with patch('requests.get') as mock_get, \
             patch('builtins.open', mock_open()) as mock_file, \
             patch('pathlib.Path.exists', return_value=True):
            
            # Mock remote response
            mock_response = mock_get.return_value
            mock_response.raise_for_status.return_value = None
            mock_response.json.return_value = remote_data
            
            # Mock local file read
            mock_file.return_value.read.return_value = json.dumps(local_data)
            
            # Mock json.load to return local data on read
            with patch('json.load', return_value=local_data):
                result = sync_swagger()
            
            assert result is True
            mock_get.assert_called_once()
    
    def test_sync_swagger_no_update_when_same(self):
        """Test that sync_swagger doesn't update when versions are same."""
        same_data = {"openapi": "3.0.1", "info": {"title": "Test", "version": "v1"}}
        
        with patch('requests.get') as mock_get, \
             patch('pathlib.Path.exists', return_value=True), \
             patch('json.load', return_value=same_data):
            
            # Mock remote response
            mock_response = mock_get.return_value
            mock_response.raise_for_status.return_value = None
            mock_response.json.return_value = same_data
            
            result = sync_swagger()
            
            assert result is False
    
    def test_sync_swagger_creates_when_missing(self):
        """Test that sync_swagger creates file when local doesn't exist."""
        remote_data = {"openapi": "3.0.1", "info": {"title": "Test", "version": "v1"}}
        
        with patch('requests.get') as mock_get, \
             patch('builtins.open', mock_open()) as mock_file, \
             patch('pathlib.Path.exists', return_value=False):
            
            # Mock remote response
            mock_response = mock_get.return_value
            mock_response.raise_for_status.return_value = None
            mock_response.json.return_value = remote_data
            
            result = sync_swagger()
            
            assert result is True
            mock_get.assert_called_once()


def test_swagger_is_current():
    """Integration test to verify local swagger.json is current with server."""
    try:
        # This will return False if already current, True if updated
        was_updated = sync_swagger()
        
        # Either way, the file should now exist and be current
        swagger_path = Path(__file__).parent.parent / "ABConnect" / "base" / "swagger.json"
        assert swagger_path.exists(), "swagger.json should exist after sync"
        
        # Verify it's valid JSON
        with open(swagger_path, 'r') as f:
            swagger_data = json.load(f)
        
        assert "openapi" in swagger_data, "swagger.json should be valid OpenAPI spec"
        assert "paths" in swagger_data, "swagger.json should contain API paths"
        
        print(f"Swagger sync status: {'Updated' if was_updated else 'Already current'}")
        
    except Exception as e:
        pytest.fail(f"Swagger sync failed: {e}")


if __name__ == "__main__":
    # Allow running this test directly to check swagger status
    test_swagger_is_current()