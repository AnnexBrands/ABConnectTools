CLI Quick Start
===============

This guide will help you get started with the ABConnect command-line interface.

Prerequisites
-------------

1. Install ABConnect:

   .. code-block:: bash

      pip install ABConnect

2. Set up your environment files:

   .. code-block:: bash

      cp .env.sample .env.staging
      cp .env.sample .env

3. Edit the files with your credentials:

   .. code-block:: bash

      # Edit .env.staging for testing
      ABCONNECT_USERNAME=your_username
      ABCONNECT_PASSWORD=your_password
      ABC_CLIENT_ID=your_app_name
      ABC_CLIENT_SECRET=your_client_secret
      ABC_ENVIRONMENT=staging

.. note::

   Contact abconnect@annexbrands.com to request a client secret.

First Steps
-----------

Verify Installation
~~~~~~~~~~~~~~~~~~~

Check that the CLI is installed correctly:

.. code-block:: bash

   ab --version

Test Authentication
~~~~~~~~~~~~~~~~~~~

Verify your credentials are working:

.. code-block:: bash

   ab me

This should display your user information if authentication is successful.

Common Tasks
------------

Looking Up Reference Data
~~~~~~~~~~~~~~~~~~~~~~~~~

Get company types:

.. code-block:: bash

   ab lookup company-types

Get other lookup values:

.. code-block:: bash

   ab lookup job-status-types
   ab lookup freight-types
   ab lookup container-types

Working with Companies
~~~~~~~~~~~~~~~~~~~~~~

Get company information by ID:

.. code-block:: bash

   ab company 12345

Search for companies:

.. code-block:: bash

   ab api raw GET /companies/search --params '{"name": "ABC", "active": true}'

Loading Data Files
~~~~~~~~~~~~~~~~~~

Load and view a CSV file:

.. code-block:: bash

   ab load contacts.csv

Convert to JSON:

.. code-block:: bash

   ab load contacts.csv --format json > contacts.json

Load Excel files:

.. code-block:: bash

   ab load report.xlsx --sheet "Data"

Making API Calls
~~~~~~~~~~~~~~~~

The ``ab api raw`` command lets you make any API call:

.. code-block:: bash

   # GET request
   ab api raw GET /companies/12345
   
   # POST request with data
   ab api raw POST /contacts --data '{"firstName": "John", "lastName": "Doe"}'
   
   # GET with query parameters
   ab api raw GET /jobs/search --params '{"status": "active", "page": 1}'

Output Formats
--------------

JSON Output
~~~~~~~~~~~

Many commands support JSON output for scripting:

.. code-block:: bash

   ab lookup company-types --format json
   ab endpoints --format json

Using with jq
~~~~~~~~~~~~~

Process JSON output with jq:

.. code-block:: bash

   # Get just company names
   ab api raw GET /companies/search | jq '.[] | .name'
   
   # Count results
   ab lookup company-types --format json | jq '. | length'

Environment Control
-------------------

Using Different Environments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By default, commands use the environment from your .env file. Override with:

.. code-block:: bash

   # Use staging
   ABC_ENVIRONMENT=staging ab company 12345
   
   # Use production
   ABC_ENVIRONMENT=production ab company 12345

Debug Mode
~~~~~~~~~~

Enable debug logging for troubleshooting:

.. code-block:: bash

   ABC_LOG_LEVEL=DEBUG ab me

Quick Examples
--------------

Data Export Script
~~~~~~~~~~~~~~~~~~

Export companies to CSV:

.. code-block:: bash

   #!/bin/bash
   ab api raw GET /companies/search --params '{"active": true}' | \
     jq -r '.[] | [.id, .name, .code] | @csv' > companies.csv

Batch Lookup
~~~~~~~~~~~~

Look up multiple values:

.. code-block:: bash

   #!/bin/bash
   for type in company-types job-status-types freight-types; do
     echo "=== $type ==="
     ab lookup $type
     echo
   done

Next Steps
----------

- See :doc:`cli` for complete command reference
- Review :doc:`examples_cli` for more examples
- Check :doc:`api/index` for available endpoints

Getting Help
------------

- Use ``ab --help`` for general help
- Use ``ab <command> --help`` for command-specific help
- Report issues at https://github.com/anthropics/claude-code/issues