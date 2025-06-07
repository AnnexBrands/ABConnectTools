"""Companies endpoint for interacting with company resources.

This module provides methods for retrieving company information from the ABC API.
It supports fetching companies by both company code and company ID.
"""

from ABConnect.api.endpoints.base import BaseEndpoint
from ABConnect.common import load_json_resource
from ABConnect.exceptions import ABConnectError


class CompaniesEndpoint(BaseEndpoint):
    """Endpoint for company-related API operations.
    
    This endpoint provides methods to retrieve company information
    from the ABC API using either company codes or UUIDs.
    
    The company code lookup uses a local cache (base/companies.json)
    to map company codes to UUIDs for better performance.
    
    Available Methods:
        - get: Retrieve company by company code (uses local cache)
        - get_id: Retrieve company by UUID (direct API call)
    """
    def get(self, CompanyCode: str) -> dict:
        """Retrieve company information by company code.
        
        This method uses a local cache (base/companies.json) to map company
        codes to UUIDs, then fetches the company details from the API.
        The cache should be periodically updated to ensure accuracy.

        Args:
            CompanyCode (str): The unique company code (e.g., 'ABC123', 'XYZ789').
                This is typically a short alphanumeric identifier assigned to
                each company.

        Returns:
            dict: A dictionary containing company information with structure::

                {
                    'id': 'uuid-string',
                    'companyCode': 'ABC123',
                    'name': 'Company Name',
                    'type': 'Customer|Vendor|Agent',
                    'addresses': [...],
                    'contacts': [...],
                    'settings': {...},
                    'active': True|False
                }

        Raises:
            ABConnectError: If the company code is not found in the local cache
                or if there's an API error fetching company details.
            
        Example:
            >>> endpoint = CompaniesEndpoint()
            >>> company = endpoint.get('ABC123')
            >>> print(f"Company Name: {company['name']}")
            >>> print(f"Company ID: {company['id']}")
            
        Note:
            This method depends on the base/companies.json file being up-to-date.
            If a company code is not found, the cache may need to be refreshed.
        """
        companies = load_json_resource("companies.json")
        companyid = companies.get(CompanyCode)

        if not companyid:
            raise ABConnectError(f"Company code {CompanyCode} not found.")

        return self._r.call("GET", f"companies/{companyid}/details")

    def get_id(self, compnayid: str) -> dict:
        """Retrieve company information by company UUID.
        
        This method directly queries the API using the company's UUID,
        bypassing the local cache lookup. It's useful when you already
        have the company ID or when the cache might be outdated.
        
        Note:
            The parameter name has a typo (compnayid instead of companyid)
            but is kept for backward compatibility.

        Args:
            compnayid (str): The company's UUID (e.g., '123e4567-e89b-12d3-a456-426614174000').
                Despite the parameter name typo, this should be a valid UUID string.

        Returns:
            dict: A dictionary containing company information with structure::

                {
                    'id': 'uuid-string',
                    'companyCode': 'ABC123',
                    'name': 'Company Name',
                    'type': 'Customer|Vendor|Agent',
                    'addresses': [
                        {
                            'id': 123,
                            'type': 'Billing|Shipping',
                            'line1': '123 Main St',
                            'city': 'New York',
                            'state': 'NY',
                            'zip': '10001'
                        }
                    ],
                    'contacts': [...],
                    'settings': {...},
                    'active': True|False,
                    'created': '2023-01-01T00:00:00Z',
                    'modified': '2023-12-01T00:00:00Z'
                }

        Raises:
            ABConnectError: If the company UUID is not found or if there's an API error.
            
        Example:
            >>> endpoint = CompaniesEndpoint()
            >>> company_id = '123e4567-e89b-12d3-a456-426614174000'
            >>> company = endpoint.get_id(company_id)
            >>> print(f"Company: {company['name']} ({company['companyCode']})")
            
        See Also:
            - get: Retrieve company by company code (uses cache)
        """
        return self._r.call("GET", f"companies/{compnayid}/details")
