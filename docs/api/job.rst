Job
===

Manage shipping and logistics jobs. Jobs represent the movement of goods from origin to destination and include quotes, bookings, tracking, and completion.

Quick Reference
---------------

.. list-table::
   :header-rows: 1
   :widths: 10 40 50

   * - Method
     - Endpoint
     - Description
   * - POST
     - /api/job/{jobDisplayId}/book
     - Book a job
   * - GET
     - /api/job/{jobDisplayId}
     - Get job by display ID
   * - GET
     - /api/job/search
     - Search jobs
   * - POST
     - /api/job/searchByDetails
     - 
   * - GET
     - /api/job/{jobDisplayId}/calendaritems
     - 
   * - PUT
     - /api/job/save
     - 
   * - POST
     - /api/job
     - 
   * - GET
     - /api/job/feedback/{jobDisplayId}
     - 
   * - POST
     - /api/job/feedback/{jobDisplayId}
     - 
   * - POST
     - /api/job/transfer/{jobDisplayId}
     - 
   * - POST
     - /api/job/{jobDisplayId}/freightitems
     - 
   * - GET
     - /api/job/{jobDisplayId}/submanagementstatus
     - 
   * - POST
     - /api/job/{jobDisplayId}/item/notes
     - 
   * - POST
     - /api/job/{jobDisplayId}/changeAgent
     - 
   * - GET
     - /api/job/{jobDisplayId}/updatePageConfig
     - 
   * - GET
     - /api/job/{jobDisplayId}/price
     - 
   * - GET
     - /api/job/jobAccessLevel
     - 
   * - GET
     - /api/job/documentConfig
     - 


.. _post-apijobjobdisplayidbook:

POST /api/job/{jobDisplayId}/book
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Book a job**

Books a job and transitions it to active status.

**Parameters:**

*Path Parameters:*

- `jobDisplayId` (string, path) *(required)*: No description available

**Response Type:**

:class:`~ABConnect.api.models.jobs.Job`

See the model documentation for detailed field descriptions.

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         
         # Initialize the API client
         api = ABConnectAPI()
         
         # Make the API call
         response = api.raw.post(
             "/api/job/{jobDisplayId}/book"
         ,
             jobDisplayId="2000000"
         
         )
         
         # Process the response
         print(response)

   .. tab:: CLI

      .. code-block:: bash

         ab api raw post /api/job/{jobDisplayId}/book \
             jobDisplayId=2000000

   .. tab:: curl

      .. code-block:: bash

         curl -X POST \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           -H 'Content-Type: application/json' \
           'https://api.abconnect.co/api/job/2000000/book'

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

.. _get-apijobjobdisplayid:

GET /api/job/{jobDisplayId}
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Get job by display ID**

Retrieves detailed information about a specific job using its display ID.

**Parameters:**

*Path Parameters:*

- `jobDisplayId` (string, path) *(required)*: No description available

**Response Type:**

:class:`~ABConnect.api.models.jobs.Job`

See the model documentation for detailed field descriptions.

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         
         # Initialize the API client
         api = ABConnectAPI()
         
         # Make the API call
         response = api.raw.get(
             "/api/job/{jobDisplayId}"
         ,
             jobDisplayId="2000000"
         
         )
         
         # Process the response
         print(response)

   .. tab:: CLI

      .. code-block:: bash

         ab api raw get /api/job/{jobDisplayId} \
             jobDisplayId=2000000

   .. tab:: curl

      .. code-block:: bash

         curl -X GET \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           'https://api.abconnect.co/api/job/2000000'

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {
        "jobDisplayId": "2000000",
        "bookedDate": "2024-08-13T14:04:04",
        "ownerCompanyId": "ed282b80-54fe-4f42-bf1b-69103ce1f76c",
        "customerContact": {
          "id": 3473290,
          "contact": {
            "id": 266841,
            "contactDisplayId": "1",
            "fullName": "Training",
            "contactTypeId": 2,
            "isBusiness": true,
            "companyId": "ed282b80-54fe-4f42-bf1b-69103ce1f76c",
            "company": {
              "companyName": "Training",
              "companyCode": "TRAINING",
              "companyPhone": "8009814202",
              "companyEmail": "training@abconnect.co"
            }
          }
        },
        "jobStatusId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "jobStatusName": "Booked",
        "jobTypeId": "a1b2c3d4-5678-90ab-cdef-1234567890ab",
        "items": [
          {
            "id": 12345,
            "description": "Widget",
            "quantity": 1,
            "weight": 10.5,
            "dimensions": {
              "length": 12,
              "width": 8,
              "height": 6
            }
          }
        ],
        "origin": {
          "address1": "123 Main St",
          "city": "Denver",
          "state": "CO",
          "zipCode": "80202"
        },
        "destination": {
          "address1": "456 Oak Ave",
          "city": "Los Angeles",
          "state": "CA",
          "zipCode": "90001"
        }
      }

