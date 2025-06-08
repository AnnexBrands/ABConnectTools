Command Line Interface
======================

ABConnect provides a comprehensive command-line interface through the ``ab`` command. This guide covers all available commands and their usage.

Installation
------------

After installing ABConnect, the ``ab`` command becomes available in your terminal:

.. code-block:: bash

   pip install ABConnect

Verify the installation:

.. code-block:: bash

   ab --version

Environment Setup
-----------------

The CLI requires environment configuration files. Create them from the sample:

.. code-block:: bash

   cp .env.sample .env.staging
   cp .env.sample .env

Edit both files with your credentials:

.. code-block:: bash

   # ABC Connect credentials
   ABCONNECT_USERNAME=your_username
   ABCONNECT_PASSWORD=your_password
   ABC_CLIENT_ID=your_app_name
   ABC_CLIENT_SECRET=your_client_secret
   
   # API environment setting
   ABC_ENVIRONMENT=staging  # or 'production'

.. note::

   To request a client secret, contact abconnect@annexbrands.com

Available Commands
------------------

Version Information
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   ab --version

Display the current version of ABConnect.

Configuration Management
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   ab config

View and manage your configuration settings.

User Information
~~~~~~~~~~~~~~~~

.. code-block:: bash

   ab me

Get information about the currently authenticated user.

Company Information
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   ab company <company_id>

Retrieve information about a specific company.

**Example:**

.. code-block:: bash

   ab company 12345

Quote Operations
~~~~~~~~~~~~~~~~

.. code-block:: bash

   ab quote <quote_type> [options]

Get shipping quotes. Supports two quote types:

- ``qq`` - Quick Quote
- ``qr`` - Quote Request

**Examples:**

.. code-block:: bash

   # Quick quote
   ab quote qq --origin "New York, NY" --destination "Los Angeles, CA"
   
   # Quote request
   ab quote qr --file quote_data.json

Lookup Values
~~~~~~~~~~~~~

.. code-block:: bash

   ab lookup <type>

Look up master constant values from the API.

**Available lookup types:**

- ``company-types``
- ``contact-types``
- ``job-statuses``
- ``container-types``

**Example:**

.. code-block:: bash

   ab lookup company-types

File Loading
~~~~~~~~~~~~

.. code-block:: bash

   ab load <file_path> [options]

Load and display data from CSV, JSON, or Excel files.

**Options:**

- ``--format`` - Specify output format (json, table, csv)
- ``--encoding`` - Specify file encoding (default: auto-detect)

**Examples:**

.. code-block:: bash

   # Load CSV file
   ab load data.csv
   
   # Load Excel file with specific sheet
   ab load report.xlsx --sheet "Sales Data"
   
   # Output as JSON
   ab load contacts.csv --format json

API Endpoints
~~~~~~~~~~~~~

.. code-block:: bash

   ab endpoints [options]

List all available API endpoints.

**Options:**

- ``--filter`` - Filter endpoints by keyword
- ``--format`` - Output format (list, json)

**Examples:**

.. code-block:: bash

   # List all endpoints
   ab endpoints
   
   # Filter by keyword
   ab endpoints --filter company
   
   # Output as JSON
   ab endpoints --format json

Raw API Calls
~~~~~~~~~~~~~

.. code-block:: bash

   ab api raw <method> <endpoint> [options]

Execute raw API calls for advanced usage.

**Options:**

- ``--data`` - JSON data for POST/PUT requests
- ``--params`` - Query parameters
- ``--headers`` - Additional headers

**Examples:**

.. code-block:: bash

   # GET request
   ab api raw GET /companies/12345
   
   # POST request with data
   ab api raw POST /contacts --data '{"name": "John Doe", "email": "john@example.com"}'
   
   # GET with query parameters
   ab api raw GET /jobs --params '{"status": "active", "limit": 10}'

Common Workflows
----------------

Finding Company Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. List company types to understand the categories:

   .. code-block:: bash

      ab lookup company-types

2. Get specific company details:

   .. code-block:: bash

      ab company 12345

Working with Quotes
~~~~~~~~~~~~~~~~~~~

1. Prepare quote data in a JSON file
2. Submit quote request:

   .. code-block:: bash

      ab quote qr --file quote_request.json

3. Check quote status using raw API:

   .. code-block:: bash

      ab api raw GET /quotes/QUOTE_ID

Data Import Workflow
~~~~~~~~~~~~~~~~~~~~

1. Prepare your data in CSV or Excel format
2. Preview the data:

   .. code-block:: bash

      ab load contacts.csv --limit 5

3. Process the full file:

   .. code-block:: bash

      ab load contacts.csv --format json > processed_contacts.json

Environment Variables
---------------------

The CLI respects these environment variables:

- ``ABC_ENVIRONMENT`` - Set to ``staging`` or ``production``
- ``ABC_LOG_LEVEL`` - Set logging verbosity (DEBUG, INFO, WARNING, ERROR)
- ``ABC_TOKEN_FILE`` - Custom path for token storage

**Example:**

.. code-block:: bash

   # Use production environment for a single command
   ABC_ENVIRONMENT=production ab company 12345

Troubleshooting
---------------

Authentication Issues
~~~~~~~~~~~~~~~~~~~~~

If you encounter authentication errors:

1. Verify your credentials in the ``.env`` file
2. Check that ``ABC_CLIENT_SECRET`` is set correctly
3. Try clearing cached tokens:

   .. code-block:: bash

      rm ~/.abconnect/token.json

Connection Problems
~~~~~~~~~~~~~~~~~~~

For connection issues:

1. Verify your internet connection
2. Check if you're using the correct environment (staging vs production)
3. Enable debug logging:

   .. code-block:: bash

      ABC_LOG_LEVEL=DEBUG ab me

File Loading Errors
~~~~~~~~~~~~~~~~~~~

When file loading fails:

1. Verify the file path is correct
2. Check file permissions
3. Try specifying encoding explicitly:

   .. code-block:: bash

      ab load data.csv --encoding utf-8

See Also
--------

- :doc:`quickstart_cli` - Quick start guide for CLI usage
- :doc:`examples_cli` - More CLI examples and use cases
- :doc:`api/index` - Full API endpoint documentation