"""
Items API Examples - Parcel and freight item operations

This module demonstrates how to work with parcel items and freight items
using the Jobs API and appropriate Pydantic models for type-safe responses.

Key learnings:
- Parcel items: Use api.jobs.parcelitems.get_parcelitems() -> ParcelItem model
- Freight items: Use api.jobs.job.get()['freightItems'] -> FreightShimpment model

Usage:
    python items.py                 # Run all examples
    python items.py parcel          # Run a single example
    python items.py help            # List available examples
"""

from typing import List
from ABConnect import models
from _base import ExampleRunner


PARCEL_JOB_ID = 4675060
FREIGHT_JOB_ID = 4637814


class ItemExamples(ExampleRunner):
    def __init__(self):
        super().__init__("Items API", api_kwargs=dict(env='staging', username='instaquote'))
        self.add("parcel", "Fetch and display parcel items", self.parcel_items)
        self.add("freight", "Fetch and display freight items", self.freight_items)
        self.add("cli", "Show CLI and curl usage examples", self.cli_and_curl_examples)

    def parcel_items(self):
        print(f"Parcel Items for Job {PARCEL_JOB_ID}\n")
        response = self.api.jobs.parcelitems.get_parcelitems(jobDisplayId=str(PARCEL_JOB_ID))

        items_data = None
        if isinstance(response, dict) and 'parcelItems' in response:
            items_data = response['parcelItems']
        elif isinstance(response, list):
            items_data = response

        if items_data is not None:
            parcel_items: List[models.ParcelItem] = [
                models.ParcelItem(**item) for item in items_data
            ]
            print(f"Found {len(parcel_items)} parcel item(s)\n")

            for idx, item in enumerate(parcel_items, 1):
                print(f"Parcel Item #{idx}:")
                print(f"  ID: {item.id}")
                print(f"  Job Item ID: {item.job_item_id}")
                print(f"  Description: {item.description}")
                print(f"  Quantity: {item.quantity}")
                print(f"  Dimensions (LxWxH): {item.job_item_pkd_length} x {item.job_item_pkd_width} x {item.job_item_pkd_height}")
                print(f"  Weight: {item.job_item_pkd_weight} lbs")
                print(f"  Value: ${item.job_item_parcel_value}")
                print(f"  Package Type ID: {item.parcel_package_type_id}")
                if idx == 1:
                    print(f"\n  Serialized (API format):")
                    print(f"  {item.model_dump(by_alias=True, exclude_none=True)}")
                print()
        else:
            print(f"Response: {response}")
            print("Unexpected response format")

    def freight_items(self):
        print(f"Freight Items for Job {FREIGHT_JOB_ID}\n")
        job = self.api.jobs.job.get(jobDisplayId=str(FREIGHT_JOB_ID))
        freight_items_data = job.get('freightItems', [])

        if freight_items_data:
            freight_items: List[models.FreightShimpment] = [
                models.FreightShimpment(**item) for item in freight_items_data
            ]
            print(f"Found {len(freight_items)} freight item(s)\n")

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
                if item.item_length or item.item_width or item.item_height:
                    print(f"  Item Dimensions (LxWxH): {item.item_length} x {item.item_width} x {item.item_height}")
                if idx == 1:
                    print(f"\n  Serialized (API format):")
                    print(f"  {item.model_dump(by_alias=True, exclude_none=True)}")
                print()
        else:
            print("No freight items found for this job")

    def cli_and_curl_examples(self):
        print("CLI Usage:\n")
        print(f"  ab jobs parcelitems get_parcelitems --jobDisplayId {PARCEL_JOB_ID}")
        print(f"  ab jobs job get --jobDisplayId {FREIGHT_JOB_ID}")

        print("\ncurl Usage:\n")
        print(f'  curl -H "Authorization: Bearer $TOKEN" "$API_BASE/api/job/{PARCEL_JOB_ID}/parcelitems"')
        print(f'  curl -H "Authorization: Bearer $TOKEN" "$API_BASE/api/job/{FREIGHT_JOB_ID}"')

        print("\nPython API:\n")
        print(f"  response = api.jobs.parcelitems.get_parcelitems(jobDisplayId='{PARCEL_JOB_ID}')")
        print("  items = [ParcelItem(**item) for item in response['parcelItems']]")
        print(f"  job = api.jobs.job.get(jobDisplayId='{FREIGHT_JOB_ID}')")
        print("  freight = [FreightShimpment(**item) for item in job['freightItems']]")


if __name__ == "__main__":
    ItemExamples().run()
