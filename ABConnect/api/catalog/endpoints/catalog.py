"""Catalog endpoint for Catalog API."""

from typing import Dict, List, Optional, Any

from .base import BaseCatalogEndpoint
from ...models.catalog import (
    CatalogExpandedDto,
    CatalogExpandedDtoPaginatedList,
    CatalogWithSellersDto,
    AddCatalogRequest,
    UpdateCatalogRequest,
)


class CatalogEndpoint(BaseCatalogEndpoint):
    """Catalog management endpoints.

    Endpoints:
        GET    /api/Catalog       - List catalogs (paginated)
        POST   /api/Catalog       - Create catalog
        GET    /api/Catalog/{id}  - Get catalog by ID
        PUT    /api/Catalog/{id}  - Update catalog
        DELETE /api/Catalog/{id}  - Delete catalog
    """

    api_path = "api/Catalog"

    def list(
        self,
        page_number: int = 1,
        page_size: int = 10,
        **kwargs,
    ) -> CatalogExpandedDtoPaginatedList:
        """List catalogs with pagination.

        Args:
            page_number: Page number (1-indexed)
            page_size: Number of items per page

        Returns:
            Paginated list of catalogs
        """
        params = {
            "PageNumber": page_number,
            "PageSize": page_size,
            **kwargs,
        }
        response = self._get(params=params)
        return CatalogExpandedDtoPaginatedList.model_validate(response)

    def get(self, catalog_id: int) -> CatalogExpandedDto:
        """Get catalog by ID.

        Args:
            catalog_id: Catalog ID

        Returns:
            Catalog with sellers and lots
        """
        response = self._get(str(catalog_id))
        return CatalogExpandedDto.model_validate(response)

    def create(self, data: AddCatalogRequest) -> CatalogWithSellersDto:
        """Create a new catalog.

        Args:
            data: Catalog creation data

        Returns:
            Created catalog with sellers
        """
        response = self._post(json=data.model_dump(by_alias=True, exclude_none=True))
        return CatalogWithSellersDto.model_validate(response)

    def update(self, catalog_id: int, data: UpdateCatalogRequest) -> CatalogWithSellersDto:
        """Update an existing catalog.

        Args:
            catalog_id: Catalog ID
            data: Catalog update data

        Returns:
            Updated catalog with sellers
        """
        response = self._put(str(catalog_id), json=data.model_dump(by_alias=True, exclude_none=True))
        return CatalogWithSellersDto.model_validate(response)

    def delete(self, catalog_id: int) -> None:
        """Delete a catalog.

        Args:
            catalog_id: Catalog ID
        """
        self._delete(str(catalog_id))
