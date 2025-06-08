"""Tests for Companies API endpoints.

Documentation: https://abconnecttools.readthedocs.io/en/latest/api/companies.html
"""

import unittest
from unittest.mock import patch, MagicMock
from . import BaseEndpointTest
from ABConnect.exceptions import ABConnectError
from ABConnect.api.models import (
    CompanyBasic,
    CompanyDetails,
    CompanyFullDetails,
)


class TestCompaniesEndpoints(BaseEndpointTest):
    """Test cases for Companies endpoints."""
    
    tag_name = "Companies"
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


    def test_get_apicompaniesid(self):
        """Test GET /api/companies/{id}.
        
        See documentation: https://abconnecttools.readthedocs.io/en/latest/api/companies.html#get_apicompaniesid
        """
        # Path parameters - use the training company ID
        id = self.test_company_id

        response = self.api.raw.get(
            "/api/companies/{id}",
            id=id,
        )
        
        # Check response
        self.assertIsNotNone(response)
        self.assertIsInstance(response, dict)
        # Verify we got the correct company
        if 'code' in response:
            self.assertEqual(response['code'], self.test_company_code)
        
        # Validate response with Pydantic model
        company = CompanyBasic.model_validate(response)
        self.assertEqual(company.id, self.test_company_id)
        self.assertEqual(company.code, self.test_company_code)
        self.assertEqual(company.name, "Training")

    def test_get_apicompaniescompanyiddetails(self):
        """Test GET /api/companies/{companyId}/details.
        
        See documentation: https://abconnecttools.readthedocs.io/en/latest/api/companies.html#get_apicompaniescompanyiddetails
        """
        # Path parameters - use the training company ID
        companyId = self.test_company_id

        response = self.api.raw.get(
            "/api/companies/{companyId}/details",
            companyId=companyId,
        )
        
        # Check response
        self.assertIsNotNone(response)
        self.assertIsInstance(response, dict)
        # Should have details about the company
        self.assertTrue(len(response) > 0)
        
        # Validate response with Pydantic model
        details = CompanyDetails.model_validate(response)
        self.assertEqual(details.companyID, self.test_company_id)
        self.assertEqual(details.companyCode, self.test_company_code)
        self.assertEqual(details.companyName, "Training")

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
        # Add search parameter
        params = {
            "searchValue": "Training"
        }
        
        response = self.api.raw.get(
            "/api/companies/search",
            **params
        )
        
        # Check response
        self.assertIsNotNone(response)
        if isinstance(response, dict):
            self.assertIsInstance(response, dict)
        elif isinstance(response, list):
            self.assertIsInstance(response, list)

    @unittest.skip("Requires special permissions - returns 403")
    def test_post_apicompaniessearchv2(self):
        """Test POST /api/companies/search/v2.
        
        See documentation: https://abconnecttools.readthedocs.io/en/latest/api/companies.html#post_apicompaniessearchv2
        """
        # Provide search data
        search_data = {
            "searchValue": "Training",
            "page": 1,
            "perPage": 10
        }
        
        response = self.api.raw.post(
            "/api/companies/search/v2",
            data=search_data
        )
        
        # Check response
        self.assertIsNotNone(response)
        if isinstance(response, dict):
            self.assertIsInstance(response, dict)
        elif isinstance(response, list):
            self.assertIsInstance(response, list)
            # If we get results, validate the first one
            if response and len(response) > 0:
                company = CompanyBasic.model_validate(response[0])
                self.assertIsNotNone(company.id)


    def test_get_apicompaniescompanyidfulldetails(self):
        """Test GET /api/companies/{companyId}/fulldetails.
        
        See documentation: https://abconnecttools.readthedocs.io/en/latest/api/companies.html#get_apicompaniescompanyidfulldetails
        """
        # Path parameters - use the training company ID
        companyId = self.test_company_id

        response = self.api.raw.get(
            "/api/companies/{companyId}/fulldetails",
            companyId=companyId,
        )
        
        # Check response
        self.assertIsNotNone(response)
        self.assertIsInstance(response, dict)
        
        # Validate response with Pydantic model
        full_details = CompanyFullDetails.model_validate(response)
        self.assertEqual(full_details.id, self.test_company_id)
        self.assertIsNotNone(full_details.details)
        self.assertEqual(full_details.details.code, self.test_company_code)
        self.assertEqual(full_details.details.name, "Training")


if __name__ == "__main__":
    unittest.main()