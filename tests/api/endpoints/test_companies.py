"""Tests for companies endpoint."""

from .base_endpoint_test import BaseEndpointTest


class TestCompaniesEndpoint(BaseEndpointTest):
    """Test suite for companies endpoint."""

    endpoint_name = "companies"
    required_models = ["Company", "CompanyDetails", "CompanyInfo"]

    def test_get_by_code(self):
        """Test getting company by code."""
        # Skip if no test company code available
        test_company_code = 'TRAINING'  # Use our test company code

        try:
            # This will require the API client to be available
            self.skipTest("API client not yet configured in test base")

            # When API is available, this would work:
            # response = self.api.companies.get(test_company_code)
            # self.assertIsInstance(response, dict)
            # self.assertIn('name', response)
        except Exception as e:
            self.skipTest(f"API not available: {e}")

    def test_cache_integration(self):
        """Test cache usage for code lookups."""
        # Test that get_cache is used for code-to-ID lookup
        endpoint_file = self.endpoints_dir / "companies.py"
        if endpoint_file.exists():
            with open(endpoint_file) as f:
                content = f.read()
                self.assertIn("get_cache", content, "Cache integration not found")
        else:
            self.skipTest("Companies endpoint file not found")

    def test_search_functionality(self):
        """Test company search."""
        self.skipTest("Search functionality not yet implemented")

    def test_convenience_get_method(self):
        """Test the convenience get() method exists."""
        endpoint_file = self.endpoints_dir / "companies.py"
        if endpoint_file.exists():
            with open(endpoint_file) as f:
                content = f.read()
                self.assertIn("def get(", content, "get() method not found")
        else:
            self.skipTest("Companies endpoint file not found")

    def test_query_builder_integration(self):
        """Test companies with query builder."""
        # Test will be implemented when query builder is available
        self.skipTest("Query builder not yet implemented")