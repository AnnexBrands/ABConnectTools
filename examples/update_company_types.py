#!/usr/bin/env python3
"""Get all company types and generate the correct enum."""

from ABConnect.api import ABConnectAPI
from ABConnect.api.models import LookupKeys
from ABConnect.config import Config
import json


def main():
    Config.load('.env.staging', force_reload=True)
    print(f"🔌 Using {Config.get_env()} environment")
    
    api = ABConnectAPI()
    
    print(f"\n🔍 Getting all company types from lookup API...")
    
    try:
        # Use the correct path format (without /api prefix)
        result = api.lookup.raw('GET', f'lookup/{LookupKeys.COMPANYTYPES.value}')
        
        print("✅ Successfully retrieved company types!")
        
        if isinstance(result, list):
            company_types = result
        else:
            company_types = result.get('data', result.get('values', []))
            
        print(f"\n📊 Found {len(company_types)} company types:")
        
        # Extract all company types with their IDs
        type_mapping = {}
        
        for item in company_types:
            if isinstance(item, dict):
                name = item.get('name', item.get('value', ''))
                type_id = item.get('id', '')
                
                if name:
                    type_mapping[name] = type_id
                    print(f"  - {name}")
                    print(f"    ID: {type_id}")
        
        # Check our test company
        print("\n🏢 Verifying against actual company data...")
        try:
            companies = api.users.access_companies()
            if companies and companies[0].get('typeId'):
                company_type_id = companies[0]['typeId']
                print(f"  Test company typeId: {company_type_id}")
                
                # Find which type this ID corresponds to
                for name, type_id in type_mapping.items():
                    if type_id == company_type_id:
                        print(f"  ✓ This corresponds to: '{name}'")
                        break
        except Exception as e:
            print(f"  Error checking companies: {e}")
        
        # Generate the corrected enum
        if type_mapping:
            print("\n📝 Here's the corrected CompanyType enum for ABConnect/api/models.py:")
            print("\n```python")
            print("class CompanyType(str, Enum):")
            print('    """Valid company types from ABC API."""')
            
            # Sort by name for consistency
            for name in sorted(type_mapping.keys()):
                # Convert to valid Python identifier
                enum_name = name.upper().replace(' ', '_').replace('-', '_')
                enum_name = ''.join(c if c.isalnum() or c == '_' else '_' for c in enum_name)
                # Remove leading numbers/underscores
                enum_name = enum_name.lstrip('_0123456789')
                if not enum_name:
                    enum_name = f"TYPE_{name.upper()}"
                    
                print(f'    {enum_name} = "{name}"')
            print("```")
            
            # Also show a mapping dictionary if needed
            print("\n# Optional: ID mapping for reference")
            print("COMPANY_TYPE_IDS = {")
            for name in sorted(type_mapping.keys()):
                print(f'    "{name}": "{type_mapping[name]}",')
            print("}")
            
    except Exception as e:
        print(f"❌ Error: {e}")
    
    print("\n✅ Complete!")


if __name__ == '__main__':
    main()