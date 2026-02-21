"""
Catalog API Examples - Catalogs, sellers, and lots

Usage:
    python catalog_api.py               # Run all examples
    python catalog_api.py catalogs      # Run a single example
    python catalog_api.py help          # List available examples
"""

from _base import ExampleRunner
from _helpers import save_fixture


class CatalogApiExamples(ExampleRunner):
    def __init__(self):
        super().__init__("Catalog API", api_kwargs=dict(env='staging', username='instaquote'))
        self.add("catalogs", "List catalogs (paginated)", self.list_catalogs)
        self.add("sellers", "List sellers (paginated)", self.list_sellers)
        self.add("lots", "List lots (paginated)", self.list_lots)

    def list_catalogs(self):
        result = self.api.catalog.catalogs.list()
        print(f"Catalogs type: {type(result)}")
        print(f"Total items: {result.total_items}")
        print(f"Page {result.page_number} of {result.total_pages}")
        print(f"Items on page: {len(result.items)}")
        save_fixture(result, "CatalogList")

    def list_sellers(self):
        result = self.api.catalog.sellers.list()
        print(f"Sellers type: {type(result)}")
        print(f"Total items: {result.total_items}")
        print(f"Page {result.page_number} of {result.total_pages}")
        print(f"Items on page: {len(result.items)}")
        save_fixture(result, "CatalogSellerList")

    def list_lots(self):
        result = self.api.catalog.lots.list()
        print(f"Lots type: {type(result)}")
        print(f"Total items: {result.total_items}")
        print(f"Page {result.page_number} of {result.total_pages}")
        print(f"Items on page: {len(result.items)}")
        save_fixture(result, "CatalogLotList")


if __name__ == "__main__":
    CatalogApiExamples().run()
