"""Demonstration of generic endpoint functionality in ABConnect v0.1.8.

This example shows how to use the new generic endpoint system that
automatically generates API methods from the OpenAPI specification.
"""

from ABConnect.api import ABConnectAPI


def main():
    """Demonstrate generic endpoint features."""
    
    # Initialize API client with generic endpoints enabled
    api = ABConnectAPI(enable_generic=True)
    
    print("ABConnect Generic Endpoints Demo")
    print("=" * 50)
    
    # 1. Show available endpoints
    print("\n1. Available Endpoints:")
    print(f"   Total endpoints: {len(api.available_endpoints)}")
    print(f"   First 10: {api.available_endpoints[:10]}")
    
    # 2. Use standard REST methods
    print("\n2. Standard REST Methods:")
    print("   These work on any endpoint automatically:")
    
    # Example: List companies
    print("\n   # List companies")
    print("   companies = api.companies.list(page=1, per_page=5)")
    
    # Example: Get specific company
    print("\n   # Get specific company")
    print("   company = api.companies.get('company-id')")
    
    # Example: Create new resource
    print("\n   # Create new resource")
    print("   new_item = api.items.create({'name': 'New Item', 'type': 'freight'})")
    
    # 3. Use the Query Builder
    print("\n3. Query Builder Pattern:")
    print("   Build complex queries with method chaining:")
    
    print("""
   # Filter, sort, and paginate
   results = api.companies.query()\\
       .filter(type='Customer', active=True)\\
       .sort('name', 'asc')\\
       .page(2, per_page=25)\\
       .execute()
   """)
    
    print("""
   # Search with field selection
   results = api.contacts.query()\\
       .search('john')\\
       .select('id', 'firstName', 'lastName', 'email')\\
       .limit(10)\\
       .execute()
   """)
    
    print("""
   # Complex filtering
   results = api.jobs.query()\\
       .where('created', 'gte', '2024-01-01')\\
       .where('status', 'in', ['active', 'pending'])\\
       .expand('items', 'tasks')\\
       .execute()
   """)
    
    # 4. Access any endpoint dynamically
    print("\n4. Dynamic Endpoint Access:")
    print("   Access any endpoint from the API spec, even if not manually implemented:")
    
    print("""
   # Access endpoints not in manual implementation
   # (These are discovered from swagger.json)
   
   # Address validation endpoint
   validation = api.address.is_valid(
       Line1='123 Main St',
       City='New York',
       State='NY',
       Zip='10001'
   )
   
   # Carrier error messages
   errors = api.admin.carrier_error_message.list()
   
   # Calendar endpoints
   calendar = api.calendar.get(
       companyId='company-uuid',
       date='2024-01-15'
   )
   """)
    
    # 5. Raw API access
    print("\n5. Raw API Access:")
    print("   For full control or undocumented endpoints:")
    
    print("""
   # Direct API call
   result = api.raw('GET', '/api/companies/search', 
                    params={'q': 'test'})
   
   # Or through an endpoint
   result = api.companies.raw('GET', '/search',
                              params={'q': 'test'})
   """)
    
    # 6. Backwards compatibility
    print("\n6. Backwards Compatibility:")
    print("   All existing code continues to work:")
    
    print("""
   # Original manual methods still work
   company = api.companies.get('COMPANY_CODE')  # By code
   company = api.companies.get_id('uuid')       # By ID
   
   # Task-specific methods
   api.tasks.schedule(jobid, '2024-01-20T09:00:00')
   api.tasks.pack_start(jobid, '2024-01-20T10:00:00')
   """)
    
    # 7. Advanced features
    print("\n7. Advanced Features:")
    
    print("""
   # Iterate through all results (automatic pagination)
   for company in api.companies.query().filter(type='Customer'):
       print(company['name'])
   
   # Get first result only
   first_active = api.jobs.query()\\
       .filter(status='active')\\
       .sort('-created')\\
       .first()
   
   # Check if results exist
   has_pending = api.tasks.query()\\
       .filter(status='pending')\\
       .exists()
   
   # Get count without fetching data
   total_customers = api.companies.query()\\
       .filter(type='Customer')\\
       .count()
   """)
    
    print("\n" + "=" * 50)
    print("With generic endpoints, you have immediate access to all 223+ API")
    print("endpoints without waiting for manual implementation!")


if __name__ == '__main__':
    main()