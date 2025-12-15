"""Bulk operations endpoint for Catalog API."""

from .base import BaseCatalogEndpoint
from ...models.catalog import BulkInsertRequest


class BulkEndpoint(BaseCatalogEndpoint):
    """Bulk operations endpoints.

    Endpoints:
        POST /api/Bulk/insert - Bulk insert catalogs, lots, and sellers
    """

    api_path = "api/Bulk"

    def insert(self, data: BulkInsertRequest) -> None:
        """Bulk insert catalogs, lots, and sellers.

        This endpoint allows inserting multiple catalogs with their
        associated lots and sellers in a single request.

        Args:
            data: Bulk insert request containing catalogs, lots, and sellers
        """
        self._post("insert", json=data.model_dump(by_alias=True, exclude_none=True, mode="json"))
