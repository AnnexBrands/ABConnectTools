"""
Companies API Examples - Getting Responses as Pydantic Objects

This example demonstrates how to work with companies and get typed responses.
"""

from ABConnect import ABConnectAPI, models
from _helpers import save_fixture
from _constants import COMPANY_ID
import json

api = ABConnectAPI(env='staging', username='instaquote')

# Get company by ID using route-based endpoint
company_obj = api.companies.get_by_id(COMPANY_ID)

# Now you have a typed Pydantic object (CompanySimple)
print(f"type: {type(company_obj)}")
print(f"name: {company_obj.name}")
print(f"code: {company_obj.code}")
save_fixture(company_obj, "CompanySimple")

# Get brands
brands = api.companies.get_brands()
print(f"Brands count: {len(brands) if isinstance(brands, list) else 'N/A'}")
save_fixture(brands, "CompanyBrands")

# Get brands tree
brands_tree = api.companies.get_brandstree()
print(f"Brands tree type: {type(brands_tree)}")
save_fixture(brands_tree, "CompanyBrandsTree")

# Get companies available by current user
available = api.companies.get_availablebycurrentuser()
print(f"Available companies count: {len(available) if isinstance(available, list) else 'N/A'}")
save_fixture(available, "CompanyAvailableByCurrentUser")

search = api.companies.get_search(search_value="Training")
print(search)
save_fixture(search, "CompanySearch_Training")

geoareacompanies = api.companies.get_geoareacompanies()
print(geoareacompanies)
save_fixture(geoareacompanies, "CompanyGeoAreaCompanies")