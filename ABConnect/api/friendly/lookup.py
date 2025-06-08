"""Friendly methods for lookup operations.

This module provides developer-friendly methods for working with lookup
endpoints, including shortcuts for common master constants.
"""

from typing import List, Dict, Any
from ABConnect.api.models import LookupKeys


class LookupFriendly:
    """Friendly methods for lookup operations.
    
    This class extends the auto-generated lookup resource with
    convenience methods for common lookups.
    """
    
    def __init__(self, lookup_resource):
        """Initialize with the underlying lookup resource.
        
        Args:
            lookup_resource: The auto-generated lookup resource
        """
        self._resource = lookup_resource
        
    def master_constant(self, key: str) -> List[Dict[str, Any]]:
        """Get master constant values by key.
        
        This is an alias for the {masterConstantKey} endpoint.
        
        Args:
            key: Master constant key (e.g., 'CompanyTypes')
            
        Returns:
            List of constant values
        """
        # Use the underlying resource method
        # The path would be /api/lookup/{masterConstantKey}
        return self._resource.get_by_masterConstantKey(masterConstantKey=key)
    
    def company_types(self) -> List[Dict[str, Any]]:
        """Get all company types.
        
        Shortcut for master_constant('CompanyTypes').
        
        Returns:
            List of company types with id and name
        """
        return self.master_constant(LookupKeys.COMPANYTYPES.value)
    
    def job_statuses(self) -> List[Dict[str, Any]]:
        """Get all job status types.
        
        Shortcut for master_constant('JobsStatusTypes').
        
        Returns:
            List of job status types
        """
        return self.master_constant(LookupKeys.JOBSSTATUSTYPES.value)
    
    def contact_types(self) -> List[Dict[str, Any]]:
        """Get all contact types.
        
        Shortcut for master_constant('ContactTypes').
        
        Returns:
            List of contact types
        """
        return self.master_constant(LookupKeys.CONTACTTYPES.value)
    
    def freight_types(self) -> List[Dict[str, Any]]:
        """Get all freight types.
        
        Shortcut for master_constant('FreightTypes').
        
        Returns:
            List of freight types
        """
        return self.master_constant(LookupKeys.FREIGHTTYPES.value)
    
    def document_types(self) -> List[Dict[str, Any]]:
        """Get all document types.
        
        Uses the dedicated /api/lookup/documentTypes endpoint.
        
        Returns:
            List of document types
        """
        return self._resource.documentTypes()
    
    def countries(self) -> List[Dict[str, Any]]:
        """Get all countries.
        
        Uses the dedicated /api/lookup/countries endpoint.
        
        Returns:
            List of countries
        """
        return self._resource.countries()
    
    def items(self) -> List[Dict[str, Any]]:
        """Get lookup items.
        
        Uses the dedicated /api/lookup/items endpoint.
        
        Returns:
            List of items
        """
        return self._resource.items()
    
    def parcel_package_types(self) -> List[Dict[str, Any]]:
        """Get parcel package types.
        
        Uses the dedicated /api/lookup/parcelPackageTypes endpoint.
        
        Returns:
            List of parcel package types
        """
        return self._resource.parcelPackageTypes()
    
    def available_keys(self) -> List[str]:
        """Get all available master constant keys.
        
        Returns:
            List of available lookup keys
        """
        return [key.value for key in LookupKeys]