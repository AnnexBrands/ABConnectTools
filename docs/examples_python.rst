Python Library Examples
=======================

This section provides practical examples of using ABConnect as a Python library.

.. contents::
   :local:
   :depth: 2

Quick Start Examples
--------------------

Basic API Usage
~~~~~~~~~~~~~~~

.. code-block:: python

   from ABConnect import ABConnectAPI
   
   # Initialize API client
   api = ABConnectAPI()
   
   # Get current user
   user = api.raw.get('/api/account/profile')
   print(f"Logged in as: {user['email']}")
   
   # Search companies
   companies = api.raw.get('/api/companies/search', page=1, per_page=10)
   for company in companies:
       print(f"{company['name']} ({company['code']})")

Working with Companies
----------------------

Search and Filter
~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Search by name
   results = api.raw.get('/api/companies/search', 
       name='ABC Corp',
       active=True
   )
   
   # Get company details
   company_id = results[0]['id']
   details = api.raw.get(f'/api/companies/{company_id}/details')
   
   # Get company setup data
   setup = api.raw.get(f'/api/company/{company_id}/setupdata')

Managing Contacts
~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Get contacts for a company
   contacts = api.raw.get('/api/contacts/search', companyId=company_id)
   
   # Create new contact
   new_contact = api.raw.post('/api/contacts', data={
       'firstName': 'John',
       'lastName': 'Doe',
       'email': 'john.doe@example.com',
       'companyId': company_id
   })
   
   # Update contact
   api.raw.put(f'/api/contacts/{contact_id}', data={
       'phone': '+1-555-123-4567'
   })

Working with Jobs
-----------------

Creating and Managing Jobs
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Create a new job
   job_data = {
       'type': 'Standard',
       'customerId': customer_id,
       'origin': {
           'address': '123 Main St',
           'city': 'New York',
           'state': 'NY',
           'zip': '10001'
       },
       'destination': {
           'address': '456 Oak Ave',
           'city': 'Los Angeles',
           'state': 'CA',
           'zip': '90001'
       }
   }
   
   job = api.raw.post('/api/job/save', data=job_data)
   job_id = job['jobDisplayId']
   
   # Get job details
   details = api.raw.get(f'/api/job/{job_id}')
   
   # Update job status
   api.raw.post(f'/api/job/{job_id}/status/quote', data={
       'status': 'Quoted'
   })

Job Timeline Management
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Get timeline
   timeline = api.raw.get(f'/api/job/{job_id}/timeline')
   
   # Add timeline task
   task = api.raw.post(f'/api/job/{job_id}/timeline', data={
       'type': 'Pickup',
       'scheduledDate': '2024-01-15T10:00:00Z',
       'duration': 60
   })
   
   # Update timeline task
   api.raw.patch(f'/api/job/{job_id}/timeline/{task_id}', data={
       'completed': True
   })

Lookup Values
-------------

Master Constants
~~~~~~~~~~~~~~~~

.. code-block:: python

   # Get all company types
   company_types = api.raw.get('/api/lookup/CompanyTypes')
   for ct in company_types:
       print(f"{ct['name']} - {ct['id']}")
   
   # Get job status types
   job_statuses = api.raw.get('/api/lookup/JobsStatusTypes')
   
   # Get countries
   countries = api.raw.get('/api/lookup/countries')

File Operations
---------------

Loading Files
~~~~~~~~~~~~~

.. code-block:: python

   from ABConnect import FileLoader
   
   loader = FileLoader()
   
   # Load CSV
   df = loader.load('data.csv')
   print(f"Loaded {len(df)} rows")
   
   # Load Excel
   excel_data = loader.load('report.xlsx', sheet_name='Sheet1')
   
   # Load JSON
   json_data = loader.load('config.json')

Quoting
-------

Quick Quote
~~~~~~~~~~~

.. code-block:: python

   from ABConnect import Quoter
   
   quoter = Quoter(type='qq')
   
   # Get a quick quote
   quote = quoter.qq(
       customer_id='CUST123',
       origin_zip='10001',
       destination_zip='90001',
       weight=1000,
       pieces=5
   )
   
   print(f"Quote ID: {quote['id']}")
   print(f"Total: ${quote['total']}")

