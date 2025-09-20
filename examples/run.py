#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ABConnect API examples and testing runner.

This module provides example functions for testing ABConnect API functionality
using the new schema-first endpoint structure.
"""

import sys
from pathlib import Path

# Add parent directory to path for importing ABConnect
sys.path.insert(0, str(Path(__file__).parent.parent))

from ABConnect import ABConnectAPI
from ABConnect.config import Config


def me():
    """Get current user profile information.
    
    Returns:
        UserProfile model with typed access to profile data
        
    Example:
        >>> profile = me()
        >>> print(f"User: {profile.contact_info.full_name}")
        >>> print(f"Email: {profile.contact_info.primary_email}")
    """
    api = ABConnectAPI()
    profile = api.account.get_profile()
    
    # Demonstrate typed access (when models work)
    print("📋 Profile Summary:")
    if isinstance(profile, dict):
        # Fallback to dict access
        print(f"   User: {profile.get('userName', 'Unknown')}")
        print(f"   Email: {profile.get('email', 'Unknown')}")
        contact_info = profile.get('contactInfo', {})
        print(f"   Full Name: {contact_info.get('fullName', 'Unknown')}")
        print(f"   Company: {contact_info.get('company', {}).get('companyName', 'Unknown')}")
    else:
        # When Pydantic models work, use typed access
        print(f"   User: {getattr(profile, 'user_name', 'Unknown')}")
        print(f"   Email: {getattr(profile, 'email', 'Unknown')}")
    
    return profile


def get_companies():
    """Get available companies for current user.
    
    Returns:
        dict: Companies data
    """
    api = ABConnectAPI()
    return api.companies.get_availablebycurrentuser()


def get_company_types():
    """Get company types lookup data.
    
    Returns:
        dict: Company types lookup data
    """
    api = ABConnectAPI()
    return api.lookup.get_masterconstant(masterConstantKey="CompanyTypes")


def get_user_roles():
    """Get available user roles.
    
    Returns:
        dict: User roles data
    """
    api = ABConnectAPI()
    return api.users.get_roles()


def run(func):
    """Execute a function and display results.
    
    Args:
        func: Function to execute (can be string name or callable)
        
    Example:
        >>> run(me)
        >>> run('get_companies')
    """
    # Handle string function names
    if isinstance(func, str):
        func_name = func
        if func_name not in globals():
            print(f"❌ Function '{func_name}' not found")
            print("Available functions:")
            funcs = [name for name, obj in globals().items() 
                    if callable(obj) and not name.startswith('_') and name != 'run']
            for func_name in sorted(funcs):
                print(f"  {func_name}")
            sys.exit(1)
        func = globals()[func_name]
    
    # Get function name for display
    func_name = getattr(func, '__name__', str(func))
    
    print(f"🔄 Executing {func_name}()...")
    
    try:
        result = func()
        print("✅ Function executed successfully")
        
        if isinstance(result, dict):
            import json
            print(json.dumps(result, indent=2))
        else:
            print(str(result))
            
    except Exception as e:
        print(f"❌ Error executing {func_name}: {e}")
        
        # Provide helpful context
        if "404" in str(e):
            print("💡 This might be due to:")
            print("   - Missing authentication")
            print("   - Incorrect API endpoint")
            print("   - Different environment (staging vs production)")
        elif "401" in str(e) or "403" in str(e):
            print("💡 This is an authentication/authorization error")
            print("   - Check your credentials in .env.staging")
            print("   - Ensure you have proper permissions")
        
        sys.exit(1)


def main():
    """Main entry point for command line usage."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="ABConnect API examples runner"
    )
    parser.add_argument(
        "function", 
        help="Function to execute (me, get_companies, get_company_types, get_user_roles)"
    )
    parser.add_argument(
        "--env", 
        choices=["staging", "production"], 
        help="Environment to use"
    )
    
    args = parser.parse_args()
    
    # Set environment if specified
    if args.env:
        Config.load(f".env.{args.env}")
        print(f"🌍 Using {args.env} environment")
    
    # Execute the function
    run(args.function)


if __name__ == "__main__":
    main()