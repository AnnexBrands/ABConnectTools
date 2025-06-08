"""Friendly methods for company operations.

This module provides developer-friendly methods for working with companies,
including helper methods that translate between different identifier types.
"""

from typing import Dict, Any, Optional
from ABConnect.common import load_json_resource
from ABConnect.exceptions import ABConnectError


class CompaniesFriendly:
    """Friendly methods for company operations.
    
    This class extends the auto-generated companies resource with
    convenience methods for common operations.
    """
    
    def __init__(self, companies_resource):
        """Initialize with the underlying companies resource.
        
        Args:
            companies_resource: The auto-generated companies resource
        """
        self._resource = companies_resource
        self._companies_cache = None
        
    def get_by_code(self, company_code: str) -> Dict[str, Any]:
        """Get company by company code.
        
        This method translates a company code to a UUID and retrieves
        the company details. It uses a local cache for performance.
        
        Args:
            company_code: The company code (e.g., 'ABC123')
            
        Returns:
            Company details dictionary
            
        Raises:
            ABConnectError: If company code not found
        """
        # Load cache if needed
        if self._companies_cache is None:
            self._companies_cache = load_json_resource("companies.json")
        
        company_id = self._companies_cache.get(company_code)
        if not company_id:
            raise ABConnectError(f"Company code {company_code} not found in cache")
        
        # Use the underlying resource method
        # This assumes the resource has a method for getting by ID
        return self._resource.get_details(id=company_id)
    
    def search_by_name(self, name: str, **kwargs) -> Dict[str, Any]:
        """Search for companies by name.
        
        Args:
            name: Company name to search for
            **kwargs: Additional search parameters
            
        Returns:
            Search results
        """
        return self._resource.search(name=name, **kwargs)
    
    def get_active_customers(self, **kwargs) -> Dict[str, Any]:
        """Get all active customer companies.
        
        Args:
            **kwargs: Additional query parameters
            
        Returns:
            List of active customer companies
        """
        return self._resource.search(
            type='Customer',
            active=True,
            **kwargs
        )
    
    def get_active_vendors(self, **kwargs) -> Dict[str, Any]:
        """Get all active vendor companies.
        
        Args:
            **kwargs: Additional query parameters
            
        Returns:
            List of active vendor companies
        """
        return self._resource.search(
            type='Vendor', 
            active=True,
            **kwargs
        )
    
    def refresh_cache(self) -> None:
        """Refresh the local companies cache.
        
        This should be called periodically to ensure the cache
        stays in sync with the API.
        """
        # TODO: Implement cache refresh logic
        # This would typically fetch all companies and update companies.json
        pass