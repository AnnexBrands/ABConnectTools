"""Pytest configuration for ABConnect tests.

This file configures pytest to use staging environment
and provides common fixtures for tests.
"""

import pytest
import os
from ABConnect.config import Config


def pytest_configure(config):
    """Configure pytest to use staging environment."""
    # Load staging configuration before any tests run
    Config.load('.env.staging', force_reload=True)
    
    # Verify we're in staging mode
    env = Config.get_env()
    print(f"\n🧪 Running tests in {env} environment")
    print(f"   API URL: {Config.get_api_base_url()}")
    print(f"   Identity URL: {Config.get_identity_url()}")


def pytest_unconfigure(config):
    """Reset configuration after tests."""
    Config.reset()


@pytest.fixture(scope='session')
def staging_config():
    """Provide staging configuration for tests."""
    return Config()


@pytest.fixture
def mock_api_response():
    """Provide a mock API response for testing."""
    def _mock_response(data=None, status_code=200):
        class MockResponse:
            def __init__(self, data, status_code):
                self.data = data
                self.status_code = status_code
                self.text = str(data)
                
            def json(self):
                return self.data
                
            def raise_for_status(self):
                if not (200 <= self.status_code < 300):
                    raise Exception(f"HTTP {self.status_code}")
                    
        return MockResponse(data or {}, status_code)
    
    return _mock_response


@pytest.fixture
def test_credentials():
    """Provide test credentials from staging environment."""
    return {
        'username': Config.get('ABCONNECT_USERNAME'),
        'password': Config.get('ABCONNECT_PASSWORD'),
        'client_id': Config.get('ABC_CLIENT_ID'),
        'client_secret': Config.get('ABC_CLIENT_SECRET'),
    }