Calendar
========

Access calendar events and scheduling information for jobs, deliveries, and appointments.

Quick Reference
---------------

.. list-table::
   :header-rows: 1
   :widths: 10 40 50

   * - Method
     - Endpoint
     - Description
   * - GET
     - /api/company/{companyId}/calendar/{date}
     - 
   * - GET
     - /api/company/{companyId}/calendar/{date}/baseinfo
     - 
   * - GET
     - /api/company/{companyId}/calendar/{date}/startofday
     - 
   * - GET
     - /api/company/{companyId}/calendar/{date}/endofday
     - 


.. _get-apicompanycompanyidcalendardate:

GET /api/company/{companyId}/calendar/{date}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Parameters:**

*Path Parameters:*

- `companyId` (string, path) *(required)*: No description available
- `date` (string, path) *(required)*: No description available

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         
         # Initialize the API client
         api = ABConnectAPI()
         
         # Make the API call
         response = api.raw.get(
             "/api/company/{companyId}/calendar/{date}"
         ,
             companyId="ed282b80-54fe-4f42-bf1b-69103ce1f76c"
         ,
             date="2024-01-15T12:00:00Z"
         
         )
         
         # Process the response
         print(response)

   .. tab:: CLI

      .. code-block:: bash

         ab api raw get /api/company/{companyId}/calendar/{date} \
             companyId=ed282b80-54fe-4f42-bf1b-69103ce1f76c \
             date=2024-01-15T12:00:00Z

   .. tab:: curl

      .. code-block:: bash

         curl -X GET \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           'https://api.abconnect.co/api/company/ed282b80-54fe-4f42-bf1b-69103ce1f76c/calendar/2024-01-15T12:00:00Z'

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {
        "status": "success",
        "data": {}
      }

----

.. _get-apicompanycompanyidcalendardatebaseinfo:

GET /api/company/{companyId}/calendar/{date}/baseinfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Parameters:**

*Path Parameters:*

- `companyId` (string, path) *(required)*: No description available
- `date` (string, path) *(required)*: No description available

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         
         # Initialize the API client
         api = ABConnectAPI()
         
         # Make the API call
         response = api.raw.get(
             "/api/company/{companyId}/calendar/{date}/baseinfo"
         ,
             companyId="ed282b80-54fe-4f42-bf1b-69103ce1f76c"
         ,
             date="2024-01-15T12:00:00Z"
         
         )
         
         # Process the response
         print(response)

   .. tab:: CLI

      .. code-block:: bash

         ab api raw get /api/company/{companyId}/calendar/{date}/baseinfo \
             companyId=ed282b80-54fe-4f42-bf1b-69103ce1f76c \
             date=2024-01-15T12:00:00Z

   .. tab:: curl

      .. code-block:: bash

         curl -X GET \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           'https://api.abconnect.co/api/company/ed282b80-54fe-4f42-bf1b-69103ce1f76c/calendar/2024-01-15T12:00:00Z/baseinfo'

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {
        "status": "success",
        "data": {}
      }

----

.. _get-apicompanycompanyidcalendardatestartofday:

GET /api/company/{companyId}/calendar/{date}/startofday
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Parameters:**

*Path Parameters:*

- `companyId` (string, path) *(required)*: No description available
- `date` (string, path) *(required)*: No description available

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         
         # Initialize the API client
         api = ABConnectAPI()
         
         # Make the API call
         response = api.raw.get(
             "/api/company/{companyId}/calendar/{date}/startofday"
         ,
             companyId="ed282b80-54fe-4f42-bf1b-69103ce1f76c"
         ,
             date="2024-01-15T12:00:00Z"
         
         )
         
         # Process the response
         print(response)

   .. tab:: CLI

      .. code-block:: bash

         ab api raw get /api/company/{companyId}/calendar/{date}/startofday \
             companyId=ed282b80-54fe-4f42-bf1b-69103ce1f76c \
             date=2024-01-15T12:00:00Z

   .. tab:: curl

      .. code-block:: bash

         curl -X GET \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           'https://api.abconnect.co/api/company/ed282b80-54fe-4f42-bf1b-69103ce1f76c/calendar/2024-01-15T12:00:00Z/startofday'

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {
        "status": "success",
        "data": {}
      }

----

.. _get-apicompanycompanyidcalendardateendofday:

GET /api/company/{companyId}/calendar/{date}/endofday
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Parameters:**

*Path Parameters:*

- `companyId` (string, path) *(required)*: No description available
- `date` (string, path) *(required)*: No description available

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         
         # Initialize the API client
         api = ABConnectAPI()
         
         # Make the API call
         response = api.raw.get(
             "/api/company/{companyId}/calendar/{date}/endofday"
         ,
             companyId="ed282b80-54fe-4f42-bf1b-69103ce1f76c"
         ,
             date="2024-01-15T12:00:00Z"
         
         )
         
         # Process the response
         print(response)

   .. tab:: CLI

      .. code-block:: bash

         ab api raw get /api/company/{companyId}/calendar/{date}/endofday \
             companyId=ed282b80-54fe-4f42-bf1b-69103ce1f76c \
             date=2024-01-15T12:00:00Z

   .. tab:: curl

      .. code-block:: bash

         curl -X GET \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           'https://api.abconnect.co/api/company/ed282b80-54fe-4f42-bf1b-69103ce1f76c/calendar/2024-01-15T12:00:00Z/endofday'

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {
        "status": "success",
        "data": {}
      }
