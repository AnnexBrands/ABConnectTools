#!/usr/bin/env python3
"""Discover valid API enumeration values using ABConnect.

This example shows how to:
1. List available API endpoints
2. Find lookup/constant endpoints
3. Discover valid values for enums like CompanyType
4. Use the API to validate our client-side enums
"""

from ABConnect.api import ABConnectAPI
from ABConnect.config import Config
import json
from typing import Set, List, Dict, Any


def discover_endpoints(api: ABConnectAPI, pattern: str = None) -> List[str]:
    """Discover available API endpoints.
    
    Args:
        api: ABConnect API client
        pattern: Optional pattern to filter endpoints (case-insensitive)
        
    Returns:
        List of matching endpoint names
    """
    if not hasattr(api, 'available_endpoints'):
        print("⚠️  Generic endpoints not enabled")
        return []
    
    endpoints = sorted(api.available_endpoints)
    
    if pattern:
        endpoints = [e for e in endpoints if pattern.lower() in e.lower()]
    
    return endpoints


def get_company_types_from_data(api: ABConnectAPI) -> Set[str]:
    """Extract company types from actual company data.
    
    Args:
        api: ABConnect API client
        
    Returns:
        Set of unique company types found
    """
    types = set()
    
    try:
        # Get accessible companies
        if hasattr(api.users, 'access_companies'):
            companies = api.users.access_companies()
            print(f"📊 Found {len(companies)} accessible companies")
            
            for company in companies:
                # Check various possible field names
                for field in ['type', 'companyType', 'company_type']:
                    if field in company and company[field]:
                        types.add(str(company[field]))
                        
            # Also check the structure of the first company
            if companies:
                print(f"\n🔍 First company structure:")
                first = companies[0]
                type_fields = {k: v for k, v in first.items() 
                              if 'type' in k.lower() and v is not None}
                for field, value in type_fields.items():
                    print(f"  {field}: {value}")
                    
    except Exception as e:
        print(f"❌ Error getting companies: {e}")
    
    return types


def discover_lookup_values(api: ABConnectAPI, key_pattern: str = None) -> Dict[str, List[Any]]:
    """Discover values from lookup/constants endpoints.
    
    Args:
        api: ABConnect API client
        key_pattern: Optional pattern to filter lookup keys
        
    Returns:
        Dictionary of lookup key to list of values
    """
    lookups = {}
    
    # Try various possible endpoint names
    lookup_endpoints = ['lookup', 'lookups', 'masterconstants', 'master_constants', 'constants']
    
    for endpoint_name in lookup_endpoints:
        if hasattr(api, endpoint_name):
            print(f"\n🔎 Checking {endpoint_name} endpoint...")
            endpoint = getattr(api, endpoint_name)
            
            try:
                # Try to list all constants/lookups
                if hasattr(endpoint, 'list'):
                    result = endpoint.list()
                    data = result.get('data', result) if isinstance(result, dict) else result
                    
                    if isinstance(data, list):
                        print(f"  Found {len(data)} items")
                        
                        # Filter by pattern if provided
                        if key_pattern:
                            data = [item for item in data 
                                   if key_pattern.lower() in str(item).lower()]
                        
                        # Group by type/category
                        for item in data[:10]:  # Show first 10
                            print(f"  - {item}")
                            
                # Try to get specific lookup values
                if hasattr(endpoint, 'get_by_key') or hasattr(endpoint, 'get'):
                    # Common lookup keys for company types
                    test_keys = ['CompanyType', 'CompanyTypes', 'COMPANY_TYPE']
                    for key in test_keys:
                        try:
                            values = endpoint.get(key) if hasattr(endpoint, 'get') else endpoint.get_by_key(key)
                            if values:
                                lookups[key] = values
                                print(f"  ✓ Found values for {key}: {values}")
                        except:
                            pass
                            
            except Exception as e:
                print(f"  Error: {e}")
    
    return lookups


def main():
    """Main discovery function."""
    # Load configuration
    Config.load('.env.staging', force_reload=True)
    print(f"🔌 Using {Config.get_env()} environment")
    print(f"🌐 API URL: {Config.get_api_base_url()}")
    
    # Initialize API client
    api = ABConnectAPI()
    
    # 1. Discover all available endpoints
    print("\n📋 Available endpoints:")
    all_endpoints = discover_endpoints(api)
    print(f"Total endpoints: {len(all_endpoints)}")
    
    # Look for lookup-related endpoints
    lookup_endpoints = discover_endpoints(api, 'lookup')
    constant_endpoints = discover_endpoints(api, 'constant')
    
    print(f"\nLookup endpoints: {lookup_endpoints}")
    print(f"Constant endpoints: {constant_endpoints}")
    
    # 2. Get company types from actual data
    print("\n🏢 Discovering company types from data...")
    company_types = get_company_types_from_data(api)
    
    if company_types:
        print(f"\n✅ Found {len(company_types)} unique company types:")
        for ct in sorted(company_types):
            print(f"  - {ct}")
    
    # 3. Try to find lookup values
    print("\n🔍 Searching for lookup values...")
    lookup_values = discover_lookup_values(api, 'company')
    
    if lookup_values:
        print("\n✅ Found lookup values:")
        for key, values in lookup_values.items():
            print(f"  {key}: {values}")
    
    # 4. Summary and recommendations
    print("\n📝 Summary:")
    if company_types:
        print(f"  Company types found in data: {sorted(company_types)}")
        print("\n  Recommended CompanyType enum:")
        print("  ```python")
        print("  class CompanyType(str, Enum):")
        for ct in sorted(company_types):
            # Convert to valid Python identifier
            enum_name = ct.upper().replace(' ', '_').replace('-', '_')
            print(f'      {enum_name} = "{ct}"')
        print("  ```")
    else:
        print("  No company types found. The API might use a different approach.")
    
    print("\n✅ Discovery complete!")


if __name__ == '__main__':
    main()