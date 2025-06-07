"""Base test class and fixtures for ABConnect tests."""

import unittest
from ABConnect import ABConnectAPI
from ABConnect.config import Config


class ABConnectTestCase(unittest.TestCase):
    """Base test case with ABConnect API setup.
    
    All test classes that need API access should inherit from this.
    """
    
    @classmethod
    def setUpClass(cls):
        """Set up test class - runs once per test class."""
        # Load staging configuration once for all tests
        Config.load('.env.staging', force_reload=True)
        print(f"\n🧪 Test environment: {Config.get_env()}")
        print(f"   API URL: {Config.get_api_base_url()}")
    
    def setUp(self):
        """Set up each test - runs before each test method."""
        # Create fresh API instance for each test
        self.api = ABConnectAPI()
        
        # Store common test data
        self.test_username = Config.get('ABCONNECT_USERNAME')
        self.test_client_id = Config.get('ABC_CLIENT_ID')
    
    def tearDown(self):
        """Clean up after each test."""
        # Any cleanup if needed
        pass
    
    @classmethod
    def tearDownClass(cls):
        """Clean up after all tests in the class."""
        # Reset config to avoid affecting other test files
        Config.reset()