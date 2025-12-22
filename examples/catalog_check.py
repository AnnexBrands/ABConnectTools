"""Catalog data checker - view catalog data from server.

Usage:
    python examples/catalog_check.py 400160
"""

import sys

from ABConnect import ABConnectAPI


def check_catalog(catalog_number: str) -> None:
    """Display catalog data from server."""
    api = ABConnectAPI()

    # Search for catalog by customer_catalog_id
    print(f"Searching for catalog: {catalog_number}")
    result = api.catalog.catalogs.list(CustomerCatalogId=catalog_number)

    if not result.items:
        print(f"Catalog {catalog_number} not found")
        return

    catalog = result.items[0]
    print(f"\nCatalog: {catalog.title}")
    print(f"  ID: {catalog.id} (Customer ID: {catalog.customer_catalog_id})")
    print(f"  Agent: {catalog.agent}")
    print(f"  Start: {catalog.start_date}")
    print(f"  End: {catalog.end_date}")
    print(f"  Completed: {catalog.is_completed}")

    # Show sellers
    if catalog.sellers:
        print(f"\nSellers ({len(catalog.sellers)}):")
        for seller in catalog.sellers:
            print(f"  {seller.name} (ID: {seller.customer_display_id})")

    # Fetch lots for this catalog
    # Note: API doesn't support server-side filtering, must filter client-side
    print(f"\nFetching lots...")
    all_lots = []
    page = 1
    while True:
        lots_result = api.catalog.lots.list(page_number=page, page_size=100)
        for lot in lots_result.items:
            if any(c.catalog_id == catalog.id for c in lot.catalogs):
                all_lots.append(lot)
        if not lots_result.has_next_page:
            break
        page += 1

    print(f"Lots ({len(all_lots)}):\n")

    # Header
    print(
        f"{'Lot #':<8} {'Item ID':<12} {'L':>6} {'W':>6} {'H':>6} {'Wgt':>6} {'CPack':>5}  Description"
    )
    print("-" * 90)

    for lot in all_lots:
        # Get lot number from catalogs association
        lot_num = ""
        for cat in lot.catalogs:
            if cat.catalog_id == catalog.id:
                lot_num = cat.lot_number
                break

        # Use initial_data for dimensions
        data = lot.initial_data
        desc = (data.description or "")[:30]

        print(
            f"{lot_num:<8} "
            f"{lot.customer_item_id or '':<12} "
            f"{data.l or 0:>6.1f} "
            f"{data.w or 0:>6.1f} "
            f"{data.h or 0:>6.1f} "
            f"{data.wgt or 0:>6.1f} "
            f"{data.cpack or '':>5}  "
            f"{desc}"
        )

    # Summary
    print(f"\n{'=' * 90}")
    print(f"Total: {len(all_lots)} lot(s)")


def main():
    if len(sys.argv) < 2:
        print("Usage: python examples/catalog_check.py <catalog_number>")
        print("Example: python examples/catalog_check.py 400160")
        sys.exit(1)

    check_catalog(sys.argv[1])


if __name__ == "__main__":
    main()
