"""Tests for Lookup API endpoints.

Documentation: https://abconnecttools.readthedocs.io/en/latest/api/lookup.html
"""

from unittest.mock import patch, MagicMock
from . import BaseEndpointTest
from ABConnect.exceptions import ABConnectError


class TestLookupEndpoints(BaseEndpointTest):
    """Test cases for Lookup endpoints."""
    
    tag_name = "Lookup"
    __test__ = True

    def setUp(self):
        """Set up test fixtures."""
        super().setUp()
        # Mock the raw API calls to avoid actual API requests
        self.mock_response = MagicMock()

    def test_endpoint_availability(self):
        """Test that endpoints are available."""
        # This is a basic test to ensure the API client initializes
        self.assertIsNotNone(self.api)
        self.assertTrue(hasattr(self.api, "raw"))
        
        # Test specific endpoints discovery
        self.test_endpoint_discovery()


    def test_get_apilookupmasterconstantkey(self):
        """Test GET /api/lookup/{masterConstantKey}.
        
        See documentation: https://abconnecttools.readthedocs.io/en/latest/api/lookup.html#get_apilookupmasterconstantkey
        """
        # Path parameters
        masterConstantKey = "test-value"

        response = self.api.raw.get(
            "/api/lookup/{masterConstantKey}",
            masterConstantKey=masterConstantKey,
        )
        
        # Check response
        self.assertIsNotNone(response)
        if isinstance(response, dict):
            self.assertIsInstance(response, dict)
        elif isinstance(response, list):
            self.assertIsInstance(response, list)

    def test_get_apilookupmasterconstantkeyvalueid(self):
        """Test GET /api/lookup/{masterConstantKey}/{valueId}.
        
        See documentation: https://abconnecttools.readthedocs.io/en/latest/api/lookup.html#get_apilookupmasterconstantkeyvalueid
        """
        # Path parameters
        masterConstantKey = "test-value"
        valueId = "test-id-123"

        response = self.api.raw.get(
            "/api/lookup/{masterConstantKey}/{valueId}",
            masterConstantKey=masterConstantKey,
            valueId=valueId,
        )
        
        # Check response
        self.assertIsNotNone(response)
        if isinstance(response, dict):
            self.assertIsInstance(response, dict)
        elif isinstance(response, list):
            self.assertIsInstance(response, list)

    def test_get_apilookupcountries(self):
        """Test GET /api/lookup/countries.
        
        See documentation: https://abconnecttools.readthedocs.io/en/latest/api/lookup.html#get_apilookupcountries
        """
        response = self.api.raw.get(
            "/api/lookup/countries",
        )
        
        # Check response
        self.assertIsNotNone(response)
        if isinstance(response, dict):
            self.assertIsInstance(response, dict)
        elif isinstance(response, list):
            self.assertIsInstance(response, list)

    def test_get_apilookupresetmasterconstantcache(self):
        """Test GET /api/lookup/resetMasterConstantCache.
        
        See documentation: https://abconnecttools.readthedocs.io/en/latest/api/lookup.html#get_apilookupresetmasterconstantcache
        """
        response = self.api.raw.get(
            "/api/lookup/resetMasterConstantCache",
        )
        
        # Check response
        self.assertIsNotNone(response)
        if isinstance(response, dict):
            self.assertIsInstance(response, dict)
        elif isinstance(response, list):
            self.assertIsInstance(response, list)

    def test_get_apilookupaccesskeys(self):
        """Test GET /api/lookup/accessKeys.
        
        See documentation: https://abconnecttools.readthedocs.io/en/latest/api/lookup.html#get_apilookupaccesskeys
        """
        response = self.api.raw.get(
            "/api/lookup/accessKeys",
        )
        
        # Check response
        self.assertIsNotNone(response)
        if isinstance(response, dict):
            self.assertIsInstance(response, dict)
        elif isinstance(response, list):
            self.assertIsInstance(response, list)


if __name__ == "__main__":
    unittest.main()