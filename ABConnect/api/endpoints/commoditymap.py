"""Commodity Map API endpoints.

New in API version 709.
Provides endpoints for managing commodity mappings between items and HS codes.
"""

from typing import List, Optional, Dict, Any
from ABConnect.api.endpoints.base import BaseEndpoint


class CommodityMapEndpoint(BaseEndpoint):
    """CommodityMap API endpoint operations.

    .. versionadded:: 709

    Handles all API operations for /api/commodity-map/* endpoints.
    Total endpoints: 5
    """

    api_path = "commodity-map"

    def post_create(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """POST /api/commodity-map

        Create a new commodity mapping.

        Args:
            data: Commodity mapping data (CommodityMapDetails model)

        Returns:
            Dict[str, Any]: Created commodity mapping data
        """
        path = "/"
        kwargs: Dict[str, Any] = {"json": data}
        return self._make_request("POST", path, **kwargs)

    def get_get(self, id: str) -> Dict[str, Any]:
        """GET /api/commodity-map/{id}

        Get a commodity mapping by ID.

        Args:
            id: Commodity map UUID

        Returns:
            Dict[str, Any]: Commodity mapping data
        """
        path = f"/{id}"
        return self._make_request("GET", path)

    def put_update(self, id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """PUT /api/commodity-map/{id}

        Update an existing commodity mapping.

        Args:
            id: Commodity map UUID
            data: Updated mapping data (CommodityMapDetails model)

        Returns:
            Dict[str, Any]: Updated commodity mapping data
        """
        path = f"/{id}"
        kwargs: Dict[str, Any] = {"json": data}
        return self._make_request("PUT", path, **kwargs)

    def delete_delete(self, id: str) -> Dict[str, Any]:
        """DELETE /api/commodity-map/{id}

        Delete a commodity mapping.

        Args:
            id: Commodity map UUID to delete

        Returns:
            Dict[str, Any]: Deletion response
        """
        path = f"/{id}"
        return self._make_request("DELETE", path)

    def post_search(self, data: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """POST /api/commodity-map/search

        Search for commodity mappings.

        Args:
            data: Search criteria

        Returns:
            List[Dict[str, Any]]: List of matching commodity mappings
        """
        path = "/search"
        kwargs: Dict[str, Any] = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
