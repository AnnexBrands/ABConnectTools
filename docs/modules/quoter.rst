Quoter Module
=============

The Quoter module handles ABC API quote operations with support for Quick Quote (qq) and Quote Request (qr) modes.

.. automodule:: ABConnect.Quoter
   :members:
   :undoc-members:
   :show-inheritance:

Quoter Class
------------

.. autoclass:: ABConnect.Quoter.Quoter
   :members:
   :undoc-members:
   :show-inheritance:
   :special-members: __init__
   :noindex:

Quote Types
-----------

Quick Quote (qq)
~~~~~~~~~~~~~~~~

Quick quotes provide immediate pricing information without creating a job:

.. code-block:: python

   from ABConnect.Quoter import Quoter
   
   quoter = Quoter(env='staging')
   
   # Get a quick quote
   response = quoter.qq(
       customer_id='CUST123',
       origin_zip='10001',
       destination_zip='90001',
       weight=1000,
       declared_value=5000
   )
   
   print(f"Quote Price: ${response['price']}")

Quote Request (qr)
~~~~~~~~~~~~~~~~~~

Quote requests create a job and return a job ID:

.. code-block:: python

   # Create a quote request
   job_id = quoter.qr(
       customer_id='CUST123',
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
           {'description': 'Box 1', 'weight': 50},
           {'description': 'Box 2', 'weight': 75}
       ]
   )
   
   print(f"Job Created: {job_id}")

Auto-Booking
------------

The Quoter supports automatic booking after quote creation:

.. code-block:: python

   # Quote with auto-booking
   job_id = quoter.qr(
       customer_id='CUST123',
       # ... other parameters
       auto_book=True
   )

Integration with Builder
------------------------

The Quoter uses the Builder module internally for request construction:

.. code-block:: python

   # The Quoter automatically uses Builder for request formatting
   # You can also manually build requests if needed
   from ABConnect.Builder import APIRequestBuilder
   
   builder = APIRequestBuilder()
   request_data = builder.build(**quote_params)
   
   # Then use with Quoter
   response = quoter._send_request(request_data)

Error Handling
--------------

.. code-block:: python

   from ABConnect.exceptions import ABConnectError
   
   try:
       response = quoter.qq(invalid_params)
   except ABConnectError as e:
       print(f"Quote failed: {e}")

Environment Configuration
-------------------------

The Quoter supports both staging and production environments:

.. code-block:: python

   # Staging environment (default)
   quoter_staging = Quoter(env='staging')
   
   # Production environment
   quoter_prod = Quoter(env='production')