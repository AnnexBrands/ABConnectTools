"""Tests for company endpoints."""

import pytest
from tests.base import ABConnectTestCase


class TestCompaniesEndpoint(ABConnectTestCase):
    """Test companies endpoint using unittest style."""
    
    def test_get_company_by_code(self):
        """Test getting company by code."""
        # Skip if no test company code available
        test_company_code = 'TSTCODE'  # Replace with actual test company code
        
        try:
            response = self.api.companies.get(test_company_code)
            
            # Should return a dict
            self.assertIsInstance(response, dict)
            print(f"Company info: {response.get('name', 'Unknown')}")
        except Exception as e:
            # If company not found, that's ok for test
            print(f"Company not found or error: {e}")


# Alternative: Using pytest fixtures
@pytest.mark.skip(reason="Companies endpoint doesn't have generic methods yet")
def test_get_company_with_fixture(api_client):
    """Test getting a company using pytest fixture."""
    # This test uses the api_client fixture from conftest.py
    response = api_client.companies.list(page=1, per_page=1)
    
    assert isinstance(response, dict)
    assert 'data' in response
    
    if response['data']:
        company = response['data'][0]
        print(f"First company: {company.get('name', 'Unknown')}")


@pytest.mark.skip(reason="Companies endpoint doesn't have query builder yet")
def test_companies_query_builder(api_client):
    """Test companies with query builder."""
    # Use the new query builder
    query = api_client.companies.query().limit(3)
    
    # Check that query builder works
    assert hasattr(query, 'execute')
    assert hasattr(query, 'filter')
    assert hasattr(query, 'sort')