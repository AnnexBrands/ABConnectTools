"""Examples for Items API endpoints and models.

This module demonstrates how to work with parcel items and freight items
using the Jobs API and appropriate Pydantic models for type-safe responses.

Key learnings:
- Parcel items: Use api.jobs.parcelitems.get_parcelitems() → ParcelItem model
- Freight items: Use api.jobs.job.get()['freightItems'] → FreightShimpment model
"""

from typing import List
from ABConnect.api import ABConnectAPI
from ABConnect.models import ParcelItem, ParcelItemWithPackage, FreightShimpment


PARCEL_JOB_ID = 4675060  # Example job ID with parcel items
FREIGHT_JOB_ID = 4637814  # Example job ID with freight items

def print_parcel_items(job_display_id: int = PARCEL_JOB_ID):
    """Fetch and display parcel items for a job.

    Parcel items are items configured for parcel shipping (UPS, FedEx, etc.)
    with specific packaging dimensions and weights.

    Args:
        job_display_id: The job display ID to fetch parcel items for
    """
    print(f"=== Parcel Items for Job {job_display_id} ===\n")

    # Initialize API client

    api = ABConnectAPI(env='staging', username='instaquote')

    try:
        # Get parcel items from the API
        response = api.jobs.parcelitems.get_parcelitems(jobDisplayId=str(job_display_id))

        # Extract parcel items from response (API returns dict with 'parcelItems' key)
        items_data = None
        if isinstance(response, dict) and 'parcelItems' in response:
            items_data = response['parcelItems']
        elif isinstance(response, list):
            items_data = response

        if items_data is not None:
            # Cast response to list of ParcelItem models
            parcel_items: List[ParcelItem] = [
                ParcelItem(**item) for item in items_data
            ]

            print(f"Found {len(parcel_items)} parcel item(s)\n")

            if len(parcel_items) == 0:
                print("No parcel items found for this job")
                print("(Job may not have parcel shipping configured)")
            else:
                # Display each parcel item with proper model access
                for idx, item in enumerate(parcel_items, 1):
                    print(f"Parcel Item #{idx}:")
                    print(f"  ID: {item.id}")
                    print(f"  Job Item ID: {item.job_item_id}")
                    print(f"  Description: {item.description}")
                    print(f"  Quantity: {item.quantity}")
                    print(f"  Dimensions (L×W×H): {item.job_item_pkd_length} × {item.job_item_pkd_width} × {item.job_item_pkd_height}")
                    print(f"  Weight: {item.job_item_pkd_weight} lbs")
                    print(f"  Value: ${item.job_item_parcel_value}")
                    print(f"  Package Type ID: {item.parcel_package_type_id}")

                    # Show model serialization
                    if idx == 1:  # Show serialization for first item only
                        print(f"\n  Serialized (API format):")
                        print(f"  {item.model_dump(by_alias=True, exclude_none=True)}")
                    print()
        else:
            print(f"Response: {response}")
            print("Unexpected response format")

    except Exception as e:
        print(f"Error fetching parcel items: {e}")
        print("\nThis is a demo - requires valid job ID with parcel items")

    print()


