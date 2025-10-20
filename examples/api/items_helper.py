"""Example demonstrating the ItemsHelper for easy item access.

This module shows how to use the ItemsHelper class which provides
convenient methods to fetch and cast items with Pydantic models.
"""

from ABConnect.api import ABConnectAPI

# Job IDs for examples
PARCEL_JOB_ID = 4675060
FREIGHT_JOB_ID = 4637814


def demonstrate_items_helper():
    """Demonstrate all ItemsHelper methods."""

    # Initialize API
    api = ABConnectAPI()

    print("=== ItemsHelper Examples ===\n")
    print("The ItemsHelper provides convenient access to different item types")
    print("with automatic Pydantic model casting for type safety.\n")

    # Example 1: Parcel Items
    print("1. PARCEL ITEMS (Parcel Shipping)")
    print("   Access: api.jobs.items.parcelitems(job_id)")
    print("   Returns: List[ParcelItem]\n")

    parcel_items = api.jobs.items.parcelitems(PARCEL_JOB_ID)
    print(f"   Found {len(parcel_items)} parcel item(s) for job {PARCEL_JOB_ID}")

    if parcel_items:
        item = parcel_items[0]
        print(f"   • Description: {item.description or 'N/A'}")
        print(f"   • Dimensions: {item.job_item_pkd_length} × {item.job_item_pkd_width} × {item.job_item_pkd_height}")
        print(f"   • Weight: {item.job_item_pkd_weight} lbs")
        print(f"   • Package Type Code: {item.package_type_code}")
    print()

    # Example 2: Freight Items
    print("2. FREIGHT ITEMS (Freight Shipping with NMFC)")
    print("   Access: api.jobs.items.freightitems(job_id)")
    print("   Returns: List[FreightShimpment]\n")

    freight_items = api.jobs.items.freightitems(FREIGHT_JOB_ID)
    print(f"   Found {len(freight_items)} freight item(s) for job {FREIGHT_JOB_ID}")

    if freight_items:
        item = freight_items[0]
        print(f"   • Freight Class: {item.freight_item_class}")
        print(f"   • NMFC Item: {item.nmfc_item}")
        print(f"   • Cube: {item.cube} cu ft")
        print(f"   • Quantity: {item.quantity}")
        if item.bol_description:
            desc = item.bol_description[:50] + "..." if len(item.bol_description) > 50 else item.bol_description
            print(f"   • BOL Description: {desc}")
    print()

    # Example 3: Job/Calendar Items
    print("3. JOB/CALENDAR ITEMS (General Calendar View)")
    print("   Access: api.jobs.items.jobitems(job_id)")
    print("   Returns: List[CalendarItem]\n")

    job_items = api.jobs.items.jobitems(FREIGHT_JOB_ID)
    print(f"   Found {len(job_items)} calendar item(s) for job {FREIGHT_JOB_ID}")

    if job_items:
        for idx, item in enumerate(job_items[:3], 1):  # Show first 3
            print(f"   Item {idx}: {item.name}")
            print(f"          {item.weight} lbs, ${item.value}")
        if len(job_items) > 3:
            print(f"   ... and {len(job_items) - 3} more items")
    print()

    # Example 4: Logged Delete Parcel Items
    print("4. DELETE PARCEL ITEMS WITH LOGGING")
    print("   Access: api.jobs.items.logged_delete_parcel_items(job_id)")
    print("   Returns: bool (success/failure)\n")
    print("   This method will:")
    print("   • Fetch all parcel items for the job")
    print("   • Create a note logging the deletion with item details")
    print("   • Delete each parcel item")
    print("   • Return True if successful, False otherwise")
    print()
    print("   Example usage:")
    print(f"   success = api.jobs.items.logged_delete_parcel_items({PARCEL_JOB_ID})")
    print("   if success:")
    print("       print('Parcel items deleted and logged')")
    print()
    print("   Note format: 'User deleted parcel items [2 Box 10x5x3 25lbs, ...]'")
    print()

    # Example 5: Replace Parcel Items
    print("5. REPLACE PARCEL ITEMS")
    print("   Access: api.jobs.items.replace_parcels(job_id, new_items)")
    print("   Returns: bool (success/failure)\n")
    print("   This method will:")
    print("   • Delete all existing parcel items with logging")
    print("   • Post new parcel items to the job")
    print("   • Return True if successful, False otherwise")
    print()
    print("   Example usage:")
    print("   from ABConnect.api.models.jobparcelitems import ParcelItem")
    print("   new_items = [")
    print("       ParcelItem(")
    print("           description='Box 1',")
    print("           quantity=2,")
    print("           job_item_pkd_length=10.0,")
    print("           job_item_pkd_width=8.0,")
    print("           job_item_pkd_height=6.0,")
    print("           job_item_pkd_weight=25.0")
    print("       )")
    print("   ]")
    print(f"   success = api.jobs.items.replace_parcels({PARCEL_JOB_ID}, new_items)")
    print("   if success:")
    print("       print('Parcel items replaced successfully')")
    print()

    # Show comparison
    print("=" * 60)
    print("COMPARISON: Old vs New Approach")
    print("=" * 60)
    print()

    print("❌ OLD WAY (Manual casting required):")
    print("   response = api.jobs.parcelitems.get_parcelitems(jobDisplayId='123')")
    print("   items_data = response['parcelItems'] if 'parcelItems' in response else response")
    print("   items = [ParcelItem(**item) for item in items_data]")
    print()

    print("✅ NEW WAY (Automatic casting):")
    print("   items = api.jobs.items.parcelitems(123)")
    print()

    print("Benefits:")
    print("  • Automatic Pydantic model casting")
    print("  • Type-safe item access")
    print("  • Handles response format differences")
    print("  • Cleaner, more readable code")
    print("  • Consistent API across all item types")
    print()


