"""Catalog API bulk loader.

Production-ready loader for catalog data from spreadsheets.
Transforms flat rows into nested BulkInsertRequest with complete data:
- Catalogs with sellers
- Lots with initial_data, overriden_data, and image_links

Expected spreadsheet columns:
    House ID, House Name        -> Seller
    Catalog ID, Catalog Title   -> Catalog
    Catalog Start Date          -> Catalog dates
    Lot ID, Lot Num, Lot Title  -> Lot identification
    Lot Description             -> noted_conditions
    Fragility                   -> cpack (nf=1, lf=2, f=3, vf=4)
    Shipping Height/Width/Depth -> Dimensions (with Dimension Type)
    Shipping Weight             -> Weight (with Weight Type)
    Shipping Quantity           -> Quantity
    Crate                       -> force_crate (ct=True)
"""

from pathlib import Path
from datetime import datetime, timedelta
from collections import defaultdict
from typing import Optional

from ABConnect import ABConnectAPI, FileLoader
from ABConnect.api.models.catalog import (
    BulkInsertRequest,
    BulkInsertCatalogRequest,
    BulkInsertSellerRequest,
    BulkInsertLotRequest,
    LotDataDto,
)


# =============================================================================
# Configuration
# =============================================================================

CPACK_MAP = {"nf": "1", "lf": "2", "f": "3", "vf": "4", "pbo": "pbo"}
DEFAULT_CPACK = "3"
DEFAULT_AGENT = "DLC"
IMAGE_URL_TEMPLATE = "https://s3.amazonaws.com/static2.liveauctioneers.com/{house_id}/{catalog_id}/{lot_id}_1_m.jpg"


# =============================================================================
# Converters
# =============================================================================


def parse_datetime(value) -> datetime:
    """Parse datetime from various formats."""
    if isinstance(value, datetime):
        return value
    if isinstance(value, str):
        for fmt in ["%Y-%m-%d %H:%M:%S", "%Y-%m-%d", "%m/%d/%Y", "%m/%d/%Y %H:%M"]:
            try:
                return datetime.strptime(value, fmt)
            except ValueError:
                continue
    raise ValueError(f"Cannot parse datetime: {value}")


def ensure_future(dt: datetime) -> datetime:
    """Ensure datetime is in the future by adding 1 year if needed."""
    now = datetime.now()
    if dt <= now:
        return dt.replace(year=dt.year + 1)
    return dt


def to_float(value, default: float = 0.0) -> float:
    """Safely convert to float."""
    if value is None or value == "":
        return default
    try:
        return float(value)
    except (ValueError, TypeError):
        return default


def to_int(value, default: int = 1) -> int:
    """Safely convert to int."""
    if value is None or value == "":
        return default
    try:
        return int(float(value))
    except (ValueError, TypeError):
        return default


def convert_dimensions(value: float, dim_type: str) -> float:
    """Convert dimensions to inches."""
    conversions = {"in": 1.0, "cm": 1 / 2.54, "mm": 1 / 25.4}
    return value * conversions.get(dim_type, 1.0)


def convert_weight(value: float, weight_type: str) -> float:
    """Convert weight to pounds."""
    conversions = {"lb": 1.0, "kg": 2.20462, "oz": 1 / 16}
    return value * conversions.get(weight_type, 1.0)


def convert_cpack(value: str) -> str:
    """Convert fragility code to cpack value."""
    if not value:
        return DEFAULT_CPACK
    return CPACK_MAP.get(value.lower().strip(), DEFAULT_CPACK)


def build_image_url(house_id: int, catalog_id: int, lot_id: int) -> str:
    """Build image URL from IDs."""
    return IMAGE_URL_TEMPLATE.format(
        house_id=house_id, catalog_id=catalog_id, lot_id=lot_id
    )


# =============================================================================
# Data Builder
# =============================================================================


