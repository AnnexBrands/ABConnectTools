#!/usr/bin/env python3
"""Fetch actual API responses for documentation examples."""

import json
import os
from pathlib import Path
from ABConnect import ABConnectAPI

# Initialize API client
api = ABConnectAPI(env='staging')

# Dictionary to store responses
responses = {
    "job": {},
    "companies": {},
    "contacts": {},
    "users": {},
    "lookups": {}
}

print("Fetching actual API responses...")

# Job endpoints
try:
    # Get job by display ID
    job = api.jobs.get("2000000")
    responses["job"]["get_job_by_display_id"] = {
        "endpoint": "/api/job/{jobDisplayId}",
        "method": "GET",
        "response": job
    }
    print("✓ Fetched job by display ID")
except Exception as e:
    print(f"✗ Error fetching job: {e}")

# Company endpoints
try:
    # Get company by ID
    company = api.companies.get("ed282b80-54fe-4f42-bf1b-69103ce1f76c")
    responses["companies"]["get_company_by_id"] = {
        "endpoint": "/api/companies/{id}",
        "method": "GET",
        "response": company
    }
    print("✓ Fetched company by ID")
    
    # Get company details
    details = api.companies.get_details("ed282b80-54fe-4f42-bf1b-69103ce1f76c")
    responses["companies"]["get_company_details"] = {
        "endpoint": "/api/companies/{companyId}/details",
        "method": "GET",
        "response": details
    }
    print("✓ Fetched company details")
    
    # Get companies available to current user
    available = api.companies.get_available()
    responses["companies"]["get_companies_available"] = {
        "endpoint": "/api/companies/availableByCurrentUser",
        "method": "GET",
        "response": available
    }
    print("✓ Fetched available companies")
except Exception as e:
    print(f"✗ Error fetching companies: {e}")

# Lookup endpoints
try:
    # Get company types
    company_types = api.raw.get("/api/lookup/CompanyTypes")
    responses["lookups"]["get_company_types"] = {
        "endpoint": "/api/lookup/{masterConstantKey}",
        "method": "GET",
        "response": company_types
    }
    print("✓ Fetched company types lookup")
    
    # Get job status types
    job_statuses = api.raw.get("/api/lookup/JobStatusTypes")
    responses["lookups"]["get_job_status_types"] = {
        "endpoint": "/api/lookup/{masterConstantKey}",
        "method": "GET",
        "response": job_statuses
    }
    print("✓ Fetched job status types lookup")
except Exception as e:
    print(f"✗ Error fetching lookups: {e}")

# Save responses
output_path = Path(__file__).parent / "api" / "response_examples.json"
output_path.parent.mkdir(exist_ok=True)

with open(output_path, 'w') as f:
    json.dump(responses, f, indent=2, default=str)

print(f"\nSaved responses to {output_path}")
print("\nResponse summary:")
for category, items in responses.items():
    if items:
        print(f"  {category}: {len(items)} responses")