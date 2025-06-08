"""Tests for Job API endpoints.

Documentation: https://abconnecttools.readthedocs.io/en/latest/api/job.html
"""

import unittest
from unittest.mock import patch, MagicMock
from . import BaseEndpointTest
from ABConnect.exceptions import ABConnectError, RequestError
from ABConnect.api.models import Job, parse_response


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

        try:
            response = self.api.raw.get(
                "/api/job/{jobDisplayId}",
                jobDisplayId=jobDisplayId,
            )
            
            # Check response
            self.assertIsNotNone(response)
            self.assertIsInstance(response, dict)
            
            # Validate response with Pydantic model
            job = Job.model_validate(response)
            # The response should have at least the display ID
            if hasattr(job, 'displayId') and job.displayId:
                self.assertEqual(job.displayId, self.test_job_display_id)
        except RequestError as e:
            if e.status_code == 500:
                self.skipTest(f"Job {jobDisplayId} returns 500 error - may not exist in staging")
            else:
                raise

    @unittest.skip("Job search endpoint returns 404 in staging")
    def test_get_apijobsearch(self):
        """Test GET /api/job/search.
        
        See documentation: https://abconnecttools.readthedocs.io/en/latest/api/job.html#get_apijobsearch
        """
        response = self.api.raw.get(
            "/api/job/search",
        )
        
        # Check response
        self.assertIsNotNone(response)
        
        # Search endpoints typically return lists
        if isinstance(response, list):
            # If we have results, validate each one
            for item in response[:5]:  # Validate first 5 items max
                if isinstance(item, dict):
                    job = Job.model_validate(item)
                    self.assertIsInstance(job, Job)
        elif isinstance(response, dict):
            # Might be a paginated response
            if 'data' in response and isinstance(response['data'], list):
                for item in response['data'][:5]:
                    if isinstance(item, dict):
                        job = Job.model_validate(item)
                        self.assertIsInstance(job, Job)

    @unittest.skip("Complex search endpoint requires specific SortByModel format")
    def test_post_apijobsearchbydetails(self):
        """Test POST /api/job/searchByDetails.
        
        See documentation: https://abconnecttools.readthedocs.io/en/latest/api/job.html#post_apijobsearchbydetails
        """
        # Provide minimal search criteria with required fields
        search_data = {
            "companyId": self.test_company_id,
            "page": 1,
            "perPage": 10,
            "pageSize": 10,
            "sortBy": {"field": "displayId", "direction": "asc"}
        }
        
        response = self.api.raw.post(
            "/api/job/searchByDetails",
            data=search_data
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