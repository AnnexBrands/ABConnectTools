#!/usr/bin/env python3
"""Explore the lookup endpoint to find how to get company types.

This example specifically investigates the lookup endpoint structure
and finds the proper way to retrieve master constants.
"""

from ABConnect.api import ABConnectAPI
from ABConnect.config import Config
import json


def explore_lookup_methods(api):
    """Explore all methods available on the lookup endpoint."""
    if not hasattr(api, 'lookup'):
        print("❌ No lookup endpoint found")
        return
        
    lookup = api.lookup
    print("📋 Methods available on lookup endpoint:")
    
    # Get all non-private methods
    methods = [m for m in dir(lookup) if not m.startswith('_') and callable(getattr(lookup, m))]
    for method in sorted(methods):
        print(f"  - lookup.{method}")
        
    # Check if it's a GenericEndpoint
    if hasattr(lookup, '__class__'):
        print(f"\n  Type: {lookup.__class__.__name__}")
        if hasattr(lookup, '_endpoints'):
            print(f"  Endpoints defined: {len(lookup._endpoints)}")
            
    return methods


def try_lookup_methods(api):
    """Try various approaches to get lookup data."""
    lookup = api.lookup
    
    print("\n🔍 Trying different lookup methods...")
    
    # 1. Try to get specific master constant keys
    test_keys = [
        'CompanyType',
        'CompanyTypes', 
        'COMPANY_TYPE',
        'company_type',
        'Type',
        'Types'
    ]
    
    for key in test_keys:
        print(f"\n  Trying lookup.get('{key}')...")
        try:
            result = lookup.get(key)
            print(f"  ✓ Success! Result: {result}")
            return result
        except Exception as e:
            error_msg = str(e)
            if '404' not in error_msg:  # Don't show 404s
                print(f"  ✗ Error: {error_msg}")
    
    # 2. Try to list all master constants
    print("\n  Trying lookup.list()...")
    try:
        result = lookup.list()
        print(f"  ✓ Success! Got {len(result.get('data', result))} items")
        
        # Show structure of first few items
        data = result.get('data', result) if isinstance(result, dict) else result
        if isinstance(data, list) and data:
            print("\n  First item structure:")
            print(f"  {json.dumps(data[0], indent=2)}")
            
        return result
    except Exception as e:
        print(f"  ✗ Error: {e}")
    
    # 3. Check for raw method access
    print("\n  Checking for raw API access...")
    if hasattr(lookup, 'raw'):
        try:
            # Try common API patterns
            paths = [
                '/lookup',
                '/lookups', 
                '/lookup/types',
                '/lookup/companyTypes',
                '/lookup/CompanyType',
                '/api/lookup',
                '/masterConstants',
                '/master-constants'
            ]
            
            for path in paths:
                print(f"    Trying GET {path}...")
                try:
                    result = lookup.raw('GET', path)
                    print(f"    ✓ Success! Got response")
                    return result
                except Exception as e:
                    if '404' not in str(e) and '405' not in str(e):
                        print(f"    ✗ {e}")
        except Exception as e:
            print(f"  Error with raw access: {e}")


def find_company_type_endpoint(api):
    """Try to find how company types are retrieved."""
    print("\n🏢 Searching for company type information...")
    
    # Check if there's a specific endpoint for types
    type_endpoints = ['types', 'companytypes', 'company_types', 'lookuptypes']
    
    for endpoint_name in type_endpoints:
        if hasattr(api, endpoint_name):
            print(f"\n  Found {endpoint_name} endpoint!")
            endpoint = getattr(api, endpoint_name)
            
            try:
                if hasattr(endpoint, 'list'):
                    result = endpoint.list()
                    print(f"  Got {len(result.get('data', []))} types")
                    return result
            except Exception as e:
                print(f"  Error: {e}")
    
    # Check the company endpoint itself
    if hasattr(api, 'companies'):
        print("\n  Checking companies endpoint for type info...")
        
        # Some APIs have a /companies/types sub-endpoint
        if hasattr(api.companies, 'types'):
            try:
                types = api.companies.types()
                print(f"  ✓ Found company types: {types}")
                return types
            except Exception as e:
                print(f"  Error: {e}")
                
        # Try raw access
        if hasattr(api.companies, 'raw'):
            try:
                types = api.companies.raw('GET', '/types')
                print(f"  ✓ Found company types via raw: {types}")
                return types
            except:
                pass


def main():
    """Main exploration function."""
    Config.load('.env.staging', force_reload=True)
    print(f"🔌 Using {Config.get_env()} environment")
    
    api = ABConnectAPI()
    
    # 1. Explore lookup endpoint structure
    methods = explore_lookup_methods(api)
    
    # 2. Try various lookup approaches
    lookup_result = try_lookup_methods(api)
    
    # 3. Try to find company type specific endpoints
    type_result = find_company_type_endpoint(api)
    
    # 4. Get a company with typeId and see if we can resolve it
    print("\n🔗 Checking typeId resolution...")
    try:
        companies = api.users.access_companies()
        if companies and companies[0].get('typeId'):
            type_id = companies[0]['typeId']
            print(f"  Company has typeId: {type_id}")
            
            # Try to look up this type ID
            if hasattr(api, 'types') or hasattr(api, 'lookup'):
                endpoint = api.types if hasattr(api, 'types') else api.lookup
                try:
                    type_info = endpoint.get(type_id)
                    print(f"  ✓ Type info: {type_info}")
                except Exception as e:
                    print(f"  ✗ Could not resolve typeId: {e}")
    except Exception as e:
        print(f"  Error: {e}")
    
    print("\n✅ Exploration complete!")
    
    # If we found any results, show them
    if lookup_result or type_result:
        print("\n📊 Results found:")
        if lookup_result:
            print(f"  Lookup result: {json.dumps(lookup_result, indent=2)[:500]}...")
        if type_result:
            print(f"  Type result: {json.dumps(type_result, indent=2)[:500]}...")


if __name__ == '__main__':
    main()