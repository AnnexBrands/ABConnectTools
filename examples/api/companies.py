"""
Companies API Examples - Getting Responses as Pydantic Objects

This example demonstrates how to work with companies and get typed responses.
"""

from ABConnect.api import ABConnectAPI, models
from _helpers import save_fixture
from _constants import COMPANY_ID

api = ABConnectAPI(env='staging', username='instaquote')

# Get company by ID using route-based endpoint
company_obj = api.companies.get_by_id(COMPANY_ID)

# Now you have a typed Pydantic object (CompanySimple)
print(f"type: {type(company_obj)}")
print(f"name: {company_obj.name}")
print(f"code: {company_obj.code}")

# Save fixture if not exists
save_fixture(company_obj, "CompanySimple")