def code_examples():
    """Show code examples for different use cases."""

    print("=" * 60)
    print("CODE EXAMPLES")
    print("=" * 60)
    print()

    print("# Example 1: Get parcel items and calculate total weight")
    print("from ABConnect.api import ABConnectAPI")
    print()
    print("api = ABConnectAPI()")
    print("items = api.jobs.items.parcelitems(4675060)")
    print("total_weight = sum(item.job_item_pkd_weight or 0 for item in items)")
    print("print(f'Total weight: {total_weight} lbs')")
    print()

    print("# Example 2: Get freight items and show NMFC classes")
    print("items = api.jobs.items.freightitems(4637814)")
    print("for item in items:")
    print("    print(f'Class {item.freight_item_class}: {item.nmfc_item}')")
    print()

    print("# Example 3: Get calendar items and calculate total value")
    print("items = api.jobs.items.jobitems(4637814)")
    print("total_value = sum(item.value or 0 for item in items)")
    print("print(f'Total value: ${total_value:,.2f}')")
    print()

    print("# Example 4: List all items with details")
    print("job_id = 4637814")
    print("parcel = api.jobs.items.parcelitems(job_id)")
    print("freight = api.jobs.items.freightitems(job_id)")
    print("calendar = api.jobs.items.jobitems(job_id)")
    print()
    print("print(f'Job {job_id} has:')")
    print("print(f'  {len(parcel)} parcel items')")
    print("print(f'  {len(freight)} freight items')")
    print("print(f'  {len(calendar)} calendar items')")
    print()

    print("# Example 5: Delete all parcel items with logging")
    print("success = api.jobs.items.logged_delete_parcel_items(4675060)")
    print("if success:")
    print("    print('All parcel items deleted and logged successfully')")
    print("else:")
    print("    print('Failed to delete parcel items - check logs')")
    print()

    print("# Example 6: Replace all parcel items with new ones")
    print("from ABConnect.api.models.jobparcelitems import ParcelItem")
    print()
    print("new_items = [")
    print("    ParcelItem(")
    print("        description='Updated Box 1',")
    print("        quantity=3,")
    print("        job_item_pkd_length=12.0,")
    print("        job_item_pkd_width=10.0,")
    print("        job_item_pkd_height=8.0,")
    print("        job_item_pkd_weight=30.0")
    print("    ),")
    print("    ParcelItem(")
    print("        description='Updated Box 2',")
    print("        quantity=1,")
    print("        job_item_pkd_length=15.0,")
    print("        job_item_pkd_width=12.0,")
    print("        job_item_pkd_height=10.0,")
    print("        job_item_pkd_weight=40.0")
    print("    )")
    print("]")
    print()
    print("success = api.jobs.items.replace_parcels(4675060, new_items)")
    print("if success:")
    print("    print('Parcel items replaced successfully')")
    print("else:")
    print("    print('Failed to replace parcel items - check logs')")
    print()


if __name__ == "__main__":
    demonstrate_items_helper()
    code_examples()
