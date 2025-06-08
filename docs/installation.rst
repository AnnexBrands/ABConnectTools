Installation
============

Requirements
------------

ABConnect requires Python 3.11 or higher.

Installing from PyPI
--------------------

The recommended way to install ABConnect is via pip:

.. code-block:: bash

   pip install ABConnect

Development Installation
------------------------

For development, clone the repository and install in editable mode:

.. code-block:: bash

   git clone https://github.com/AnnexBrands/ABConnectTools.git
   cd ABConnectTools
   pip install -e .[dev]

This will install the package along with development dependencies needed for testing and documentation.

Environment Configuration
-------------------------

ABConnect uses environment variables for configuration. You'll need to create two environment files from the sample:

.. code-block:: bash

   # Copy the sample to create both staging and production environment files
   cp .env.sample .env.staging
   cp .env.sample .env

Configuration Variables
~~~~~~~~~~~~~~~~~~~~~~~

Edit both ``.env.staging`` and ``.env`` files with your credentials:

.. code-block:: bash

   # ABC Connect credentials
   ABCONNECT_USERNAME=your_username
   ABCONNECT_PASSWORD=your_password
   ABC_CLIENT_ID=your_app_name
   ABC_CLIENT_SECRET=your_client_secret
   
   # API environment setting
   ABC_ENVIRONMENT=staging  # or 'production' for .env file

.. note::

   To request a client secret for API access, please contact abconnect@annexbrands.com

Environment Usage
~~~~~~~~~~~~~~~~~

- ``.env.staging`` - Used automatically by tests and development
- ``.env`` - Used for production operations

The package will automatically use ``.env.staging`` when running tests via pytest.

Django Integration
------------------

For Django projects, ABConnect supports session-based token storage. Add to your Django settings:

.. code-block:: python

   # In your Django settings.py
   INSTALLED_APPS = [
       # ... other apps
       'ABConnect',
   ]

The API client will automatically use Django's session storage when available.