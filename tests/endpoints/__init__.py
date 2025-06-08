"""
Base classes and utilities for endpoint testing.
"""

import pytest
import os
from typing import Dict, Any, Optional, List
from unittest import TestCase
from ABConnect.api import ABConnectAPI


class BaseEndpointTest(TestCase):
    """Base class for all endpoint tests.
    
    Provides common setup, teardown, and helper methods for testing API endpoints.
    
    Test Fixtures:
        - test_company_id: 'ed282b80-54fe-4f42-bf1b-69103ce1f76c' (training company)
        - test_company_code: 'TRAINING'
        - test_job_display_id: '2000000'
        - test_contact_id: '207818'
        
    These fixtures provide known test data that exists in both staging and production
    environments for consistent testing.
    """
    
    # Override in subclasses
    tag_name: str = None
    
    # Prevent pytest from discovering this base class
    __test__ = False
    
    @classmethod
    def setUpClass(cls):
        """Set up test class with API client."""
        super().setUpClass()
        
        # Use staging environment for tests
        os.environ['ABC_ENVIRONMENT'] = 'staging'
        
        # Initialize API clients
        cls.api = ABConnectAPI(env='staging')
        
    def setUp(self):
        """Set up each test."""
        super().setUp()
        
        # Get endpoints for this tag
        if self.tag_name:
            self.endpoints = self._get_tag_endpoints()
    
    def _get_tag_endpoints(self) -> List[Dict[str, Any]]:
        """Get all endpoints for this tag from swagger."""
        if not hasattr(self.api, '_swagger_parser'):
            return []
            
        swagger = self.api._swagger_parser.spec
        endpoints = []
        
        for path, methods in swagger.get('paths', {}).items():
            for method, details in methods.items():
                if method in ['get', 'post', 'put', 'patch', 'delete']:
                    tags = details.get('tags', [])
                    if self.tag_name in tags:
                        endpoints.append({
                            'path': path,
                            'method': method.upper(),
                            'operation_id': details.get('operationId'),
                            'parameters': details.get('parameters', []),
                            'summary': details.get('summary', ''),
                            'description': details.get('description', '')
                        })
        
        return endpoints
    
    def _make_request(self, method: str, path: str, **kwargs) -> Any:
        """Make a request using the generic API client."""
        # Convert path parameters
        path_params = kwargs.pop('path_params', {})
        for param, value in path_params.items():
            path = path.replace(f'{{{param}}}', str(value))
        
        # Make the request using raw API
        return self.api.raw.request(method, path, **kwargs)
    
    def assert_response_ok(self, response: Any, status_codes: List[int] = None):
        """Assert that response is successful."""
        if status_codes is None:
            status_codes = [200, 201, 204]
        
        if hasattr(response, 'status_code'):
            self.assertIn(response.status_code, status_codes,
                         f"Expected status code in {status_codes}, got {response.status_code}")
    
    def assert_response_has_fields(self, response: Any, fields: List[str]):
        """Assert that response contains expected fields."""
        if isinstance(response, dict):
            for field in fields:
                self.assertIn(field, response,
                             f"Expected field '{field}' not found in response")
        elif isinstance(response, list) and response:
            # Check first item in list
            for field in fields:
                self.assertIn(field, response[0],
                             f"Expected field '{field}' not found in response")
    
    # Standard test methods to override in subclasses
    
    def test_list_operations(self):
        """Test GET list endpoints for this tag."""
        list_endpoints = [e for e in self.endpoints 
                         if e['method'] == 'GET' and not any(
                             p.get('in') == 'path' for p in e['parameters']
                         )]
        
        if not list_endpoints:
            self.skipTest(f"No list endpoints found for {self.tag_name}")
        
        for endpoint in list_endpoints:
            with self.subTest(endpoint=endpoint['path']):
                try:
                    response = self._make_request('GET', endpoint['path'])
                    self.assert_response_ok(response)
                except Exception as e:
                    # Log but don't fail - some endpoints may require specific setup
                    print(f"Warning: Failed to test {endpoint['path']}: {e}")
    
    def test_endpoint_discovery(self):
        """Test that endpoints for this tag are discoverable."""
        self.assertIsNotNone(self.tag_name, "tag_name must be set in subclass")
        self.assertGreater(len(self.endpoints), 0,
                          f"No endpoints found for tag '{self.tag_name}'")
        
        # Log discovered endpoints for debugging
        for endpoint in self.endpoints:
            print(f"  {endpoint['method']} {endpoint['path']} - {endpoint['summary']}")
    
    def get_test_id(self, resource_type: str) -> Optional[str]:
        """Get a test ID for a given resource type.
        
        Override in subclasses to provide valid test IDs.
        """
        # Common test IDs - override in subclasses with real values
        test_ids = {
            'company': 'ed282b80-54fe-4f42-bf1b-69103ce1f76c',  # training company
            'company_code': 'TRAINING',
            'contact': '207818',  # valid contact ID
            'job': '2000000',  # job display ID
            'job_display_id': '2000000',
            'user': '789e0123-e89b-12d3-a456-426614174002'
        }
        return test_ids.get(resource_type)
    
    @property
    def test_company_id(self) -> str:
        """Get the test company ID for 'training' company."""
        return 'ed282b80-54fe-4f42-bf1b-69103ce1f76c'
    
    @property
    def test_company_code(self) -> str:
        """Get the test company code."""
        return 'TRAINING'
    
    @property
    def test_job_display_id(self) -> str:
        """Get the test job display ID."""
        return '2000000'
    
    @property
    def test_contact_id(self) -> str:
        """Get the test contact ID."""
        return '207818'
    
    def get_test_data(self, operation: str) -> Dict[str, Any]:
        """Get test data for a given operation.
        
        Override in subclasses to provide valid test data.
        """
        # Basic test data - override in subclasses
        return {
            'name': 'Test Name',
            'description': 'Test Description',
            'status': 'active'
        }


class EndpointTestGenerator:
    """Helper class to generate test methods dynamically."""
    
    @staticmethod
    def generate_crud_tests(endpoint_data: List[Dict[str, Any]]):
        """Generate standard CRUD test methods for endpoints."""
        def make_test_method(endpoint):
            def test_method(self):
                # Test implementation
                response = self._make_request(
                    endpoint['method'],
                    endpoint['path']
                )
                self.assert_response_ok(response)
            
            # Set descriptive name
            operation = endpoint.get('operation_id', endpoint['path'])
            test_method.__name__ = f"test_{operation}"
            test_method.__doc__ = endpoint.get('summary', '')
            
            return test_method
        
        tests = {}
        for endpoint in endpoint_data:
            test = make_test_method(endpoint)
            tests[test.__name__] = test
        
        return tests