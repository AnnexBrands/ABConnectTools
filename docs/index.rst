.. ABConnect documentation master file

ABConnect Documentation
=======================

ABConnect is a Python package for Annex Brands data processing and API interactions.

.. toctree::
   :maxdepth: 2
   :caption: Getting Started:

   installation
   quickstart_python
   quickstart_cli

.. toctree::
   :maxdepth: 2
   :caption: Command Line Interface:

   cli
   examples_cli

.. toctree::
   :maxdepth: 2
   :caption: Python Library:

   api_reference
   modules/index
   examples_python

.. toctree::
   :maxdepth: 2
   :caption: API Documentation:

   api/index
   api_models

.. toctree::
   :maxdepth: 2
   :caption: Reference:

   changelog

Overview
--------

ABConnect provides a comprehensive set of tools for interacting with the Annex Brands ABC API. The package is structured around four main modules:

* **Builder**: Dynamically constructs API requests from static JSON templates
* **Quoter**: Handles ABC API quote operations with Quick Quote and Quote Request modes
* **Loader**: Provides robust file loading for CSV, JSON, and XLSX formats
* **API**: Full-featured API client with endpoint-specific classes

Key Features
------------

* Automatic access to all 223+ API endpoints via generic endpoint system
* Fluent query builder for complex API queries
* Pydantic models for type-safe API responses
* Template-based request construction
* Flexible authentication with token storage
* Support for both staging and production environments
* Comprehensive API endpoint coverage
* Automatic encoding detection for file loading
* Django compatibility for session-based authentication

Requirements
------------

* Python 3.11 or higher
* See ``pyproject.toml`` for full dependency list

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`