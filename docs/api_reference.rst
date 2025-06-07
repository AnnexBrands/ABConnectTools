API Reference
=============

This section provides detailed documentation for all ABConnect API endpoints.

.. contents:: Table of Contents
   :local:
   :depth: 2

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