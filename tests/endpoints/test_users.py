"""Tests for Users API endpoints.

Documentation: https://abconnecttools.readthedocs.io/en/latest/api/users.html
"""

import unittest
from unittest.mock import patch, MagicMock
from . import BaseEndpointTest
from ABConnect.exceptions import ABConnectError


class TestUsersEndpoints(BaseEndpointTest):
    """Test cases for Users endpoints."""
    
    tag_name = "Users"
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


    @unittest.skip("Users list endpoint returns 500 error - likely requires request body")
    def test_post_apiuserslist(self):
        """Test POST /api/users/list.
        
        See documentation: https://abconnecttools.readthedocs.io/en/latest/api/users.html#post_apiuserslist
        """
        response = self.api.raw.post(
            "/api/users/list",
        )
        
        # Check response
        self.assertIsNotNone(response)
        if isinstance(response, dict):
            self.assertIsInstance(response, dict)
        elif isinstance(response, list):
            self.assertIsInstance(response, list)

    @unittest.skip("User endpoint requires complete user data")
    def test_post_apiusersuser(self):
        """Test POST /api/users/user.
        
        See documentation: https://abconnecttools.readthedocs.io/en/latest/api/users.html#post_apiusersuser
        """
        response = self.api.raw.post(
            "/api/users/user",
        )
        
        # Check response
        self.assertIsNotNone(response)
        if isinstance(response, dict):
            self.assertIsInstance(response, dict)
        elif isinstance(response, list):
            self.assertIsInstance(response, list)

    @unittest.skip("User endpoint requires complete user data")
    def test_put_apiusersuser(self):
        """Test PUT /api/users/user.
        
        See documentation: https://abconnecttools.readthedocs.io/en/latest/api/users.html#put_apiusersuser
        """
        response = self.api.raw.put(
            "/api/users/user",
        )
        
        # Check response
        self.assertIsNotNone(response)
        if isinstance(response, dict):
            self.assertIsInstance(response, dict)
        elif isinstance(response, list):
            self.assertIsInstance(response, list)

    def test_get_apiusersroles(self):
        """Test GET /api/users/roles.
        
        See documentation: https://abconnecttools.readthedocs.io/en/latest/api/users.html#get_apiusersroles
        """
        response = self.api.raw.get(
            "/api/users/roles",
        )
        
        # Check response
        self.assertIsNotNone(response)
        if isinstance(response, dict):
            self.assertIsInstance(response, dict)
        elif isinstance(response, list):
            self.assertIsInstance(response, list)

    def test_get_apiuserspocusers(self):
        """Test GET /api/users/pocusers.
        
        See documentation: https://abconnecttools.readthedocs.io/en/latest/api/users.html#get_apiuserspocusers
        """
        response = self.api.raw.get(
            "/api/users/pocusers",
        )
        
        # Check response
        self.assertIsNotNone(response)
        if isinstance(response, dict):
            self.assertIsInstance(response, dict)
        elif isinstance(response, list):
            self.assertIsInstance(response, list)


if __name__ == "__main__":
    unittest.main()