#!/usr/bin/env python3
"""Debug the lookup endpoint to understand its structure."""

from ABConnect.api import ABConnectAPI
from ABConnect.config import Config
import json


def main():
    Config.load('.env.staging', force_reload=True)
    print(f"🔌 Using {Config.get_env()} environment")
    
    api = ABConnectAPI()
    
    print("\n🔍 Debugging lookup endpoint...")
    
    # First check what class the lookup endpoint is
    if hasattr(api, 'lookup'):
        print(f"  lookup endpoint type: {type(api.lookup)}")
        print(f"  lookup endpoint class: {api.lookup.__class__.__name__}")
        
        # Check the base URL
        if hasattr(api.lookup, '_r'):
            print(f"  Base URL: {api.lookup._r.base_url}")
            
        # Try the exact paths from swagger
        test_paths = [
            'api/lookup/CompanyTypes',  # Full path
            'lookup/CompanyTypes',       # Without /api prefix
            'CompanyTypes',              # Just the key
            '/CompanyTypes',             # With leading slash
        ]
        
        print("\n  Testing different path formats:")
        for path in test_paths:
            try:
                print(f"\n  Trying: {path}")
                result = api.lookup.raw('GET', path)
                print(f"  ✓ Success! Response type: {type(result)}")
                if isinstance(result, (dict, list)):
                    print(f"  Response: {json.dumps(result, indent=2)[:300]}...")
                else:
                    print(f"  Response: {str(result)[:300]}...")
                return result
            except Exception as e:
                print(f"  ✗ Error: {e}")
        
        # Try using the standard get method
        print("\n  Trying standard get method:")
        try:
            result = api.lookup.get('CompanyTypes')
            print(f"  ✓ Success with get()!")
            print(f"  Response: {json.dumps(result, indent=2)[:300]}...")
        except Exception as e:
            print(f"  ✗ Error: {e}")
            
    else:
        print("  ❌ No lookup endpoint found!")
        
    # Check what generic endpoints were created
    if hasattr(api, '_generic_endpoints'):
        print(f"\n📋 Generic endpoints: {list(api._generic_endpoints.keys())[:10]}...")
        
    print("\n✅ Debug complete!")


if __name__ == '__main__':
    main()