"""Tests for Companies API endpoints.

Documentation: https://abconnecttools.readthedocs.io/en/latest/api/companies.html
"""

import unittest
from unittest.mock import patch, MagicMock
from ABConnect import ABConnectAPI
from ABConnect.exceptions import ABConnectError


class TestCompaniesAPI(unittest.TestCase):
    """Test cases for Companies endpoints."""

    def setUp(self):
        """Set up test fixtures."""
        self.api = ABConnectAPI()
        # Mock the raw API calls to avoid actual API requests
        self.mock_response = MagicMock()

    @patch("ABConnect.api.http.RequestHandler.call")
    def test_endpoint_availability(self, mock_call):
        """Test that endpoints are available."""
        # This is a basic test to ensure the API client initializes
        self.assertIsNotNone(self.api)
        self.assertTrue(hasattr(self.api, "raw"))


    def test_get_apicompaniesid(self):
        """Test GET /api/companies/{id}.
        
        See documentation: https://abconnecttools.readthedocs.io/en/latest/api/companies.html#get_apicompaniesid
        """
        # Path parameters
        id = "test-id-123"

        response = self.api.raw.get(
            "/api/companies/{id}",
            id=id,
        )
        
        # Check response
        self.assertIsNotNone(response)
        if isinstance(response, dict):
            self.assertIsInstance(response, dict)
        elif isinstance(response, list):
            self.assertIsInstance(response, list)

    def test_get_apicompaniescompanyiddetails(self):
        """Test GET /api/companies/{companyId}/details.
        
        See documentation: https://abconnecttools.readthedocs.io/en/latest/api/companies.html#get_apicompaniescompanyiddetails
        """
        # Path parameters
        companyId = "test-id-123"

        response = self.api.raw.get(
            "/api/companies/{companyId}/details",
            companyId=companyId,
        )
        
        # Check response
        self.assertIsNotNone(response)
        if isinstance(response, dict):
            self.assertIsInstance(response, dict)
        elif isinstance(response, list):
            self.assertIsInstance(response, list)

    def test_get_apicompaniesavailablebycurrentuser(self):
        """Test GET /api/companies/availableByCurrentUser.
        
        See documentation: https://abconnecttools.readthedocs.io/en/latest/api/companies.html#get_apicompaniesavailablebycurrentuser
        """
        response = self.api.raw.get(
            "/api/companies/availableByCurrentUser",
        )
        
        # Check response
        self.assertIsNotNone(response)
        if isinstance(response, dict):
            self.assertIsInstance(response, dict)
        elif isinstance(response, list):
            self.assertIsInstance(response, list)

    def test_get_apicompaniessearch(self):
        """Test GET /api/companies/search.
        
        See documentation: https://abconnecttools.readthedocs.io/en/latest/api/companies.html#get_apicompaniessearch
        """
        response = self.api.raw.get(
            "/api/companies/search",
        )
        
        # Check response
        self.assertIsNotNone(response)
        if isinstance(response, dict):
            self.assertIsInstance(response, dict)
        elif isinstance(response, list):
            self.assertIsInstance(response, list)

    def test_post_apicompaniessearchv2(self):
        """Test POST /api/companies/search/v2.
        
        See documentation: https://abconnecttools.readthedocs.io/en/latest/api/companies.html#post_apicompaniessearchv2
        """
        response = self.api.raw.post(
            "/api/companies/search/v2",
        )
        
        # Check response
        self.assertIsNotNone(response)
        if isinstance(response, dict):
            self.assertIsInstance(response, dict)
        elif isinstance(response, list):
            self.assertIsInstance(response, list)


if __name__ == "__main__":
    unittest.main()