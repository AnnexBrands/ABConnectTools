API Reference
=============

This section provides detailed documentation for using ABConnect API endpoints.

.. contents:: Table of Contents
   :local:
   :depth: 2

API Access Methods
------------------

Raw API Access
~~~~~~~~~~~~~~

Direct access to any API endpoint:

.. code-block:: bash

   # Basic GET request
   ab api raw get /api/companies/{id} id=123e4567-e89b-12d3-a456-426614174000

   # GET with query parameters  
   ab api raw get /api/companies/search page=1 per_page=20 name=ABC

   # POST with data
   ab api raw post /api/jobs data=@job.json

   # PUT with inline data
   ab api raw put /api/contacts/{id} id=123 data='{"name":"John Doe"}'

   # DELETE request
   ab api raw delete /api/jobs/{id} id=JOB-2024-001

Python Usage
~~~~~~~~~~~~

.. code-block:: python

   from ABConnect import ABConnectAPI
   
   api = ABConnectAPI()
   
   # Raw API access
   result = api.raw.get('/api/companies/search', page=1, per_page=20)
   
   # Tagged resource access
   companies = api.companies.search(name='ABC', active=True)
   
   # Friendly method access
   company = api.companies.get_by_code('ABC123')

Authentication
--------------

.. autoclass:: ABConnect.api.auth.TokenStorage
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: ABConnect.api.auth.FileTokenStorage
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: ABConnect.api.auth.SessionTokenStorage
   :members:
   :undoc-members:
   :show-inheritance:

API Client
----------

.. autoclass:: ABConnect.api.client.ABConnectAPI
   :members:
   :undoc-members:
   :show-inheritance:

Generic Endpoints
-----------------

.. autoclass:: ABConnect.api.generic.GenericEndpoint
   :members:
   :undoc-members:
   :show-inheritance:

Query Builder
-------------

.. autoclass:: ABConnect.api.query.QueryBuilder
   :members:
   :undoc-members:
   :show-inheritance:

Swagger Parser
--------------

.. autoclass:: ABConnect.api.swagger.SwaggerParser
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: ABConnect.api.swagger.EndpointDefinition
   :members:
   :undoc-members:
   :show-inheritance:

Response Models
---------------

.. automodule:: ABConnect.api.models
   :members:
   :undoc-members:
   :show-inheritance:

Endpoints
---------

The endpoint classes provide specific functionality for different API resources.
For detailed documentation of each endpoint, see the API module documentation.

.. _companies:

Companies
~~~~~~~~~

.. autoclass:: ABConnect.api.endpoints.companies.CompaniesEndpoint
   :members:
   :noindex:

.. _contacts:

Contacts
~~~~~~~~

.. autoclass:: ABConnect.api.endpoints.contacts.ContactsEndpoint
   :members:
   :noindex:

.. _documents:

Documents
~~~~~~~~~

.. autoclass:: ABConnect.api.endpoints.docs.DocsEndpoint
   :members:
   :noindex:

.. _forms:

Forms
~~~~~

.. autoclass:: ABConnect.api.endpoints.forms.FormsEndpoint
   :members:
   :noindex:

.. _items:

Items
~~~~~

.. autoclass:: ABConnect.api.endpoints.items.ItemsEndpoint
   :members:
   :noindex:

.. _jobs:

Jobs
~~~~

.. autoclass:: ABConnect.api.endpoints.jobs.JobsEndpoint
   :members:
   :noindex:

.. _tasks:

Tasks
~~~~~

.. autoclass:: ABConnect.api.endpoints.tasks.TasksEndpoint
   :members:
   :noindex:

.. _users:

Users
~~~~~

.. autoclass:: ABConnect.api.endpoints.users.UsersEndpoint
   :members:
   :noindex:

HTTP Client
-----------

.. automodule:: ABConnect.api.http
   :members:
   :undoc-members:
   :show-inheritance:

Exceptions
----------

.. automodule:: ABConnect.exceptions
   :members:
   :undoc-members:
   :show-inheritance: