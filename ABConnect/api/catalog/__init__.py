"""Catalog API client package.

Provides access to the Catalog service API (catalog-api.abconnect.co).
Uses the same identity token as ACPortal API.

Example:
    >>> from ABConnect.api import ABConnectAPI
    >>> api = ABConnectAPI()
    >>>
    >>> # List catalogs
    >>> catalogs = api.catalog.catalogs.list()
    >>>
    >>> # Create a new catalog
    >>> from ABConnect.api.models.catalog import AddCatalogRequest
    >>> from datetime import datetime
    >>> request = AddCatalogRequest(
    ...     customer_catalog_id="CAT-001",
    ...     title="My Catalog",
    ...     start_date=datetime.now(),
    ...     end_date=datetime.now(),
    ... )
    >>> catalog = api.catalog.catalogs.create(request)
"""

from .http_client import CatalogRequestHandler
from .endpoints import (
    BaseCatalogEndpoint,
    CatalogEndpoint,
    LotEndpoint,
    SellerEndpoint,
    BulkEndpoint,
)


class CatalogAPI:
    """Catalog API client.

    Provides access to Catalog service endpoints:
        - catalogs: Catalog management
        - lots: Lot management
        - sellers: Seller management
        - bulk: Bulk operations

    This client shares token storage with ACPortal API, so authentication
    is handled by the parent ABConnectAPI client.

    Attributes:
        catalogs: Catalog management endpoints
        lots: Lot management endpoints
        sellers: Seller management endpoints
        bulk: Bulk operation endpoints
    """

    def __init__(self, token_storage):
        """Initialize the Catalog API client.

        Args:
            token_storage: Token storage instance (shared with ACPortal)
        """
        # Create catalog-specific request handler
        self._handler = CatalogRequestHandler(token_storage)

        # Set handler for all catalog endpoints
        BaseCatalogEndpoint.set_request_handler(self._handler)

        # Initialize endpoints
        self.catalogs = CatalogEndpoint()
        self.lots = LotEndpoint()
        self.sellers = SellerEndpoint()
        self.bulk = BulkEndpoint()


__all__ = [
    'CatalogAPI',
    'CatalogRequestHandler',
    'BaseCatalogEndpoint',
    'CatalogEndpoint',
    'LotEndpoint',
    'SellerEndpoint',
    'BulkEndpoint',
]