def print_freight_items(job_display_id: int = 4637814):
    """Fetch and display freight items for a job.

    Freight items are items configured for freight shipping (LTL, FTL, etc.)
    with NMFC classifications and freight-specific details.

    Args:
        job_display_id: The job display ID to fetch freight items for
    """
    print(f"=== Freight Items for Job {job_display_id} ===\n")

    # Initialize API client
    api = ABConnectAPI()

    try:
        # Get the full job from the API
        job = api.jobs.job.get(jobDisplayId=str(job_display_id))

        # Extract freight items from the job
        freight_items_data = job.get('freightItems', [])

        if freight_items_data:
            # Cast response to list of FreightShimpment models
            freight_items: List[FreightShimpment] = [
                FreightShimpment(**item) for item in freight_items_data
            ]

            print(f"Found {len(freight_items)} freight item(s)\n")

            # Display each freight item with proper model access
            for idx, item in enumerate(freight_items, 1):
                print(f"Freight Item #{idx}:")
                print(f"  Job Freight ID: {item.job_freight_id}")
                print(f"  Freight Item ID: {item.freight_item_id}")
                print(f"  Quantity: {item.quantity}")
                print(f"  Freight Class: {item.freight_item_class}")
                print(f"  NMFC Item: {item.nmfc_item}")
                print(f"  Cube: {item.cube} cubic feet")
                print(f"  Total Weight: {item.total_weight} lbs" if item.total_weight else "  Total Weight: Not specified")
                print(f"  Freight Item Value: {item.freight_item_value}")
                print(f"  BOL Description: {item.bol_description[:50]}..." if item.bol_description and len(item.bol_description) > 50 else f"  BOL Description: {item.bol_description}")

                # Show dimensions if available
                if item.item_length or item.item_width or item.item_height:
                    print(f"  Item Dimensions (L×W×H): {item.item_length} × {item.item_width} × {item.item_height}")

                # Show model serialization
                if idx == 1:  # Show serialization for first item only
                    print(f"\n  Serialized (API format):")
                    serialized = item.model_dump(by_alias=True, exclude_none=True)
                    print(f"  {serialized}")
                print()
        else:
            print(f"No freight items found for this job")
            print("(Job may not have freight shipping configured)")

    except Exception as e:
        print(f"Error fetching freight items: {e}")
        print("\nThis is a demo - requires valid job ID with freight items")
        import traceback
        traceback.print_exc()

    print()


def main():
    """Main examples runner."""
    print("=== ABConnect Items API Examples ===\n")

    print("This module demonstrates working with two types of items:\n")
    print("1. Parcel Items - For parcel shipping (UPS, FedEx, USPS)")
    print("   Model: ParcelItem from jobparcelitems.py")
    print("   Endpoint: api.jobs.parcelitems.get_parcelitems()")
    print()
    print("2. Freight Items - For freight shipping (LTL, FTL) with NMFC classifications")
    print("   Model: FreightShimpment from job.py")
    print("   Access: api.jobs.job.get()['freightItems']")
    print()

    # Example 1: Print parcel items
    print_parcel_items(job_display_id=PARCEL_JOB_ID)

    # Example 2: Print freight items
    print_freight_items(job_display_id=FREIGHT_JOB_ID)

    # Show CLI and curl examples
    cli_and_curl_examples()


def cli_and_curl_examples():
    """CLI and curl usage examples."""
    print("=== CLI Usage Examples ===\n")

    print("# Get parcel items for a job")
    print(f"ab jobs parcelitems get_parcelitems --jobDisplayId {PARCEL_JOB_ID}")
    print()

    print("# Get job with freight items")
    print(f"ab jobs job get --jobDisplayId {FREIGHT_JOB_ID}")
    print()

    print("=== curl Examples ===\n")

    print("# Get parcel items")
    print("curl -H \"Authorization: Bearer $TOKEN\" \\")
    print(f"     \"$API_BASE/api/job/{PARCEL_JOB_ID}/parcelitems\"")
    print()

    print("# Get job (includes freight items)")
    print("curl -H \"Authorization: Bearer $TOKEN\" \\")
    print(f"     \"$API_BASE/api/job/{FREIGHT_JOB_ID}\"")
    print()

    print("=== Python API Examples ===\n")

    print("from ABConnect.api import ABConnectAPI")
    print("from ABConnect.api.models.jobparcelitems import ParcelItem")
    print("from ABConnect.api.models.job import FreightShimpment")
    print()
    print("api = ABConnectAPI()")
    print()
    print("# Get and cast parcel items")
    print(f"response = api.jobs.parcelitems.get_parcelitems(jobDisplayId='{PARCEL_JOB_ID}')")
    print("items_data = response['parcelItems'] if 'parcelItems' in response else response")
    print("parcel_items = [ParcelItem(**item) for item in items_data]")
    print("for item in parcel_items:")
    print("    print(f'{item.description}: {item.job_item_pkd_weight} lbs')")
    print()
    print("# Get job and cast freight items")
    print(f"job = api.jobs.job.get(jobDisplayId='{FREIGHT_JOB_ID}')")
    print("freight_items = [FreightShimpment(**item) for item in job['freightItems']]")
    print("for item in freight_items:")
    print("    print(f'{item.freight_item_class} (NMFC: {item.nmfc_item}): {item.cube} cu ft')")
    print()


if __name__ == "__main__":
    main()