Quote Request
~~~~~~~~~~~~~

.. code-block:: python

   # Create a quote request
   quoter = Quoter(type='qr', auto_book=True)
   
   quote_request = quoter.qr(
       customer_id='CUST123',
       origin_zip='10001',
       destination_zip='90001',
       items=[
           {'weight': 500, 'class': '85'},
           {'weight': 300, 'class': '70'}
       ]
   )

Error Handling
--------------

Handling API Errors
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from ABConnect.exceptions import ABConnectError, RequestError
   
   try:
       company = api.raw.get('/api/companies/invalid-id')
   except RequestError as e:
       if e.status_code == 404:
           print("Company not found")
       else:
           print(f"API error: {e.message}")
   except ABConnectError as e:
       print(f"ABConnect error: {e}")

Pagination
----------

Handling Paginated Results
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Get all companies with pagination
   all_companies = []
   page = 1
   per_page = 100
   
   while True:
       results = api.raw.get('/api/companies/search', 
           page=page, 
           per_page=per_page
       )
       
       if not results:
           break
           
       all_companies.extend(results)
       
       # Check if we have more pages
       if len(results) < per_page:
           break
           
       page += 1
   
   print(f"Retrieved {len(all_companies)} companies")

Advanced Usage
--------------

Bulk Operations
~~~~~~~~~~~~~~~

.. code-block:: python

   # Bulk update contacts
   contacts_to_update = [
       {'id': '123', 'phone': '+1-555-111-1111'},
       {'id': '456', 'phone': '+1-555-222-2222'},
       {'id': '789', 'phone': '+1-555-333-3333'}
   ]
   
   for contact in contacts_to_update:
       api.raw.put(f"/api/contacts/{contact['id']}", data={
           'phone': contact['phone']
       })
       print(f"Updated contact {contact['id']}")

Custom Headers
~~~~~~~~~~~~~~

.. code-block:: python

   # Use custom headers
   response = api._request_handler.call(
       'GET',
       'companies/search',
       headers={'X-Custom-Header': 'value'},
       params={'page': 1}
   )

Environment Configuration
-------------------------

Switching Environments
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Use staging environment
   from ABConnect import ABConnectAPI
   
   api_staging = ABConnectAPI(env='staging')
   
   # Or configure via environment variable
   import os
   os.environ['ABC_ENVIRONMENT'] = 'staging'
   api = ABConnectAPI()

Django Integration
------------------

Session-Based Authentication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # In Django view
   from ABConnect import ABConnectAPI
   
   def my_view(request):
       # Use Django session for token storage
       api = ABConnectAPI(request=request)
       
       # API calls will use session-stored tokens
       user = api.raw.get('/api/account/profile')
       
       return render(request, 'template.html', {'user': user})

Using Generic Endpoints
-----------------------

Automatic Endpoint Discovery
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from ABConnect.api.generic import GenericEndpoints
   
   # Initialize with automatic discovery
   endpoints = GenericEndpoints()
   
   # Access any endpoint dynamically
   response = endpoints.companies.search(page=1, per_page=10)
   
   # Or use path-style access
   response = endpoints.call('companies/search', page=1)

Query Builder
~~~~~~~~~~~~~

.. code-block:: python

   from ABConnect.api.query import QueryBuilder
   
   # Build complex queries
   query = QueryBuilder()
   results = (query
       .filter(status='active')
       .filter(created_after='2024-01-01')
       .sort_by('created_at', desc=True)
       .limit(50)
       .page(1)
       .execute('/api/jobs/search'))

Response Models
~~~~~~~~~~~~~~~

.. code-block:: python

   # Responses are automatically parsed into Pydantic models
   companies = endpoints.companies.search()
   
   # Access fields with type safety
   for company in companies:
       print(f"ID: {company.id}")
       print(f"Name: {company.name}")
       print(f"Created: {company.created_at}")

See Also
--------

- :doc:`api_reference` - Complete API class reference
- :doc:`modules/index` - Detailed module documentation
- :doc:`quickstart_python` - Getting started with the Python library