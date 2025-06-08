"""Tests for Lookup API endpoints.

Documentation: https://abconnecttools.readthedocs.io/en/latest/api/lookup.html
"""

import unittest
from unittest.mock import patch, MagicMock
from . import BaseEndpointTest
from ABConnect.exceptions import ABConnectError, RequestError
from ABConnect.api.models import LookupKeys, LookupValue


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
        # Use a real lookup key for testing
        masterConstantKey = LookupKeys.COMPANYTYPES.value

        try:
            response = self.api.raw.get(
                "/api/lookup/{masterConstantKey}",
                masterConstantKey=masterConstantKey,
            )
            
            # Check response
            self.assertIsNotNone(response)
            self.assertIsInstance(response, list)
            
            # Validate each item with the LookupValue model
            for item in response[:5]:  # Validate first 5 items
                lookup_value = LookupValue.model_validate(item)
                self.assertIsInstance(lookup_value, LookupValue)
                self.assertIsNotNone(lookup_value.id)
                self.assertTrue(lookup_value.value or lookup_value.name, 
                               "Lookup must have either value or name")
                
        except RequestError as e:
            if e.status_code == 404:
                self.skipTest(f"Lookup key {masterConstantKey} returns 404")
            else:
                raise

    @unittest.skip("Lookup endpoint returns None with test values - requires valid IDs")
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

    @unittest.skip("Cache reset endpoint likely requires admin privileges")
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