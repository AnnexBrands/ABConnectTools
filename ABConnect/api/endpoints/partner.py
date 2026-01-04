"""Partner API endpoints.

New in API version 709.
Provides endpoints for managing partners.
"""

from typing import List, Optional, Dict, Any
from ABConnect.api.endpoints.base import BaseEndpoint
from ABConnect.api.routes import SCHEMA


class PartnerEndpoint(BaseEndpoint):
    """Partner API endpoint operations.

    .. versionadded:: 709

    Handles all API operations for /api/partner/* endpoints.
    Total endpoints: 3
    """

    api_path = "partner"
    routes = SCHEMA["PARTNER"]

    def get_list(self) -> List[Dict[str, Any]]:
        """GET /api/partner

        Get list of all partners.

        Returns:
            List[Dict[str, Any]]: List of partners
        """
        route = self.routes['GET']
        return self._make_request(route)

    def get_get(self, id: str) -> Dict[str, Any]:
        """GET /api/partner/{id}

        Get a partner by ID.

        Args:
            id: Partner UUID

        Returns:
            Dict[str, Any]: Partner data
        """
        route = self.routes['GET']
        route.params = {"id": id}
        return self._make_request(route)

    def post_search(self, data: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """POST /api/partner/search

        Search for partners.

        Args:
            data: Search criteria

        Returns:
            List[Dict[str, Any]]: List of matching partners (PartnerServiceResponse)
        """
        route = self.routes['POST_SEARCH']
        kwargs: Dict[str, Any] = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)
