"""Tests for ABConnect.Quoter module."""

from ..base_test import ABConnectTestCase


class QuoterTestCase(ABConnectTestCase):
    """Base test class for Quoter tests.

    Provides quoter-specific test helpers.
    """

    @classmethod
    def setUpClass(cls):
        """Set up test class with quoter resources."""
        super().setUpClass()
        cls.quoter_module_path = cls.project_root / "ABConnect" / "Quoter.py"

    def create_sample_quote_data(self) -> dict:
        """Create sample data for quote testing."""
        return {
            "origin": {
                "address": "123 Origin St",
                "city": "Origin City",
                "state": "CA",
                "zip": "90210"
            },
            "destination": {
                "address": "456 Dest Ave",
                "city": "Dest City",
                "state": "NY",
                "zip": "10001"
            },
            "items": [
                {
                    "description": "Test Item",
                    "weight": 100,
                    "dimensions": {"length": 10, "width": 10, "height": 10}
                }
            ]
        }

    def assert_quote_response(self, response: dict):
        """Assert that a quote response has required fields."""
        required_fields = ["quote_id", "total_cost", "service_level"]
        for field in required_fields:
            self.assertIn(field, response, f"Quote response missing {field}")