----

.. _get-apijobsearch:

GET /api/job/search
~~~~~~~~~~~~~~~~~~~

**Search jobs**

Search for jobs using various criteria such as status, date range, customer, or location.

**Parameters:**

*Query Parameters:*

- `jobDisplayId` (integer, query): No description available

**Response Type:**

Array of :class:`~ABConnect.api.models.jobs.Job` objects

See the model documentation for detailed field descriptions.

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         
         # Initialize the API client
         api = ABConnectAPI()
         
         # Make the API call
         response = api.raw.get(
             "/api/job/search"
         
         )
         
         # Process the response
         print(response)

   .. tab:: CLI

      .. code-block:: bash

         ab api raw get /api/job/search

   .. tab:: curl

      .. code-block:: bash

         curl -X GET \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           'https://api.abconnect.co/api/job/search'

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      []

----

.. _post-apijobsearchbydetails:

POST /api/job/searchByDetails
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         
         # Initialize the API client
         api = ABConnectAPI()
         
         # Make the API call
         response = api.raw.post(
             "/api/job/searchByDetails"
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

         ab api raw post /api/job/searchByDetails

   .. tab:: curl

      .. code-block:: bash

         curl -X POST \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           -H 'Content-Type: application/json' \
           -d '{
               "example": "data"
           }' \
           'https://api.abconnect.co/api/job/searchByDetails'

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      []

----

.. _get-apijobjobdisplayidcalendaritems:

GET /api/job/{jobDisplayId}/calendaritems
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Parameters:**

*Path Parameters:*

- `jobDisplayId` (integer, path) *(required)*: No description available

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         
         # Initialize the API client
         api = ABConnectAPI()
         
         # Make the API call
         response = api.raw.get(
             "/api/job/{jobDisplayId}/calendaritems"
         ,
             jobDisplayId=2000000
         
         )
         
         # Process the response
         print(response)

   .. tab:: CLI

      .. code-block:: bash

         ab api raw get /api/job/{jobDisplayId}/calendaritems \
             jobDisplayId=2000000

   .. tab:: curl

      .. code-block:: bash

         curl -X GET \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           'https://api.abconnect.co/api/job/2000000/calendaritems'

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      []

----

.. _put-apijobsave:

PUT /api/job/save
~~~~~~~~~~~~~~~~~

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         
         # Initialize the API client
         api = ABConnectAPI()
         
         # Make the API call
         response = api.raw.put(
             "/api/job/save"
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

         ab api raw put /api/job/save

   .. tab:: curl

      .. code-block:: bash

         curl -X PUT \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           -H 'Content-Type: application/json' \
           -d '{
               "example": "data"
           }' \
           'https://api.abconnect.co/api/job/save'

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {
        "id": "123e4567-e89b-12d3-a456-426614174000",
        "status": "updated",
        "message": "Resource updated successfully"
      }

----

.. _post-apijob:

POST /api/job
~~~~~~~~~~~~~

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         
         # Initialize the API client
         api = ABConnectAPI()
         
         # Make the API call
         response = api.raw.post(
             "/api/job"
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

         ab api raw post /api/job

   .. tab:: curl

      .. code-block:: bash

         curl -X POST \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           -H 'Content-Type: application/json' \
           -d '{
               "example": "data"
           }' \
           'https://api.abconnect.co/api/job'

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

.. _get-apijobfeedbackjobdisplayid:

GET /api/job/feedback/{jobDisplayId}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Parameters:**

*Path Parameters:*

