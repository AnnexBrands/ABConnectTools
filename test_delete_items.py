#!/usr/bin/env python
"""Test script to verify logged_delete_parcel_items works correctly."""

import logging
from ABConnect.api import ABConnectAPI

# Enable debug logging to see everything
logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)s:%(name)s:%(message)s'
)

JOB = 4675060

print("=" * 60)
print("Testing logged_delete_parcel_items")
print("=" * 60)

# Initialize API
api = ABConnectAPI()

# Check items before
print("\n1. Checking parcel items BEFORE deletion...")
items_before = api.jobs.items.parcelitems(JOB)
print(f"   Found {len(items_before)} items:")
for item in items_before:
    print(f"   - ID: {item.id}, Description: '{item.description}', Qty: {item.quantity}")

# Attempt deletion
print(f"\n2. Calling logged_delete_parcel_items({JOB})...")
result = api.jobs.items.logged_delete_parcel_items(JOB)
print(f"   Result: {result}")

# Check items after
print("\n3. Checking parcel items AFTER deletion...")
items_after = api.jobs.items.parcelitems(JOB)
print(f"   Found {len(items_after)} items:")
for item in items_after:
    print(f"   - ID: {item.id}, Description: '{item.description}', Qty: {item.quantity}")

print("\n" + "=" * 60)
print(f"Summary: Started with {len(items_before)} items, ended with {len(items_after)} items")
print("=" * 60)
