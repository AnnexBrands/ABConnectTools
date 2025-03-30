import requests
import logging
from ABConnect.Builder import APIRequestBuilder

logger = logging.getLogger(__name__)


class Quoter:
    """
    Provides functionality for requesting and handling quotes via the ABC API.

    Parameters:
        env (str): 'staging' or '' for production.
        JobType (str): 'Regular' for full service, '3PL' for eLabel. Default is 'Regular'.
        type (str): 'qr' for quote request or 'qq' for quick quote. Default is 'qq'.
        auto_book (bool): If True, attempts to book the quote automatically.

    Usage:
        q = Quoter(env='staging', type='qr', auto_book=True)
        or
        q = Quoter()
    """

    def __init__(self, *args, **kwargs):
        self.env = kwargs.get("env", "")
        self.jobType = kwargs.get("JobType", "Regular")
        self.request_type = kwargs.get("type", "qq").lower()  # Normalize to lower-case.
        self.auto_book = kwargs.get("auto_book", False)

        self.url = {
            "qq": f"https://api.{self.env}abconnect.co/api/autoprice/quickquote",
            "qr": f"https://api.{self.env}abconnect.co/api/autoprice/v2/quoterequest",
        }.get(self.request_type)

        if not self.url:
            raise ValueError(
                "Invalid request type specified. Use 'qq' for quick quote or 'qr' for quote request."
            )

        self.builder = APIRequestBuilder(req_type=self.jobType)
        self.data = None
        self.response_json = None
        self.parsed_data = None

    def load_request(self, data):
        """
        Loads the request payload.

        Args:
            data (dict): The JSON payload to be sent to the API.
        """
        self.data = data
        return self

    def call_quoter(self):
        """
        Calls the ABC API with the current request data.
        Raises an exception if the API call fails.
        """
        try:
            response = requests.post(self.url, json=self.data)
        except requests.RequestException as e:
            logger.error("Network error during API call: %s", e)
            raise Exception("Failed to connect to ABC API") from e

        if response.status_code == 200:
            try:
                self.response_json = response.json()
            except ValueError as e:
                logger.error("Response is not valid JSON: %s", response.text)
                raise Exception("Invalid JSON response from ABC API") from e
        else:
            msg = f"{response.status_code} error from ABC API: {response.text}"
            logger.error(msg)
            raise Exception(msg)

    def parse_qr_response(self):
        """
        Parses the quote request (qr) response from the API.
        """
        try:
            quote = self.response_json["SubmitNewQuoteRequestV2Result"]
        except KeyError as e:
            logger.error("Expected key missing in QR response: %s", e)
            raise Exception("Malformed QR response from ABC API") from e

        self.parsed_data = {
            "quote_certified": quote.get("QuoteCertified", False),
            "jobid": quote.get("JobID"),
            "job": quote.get("JobDisplayID"),
            "bookingkey": quote.get("BookingKey"),
            "Pickup": quote.get("PriceBreakdown", {}).get("Pickup", 0),
            "Packaging": quote.get("PriceBreakdown", {}).get("Packaging", 0),
            "Transportation": quote.get("PriceBreakdown", {}).get("Transportation", 0),
            "Insurance": quote.get("PriceBreakdown", {}).get("Insurance", 0),
            "Delivery": quote.get("PriceBreakdown", {}).get("Delivery", 0),
            "total": quote.get("TotalAmount", 0),
        }

    def parse_qq_response(self):
        """
        Parses the quick quote (qq) response from the API.
        """
        try:
            quote = self.response_json["SubmitQuickQuoteRequestPOSTResult"]
        except KeyError as e:
            logger.error("Expected key missing in QQ response: %s", e)
            raise Exception("Malformed QQ response from ABC API") from e

        self.parsed_data = {
            "jobid": None,
            "quote_certified": quote.get("QuoteCertified", False),
            "job": "Quick Quote",
            "bookingkey": None,
            "Pickup": quote.get("PriceBreakdown", {}).get("Pickup", 0),
            "Packaging": quote.get("PriceBreakdown", {}).get("Packaging", 0),
            "Transportation": quote.get("PriceBreakdown", {}).get("Transportation", 0),
            "Insurance": quote.get("PriceBreakdown", {}).get("Insurance", 0),
            "Delivery": quote.get("PriceBreakdown", {}).get("Delivery", 0),
            "total": quote.get("TotalAmount", 0),
        }

    def parse_response(self):
        """
        Parses the API response based on the request type.
        """
        if self.request_type == "qq":
            self.parse_qq_response()
        elif self.request_type == "qr":
            self.parse_qr_response()
        else:
            raise ValueError("Unsupported request type for parsing response.")

    def book(self):
        """
        Attempts to book the quote using the booking URL.
        Raises an exception if the booking fails.
        """
        try:
            book_url = "https://abconnect.co/book/{job}?key={bookingkey}"
            url = book_url.format(
                job=self.parsed_data.get("job", ""),
                bookingkey=self.parsed_data.get("bookingkey", ""),
            )
            response = requests.get(url)
            if response.status_code != 200:
                msg = f"Booking failed for {self.parsed_data.get('job', 'Unknown Job')}: {response.text}"
                logger.error(msg)
                raise Exception(msg)
        except Exception as e:
            logger.error("Error during booking: %s", e)
            raise

    def cleanup(self):
        """
        Cleans up stored request and response data.
        """
        self.data = None
        self.response_json = None

    def run(self):
        """
        Executes the full quoting process.

        Raises:
            Exception: If no request data is loaded or if any step fails.
        Returns:
            self: The Quoter instance after processing.
        """
        if not self.data:
            raise Exception("No data - must call load_request() first")
        self.call_quoter()
        self.parse_response()
        if self.auto_book:
            self.book()
        self.cleanup()
        return self

    def get_quote_summary(self) -> str:
        """
        Returns a formatted summary of the quote.

        Returns:
            A string with quote details.
        """
        if not self.parsed_data:
            raise Exception("No parsed quote data available. Call run() first.")

        certified = (
            "Certified" if self.parsed_data.get("quote_certified") else "Not Certified"
        )
        summary = (
            f"Quote: {self.parsed_data.get('job', 'N/A')}\n"
            f"Certified: {certified}\n"
            f"Pickup: ${self.parsed_data.get('Pickup', 0):.2f}\n"
            f"Packaging: ${self.parsed_data.get('Packaging', 0):.2f}\n"
            f"Ship: ${self.parsed_data.get('Transportation', 0):.2f}\n"
            f"Insurance: ${self.parsed_data.get('Insurance', 0):.2f}\n"
            f"Delivery: ${self.parsed_data.get('Delivery', 0):.2f}\n"
            f"Total: ${self.parsed_data.get('total', 0):.2f}\n"
        )
        return summary

    def __str__(self) -> str:
        return self.get_quote_summary()