- `jobDisplayId` (string, path) *(required)*: No description available

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         
         # Initialize the API client
         api = ABConnectAPI()
         
         # Make the API call
         response = api.raw.get(
             "/api/job/feedback/{jobDisplayId}"
         ,
             jobDisplayId="2000000"
         
         )
         
         # Process the response
         print(response)

   .. tab:: CLI

      .. code-block:: bash

         ab api raw get /api/job/feedback/{jobDisplayId} \
             jobDisplayId=2000000

   .. tab:: curl

      .. code-block:: bash

         curl -X GET \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           'https://api.abconnect.co/api/job/feedback/2000000'

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {
        "status": "success",
        "data": {}
      }

----

.. _post-apijobfeedbackjobdisplayid:

POST /api/job/feedback/{jobDisplayId}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Parameters:**

*Path Parameters:*

- `jobDisplayId` (string, path) *(required)*: No description available

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         
         # Initialize the API client
         api = ABConnectAPI()
         
         # Make the API call
         response = api.raw.post(
             "/api/job/feedback/{jobDisplayId}"
         ,
             jobDisplayId="2000000"
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

         ab api raw post /api/job/feedback/{jobDisplayId} \
             jobDisplayId=2000000

   .. tab:: curl

      .. code-block:: bash

         curl -X POST \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           -H 'Content-Type: application/json' \
           -d '{
               "example": "data"
           }' \
           'https://api.abconnect.co/api/job/feedback/2000000'

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

.. _post-apijobtransferjobdisplayid:

POST /api/job/transfer/{jobDisplayId}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Parameters:**

*Path Parameters:*

- `jobDisplayId` (string, path) *(required)*: No description available

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         
         # Initialize the API client
         api = ABConnectAPI()
         
         # Make the API call
         response = api.raw.post(
             "/api/job/transfer/{jobDisplayId}"
         ,
             jobDisplayId="2000000"
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

         ab api raw post /api/job/transfer/{jobDisplayId} \
             jobDisplayId=2000000

   .. tab:: curl

      .. code-block:: bash

         curl -X POST \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           -H 'Content-Type: application/json' \
           -d '{
               "example": "data"
           }' \
           'https://api.abconnect.co/api/job/transfer/2000000'

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

.. _post-apijobjobdisplayidfreightitems:

POST /api/job/{jobDisplayId}/freightitems
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Parameters:**

*Path Parameters:*

- `jobDisplayId` (string, path) *(required)*: No description available

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         
         # Initialize the API client
         api = ABConnectAPI()
         
         # Make the API call
         response = api.raw.post(
             "/api/job/{jobDisplayId}/freightitems"
         ,
             jobDisplayId="2000000"
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

         ab api raw post /api/job/{jobDisplayId}/freightitems \
             jobDisplayId=2000000

   .. tab:: curl

      .. code-block:: bash

         curl -X POST \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           -H 'Content-Type: application/json' \
           -d '{
               "example": "data"
           }' \
           'https://api.abconnect.co/api/job/2000000/freightitems'

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

.. _get-apijobjobdisplayidsubmanagementstatus:

GET /api/job/{jobDisplayId}/submanagementstatus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Parameters:**

*Path Parameters:*

- `jobDisplayId` (string, path) *(required)*: No description available

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         
         # Initialize the API client
         api = ABConnectAPI()
         
         # Make the API call
         response = api.raw.get(
             "/api/job/{jobDisplayId}/submanagementstatus"
         ,
             jobDisplayId="2000000"
         
         )
         
         # Process the response
         print(response)

   .. tab:: CLI

      .. code-block:: bash

         ab api raw get /api/job/{jobDisplayId}/submanagementstatus \
             jobDisplayId=2000000

   .. tab:: curl

      .. code-block:: bash

         curl -X GET \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           'https://api.abconnect.co/api/job/2000000/submanagementstatus'

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      []

----

.. _post-apijobjobdisplayiditemnotes:

POST /api/job/{jobDisplayId}/item/notes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Parameters:**

*Path Parameters:*

