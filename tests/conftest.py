"""Pytest configuration and fixtures for ABConnect tests."""

import pytest
from ABConnect import ABConnectAPI, models as _models
from ABConnect.routes import SCHEMA
import json
from pathlib import Path
fixtures = Path(__file__).parent / "fixtures"

def pytest_configure(config):
    """Register custom pytest markers."""
    config.addinivalue_line("markers", "integration: marks tests as integration tests (require API access)")
    config.addinivalue_line("markers", "slow: marks tests as slow running")


@pytest.fixture(scope="session")
def api():
    """Session-scoped ABConnectAPI instance for staging environment."""
    return ABConnectAPI(env='staging', username='training')


@pytest.fixture(scope="session")
def models():
    """Provide ABConnect models module for isinstance checks in tests."""
    return _models

@pytest.fixture(scope="session")
def schema():
    return SCHEMA

@pytest.fixture
def ContactDetailsData():
    return json.loads((fixtures / "ContactDetails.json").read_text())


@pytest.fixture
def CompanySimpleData():
    return json.loads((fixtures / "CompanySimple.json").read_text())