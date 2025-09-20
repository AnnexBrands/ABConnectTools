"""Notifications API endpoints.

Auto-generated from swagger.json specification.
Provides type-safe access to notifications/* endpoints.
"""

from .base import BaseEndpoint


class NotificationsEndpoint(BaseEndpoint):
    """Notifications API endpoint operations.
    
    Handles all API operations for /api/notifications/* endpoints.
    Total endpoints: 1
    """
    
    api_path = "notifications"

    def get_get(self) -> dict:
        """GET /api/notifications
        
        
        
        Returns:
            dict: API response data
        """
        path = "/"
        kwargs = {}
        return self._make_request("GET", path, **kwargs)
