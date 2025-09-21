"""Tests for Quick Quote (qq) functionality."""

from unittest.mock import patch, MagicMock
from . import QuoterTestCase
from ABConnect.Quoter import Quoter


class TestQuickQuote(QuoterTestCase):
    """Test suite for Quick Quote mode."""

    def setUp(self):
        """Set up test fixtures."""
        super().setUp()
        self.sample_qq_response = {
            "SubmitQuickQuoteRequestPOSTResult": {
                "QuoteCertified": True,
                "PriceBreakdown": {
                    "Pickup": 10.0,
                    "Packaging": 5.0,
                    "Transportation": 15.0,
                    "Insurance": 2.0,
                    "Delivery": 3.0,
                },
                "TotalAmount": 35.0,
            }
        }

    @patch("ABConnect.Quoter.requests.post")
    def test_quick_quote_generation(self, mock_post):
        """Test generating a quick quote."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = self.sample_qq_response
        mock_post.return_value = mock_response

        quoter = Quoter(env="", type="qq", auto_book=False)
        quoter.load_request(self.create_sample_quote_data())
        quoter.call_quoter()
        quoter.parse_response()

        # Quick quotes should be certified
        self.assertEqual(quoter.parsed_data["quote_certified"], True)
        self.assertEqual(quoter.parsed_data["job"], "Quick Quote")

    def test_quick_quote_no_booking_info(self):
        """Test that quick quotes don't return booking information."""
        with patch("ABConnect.Quoter.requests.post") as mock_post:
            mock_response = MagicMock()
            mock_response.status_code = 200
            mock_response.json.return_value = self.sample_qq_response
            mock_post.return_value = mock_response

            quoter = Quoter(env="", type="qq", auto_book=False)
            quoter.load_request({"test": "data"})
            quoter.call_quoter()
            quoter.parse_response()

            # Quick quotes don't provide booking information
            self.assertIsNone(quoter.parsed_data["jobid"])
            self.assertIsNone(quoter.parsed_data["bookingkey"])

    def test_fast_response_time(self):
        """Test that quick quotes are fast."""
        self.skipTest("Performance testing not implemented")

    def test_quote_accuracy(self):
        """Test accuracy of quick quote estimates."""
        self.skipTest("Accuracy testing requires real API comparison")

    def test_multiple_service_levels(self):
        """Test quick quotes for different service levels."""
        self.skipTest("Not yet implemented")