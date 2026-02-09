"""
ItemsHelper Examples - Convenient item access with automatic Pydantic casting

This module shows how to use the ItemsHelper class which provides
convenient methods to fetch and cast items with Pydantic models.

Usage:
    python items_helper.py              # Run all examples
    python items_helper.py parcel       # Run a single example
    python items_helper.py help         # List available examples
"""

from _base import ExampleRunner


PARCEL_JOB_ID = 4675060
FREIGHT_JOB_ID = 4637814


class ItemsHelperExamples(ExampleRunner):
    def __init__(self):
        super().__init__("ItemsHelper API")
        self.add("parcel", "Parcel items via ItemsHelper", self.parcel_items)
        self.add("freight", "Freight items via ItemsHelper", self.freight_items)
        self.add("calendar", "Calendar/job items via ItemsHelper", self.calendar_items)
        self.add("delete", "Logged delete parcel items (docs only)", self.delete_docs)
        self.add("replace", "Replace parcel items (docs only)", self.replace_docs)
        self.add("comparison", "Old vs new approach comparison", self.comparison)

    def parcel_items(self):
        print("PARCEL ITEMS (Parcel Shipping)")
        print("  Access: api.jobs.items.parcelitems(job_id)")
        print("  Returns: List[ParcelItem]\n")

        parcel_items = self.api.jobs.items.parcelitems(PARCEL_JOB_ID)
        print(f"  Found {len(parcel_items)} parcel item(s) for job {PARCEL_JOB_ID}")
        if parcel_items:
            item = parcel_items[0]
            print(f"  Description: {item.description or 'N/A'}")
            print(f"  Dimensions: {item.job_item_pkd_length} x {item.job_item_pkd_width} x {item.job_item_pkd_height}")
            print(f"  Weight: {item.job_item_pkd_weight} lbs")
            print(f"  Package Type Code: {item.package_type_code}")

    def freight_items(self):
        print("FREIGHT ITEMS (Freight Shipping with NMFC)")
        print("  Access: api.jobs.items.freightitems(job_id)")
        print("  Returns: List[FreightShimpment]\n")

        freight_items = self.api.jobs.items.freightitems(FREIGHT_JOB_ID)
        print(f"  Found {len(freight_items)} freight item(s) for job {FREIGHT_JOB_ID}")
        if freight_items:
            item = freight_items[0]
            print(f"  Freight Class: {item.freight_item_class}")
            print(f"  NMFC Item: {item.nmfc_item}")
            print(f"  Cube: {item.cube} cu ft")
            print(f"  Quantity: {item.quantity}")
            if item.bol_description:
                desc = item.bol_description[:50] + "..." if len(item.bol_description) > 50 else item.bol_description
                print(f"  BOL Description: {desc}")

    def calendar_items(self):
        print("JOB/CALENDAR ITEMS (General Calendar View)")
        print("  Access: api.jobs.items.jobitems(job_id)")
        print("  Returns: List[CalendarItem]\n")

        job_items = self.api.jobs.items.jobitems(FREIGHT_JOB_ID)
        print(f"  Found {len(job_items)} calendar item(s) for job {FREIGHT_JOB_ID}")
        if job_items:
            for idx, item in enumerate(job_items[:3], 1):
                print(f"  Item {idx}: {item.name}")
                print(f"          {item.weight} lbs, ${item.value}")
            if len(job_items) > 3:
                print(f"  ... and {len(job_items) - 3} more items")

    def delete_docs(self):
        print("DELETE PARCEL ITEMS WITH LOGGING")
        print("  Access: api.jobs.items.logged_delete_parcel_items(job_id)")
        print("  Returns: bool (success/failure)\n")
        print("  Usage:")
        print(f"    success = api.jobs.items.logged_delete_parcel_items({PARCEL_JOB_ID})")
        print("    if success:")
        print("        print('Parcel items deleted and logged')")
        print("\n  Note format: 'User deleted parcel items [2 Box 10x5x3 25lbs, ...]'")

    def replace_docs(self):
        print("REPLACE PARCEL ITEMS")
        print("  Access: api.jobs.items.replace_parcels(job_id, new_items)")
        print("  Returns: bool (success/failure)\n")
        print("  Usage:")
        print("    from ABConnect.api.models.jobparcelitems import ParcelItem")
        print("    new_items = [ParcelItem(description='Box 1', quantity=2, ...)]")
        print(f"    success = api.jobs.items.replace_parcels({PARCEL_JOB_ID}, new_items)")

    def comparison(self):
        print("OLD WAY (Manual casting required):")
        print("  response = api.jobs.parcelitems.get_parcelitems(jobDisplayId='123')")
        print("  items_data = response['parcelItems'] if 'parcelItems' in response else response")
        print("  items = [ParcelItem(**item) for item in items_data]")
        print()
        print("NEW WAY (Automatic casting):")
        print("  items = api.jobs.items.parcelitems(123)")


if __name__ == "__main__":
    ItemsHelperExamples().run()
