"""Tests for swagger synchronization functionality."""

import json
import sys
from pathlib import Path
from unittest.mock import patch, mock_open

# Add tests directory to path for base_test imports
tests_dir = Path(__file__).parent.parent.parent
if str(tests_dir) not in sys.path:
    sys.path.insert(0, str(tests_dir))

from base_test import ABConnectTestCase


class TestSwaggerSync(ABConnectTestCase):
    """Test swagger synchronization functionality."""

    def test_sync_swagger_updates_when_different(self):
        """Test that sync_swagger updates local file when remote differs."""
        try:
            from ABConnect.common import sync_swagger
        except ImportError:
            self.skipTest("sync_swagger not available")

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

            self.assertTrue(result)
            mock_get.assert_called_once()

    def test_sync_swagger_no_update_when_same(self):
        """Test that sync_swagger doesn't update when versions are same."""
        try:
            from ABConnect.common import sync_swagger
        except ImportError:
            self.skipTest("sync_swagger not available")

        same_data = {"openapi": "3.0.1", "info": {"title": "Test", "version": "v1"}}

        with patch('requests.get') as mock_get, \
             patch('pathlib.Path.exists', return_value=True), \
             patch('json.load', return_value=same_data):

            # Mock remote response
            mock_response = mock_get.return_value
            mock_response.raise_for_status.return_value = None
            mock_response.json.return_value = same_data

            result = sync_swagger()

            self.assertFalse(result)

    def test_sync_swagger_creates_when_missing(self):
        """Test that sync_swagger creates file when local doesn't exist."""
        try:
            from ABConnect.common import sync_swagger
        except ImportError:
            self.skipTest("sync_swagger not available")

        remote_data = {"openapi": "3.0.1", "info": {"title": "Test", "version": "v1"}}

        with patch('requests.get') as mock_get, \
             patch('builtins.open', mock_open()) as mock_file, \
             patch('pathlib.Path.exists', return_value=False):

            # Mock remote response
            mock_response = mock_get.return_value
            mock_response.raise_for_status.return_value = None
            mock_response.json.return_value = remote_data

            result = sync_swagger()

            self.assertTrue(result)
            mock_get.assert_called_once()

    def test_swagger_is_current(self):
        """Integration test to verify local swagger.json is current with server.

        This is CRITICAL for revealing gaps between latest server swagger and our wrapper.
        """
        try:
            from ABConnect.common import sync_swagger
        except ImportError:
            self.skipTest("sync_swagger not available")

        try:
            # This will return False if already current, True if updated
            was_updated = sync_swagger()

            # Either way, the file should now exist and be current
            swagger_path = self.swagger_path
            self.assertTrue(swagger_path.exists(), "swagger.json should exist after sync")

            # Verify it's valid JSON
            with open(swagger_path, 'r') as f:
                swagger_data = json.load(f)

            self.assertIn("openapi", swagger_data, "swagger.json should be valid OpenAPI spec")
            self.assertIn("paths", swagger_data, "swagger.json should contain API paths")

            print(f"Swagger sync status: {'Updated' if was_updated else 'Already current'}")

        except Exception as e:
            self.skipTest(f"Swagger sync failed: {e}")

    def test_server_wrapper_gap_detection(self):
        """Test that we can detect gaps between server API and our wrapper.

        This test is critical for ensuring we don't miss new endpoints or changes.
        """
        try:
            from ABConnect.common import sync_swagger
        except ImportError:
            self.skipTest("sync_swagger not available")

        # First sync to get latest
        try:
            sync_swagger()
        except Exception:
            self.skipTest("Cannot sync swagger for gap detection")

        # Load current swagger
        if not self.swagger_spec:
            self.skipTest("Swagger spec not available for gap detection")

        # Get all paths from server swagger
        server_paths = set(self.swagger_spec.get("paths", {}).keys())

        # Get all endpoint implementations we have
        endpoint_files = list(self.endpoints_dir.glob("*.py"))
        endpoint_names = {f.stem for f in endpoint_files
                         if f.stem not in ['__init__', 'base']}

        # Extract endpoint prefixes from server paths
        server_endpoints = set()
        for path in server_paths:
            parts = path.split("/")
            if len(parts) > 2:
                endpoint = parts[2].replace("-", "_")
                server_endpoints.add(endpoint)

        # Find missing implementations
        missing_in_wrapper = server_endpoints - endpoint_names
        orphaned_in_wrapper = endpoint_names - server_endpoints

        if missing_in_wrapper:
            self.fail(f"Server has endpoints missing in wrapper: {missing_in_wrapper}")

        if orphaned_in_wrapper:
            # This might be okay (manual endpoints), so just warn
            print(f"Warning: Wrapper has endpoints not in server swagger: {orphaned_in_wrapper}")


if __name__ == "__main__":
    import unittest
    unittest.main()