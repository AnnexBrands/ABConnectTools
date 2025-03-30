from ABConnect.api.endpoints.base import BaseEndpoint
from ABConnect.common import load_json_resource
from ABConnect.exceptions import ABConnectError


class CompaniesEndpoint(BaseEndpoint):
    def get(self, CompanyCode: str) -> dict:
        """
        Call the ABConnect get company endpoint by company code.
        Depends on periodic update to base/companies.json.

        Args:
            CompanyCode (str): The company code to retrieve user information for.

        Returns:
            dict: The user information for the specified company code.
        """
        companies = load_json_resource("companies.json")
        companyid = companies.get(CompanyCode)

        if not companyid:
            raise ABConnectError(f"Company code {CompanyCode} not found.")

        return self._r.call("GET", f"companies/{companyid}/details")
