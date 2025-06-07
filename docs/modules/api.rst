API Module
==========

The API module provides a comprehensive client for interacting with the Annex Brands ABC API.

.. automodule:: ABConnect.api
   :members:
   :undoc-members:
   :show-inheritance:

Overview
--------

The API module is organized into several components:

* **APIClient** - Main client class that provides access to all endpoints
* **Auth** - Authentication and token management
* **HTTP** - Low-level HTTP request handling
* **Endpoints** - Specific endpoint implementations

APIClient
---------

.. autoclass:: ABConnect.api.client.ABConnectAPI
   :members:
   :undoc-members:
   :show-inheritance:
   :noindex:

Usage Example
~~~~~~~~~~~~~

.. code-block:: python

   from ABConnect.api import APIClient
   
   # Initialize client
   client = APIClient(env='staging')
   
   # Authenticate
   client.auth.login(username='user', password='pass')
   
   # Access endpoints
   companies = client.companies.get('COMPANY_CODE')
   jobs = client.jobs.get('job-id')
   user = client.users.me()

Authentication
--------------

The API supports multiple authentication methods:

Token-Based Authentication
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Login and get token
   client.auth.login(username='user', password='pass')
   
   # Token is automatically stored and used for requests
   # Logout when done
   client.auth.logout()

Session-Based Authentication (Django)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When used in a Django environment, tokens are automatically stored in the session:

.. code-block:: python

   # In a Django view
   client = APIClient(env='production')
   client.auth.login(username=request.POST['username'], 
                     password=request.POST['password'])
   
   # Token is stored in request.session

Token Storage
~~~~~~~~~~~~~

The API client supports flexible token storage:

* **File-based storage** - Default for standalone usage
* **Session-based storage** - Automatic when Django is detected
* **Custom storage** - Implement your own token storage backend

Environment Configuration
-------------------------

.. code-block:: python

   # Staging environment
   staging_client = APIClient(env='staging')
   
   # Production environment
   prod_client = APIClient(env='production')
   
   # Custom base URL
   custom_client = APIClient(base_url='https://custom.api.com')

Error Handling
--------------

All API errors are raised as `ABConnectError`:

.. code-block:: python

   from ABConnect.exceptions import ABConnectError
   
   try:
       result = client.companies.get('INVALID')
   except ABConnectError as e:
       print(f"API Error: {e.message}")
       print(f"Status Code: {e.status_code}")
       print(f"Response: {e.response}")

Endpoint Documentation
----------------------

See the :doc:`/api_reference` for detailed documentation of each endpoint.