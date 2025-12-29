"""Commodity API endpoints.

New in API version 709.
Provides endpoints for managing commodities (HS codes, tariff classifications).
"""

from typing import List, Optional, Dict, Any
from ABConnect.api.endpoints.base import BaseEndpoint


class CommodityEndpoint(BaseEndpoint):
    """Commodity API endpoint operations.

    .. versionadded:: 709

    Handles all API operations for /api/commodity/* endpoints.
    Total endpoints: 5
    """

    api_path = "commodity"

    def post_create(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """POST /api/commodity

        Create a new commodity.

        Args:
            data: Commodity data (CommodityDetails model)

        Returns:
            Dict[str, Any]: Created commodity data
        """
        path = "/"
        kwargs: Dict[str, Any] = {"json": data}
        return self._make_request("POST", path, **kwargs)

    def get_get(self, id: str) -> Dict[str, Any]:
        """GET /api/commodity/{id}

        Get a commodity by ID.

        Args:
            id: Commodity UUID

        Returns:
            Dict[str, Any]: Commodity data (CommodityWithParents model)
        """
        path = f"/{id}"
        return self._make_request("GET", path)

    def put_update(self, id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """PUT /api/commodity/{id}

        Update an existing commodity.

        Args:
            id: Commodity UUID
            data: Updated commodity data (CommodityDetails model)

        Returns:
            Dict[str, Any]: Updated commodity data
        """
        path = f"/{id}"
        kwargs: Dict[str, Any] = {"json": data}
        return self._make_request("PUT", path, **kwargs)

    def post_search(self, data: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """POST /api/commodity/search

        Search for commodities.

        Args:
            data: Search criteria

        Returns:
            List[Dict[str, Any]]: List of matching commodities
        """
        path = "/search"
        kwargs: Dict[str, Any] = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)

    def post_suggestions(
        self, data: Optional[Dict[str, Any]] = None
    ) -> List[Dict[str, Any]]:
        """POST /api/commodity/suggestions

        Get commodity suggestions based on input.

        Args:
            data: Suggestion request data

        Returns:
            List[Dict[str, Any]]: List of suggested commodities
        """
        path = "/suggestions"
        kwargs: Dict[str, Any] = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
