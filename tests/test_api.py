"""Tests for ABConnect API client."""

import unittest
from unittest.mock import patch, MagicMock
from ABConnect import ABConnectAPI
from ABConnect.config import Config


class TestABConnectAPI(unittest.TestCase):
    """Test cases for ABConnect API client."""
    
    def setUp(self):
        """Set up test fixtures."""
        Config.load(".env.staging", force_reload=True)
        self.api = ABConnectAPI()
        
    def test_api_initialization(self):
        """Test API client initialization."""
        self.assertIsNotNone(self.api)
        self.assertTrue(hasattr(self.api, 'raw'))
        self.assertTrue(hasattr(self.api, 'users'))
        self.assertTrue(hasattr(self.api, 'companies'))
        
    def test_raw_api_available(self):
        """Test raw API is available."""
        self.assertTrue(hasattr(self.api.raw, 'get'))
        self.assertTrue(hasattr(self.api.raw, 'post'))
        self.assertTrue(hasattr(self.api.raw, 'put'))
        self.assertTrue(hasattr(self.api.raw, 'delete'))
        
    @patch('ABConnect.api.http.RequestHandler.call')
    def test_raw_get(self, mock_call):
        """Test raw GET request."""
        mock_call.return_value = {'status': 'success'}
        
        result = self.api.raw.get('/api/test')
        
        mock_call.assert_called_once_with('GET', 'test', params={})
        self.assertEqual(result, {'status': 'success'})
        
    @patch('ABConnect.api.http.RequestHandler.call')
    def test_raw_post(self, mock_call):
        """Test raw POST request."""
        mock_call.return_value = {'id': '123', 'status': 'created'}
        
        data = {'name': 'Test'}
        result = self.api.raw.post('/api/test', data=data)
        
        mock_call.assert_called_once_with('POST', 'test', json=data, params={})
        self.assertEqual(result['status'], 'created')
        
    def test_available_endpoints(self):
        """Test listing available endpoints."""
        endpoints = self.api.available_endpoints
        
        self.assertIsInstance(endpoints, list)
        self.assertIn('users', endpoints)
        self.assertIn('companies', endpoints)
        self.assertGreater(len(endpoints), 10)  # Should have many endpoints
        
    def test_endpoint_info(self):
        """Test getting endpoint information."""
        # Test manual endpoint
        info = self.api.get_endpoint_info('users')
        self.assertEqual(info['name'], 'users')
        self.assertEqual(info['type'], 'manual')
        self.assertIn('methods', info)
        
        # Test lookup endpoint special handling
        info = self.api.get_endpoint_info('lookup')
        self.assertIn('lookup_keys', info)


if __name__ == "__main__":
    unittest.main()
