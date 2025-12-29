"""Webhooks API endpoints.

Auto-generated from swagger.json specification.
Provides type-safe access to webhooks/* endpoints.
"""

from ABConnect.api.endpoints.base import BaseEndpoint


class WebhooksEndpoint(BaseEndpoint):
    """Webhooks API endpoint operations.
    
    Handles all API operations for /api/webhooks/* endpoints.
    Total endpoints: 4
    """
    
    api_path = "webhooks"

    def post_stripe_handle(self) -> dict:
        """POST /api/webhooks/stripe/handle
        
        
        
        Returns:
            dict: API response data
        """
        path = "/stripe/handle"
        kwargs = {}
        return self._make_request("POST", path, **kwargs)
    def post_stripe_connect_handle(self) -> dict:
        """POST /api/webhooks/stripe/connect/handle
        
        
        
        Returns:
            dict: API response data
        """
        path = "/stripe/connect/handle"
        kwargs = {}
        return self._make_request("POST", path, **kwargs)
    def post_stripe_checkout_session_completed(self) -> dict:
        """POST /api/webhooks/stripe/checkout.session.completed
        
        
        
        Returns:
            dict: API response data
        """
        path = "/stripe/checkout.session.completed"
        kwargs = {}
        return self._make_request("POST", path, **kwargs)
    def post_twilio_smsstatuscallback(self, data: dict = None) -> dict:
        """POST /api/webhooks/twilio/smsStatusCallback
        
        
        
        Returns:
            dict: API response data
        """
        path = "/twilio/smsStatusCallback"
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