- `jobDisplayId` (string, path) *(required)*: No description available

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         
         # Initialize the API client
         api = ABConnectAPI()
         
         # Make the API call
         response = api.raw.post(
             "/api/job/{jobDisplayId}/item/notes"
         ,
             jobDisplayId="2000000"
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

         ab api raw post /api/job/{jobDisplayId}/item/notes \
             jobDisplayId=2000000

   .. tab:: curl

      .. code-block:: bash

         curl -X POST \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           -H 'Content-Type: application/json' \
           -d '{
               "example": "data"
           }' \
           'https://api.abconnect.co/api/job/2000000/item/notes'

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

.. _post-apijobjobdisplayidchangeagent:

POST /api/job/{jobDisplayId}/changeAgent
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Parameters:**

*Path Parameters:*

- `jobDisplayId` (string, path) *(required)*: No description available

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         
         # Initialize the API client
         api = ABConnectAPI()
         
         # Make the API call
         response = api.raw.post(
             "/api/job/{jobDisplayId}/changeAgent"
         ,
             jobDisplayId="2000000"
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

         ab api raw post /api/job/{jobDisplayId}/changeAgent \
             jobDisplayId=2000000

   .. tab:: curl

      .. code-block:: bash

         curl -X POST \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           -H 'Content-Type: application/json' \
           -d '{
               "example": "data"
           }' \
           'https://api.abconnect.co/api/job/2000000/changeAgent'

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

.. _get-apijobjobdisplayidupdatepageconfig:

GET /api/job/{jobDisplayId}/updatePageConfig
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Parameters:**

*Path Parameters:*

- `jobDisplayId` (string, path) *(required)*: No description available

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         
         # Initialize the API client
         api = ABConnectAPI()
         
         # Make the API call
         response = api.raw.get(
             "/api/job/{jobDisplayId}/updatePageConfig"
         ,
             jobDisplayId="2000000"
         
         )
         
         # Process the response
         print(response)

   .. tab:: CLI

      .. code-block:: bash

         ab api raw get /api/job/{jobDisplayId}/updatePageConfig \
             jobDisplayId=2000000

   .. tab:: curl

      .. code-block:: bash

         curl -X GET \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           'https://api.abconnect.co/api/job/2000000/updatePageConfig'

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {
        "status": "success",
        "data": {}
      }

----

.. _get-apijobjobdisplayidprice:

GET /api/job/{jobDisplayId}/price
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Parameters:**

*Path Parameters:*

- `jobDisplayId` (string, path) *(required)*: No description available

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         
         # Initialize the API client
         api = ABConnectAPI()
         
         # Make the API call
         response = api.raw.get(
             "/api/job/{jobDisplayId}/price"
         ,
             jobDisplayId="2000000"
         
         )
         
         # Process the response
         print(response)

   .. tab:: CLI

      .. code-block:: bash

         ab api raw get /api/job/{jobDisplayId}/price \
             jobDisplayId=2000000

   .. tab:: curl

      .. code-block:: bash

         curl -X GET \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           'https://api.abconnect.co/api/job/2000000/price'

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {
        "status": "success",
        "data": {}
      }

----

.. _get-apijobjobaccesslevel:

GET /api/job/jobAccessLevel
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Parameters:**

*Query Parameters:*

- `jobDisplayId` (string, query): No description available
- `jobItemId` (string, query): No description available

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         
         # Initialize the API client
         api = ABConnectAPI()
         
         # Make the API call
         response = api.raw.get(
             "/api/job/jobAccessLevel"
         
         )
         
         # Process the response
         print(response)

   .. tab:: CLI

      .. code-block:: bash

         ab api raw get /api/job/jobAccessLevel

   .. tab:: curl

      .. code-block:: bash

         curl -X GET \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           'https://api.abconnect.co/api/job/jobAccessLevel'

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {
        "status": "success",
        "data": {}
      }

----

.. _get-apijobdocumentconfig:

GET /api/job/documentConfig
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         
         # Initialize the API client
         api = ABConnectAPI()
         
         # Make the API call
         response = api.raw.get(
             "/api/job/documentConfig"
         
         )
         
         # Process the response
         print(response)

   .. tab:: CLI

      .. code-block:: bash

         ab api raw get /api/job/documentConfig

   .. tab:: curl

      .. code-block:: bash

         curl -X GET \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           'https://api.abconnect.co/api/job/documentConfig'

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {
        "status": "success",
        "data": {}
      }
