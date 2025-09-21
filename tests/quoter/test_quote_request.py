"""Tests for Quote Request (qr) functionality."""

from unittest.mock import patch, MagicMock
from . import QuoterTestCase
from ABConnect.Quoter import Quoter


class TestQuoteRequest(QuoterTestCase):
    """Test suite for Quote Request mode."""

    def setUp(self):
        """Set up test fixtures."""
        super().setUp()
        self.sample_qr_response = {
            "SubmitNewQuoteRequestV2Result": {
                "QuoteCertified": False,
                "JobID": "J123",
                "JobDisplayID": "Display123",
                "BookingKey": "BK123",
                "PriceBreakdown": {
                    "Pickup": 12.0,
                    "Packaging": 6.0,
                    "Transportation": 18.0,
                    "Insurance": 2.5,
                    "Delivery": 3.5,
                },
                "TotalAmount": 42.0,
            }
        }

    @patch("ABConnect.Quoter.requests.post")
    def test_full_quote_generation(self, mock_post):
        """Test generating a full quote request."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = self.sample_qr_response
        mock_post.return_value = mock_response

        quoter = Quoter(env="", type="qr", auto_book=False)
        quoter.load_request(self.create_sample_quote_data())
        quoter.call_quoter()
        quoter.parse_response()

        # Quote requests provide booking information
        self.assertEqual(quoter.parsed_data["jobid"], "J123")
        self.assertEqual(quoter.parsed_data["job"], "Display123")
        self.assertEqual(quoter.parsed_data["bookingkey"], "BK123")

    def test_booking_capability(self):
        """Test quote request booking capability."""
        with patch("ABConnect.Quoter.requests.post") as mock_post:
            mock_response = MagicMock()
            mock_response.status_code = 200
            mock_response.json.return_value = self.sample_qr_response
            mock_post.return_value = mock_response

            quoter = Quoter(env="", type="qr", auto_book=False)
            quoter.load_request({"test": "data"})
            quoter.call_quoter()
            quoter.parse_response()

            # Should have booking key for future booking
            self.assertIsNotNone(quoter.parsed_data["bookingkey"])
            self.assertEqual(quoter.parsed_data["bookingkey"], "BK123")

    def test_detailed_pricing(self):
        """Test detailed pricing breakdown."""
        with patch("ABConnect.Quoter.requests.post") as mock_post:
            mock_response = MagicMock()
            mock_response.status_code = 200
            mock_response.json.return_value = self.sample_qr_response
            mock_post.return_value = mock_response

            quoter = Quoter(env="", type="qr", auto_book=False)
            quoter.load_request({"test": "data"})
            quoter.call_quoter()
            quoter.parse_response()

            parsed = quoter.parsed_data
            self.assertEqual(parsed["Pickup"], 12.0)
            self.assertEqual(parsed["Packaging"], 6.0)
            self.assertEqual(parsed["Transportation"], 18.0)
            self.assertEqual(parsed["Insurance"], 2.5)
            self.assertEqual(parsed["Delivery"], 3.5)
            self.assertEqual(parsed["total"], 42.0)

    def test_carrier_selection(self):
        """Test carrier selection options."""
        self.skipTest("Carrier selection testing not yet implemented")