#!/usr/bin/env python3
"""Test that our CompanyType enum matches the API values."""

from ABConnect.api import ABConnectAPI
from ABConnect.api.models import CompanyType, COMPANY_TYPE_IDS
from ABConnect.config import Config


def main():
    Config.load('.env.staging', force_reload=True)
    print(f"🔌 Using {Config.get_env()} environment")
    
    # Test 1: Verify enum values
    print("\n✅ CompanyType enum values:")
    for company_type in CompanyType:
        print(f"  - {company_type.name} = '{company_type.value}'")
    
    # Test 2: Verify we can look up by value
    print("\n🔍 Testing enum lookup:")
    test_values = ["Customer", "Vendor", "Agent", "National Account"]
    for value in test_values:
        try:
            ct = CompanyType(value)
            print(f"  ✓ CompanyType('{value}') = {ct.name}")
        except ValueError:
            print(f"  ✗ CompanyType('{value}') - NOT FOUND")
    
    # Test 3: Verify ID mapping
    print("\n🆔 Company Type ID mapping:")
    for name, type_id in COMPANY_TYPE_IDS.items():
        print(f"  {name}: {type_id}")
    
    # Test 4: Verify against actual API data
    print("\n🏢 Testing with actual company data:")
    api = ABConnectAPI()
    
    try:
        companies = api.users.access_companies()
        if companies:
            company = companies[0]
            type_id = company.get('typeId')
            
            if type_id:
                print(f"  Company typeId: {type_id}")
                
                # Find the type name from our mapping
                type_name = None
                for name, tid in COMPANY_TYPE_IDS.items():
                    if tid == type_id:
                        type_name = name
                        break
                
                if type_name:
                    print(f"  ✓ Maps to: '{type_name}'")
                    
                    # Verify it's in our enum
                    try:
                        ct = CompanyType(type_name)
                        print(f"  ✓ Valid enum value: {ct.name}")
                    except ValueError:
                        print(f"  ✗ NOT in enum!")
                else:
                    print(f"  ✗ Unknown typeId!")
    except Exception as e:
        print(f"  Error: {e}")
    
    print("\n✅ Test complete!")


if __name__ == '__main__':
    main()