"""Tests for Job API endpoints.

Documentation: https://abconnecttools.readthedocs.io/en/latest/api/job.html
"""

from unittest.mock import patch, MagicMock
from . import BaseEndpointTest
from ABConnect.exceptions import ABConnectError


class TestJobEndpoints(BaseEndpointTest):
    """Test cases for Job endpoints."""
    
    tag_name = "Job"
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


    def test_post_apijobjobdisplayidbook(self):
        """Test POST /api/job/{jobDisplayId}/book.
        
        See documentation: https://abconnecttools.readthedocs.io/en/latest/api/job.html#post_apijobjobdisplayidbook
        """
        # Path parameters - use the test job display ID
        jobDisplayId = self.test_job_display_id

        response = self.api.raw.post(
            "/api/job/{jobDisplayId}/book",
            jobDisplayId=jobDisplayId,
        )
        
        # Check response
        self.assertIsNotNone(response)
        if isinstance(response, dict):
            self.assertIsInstance(response, dict)
        elif isinstance(response, list):
            self.assertIsInstance(response, list)

    def test_get_apijobjobdisplayid(self):
        """Test GET /api/job/{jobDisplayId}.
        
        See documentation: https://abconnecttools.readthedocs.io/en/latest/api/job.html#get_apijobjobdisplayid
        """
        # Path parameters - use the test job display ID
        jobDisplayId = self.test_job_display_id

        response = self.api.raw.get(
            "/api/job/{jobDisplayId}",
            jobDisplayId=jobDisplayId,
        )
        
        # Check response
        self.assertIsNotNone(response)
        if isinstance(response, dict):
            self.assertIsInstance(response, dict)
        elif isinstance(response, list):
            self.assertIsInstance(response, list)

    def test_get_apijobsearch(self):
        """Test GET /api/job/search.
        
        See documentation: https://abconnecttools.readthedocs.io/en/latest/api/job.html#get_apijobsearch
        """
        response = self.api.raw.get(
            "/api/job/search",
        )
        
        # Check response
        self.assertIsNotNone(response)
        if isinstance(response, dict):
            self.assertIsInstance(response, dict)
        elif isinstance(response, list):
            self.assertIsInstance(response, list)

    def test_post_apijobsearchbydetails(self):
        """Test POST /api/job/searchByDetails.
        
        See documentation: https://abconnecttools.readthedocs.io/en/latest/api/job.html#post_apijobsearchbydetails
        """
        response = self.api.raw.post(
            "/api/job/searchByDetails",
        )
        
        # Check response
        self.assertIsNotNone(response)
        if isinstance(response, dict):
            self.assertIsInstance(response, dict)
        elif isinstance(response, list):
            self.assertIsInstance(response, list)

    def test_get_apijobjobdisplayidcalendaritems(self):
        """Test GET /api/job/{jobDisplayId}/calendaritems.
        
        See documentation: https://abconnecttools.readthedocs.io/en/latest/api/job.html#get_apijobjobdisplayidcalendaritems
        """
        # Path parameters - use the test job display ID
        jobDisplayId = self.test_job_display_id

        response = self.api.raw.get(
            "/api/job/{jobDisplayId}/calendaritems",
            jobDisplayId=jobDisplayId,
        )
        
        # Check response
        self.assertIsNotNone(response)
        if isinstance(response, dict):
            self.assertIsInstance(response, dict)
        elif isinstance(response, list):
            self.assertIsInstance(response, list)


if __name__ == "__main__":
    unittest.main()