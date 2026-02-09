"""
Companies API Examples - Getting Responses as Pydantic Objects

This example demonstrates how to work with companies and get typed responses.

Usage:
    python companies.py              # Run all examples
    python companies.py get          # Run a single example
    python companies.py help         # List available examples
"""

from ABConnect import models
from _base import ExampleRunner
from _helpers import save_fixture
from _constants import COMPANY_ID


class CompanyExamples(ExampleRunner):
    def __init__(self):
        super().__init__("Companies API", api_kwargs=dict(username="instaquote"))
        self.add("get", "Get company by ID", self.get_company)
        self.add("brands", "Get all brands", self.get_brands)
        self.add("brandstree", "Get brands tree", self.get_brands_tree)
        self.add("available", "Get companies available to current user", self.get_available)
        self.add("search", "Search companies by name", self.search)
        self.add("geoarea", "Get geo area companies", self.get_geoarea)

    def get_company(self):
        company_obj = self.api.companies.get(COMPANY_ID)
        print(f"type: {type(company_obj)}")
        print(f"name: {company_obj.details.name}")
        print(f"code: {company_obj.details.code}")
        save_fixture(company_obj, "CompanySimple")

    def get_brands(self):
        brands = self.api.companies.get_brands()
        print(f"Brands count: {len(brands) if isinstance(brands, list) else 'N/A'}")
        save_fixture(brands, "CompanyBrands")

    def get_brands_tree(self):
        brands_tree = self.api.companies.get_brandstree()
        print(f"Brands tree type: {type(brands_tree)}")
        save_fixture(brands_tree, "CompanyBrandsTree")

    def get_available(self):
        available = self.api.companies.get_availablebycurrentuser()
        print(f"Available companies count: {len(available) if isinstance(available, list) else 'N/A'}")
        save_fixture(available, "CompanyAvailableByCurrentUser")

    def search(self):
        search = self.api.companies.get_search(search_value="Training")
        print(search)
        save_fixture(search, "CompanySearch_Training")

    def get_geoarea(self):
        geoareacompanies = self.api.companies.get_geoareacompanies()
        print(geoareacompanies)
        save_fixture(geoareacompanies, "CompanyGeoAreaCompanies")


if __name__ == "__main__":
    CompanyExamples().run()
