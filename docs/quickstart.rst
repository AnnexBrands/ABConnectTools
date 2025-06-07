Quick Start Guide
=================

This guide will help you get started with ABConnect quickly.

Basic Usage
-----------

API Client
~~~~~~~~~~

Initialize the API client and authenticate:

.. code-block:: python

   from ABConnect.api import APIClient
   
   # Initialize client
   client = APIClient(env='staging')  # or 'production'
   
   # Authenticate
   client.auth.login(username='your_username', password='your_password')
   
   # Get user information
   user_info = client.users.me()
   print(user_info)

Working with Companies
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Get company by code
   company = client.companies.get('COMPANY_CODE')
   
   # Get company by ID
   company = client.companies.get_id('company-uuid')
   
   # Get accessible companies
   companies = client.users.access_companies()

Working with Jobs
~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Get job details
   job = client.jobs.get('job-id')
   
   # Change job agent
   client.jobs.change_agent(
       jobid='job-id',
       CompanyCode='NEW_AGENT_CODE',
       serviceType='service-type',
       recalculatePrice=True,
       applyRebate=False
   )

Using the Builder
-----------------

The Builder module helps construct API requests:

.. code-block:: python

   from ABConnect import Builder
   
   # Initialize builder
   builder = Builder.APIRequestBuilder()
   
   # Build a request
   request_data = builder.build(
       customer_id='123',
       job_type='Regular',
       # ... other parameters
   )

Using the Loader
----------------

Load data from various file formats:

.. code-block:: python

   from ABConnect import Loader
   
   # Initialize loader
   loader = Loader.FileLoader()
   
   # Load CSV file
   df = loader.load('data.csv')
   
   # Load Excel file with specific sheet
   df = loader.load('data.xlsx', sheet_name='Sheet1')
   
   # Load JSON file
   data = loader.load('data.json')

Using the Quoter
----------------

Get quotes from the ABC API:

.. code-block:: python

   from ABConnect import Quoter
   
   # Initialize quoter
   quoter = Quoter.Quoter(env='staging')
   
   # Quick quote
   quote_response = quoter.qq(
       customer_id='123',
       origin_zip='12345',
       destination_zip='67890',
       # ... other parameters
   )
   
   # Quote request (returns job ID)
   job_id = quoter.qr(
       customer_id='123',
       origin_zip='12345',
       destination_zip='67890',
       # ... other parameters
   )

Error Handling
--------------

ABConnect uses custom exceptions for error handling:

.. code-block:: python

   from ABConnect.exceptions import ABConnectError
   
   try:
       result = client.companies.get('INVALID_CODE')
   except ABConnectError as e:
       print(f"API Error: {e}")

Next Steps
----------

* Review the :doc:`api_reference` for detailed API documentation
* Check out :doc:`examples` for more complex use cases
* See :doc:`modules/index` for detailed module documentation