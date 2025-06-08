ContactHistory
==============

Quick Reference
---------------

.. list-table::
   :header-rows: 1
   :widths: 10 40 50

   * - Method
     - Endpoint
     - Description
   * - POST
     - /api/contacts/{contactId}/history
     - 
   * - GET
     - /api/contacts/{contactId}/history/aggregated
     - 
   * - GET
     - /api/contacts/{contactId}/history/graphdata
     - 


.. _post-apicontactscontactidhistory:

POST /api/contacts/{contactId}/history
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Parameters:**

*Path Parameters:*

- `contactId` (integer, path) *(required)*: No description available

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         
         # Initialize the API client
         api = ABConnectAPI()
         
         # Make the API call
         response = api.raw.post(
             "/api/contacts/{contactId}/history"
         ,
             contactId=456e7890-e89b-12d3-a456-426614174001
         ,
             data=
             {
                 "example": "data"
         }
         
         )
         
         # Process the response
         print(response)

   .. tab:: CLI

      .. code-block:: bash

         ab api raw post /api/contacts/{contactId}/history \
             contactId=456e7890-e89b-12d3-a456-426614174001

   .. tab:: curl

      .. code-block:: bash

         curl -X POST \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           -H 'Content-Type: application/json' \
           -d '{
               "example": "data"
           }' \
           'https://api.abconnect.co/api/contacts/456e7890-e89b-12d3-a456-426614174001/history'

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {
        "id": "789e0123-e89b-12d3-a456-426614174002",
        "status": "created",
        "message": "Resource created successfully"
      }

----

.. _get-apicontactscontactidhistoryaggregated:

GET /api/contacts/{contactId}/history/aggregated
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Parameters:**

*Path Parameters:*

- `contactId` (integer, path) *(required)*: No description available

*Query Parameters:*

- `statuses` (array, query): No description available

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         
         # Initialize the API client
         api = ABConnectAPI()
         
         # Make the API call
         response = api.raw.get(
             "/api/contacts/{contactId}/history/aggregated"
         ,
             contactId=456e7890-e89b-12d3-a456-426614174001
         
         )
         
         # Process the response
         print(response)

   .. tab:: CLI

      .. code-block:: bash

         ab api raw get /api/contacts/{contactId}/history/aggregated \
             contactId=456e7890-e89b-12d3-a456-426614174001

   .. tab:: curl

      .. code-block:: bash

         curl -X GET \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           'https://api.abconnect.co/api/contacts/456e7890-e89b-12d3-a456-426614174001/history/aggregated'

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {
        "status": "success",
        "data": {}
      }

----

.. _get-apicontactscontactidhistorygraphdata:

GET /api/contacts/{contactId}/history/graphdata
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Parameters:**

*Path Parameters:*

- `contactId` (integer, path) *(required)*: No description available

*Query Parameters:*

- `statuses` (array, query): No description available

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         
         # Initialize the API client
         api = ABConnectAPI()
         
         # Make the API call
         response = api.raw.get(
             "/api/contacts/{contactId}/history/graphdata"
         ,
             contactId=456e7890-e89b-12d3-a456-426614174001
         
         )
         
         # Process the response
         print(response)

   .. tab:: CLI

      .. code-block:: bash

         ab api raw get /api/contacts/{contactId}/history/graphdata \
             contactId=456e7890-e89b-12d3-a456-426614174001

   .. tab:: curl

      .. code-block:: bash

         curl -X GET \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           'https://api.abconnect.co/api/contacts/456e7890-e89b-12d3-a456-426614174001/history/graphdata'

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {
        "status": "success",
        "data": {}
      }

----
