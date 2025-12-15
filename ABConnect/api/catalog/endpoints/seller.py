"""Seller endpoint for Catalog API."""

from typing import Optional

from .base import BaseCatalogEndpoint
from ...models.catalog import (
    SellerDto,
    SellerExpandedDto,
    SellerExpandedDtoPaginatedList,
    AddSellerRequest,
    UpdateSellerRequest,
)


class SellerEndpoint(BaseCatalogEndpoint):
    """Seller management endpoints.

    Endpoints:
        GET    /api/Seller       - List sellers (paginated)
        POST   /api/Seller       - Create seller
        GET    /api/Seller/{id}  - Get seller by ID
        PUT    /api/Seller/{id}  - Update seller
        DELETE /api/Seller/{id}  - Delete seller
    """

    api_path = "api/Seller"

    def list(
        self,
        page_number: int = 1,
        page_size: int = 10,
        **kwargs,
    ) -> SellerExpandedDtoPaginatedList:
        """List sellers with pagination.

        Args:
            page_number: Page number (1-indexed)
            page_size: Number of items per page

        Returns:
            Paginated list of sellers with their catalogs
        """
        params = {
            "PageNumber": page_number,
            "PageSize": page_size,
            **kwargs,
        }
        response = self._get(params=params)
        return SellerExpandedDtoPaginatedList.model_validate(response)

    def get(self, seller_id: int) -> SellerExpandedDto:
        """Get seller by ID.

        Args:
            seller_id: Seller ID

        Returns:
            Seller with associated catalogs
        """
        response = self._get(str(seller_id))
        return SellerExpandedDto.model_validate(response)

    def create(self, data: AddSellerRequest) -> SellerDto:
        """Create a new seller.

        Args:
            data: Seller creation data

        Returns:
            Created seller
        """
        response = self._post(json=data.model_dump(by_alias=True, exclude_none=True))
        return SellerDto.model_validate(response)

    def update(self, seller_id: int, data: UpdateSellerRequest) -> SellerDto:
        """Update an existing seller.

        Args:
            seller_id: Seller ID
            data: Seller update data

        Returns:
            Updated seller
        """
        response = self._put(str(seller_id), json=data.model_dump(by_alias=True, exclude_none=True))
        return SellerDto.model_validate(response)

    def delete(self, seller_id: int) -> None:
        """Delete a seller.

        Args:
            seller_id: Seller ID
        """
        self._delete(str(seller_id))
