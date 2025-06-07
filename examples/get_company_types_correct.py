#!/usr/bin/env python3
"""Get valid company types using the correct lookup key.

This example uses the LookupKeys enum to get CompanyTypes
from the lookup API and update our CompanyType enum.
"""

from ABConnect.api import ABConnectAPI
from ABConnect.api.models import LookupKeys
from ABConnect.config import Config
import json


def main():
    """Get company types from the API using the correct key."""
    Config.load('.env.staging', force_reload=True)
    print(f"🔌 Using {Config.get_env()} environment")
    
    api = ABConnectAPI()
    
    print(f"\n🔍 Retrieving company types using key: '{LookupKeys.COMPANYTYPES.value}'")
    
    try:
        # Use the correct lookup key
        result = api.lookup.raw('GET', f'/{LookupKeys.COMPANYTYPES.value}')
        
        print("✅ Successfully retrieved company types!")
        
        # Parse the response
        if isinstance(result, list):
            company_types = result
        elif isinstance(result, dict):
            # Could be wrapped in 'data' or 'values'
            company_types = result.get('data', result.get('values', result))
        else:
            company_types = []
            
        if not isinstance(company_types, list):
            print(f"\n📊 Response structure:")
            print(json.dumps(result, indent=2))
            return
            
        print(f"\n📊 Found {len(company_types)} company types:")
        
        # Extract values and IDs
        type_mapping = {}
        
        for item in company_types:
            if isinstance(item, dict):
                # Extract the display value and ID
                value = item.get('value', item.get('name', item.get('text', '')))
                type_id = item.get('id', item.get('valueId', ''))
                
                if value:
                    type_mapping[value] = type_id
                    print(f"  - {value}")
                    if type_id:
                        print(f"    ID: {type_id}")
            else:
                # Simple string value
                type_mapping[str(item)] = None
                print(f"  - {item}")
        
        # Check if our test company's typeId matches
        print("\n🏢 Verifying against actual company data...")
        try:
            companies = api.users.access_companies()
            if companies and companies[0].get('typeId'):
                company_type_id = companies[0]['typeId']
                print(f"  Company typeId: {company_type_id}")
                
                # Find which type this ID corresponds to
                for value, type_id in type_mapping.items():
                    if type_id == company_type_id:
                        print(f"  ✓ This corresponds to: '{value}'")
                        break
        except Exception as e:
            print(f"  Error checking companies: {e}")
        
        # Generate the corrected enum
        if type_mapping:
            print("\n📝 Corrected CompanyType enum:")
            print("```python")
            print("class CompanyType(str, Enum):")
            print('    """Valid company types from API."""')
            
            for value in sorted(type_mapping.keys()):
                # Convert to valid Python identifier
                enum_name = value.upper().replace(' ', '_').replace('-', '_')
                enum_name = ''.join(c if c.isalnum() or c == '_' else '_' for c in enum_name)
                # Remove leading numbers if any
                if enum_name and enum_name[0].isdigit():
                    enum_name = '_' + enum_name
                    
                print(f'    {enum_name} = "{value}"')
            print("```")
            
    except Exception as e:
        print(f"❌ Error: {e}")
        
        # If it's a 404, try to discover what keys are available
        if '404' in str(e):
            print("\n💡 Trying to discover available lookup keys...")
            
            # Try some common patterns
            test_keys = [
                "CompanyType",  # Singular
                "CompanyTypes",  # Plural  
                "COMPANY_TYPES",  # Uppercase
                "company-types",  # Hyphenated
                "CompanyTypeList",  # List suffix
            ]
            
            for key in test_keys:
                try:
                    result = api.lookup.raw('GET', f'/{key}')
                    print(f"  ✓ Found working key: '{key}'")
                    print(f"    Result: {json.dumps(result, indent=2)[:200]}...")
                    break
                except:
                    continue
    
    print("\n✅ Complete!")


if __name__ == '__main__':
    main()