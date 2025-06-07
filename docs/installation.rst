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

   git clone <repository-url>
   cd ABConnectTools
   pip install -e .[dev]

This will install the package along with development dependencies needed for testing and documentation.

Environment Configuration
-------------------------

ABConnect uses environment variables for configuration. Create a ``.env`` file in your project root:

.. code-block:: bash

   # Copy the sample environment file
   cp ABConnect/dotenv.sample .env

Then edit the ``.env`` file with your configuration:

.. code-block:: bash

   # API Configuration
   API_BASE_URL=https://api.example.com
   API_TOKEN=your-api-token
   
   # Environment (staging or production)
   ENVIRONMENT=staging

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