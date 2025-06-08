RfQ
===

Quick Reference
---------------

.. list-table::
   :header-rows: 1
   :widths: 10 40 50

   * - Method
     - Endpoint
     - Description
   * - GET
     - /api/rfq/{rfqId}
     - 
   * - POST
     - /api/rfq/{rfqId}/accept
     - 
   * - POST
     - /api/rfq/{rfqId}/decline
     - 
   * - POST
     - /api/rfq/{rfqId}/cancel
     - 
   * - POST
     - /api/rfq/{rfqId}/acceptwinner
     - 
   * - POST
     - /api/rfq/{rfqId}/comment
     - 
   * - GET
     - /api/rfq/forjob/{jobId}
     - 


.. _get-apirfqrfqid:

GET /api/rfq/{rfqId}
~~~~~~~~~~~~~~~~~~~~

**Parameters:**

*Path Parameters:*

- `rfqId` (integer, path) *(required)*: No description available

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         
         # Initialize the API client
         api = ABConnectAPI()
         
         # Make the API call
         response = api.raw.get(
             "/api/rfq/{rfqId}"
         ,
             rfqId=789e0123-e89b-12d3-a456-426614174002
         
         )
         
         # Process the response
         print(response)

   .. tab:: CLI

      .. code-block:: bash

         ab api raw get /api/rfq/{rfqId} \
             rfqId=789e0123-e89b-12d3-a456-426614174002

   .. tab:: curl

      .. code-block:: bash

         curl -X GET \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           'https://api.abconnect.co/api/rfq/789e0123-e89b-12d3-a456-426614174002'

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {
        "status": "success",
        "data": {}
      }

----

.. _post-apirfqrfqidaccept:

POST /api/rfq/{rfqId}/accept
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Parameters:**

*Path Parameters:*

- `rfqId` (integer, path) *(required)*: No description available

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         
         # Initialize the API client
         api = ABConnectAPI()
         
         # Make the API call
         response = api.raw.post(
             "/api/rfq/{rfqId}/accept"
         ,
             rfqId=789e0123-e89b-12d3-a456-426614174002
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

         ab api raw post /api/rfq/{rfqId}/accept \
             rfqId=789e0123-e89b-12d3-a456-426614174002

   .. tab:: curl

      .. code-block:: bash

         curl -X POST \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           -H 'Content-Type: application/json' \
           -d '{
               "example": "data"
           }' \
           'https://api.abconnect.co/api/rfq/789e0123-e89b-12d3-a456-426614174002/accept'

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

.. _post-apirfqrfqiddecline:

POST /api/rfq/{rfqId}/decline
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Parameters:**

*Path Parameters:*

- `rfqId` (integer, path) *(required)*: No description available

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         
         # Initialize the API client
         api = ABConnectAPI()
         
         # Make the API call
         response = api.raw.post(
             "/api/rfq/{rfqId}/decline"
         ,
             rfqId=789e0123-e89b-12d3-a456-426614174002
         
         )
         
         # Process the response
         print(response)

   .. tab:: CLI

      .. code-block:: bash

         ab api raw post /api/rfq/{rfqId}/decline \
             rfqId=789e0123-e89b-12d3-a456-426614174002

   .. tab:: curl

      .. code-block:: bash

         curl -X POST \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           -H 'Content-Type: application/json' \
           'https://api.abconnect.co/api/rfq/789e0123-e89b-12d3-a456-426614174002/decline'

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

.. _post-apirfqrfqidcancel:

POST /api/rfq/{rfqId}/cancel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Parameters:**

*Path Parameters:*

- `rfqId` (integer, path) *(required)*: No description available

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         
         # Initialize the API client
         api = ABConnectAPI()
         
         # Make the API call
         response = api.raw.post(
             "/api/rfq/{rfqId}/cancel"
         ,
             rfqId=789e0123-e89b-12d3-a456-426614174002
         
         )
         
         # Process the response
         print(response)

   .. tab:: CLI

      .. code-block:: bash

         ab api raw post /api/rfq/{rfqId}/cancel \
             rfqId=789e0123-e89b-12d3-a456-426614174002

   .. tab:: curl

      .. code-block:: bash

         curl -X POST \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           -H 'Content-Type: application/json' \
           'https://api.abconnect.co/api/rfq/789e0123-e89b-12d3-a456-426614174002/cancel'

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

.. _post-apirfqrfqidacceptwinner:

POST /api/rfq/{rfqId}/acceptwinner
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Parameters:**

*Path Parameters:*

- `rfqId` (integer, path) *(required)*: No description available

*Query Parameters:*

- `finalAmount` (number, query): No description available

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         
         # Initialize the API client
         api = ABConnectAPI()
         
         # Make the API call
         response = api.raw.post(
             "/api/rfq/{rfqId}/acceptwinner"
         ,
             rfqId=789e0123-e89b-12d3-a456-426614174002
         
         )
         
         # Process the response
         print(response)

   .. tab:: CLI

      .. code-block:: bash

         ab api raw post /api/rfq/{rfqId}/acceptwinner \
             rfqId=789e0123-e89b-12d3-a456-426614174002

   .. tab:: curl

      .. code-block:: bash

         curl -X POST \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           -H 'Content-Type: application/json' \
           'https://api.abconnect.co/api/rfq/789e0123-e89b-12d3-a456-426614174002/acceptwinner'

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

.. _post-apirfqrfqidcomment:

POST /api/rfq/{rfqId}/comment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Parameters:**

*Path Parameters:*

- `rfqId` (integer, path) *(required)*: No description available

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         
         # Initialize the API client
         api = ABConnectAPI()
         
         # Make the API call
         response = api.raw.post(
             "/api/rfq/{rfqId}/comment"
         ,
             rfqId=789e0123-e89b-12d3-a456-426614174002
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

         ab api raw post /api/rfq/{rfqId}/comment \
             rfqId=789e0123-e89b-12d3-a456-426614174002

   .. tab:: curl

      .. code-block:: bash

         curl -X POST \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           -H 'Content-Type: application/json' \
           -d '{
               "example": "data"
           }' \
           'https://api.abconnect.co/api/rfq/789e0123-e89b-12d3-a456-426614174002/comment'

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

.. _get-apirfqforjobjobid:

GET /api/rfq/forjob/{jobId}
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Parameters:**

*Path Parameters:*

- `jobId` (integer, path) *(required)*: No description available

*Query Parameters:*

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
             "/api/rfq/forjob/{jobId}"
         ,
             jobId="JOB-2024-001"
         
         )
         
         # Process the response
         print(response)

   .. tab:: CLI

      .. code-block:: bash

         ab api raw get /api/rfq/forjob/{jobId} \
             jobId=JOB-2024-001

   .. tab:: curl

      .. code-block:: bash

         curl -X GET \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           'https://api.abconnect.co/api/rfq/forjob/JOB-2024-001'

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {
        "status": "success",
        "data": {}
      }
