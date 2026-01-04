"""Notifications API endpoints.

Auto-generated from swagger.json specification.
Provides type-safe access to notifications/* endpoints.
"""

from ABConnect.api.endpoints.base import BaseEndpoint
from ABConnect.api.routes import SCHEMA


class NotificationsEndpoint(BaseEndpoint):
    """Notifications API endpoint operations.

    Handles all API operations for /api/notifications/* endpoints.
    Total endpoints: 1
    """

    api_path = "notifications"
    routes = SCHEMA["NOTIFICATIONS"]

    def get_get(self) -> dict:
        """GET /api/notifications

        Returns:
            dict: API response data
        """
        route = self.routes['GET']
        return self._make_request(route)
