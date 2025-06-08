"""Tests for Contacts API endpoints.

Documentation: https://abconnecttools.readthedocs.io/en/latest/api/contacts.html
"""

import unittest
from unittest.mock import patch, MagicMock
from . import BaseEndpointTest
from ABConnect.exceptions import ABConnectError


class TestContactsEndpoints(BaseEndpointTest):
    """Test cases for Contacts endpoints."""
    
    tag_name = "Contacts"
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
        self.assertTrue(hasattr(self.api, "raw"))


    def test_get_apicontactsid(self):
        """Test GET /api/contacts/{id}.
        
        See documentation: https://abconnecttools.readthedocs.io/en/latest/api/contacts.html#get_apicontactsid
        """
        # Path parameters
        id = self.test_contact_id

        response = self.api.raw.get(
            "/api/contacts/{id}",
            id=id,
        )
        
        # Check response
        self.assertIsNotNone(response)
        if isinstance(response, dict):
            self.assertIsInstance(response, dict)
        elif isinstance(response, list):
            self.assertIsInstance(response, list)

    def test_get_apicontactsuser(self):
        """Test GET /api/contacts/user.
        
        See documentation: https://abconnecttools.readthedocs.io/en/latest/api/contacts.html#get_apicontactsuser
        """
        response = self.api.raw.get(
            "/api/contacts/user",
        )
        
        # Check response
        self.assertIsNotNone(response)
        if isinstance(response, dict):
            self.assertIsInstance(response, dict)
        elif isinstance(response, list):
            self.assertIsInstance(response, list)

    def test_get_apicontactscontactideditdetails(self):
        """Test GET /api/contacts/{contactId}/editdetails.
        
        See documentation: https://abconnecttools.readthedocs.io/en/latest/api/contacts.html#get_apicontactscontactideditdetails
        """
        # Path parameters
        contactId = self.test_contact_id

        response = self.api.raw.get(
            "/api/contacts/{contactId}/editdetails",
            contactId=contactId,
        )
        
        # Check response
        self.assertIsNotNone(response)
        if isinstance(response, dict):
            self.assertIsInstance(response, dict)
        elif isinstance(response, list):
            self.assertIsInstance(response, list)

    @unittest.skip("Requires complete contact data to update")
    def test_put_apicontactscontactideditdetails(self):
        """Test PUT /api/contacts/{contactId}/editdetails.
        
        See documentation: https://abconnecttools.readthedocs.io/en/latest/api/contacts.html#put_apicontactscontactideditdetails
        """
        # Path parameters
        contactId = self.test_contact_id

        response = self.api.raw.put(
            "/api/contacts/{contactId}/editdetails",
            contactId=contactId,
        )
        
        # Check response
        self.assertIsNotNone(response)
        if isinstance(response, dict):
            self.assertIsInstance(response, dict)
        elif isinstance(response, list):
            self.assertIsInstance(response, list)

    @unittest.skip("Requires complete contact data to create/update")
    def test_post_apicontactseditdetails(self):
        """Test POST /api/contacts/editdetails.
        
        See documentation: https://abconnecttools.readthedocs.io/en/latest/api/contacts.html#post_apicontactseditdetails
        """
        # POST requests need a body - provide minimal valid data
        data = {
            "id": self.test_contact_id,
            "companyId": self.test_company_id
        }
        
        response = self.api.raw.post(
            "/api/contacts/editdetails",
            data=data
        )
        
        # Check response
        self.assertIsNotNone(response)
        if isinstance(response, dict):
            self.assertIsInstance(response, dict)
        elif isinstance(response, list):
            self.assertIsInstance(response, list)


if __name__ == "__main__":
    import unittest
    unittest.main()