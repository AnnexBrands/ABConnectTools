"""
Companies API Examples - Getting Responses as Pydantic Objects

This example demonstrates how to work with companies and get typed responses.
"""

from ABConnect.api import ABConnectAPI, models
from _helpers import save_fixture

api = ABConnectAPI(env='staging', username='instaquote')

# Training company ID (from Contact fixture data)
TRAINING_COMPANY_ID = "ed282b80-54fe-4f42-bf1b-69103ce1f76c"

# Get company by ID using route-based endpoint
company_obj = api.companies.get_by_id(TRAINING_COMPANY_ID)

# Now you have a typed Pydantic object (CompanySimple)
print(f"type: {type(company_obj)}")
print(f"name: {company_obj.name}")
print(f"code: {company_obj.code}")

# Save fixture if not exists
save_fixture(company_obj, "CompanySimple")
