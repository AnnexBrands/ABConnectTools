"""Pytest configuration and fixtures for ABConnect tests."""

import pytest
from ABConnect import ABConnectAPI, models


@pytest.fixture(scope="session")
def api():
    return ABConnectAPI(env='staging', username='training')

@pytest.fixture(scope="session")
def models():
    return models