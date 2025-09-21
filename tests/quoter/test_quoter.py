"""Tests for Quoter main class."""

from unittest.mock import patch, MagicMock
from . import QuoterTestCase
from ABConnect.Quoter import Quoter


class TestQuoter(QuoterTestCase):
    """Test suite for Quoter class."""

    def setUp(self):
        """Set up test fixtures."""
        super().setUp()
        # Sample responses for quick quote (qq) and quote request (qr)
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

    def test_quoter_initialization(self):
        """Test quoter initialization."""
        quoter = Quoter(env="", type="qq", auto_book=False)
        self.assertIsNotNone(quoter)

    @patch("ABConnect.Quoter.requests.post")
    def test_quick_quote_response(self, mock_post):
        """Test processing quick quote response."""
        # Setup a successful quick quote response.
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = self.sample_qq_response
        mock_post.return_value = mock_response

        quoter = Quoter(env="", type="qq", auto_book=False)
        # Load some dummy data.
        quoter.load_request({"test": "data"})
        quoter.call_quoter()
        quoter.parse_response()

        parsed = quoter.parsed_data
        self.assertEqual(parsed["quote_certified"], True)
        self.assertEqual(parsed["Pickup"], 10.0)
        self.assertEqual(parsed["Packaging"], 5.0)
        self.assertEqual(parsed["Transportation"], 15.0)
        self.assertEqual(parsed["Insurance"], 2.0)
        self.assertEqual(parsed["Delivery"], 3.0)
        self.assertEqual(parsed["total"], 35.0)
        self.assertEqual(parsed["job"], "Quick Quote")
        # Quick quote response sets jobid and bookingkey to None.
        self.assertIsNone(parsed["jobid"])
        self.assertIsNone(parsed["bookingkey"])

    @patch("ABConnect.Quoter.requests.post")
    def test_quote_request_response(self, mock_post):
        """Test processing quote request response."""
        # Setup a successful quote request response.
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = self.sample_qr_response
        mock_post.return_value = mock_response

        quoter = Quoter(env="", type="qr", auto_book=False)
        quoter.load_request({"test": "data"})
        quoter.call_quoter()
        quoter.parse_response()

        parsed = quoter.parsed_data
        self.assertEqual(parsed["quote_certified"], False)
        self.assertEqual(parsed["jobid"], "J123")
        self.assertEqual(parsed["job"], "Display123")
        self.assertEqual(parsed["bookingkey"], "BK123")
        self.assertEqual(parsed["Pickup"], 12.0)
        self.assertEqual(parsed["Packaging"], 6.0)
        self.assertEqual(parsed["Transportation"], 18.0)
        self.assertEqual(parsed["Insurance"], 2.5)
        self.assertEqual(parsed["Delivery"], 3.5)
        self.assertEqual(parsed["total"], 42.0)

    def test_builder_integration(self):
        """Test integration with APIRequestBuilder."""
        self.skipTest("Not yet implemented")

    def test_api_integration(self):
        """Test integration with ABConnect API."""
        self.skipTest("Not yet implemented")

    def test_auto_booking_functionality(self):
        """Test auto-booking capability."""
        quoter = Quoter(env="", type="qr", auto_book=True)
        self.assertTrue(quoter.auto_book)