class CatalogDataBuilder:
    """Builds BulkInsertRequest from spreadsheet rows."""

    def __init__(self, agent: str = DEFAULT_AGENT):
        self.agent = agent
        self.catalogs_data: dict[int, dict] = {}
        self.catalog_sellers: dict[int, dict[int, dict]] = defaultdict(dict)
        self.catalog_lots: dict[int, list] = defaultdict(list)

    def add_row(self, row: dict) -> None:
        """Process a single spreadsheet row."""
        catalog_id = to_int(row["Catalog ID"])
        seller_id = to_int(row["House ID"])

        self._add_catalog(catalog_id, row)
        self._add_seller(catalog_id, seller_id, row)
        self._add_lot(catalog_id, seller_id, row)

    def _add_catalog(self, catalog_id: int, row: dict) -> None:
        """Add or update catalog data."""
        if catalog_id in self.catalogs_data:
            return

        start_date = ensure_future(parse_datetime(row["Catalog Start Date"]))
        end_date = start_date + timedelta(hours=1)

        self.catalogs_data[catalog_id] = {
            "customer_catalog_id": str(catalog_id),
            "title": row.get("Catalog Title", ""),
            "start_date": start_date,
            "end_date": end_date,
            "agent": row.get("Agent", self.agent),
        }

    def _add_seller(self, catalog_id: int, seller_id: int, row: dict) -> None:
        """Add unique seller to catalog."""
        if seller_id in self.catalog_sellers[catalog_id]:
            return

        self.catalog_sellers[catalog_id][seller_id] = {
            "customer_display_id": seller_id,
            "name": row.get("House Name"),
            "is_active": True,
        }

    def _add_lot(self, catalog_id: int, seller_id: int, row: dict) -> None:
        """Add lot with complete data."""
        # Parse identifiers
        lot_id = to_int(row["Lot ID"])
        lot_number = str(row.get("Lot Num", "")).strip()
        lot_title = row.get("Lot Title", "")
        lot_description = row.get("Lot Description", "")

        # Parse dimensions
        dim_type = row.get("Shipping Dimension Type", "in")
        weight_type = row.get("Shipping Weight Type", "lb")

        h = convert_dimensions(to_float(row.get("Shipping Height")), dim_type)
        w = convert_dimensions(to_float(row.get("Shipping Width")), dim_type)
        l = convert_dimensions(to_float(row.get("Shipping Depth")), dim_type)
        wgt = convert_weight(to_float(row.get("Shipping Weight")), weight_type)
        qty = to_int(row.get("Shipping Quantity"), 1)

        # Parse flags
        fragility = row.get("Fragility", "f")
        cpack = convert_cpack(fragility)
        force_crate = str(row.get("Crate", "")).lower() == "ct"

        # Build description with lot number prefix
        description = f"{lot_number} {lot_title}".strip()

        # Build initial_data (raw dimensions only)
        initial_data = LotDataDto(
            qty=qty,
            h=h,
            w=w,
            l=l,
            wgt=wgt,
            cpack=cpack,
            description=description,
            notes=lot_description,
            force_crate=force_crate,
        )

        # Build override_data (with cpack, noted_conditions, description)
        override_data = LotDataDto(
            qty=qty,
            h=h,
            w=w,
            l=l,
            wgt=wgt,
            cpack=cpack,
            description=description,
            notes=lot_description,
            force_crate=force_crate,
        )

        # Build image link
        image_url = build_image_url(seller_id, catalog_id, lot_id)

        # Create lot request
        lot = BulkInsertLotRequest(
            customer_item_id=str(lot_id),
            lot_number=lot_number,
            initial_data=initial_data,
            overriden_data=[override_data],
            image_links=[image_url],
        )

        self.catalog_lots[catalog_id].append(lot)

    def build(self) -> BulkInsertRequest:
        """Build final BulkInsertRequest."""
        catalogs = []

        for catalog_id, cat_data in self.catalogs_data.items():
            sellers = [
                BulkInsertSellerRequest(**s)
                for s in self.catalog_sellers[catalog_id].values()
            ]

            catalog = BulkInsertCatalogRequest(
                customer_catalog_id=cat_data["customer_catalog_id"],
                title=cat_data["title"],
                start_date=cat_data["start_date"],
                end_date=cat_data["end_date"],
                agent=cat_data["agent"],
                sellers=sellers,
                lots=self.catalog_lots[catalog_id],
            )
            catalogs.append(catalog)

        return BulkInsertRequest(catalogs=catalogs)

    def summary(self) -> str:
        """Return summary of built data."""
        lines = [f"Catalogs: {len(self.catalogs_data)}"]
        for catalog_id, cat_data in self.catalogs_data.items():
            sellers = len(self.catalog_sellers[catalog_id])
            lots = len(self.catalog_lots[catalog_id])
            lines.append(f"  {catalog_id}: {cat_data['title'][:40]}")
            lines.append(f"    Sellers: {sellers}, Lots: {lots}")
        return "\n".join(lines)


# =============================================================================
# Main Functions
# =============================================================================


def load_catalog(
    file_path: str | Path, agent: str = DEFAULT_AGENT, dry_run: bool = False
) -> BulkInsertRequest:
    """Load catalog data from spreadsheet and insert via API.

    Args:
        file_path: Path to spreadsheet (xlsx, csv, json)
        agent: Default agent code for catalogs
        dry_run: If True, build request but don't send to API

    Returns:
        BulkInsertRequest that was sent (or would be sent if dry_run)
    """
    # Load data
    path = Path(file_path)
    print(f"Loading: {path.name}")
    data = FileLoader(path.as_posix()).data
    print(f"Rows: {len(data)}")

    # Build request
    builder = CatalogDataBuilder(agent=agent)
    for row in data:
        builder.add_row(row)

    request = builder.build()
    print(f"\n{builder.summary()}")

    # Send to API
    if dry_run:
        print("\n[DRY RUN] Skipping API call")
    else:
        print("\nSending to API...")
        api = ABConnectAPI()
        api.catalog.bulk.insert(request)
        print("Done!")

    return request


def main():
    """Example usage."""
    import sys

    # Check for dry-run flag
    dry_run = "--dry-run" in sys.argv or "-n" in sys.argv

    # Get positional arguments (exclude flags)
    args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]

    # Default file or from command line
    if args:
        file_path = args[0]
    else:
        file_path = Path.cwd() / "examples" / "shipping-info-400160.xlsx"

    load_catalog(file_path, dry_run=dry_run)


if __name__ == "__main__":
    main()
