Examples
========

This section provides practical examples of using ABConnect in various scenarios.

Complete Workflow Example
-------------------------

This example shows a complete workflow from authentication to job creation and tracking:

.. code-block:: python

   from ABConnect.api import APIClient
   from ABConnect.Quoter import Quoter
   from ABConnect.exceptions import ABConnectError
   
   # Initialize clients
   client = APIClient(env='staging')
   quoter = Quoter(env='staging')
   
   try:
       # Authenticate
       client.auth.login(username='your_username', password='your_password')
       
       # Get company information
       company = client.companies.get('COMPANY_CODE')
       print(f"Working with company: {company['name']}")
       
       # Create a quote request
       job_id = quoter.qr(
           customer_id=company['id'],
           origin_address={
               'street': '123 Main St',
               'city': 'New York',
               'state': 'NY',
               'zip': '10001'
           },
           destination_address={
               'street': '456 Oak Ave',
               'city': 'Los Angeles',
               'state': 'CA',
               'zip': '90001'
           },
           items=[
               {'description': 'Furniture', 'weight': 500, 'value': 1000},
               {'description': 'Electronics', 'weight': 100, 'value': 2000}
           ],
           auto_book=True
       )
       
       print(f"Job created: {job_id}")
       
       # Get job details
       job = client.jobs.get(job_id)
       print(f"Job status: {job['status']}")
       
       # Update task timeline
       client.tasks.schedule(
           jobid=job_id,
           start='2024-01-15T09:00:00',
           end='2024-01-15T17:00:00',
           createEmail=True
       )
       
       # Upload documents
       with open('invoice.pdf', 'rb') as f:
           client.docs.upload(
               jobid=job_id,
               files=[('file', f)],
               data={'description': 'Customer Invoice'}
           )
       
   except ABConnectError as e:
       print(f"Error: {e}")
   finally:
       # Always logout
       client.auth.logout()

Bulk Data Processing
--------------------

Process multiple files and create jobs in bulk:

.. code-block:: python

   from ABConnect.Loader import FileLoader
   from ABConnect.api import APIClient
   from ABConnect.Builder import APIRequestBuilder
   import pandas as pd
   
   # Initialize components
   loader = FileLoader()
   client = APIClient(env='production')
   builder = APIRequestBuilder()
   
   # Load shipment data
   shipments_df = loader.load('shipments.csv')
   
   # Process each shipment
   results = []
   for idx, row in shipments_df.iterrows():
       try:
           # Build request
           request = builder.build(
               customer_id=row['customer_id'],
               job_type=row['job_type'],
               origin_zip=row['origin_zip'],
               destination_zip=row['destination_zip'],
               weight=row['weight'],
               declared_value=row['value']
           )
           
           # Create job
           response = client.jobs.create(request)
           results.append({
               'shipment_id': row['shipment_id'],
               'job_id': response['id'],
               'status': 'created'
           })
           
       except Exception as e:
           results.append({
               'shipment_id': row['shipment_id'],
               'job_id': None,
               'status': f'error: {str(e)}'
           })
   
   # Save results
   results_df = pd.DataFrame(results)
   results_df.to_csv('job_creation_results.csv', index=False)

Django Integration
------------------

Example Django view using ABConnect:

.. code-block:: python

   # views.py
   from django.shortcuts import render, redirect
   from django.contrib import messages
   from ABConnect.api import APIClient
   from ABConnect.exceptions import ABConnectError
   
   def create_shipment(request):
       if request.method == 'POST':
           client = APIClient(env='production')
           
           try:
               # Login using session storage
               if not request.session.get('abc_token'):
                   client.auth.login(
                       username=settings.ABC_USERNAME,
                       password=settings.ABC_PASSWORD
                   )
               
               # Create shipment from form data
               job_data = {
                   'customer_id': request.POST['customer_id'],
                   'origin_address': {
                       'street': request.POST['origin_street'],
                       'city': request.POST['origin_city'],
                       'state': request.POST['origin_state'],
                       'zip': request.POST['origin_zip']
                   },
                   'destination_address': {
                       'street': request.POST['dest_street'],
                       'city': request.POST['dest_city'],
                       'state': request.POST['dest_state'],
                       'zip': request.POST['dest_zip']
                   },
                   'items': []
               }
               
               # Add items
               for i in range(int(request.POST.get('item_count', 0))):
                   job_data['items'].append({
                       'description': request.POST[f'item_{i}_desc'],
                       'weight': float(request.POST[f'item_{i}_weight']),
                       'value': float(request.POST[f'item_{i}_value'])
                   })
               
               # Create job
               job = client.jobs.create(job_data)
               
               messages.success(request, f"Shipment created: {job['id']}")
               return redirect('shipment_detail', job_id=job['id'])
               
           except ABConnectError as e:
               messages.error(request, f"Failed to create shipment: {e}")
               return redirect('create_shipment')
       
       return render(request, 'create_shipment.html')

Custom Error Handling
---------------------

Implement custom error handling and retry logic:

.. code-block:: python

   import time
   from functools import wraps
   from ABConnect.exceptions import ABConnectError
   
   def retry_on_error(max_retries=3, delay=1):
       """Decorator to retry API calls on failure"""
       def decorator(func):
           @wraps(func)
           def wrapper(*args, **kwargs):
               last_error = None
               for attempt in range(max_retries):
                   try:
                       return func(*args, **kwargs)
                   except ABConnectError as e:
                       last_error = e
                       if e.status_code in [500, 502, 503, 504]:
                           # Retry on server errors
                           time.sleep(delay * (attempt + 1))
                           continue
                       else:
                           # Don't retry on client errors
                           raise
               raise last_error
           return wrapper
       return decorator
   
   # Usage
   @retry_on_error(max_retries=3, delay=2)
   def create_job_with_retry(client, job_data):
       return client.jobs.create(job_data)

Async Operations
----------------

Example using asyncio for concurrent operations:

.. code-block:: python

   import asyncio
   from concurrent.futures import ThreadPoolExecutor
   from ABConnect.api import APIClient
   
   async def process_jobs_async(job_ids):
       """Process multiple jobs concurrently"""
       client = APIClient(env='production')
       client.auth.login(username='user', password='pass')
       
       # Create thread pool for sync API calls
       executor = ThreadPoolExecutor(max_workers=10)
       loop = asyncio.get_event_loop()
       
       # Define async wrapper
       async def get_job_async(job_id):
           return await loop.run_in_executor(
               executor, 
               client.jobs.get, 
               job_id
           )
       
       # Process all jobs concurrently
       tasks = [get_job_async(job_id) for job_id in job_ids]
       results = await asyncio.gather(*tasks, return_exceptions=True)
       
       # Process results
       successful = []
       failed = []
       for job_id, result in zip(job_ids, results):
           if isinstance(result, Exception):
               failed.append((job_id, str(result)))
           else:
               successful.append(result)
       
       return successful, failed
   
   # Usage
   job_ids = ['job1', 'job2', 'job3', ...]
   successful, failed = asyncio.run(process_jobs_async(job_ids))