"""Lot endpoint for Catalog API."""

from typing import List, Optional

from .base import BaseCatalogEndpoint
from ...models.catalog import (
    LotDto,
    LotDtoPaginatedList,
    LotOverrideDto,
    AddLotRequest,
    UpdateLotRequest,
    GetLotsOverridesQuery,
)


class LotEndpoint(BaseCatalogEndpoint):
    """Lot management endpoints.

    Endpoints:
        GET    /api/Lot              - List lots (paginated)
        POST   /api/Lot              - Create lot
        GET    /api/Lot/{id}         - Get lot by ID
        PUT    /api/Lot/{id}         - Update lot
        DELETE /api/Lot/{id}         - Delete lot
        POST   /api/Lot/get-overrides - Get lot overrides
    """

    api_path = "api/Lot"

    def list(
        self,
        page_number: int = 1,
        page_size: int = 10,
        customer_catalog_id: Optional[str] = None,
        **kwargs,
    ) -> LotDtoPaginatedList:
        """List lots with pagination.

        Args:
            page_number: Page number (1-indexed)
            page_size: Number of items per page
            customer_catalog_id: Filter by customer catalog ID (e.g., "400160")

        Returns:
            Paginated list of lots
        """
        params = {
            "PageNumber": page_number,
            "PageSize": page_size,
            **kwargs,
        }
        if customer_catalog_id is not None:
            params["CustomerCatalogId"] = customer_catalog_id
        response = self._get(params=params)
        return LotDtoPaginatedList.model_validate(response)

    def get(self, lot_id: int) -> LotDto:
        """Get lot by ID.

        Args:
            lot_id: Lot ID

        Returns:
            Lot data
        """
        response = self._get(str(lot_id))
        return LotDto.model_validate(response)

    def create(self, data: AddLotRequest) -> LotDto:
        """Create a new lot.

        Args:
            data: Lot creation data

        Returns:
            Created lot
        """
        response = self._post(json=data.model_dump(by_alias=True, exclude_none=True, mode="json"))
        return LotDto.model_validate(response)

    def update(self, lot_id: int, data: UpdateLotRequest) -> LotDto:
        """Update an existing lot.

        Args:
            lot_id: Lot ID
            data: Lot update data

        Returns:
            Updated lot
        """
        response = self._put(str(lot_id), json=data.model_dump(by_alias=True, exclude_none=True, mode="json"))
        return LotDto.model_validate(response)

    def delete(self, lot_id: int) -> None:
        """Delete a lot.

        Args:
            lot_id: Lot ID
        """
        self._delete(str(lot_id))

    def get_overrides(self, query: GetLotsOverridesQuery) -> List[LotOverrideDto]:
        """Get lot overrides based on query criteria.

        Args:
            query: Query parameters for filtering overrides

        Returns:
            List of lot overrides
        """
        response = self._post(
            "get-overrides",
            json=query.model_dump(by_alias=True, exclude_none=True)
        )
        return [LotOverrideDto.model_validate(item) for item in response]
