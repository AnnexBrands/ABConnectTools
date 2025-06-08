#!/usr/bin/env python3
"""Get valid company types from the lookup API.

This example shows the correct way to use the lookup endpoint
to retrieve master constant values like CompanyType.
"""

from ABConnect.api import ABConnectAPI
from ABConnect.config import Config
import json


def get_lookup_values(api, master_constant_key: str):
    """Get all values for a master constant key.
    
    Args:
        api: ABConnect API client
        master_constant_key: The master constant key (e.g., 'CompanyType')
        
    Returns:
        List of values or None if not found
    """
    if not hasattr(api, 'lookup'):
        print("❌ No lookup endpoint available")
        return None
        
    try:
        # Use the correct pattern: /api/lookup/{masterConstantKey}
        result = api.lookup.raw('GET', f'/{master_constant_key}')
        print(f"✓ Successfully retrieved {master_constant_key}")
        return result
    except Exception as e:
        print(f"✗ Error getting {master_constant_key}: {e}")
        return None


def main():
    """Get company types from the API."""
    Config.load('.env.staging', force_reload=True)
    print(f"🔌 Using {Config.get_env()} environment")
    
    api = ABConnectAPI()
    
    print("\n🔍 Retrieving company types from lookup API...")
    
    # Try different possible master constant keys
    possible_keys = [
        'CompanyType',
        'CompanyTypes',
        'Company Type',
        'company_type',
        'COMPANY_TYPE'
    ]
    
    company_types = None
    successful_key = None
    
    for key in possible_keys:
        print(f"\n  Trying key: '{key}'")
        result = get_lookup_values(api, key)
        
        if result:
            company_types = result
            successful_key = key
            break
    
    if company_types:
        print(f"\n✅ Found company types using key '{successful_key}':")
        
        # Handle different response formats
        if isinstance(company_types, dict):
            # Could be {'data': [...]} or {'values': [...]} or direct dict
            values = company_types.get('data', company_types.get('values', company_types))
        else:
            values = company_types
            
        if isinstance(values, list):
            print(f"  Total values: {len(values)}")
            print("\n  Company type values:")
            
            # Extract the actual values depending on structure
            type_values = []
            for item in values:
                if isinstance(item, dict):
                    # Could be {'id': '...', 'value': '...', 'name': '...'}
                    value = item.get('value', item.get('name', item.get('text', str(item))))
                    type_values.append(value)
                    print(f"    - {value}")
                    if 'id' in item:
                        print(f"      ID: {item['id']}")
                else:
                    type_values.append(str(item))
                    print(f"    - {item}")
            
            # Generate enum code
            print("\n📝 Recommended CompanyType enum:")
            print("```python")
            print("class CompanyType(str, Enum):")
            print('    """Valid company types from API."""')
            
            for value in sorted(set(type_values)):
                # Convert to valid Python identifier
                enum_name = value.upper().replace(' ', '_').replace('-', '_')
                # Remove any non-alphanumeric characters
                enum_name = ''.join(c if c.isalnum() or c == '_' else '_' for c in enum_name)
                print(f'    {enum_name} = "{value}"')
            print("```")
            
        elif isinstance(values, dict):
            print(f"\n  Response structure: {json.dumps(values, indent=2)}")
    else:
        print("\n❌ Could not find company types")
        print("\n💡 Tip: Check the API documentation for the correct master constant key")
        
        # Try to discover available master constants
        print("\n📋 Attempting to list all available master constants...")
        try:
            all_constants = api.lookup.raw('GET', '')
            print(f"  Available constants: {json.dumps(all_constants, indent=2)[:500]}...")
        except Exception as e:
            print(f"  Could not list constants: {e}")
    
    # Also check what typeId we have in company data
    print("\n🏢 Checking company data for type information...")
    try:
        companies = api.users.access_companies()
        if companies and companies[0].get('typeId'):
            type_id = companies[0]['typeId']
            print(f"  Company has typeId: {type_id}")
            
            # Try to resolve this specific type
            if successful_key:
                try:
                    type_info = api.lookup.raw('GET', f'/{successful_key}/{type_id}')
                    print(f"  Type details: {json.dumps(type_info, indent=2)}")
                except Exception as e:
                    print(f"  Could not get type details: {e}")
    except Exception as e:
        print(f"  Error checking companies: {e}")
    
    print("\n✅ Discovery complete!")


if __name__ == '__main__':
    main()