Note
====

Quick Reference
---------------

.. list-table::
   :header-rows: 1
   :widths: 10 40 50

   * - Method
     - Endpoint
     - Description
   * - GET
     - /api/note
     - 
   * - POST
     - /api/note
     - 
   * - PUT
     - /api/note/{id}
     - 
   * - GET
     - /api/note/suggestUsers
     - 


.. _get-apinote:

GET /api/note
~~~~~~~~~~~~~

**Parameters:**

*Query Parameters:*

- `category` (array, query): No description available
- `jobId` (string, query): No description available
- `contactId` (integer, query): No description available
- `companyId` (string, query): No description available

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         
         # Initialize the API client
         api = ABConnectAPI()
         
         # Make the API call
         response = api.raw.get(
             "/api/note"
         
         )
         
         # Process the response
         print(response)

   .. tab:: CLI

      .. code-block:: bash

         ab api raw get /api/note

   .. tab:: curl

      .. code-block:: bash

         curl -X GET \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           'https://api.abconnect.co/api/note'

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {
        "status": "success",
        "data": {}
      }

----

.. _post-apinote:

POST /api/note
~~~~~~~~~~~~~~

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         
         # Initialize the API client
         api = ABConnectAPI()
         
         # Make the API call
         response = api.raw.post(
             "/api/note"
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

         ab api raw post /api/note

   .. tab:: curl

      .. code-block:: bash

         curl -X POST \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           -H 'Content-Type: application/json' \
           -d '{
               "example": "data"
           }' \
           'https://api.abconnect.co/api/note'

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

.. _put-apinoteid:

PUT /api/note/{id}
~~~~~~~~~~~~~~~~~~

**Parameters:**

*Path Parameters:*

- `id` (integer, path) *(required)*: No description available

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         
         # Initialize the API client
         api = ABConnectAPI()
         
         # Make the API call
         response = api.raw.put(
             "/api/note/{id}"
         ,
             id=789e0123-e89b-12d3-a456-426614174002
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

         ab api raw put /api/note/{id} \
             id=789e0123-e89b-12d3-a456-426614174002

   .. tab:: curl

      .. code-block:: bash

         curl -X PUT \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           -H 'Content-Type: application/json' \
           -d '{
               "example": "data"
           }' \
           'https://api.abconnect.co/api/note/789e0123-e89b-12d3-a456-426614174002'

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {}

----

.. _get-apinotesuggestusers:

GET /api/note/suggestUsers
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Parameters:**

*Query Parameters:*

- `SearchKey` (string, query) *(required)*: No description available
- `JobFranchiseeId` (string, query): No description available
- `CompanyId` (string, query): No description available

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         
         # Initialize the API client
         api = ABConnectAPI()
         
         # Make the API call
         response = api.raw.get(
             "/api/note/suggestUsers"
         ,
             SearchKey="example-value"
         
         )
         
         # Process the response
         print(response)

   .. tab:: CLI

      .. code-block:: bash

         ab api raw get /api/note/suggestUsers \
             SearchKey=example-value

   .. tab:: curl

      .. code-block:: bash

         curl -X GET \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           'https://api.abconnect.co/api/note/suggestUsers?SearchKey=example-value'

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      []
