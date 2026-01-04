"""Values API endpoints.

Auto-generated from swagger.json specification.
Provides type-safe access to Values/* endpoints.
"""

from typing import Optional
from ABConnect.api.endpoints.base import BaseEndpoint
from ABConnect.api.routes import SCHEMA


class ValuesEndpoint(BaseEndpoint):
    """Values API endpoint operations.

    Handles all API operations for /api/Values/* endpoints.
    Total endpoints: 1
    """

    api_path = "Values"
    routes = SCHEMA["VALUES"]

    def get_get(self, code: Optional[str] = None) -> dict:
        """GET /api/Values

        Returns:
            dict: API response data
        """
        route = self.routes['GET']
        if code is not None:
            route.params = {"code": code}
        return self._make_request(route)
