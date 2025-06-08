JobPayment
==========

Process and track payments for jobs including credit cards, ACH, and other payment methods.

Quick Reference
---------------

.. list-table::
   :header-rows: 1
   :widths: 10 40 50

   * - Method
     - Endpoint
     - Description
   * - GET
     - /api/job/{jobDisplayId}/payment/create
     - 
   * - POST
     - /api/job/{jobDisplayId}/payment/ACHPaymentSession
     - 
   * - POST
     - /api/job/{jobDisplayId}/payment/ACHCreditTransfer
     - 
   * - GET
     - /api/job/{jobDisplayId}/payment
     - 
   * - POST
     - /api/job/{jobDisplayId}/payment/attachCustomerBank
     - 
   * - POST
     - /api/job/{jobDisplayId}/payment/verifyJobACHSource
     - 
   * - POST
     - /api/job/{jobDisplayId}/payment/cancelJobACHVerification
     - 
   * - GET
     - /api/job/{jobDisplayId}/payment/sources
     - 
   * - POST
     - /api/job/{jobDisplayId}/payment/bysource
     - 
   * - POST
     - /api/job/{jobDisplayId}/payment/banksource
     - 


.. _get-apijobjobdisplayidpaymentcreate:

GET /api/job/{jobDisplayId}/payment/create
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
             "/api/job/{jobDisplayId}/payment/create"
         ,
             jobDisplayId="2000000"
         
         )
         
         # Process the response
         print(response)

   .. tab:: CLI

      .. code-block:: bash

         ab api raw get /api/job/{jobDisplayId}/payment/create \
             jobDisplayId=2000000

   .. tab:: curl

      .. code-block:: bash

         curl -X GET \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           'https://api.abconnect.co/api/job/2000000/payment/create'

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {
        "status": "success",
        "data": {}
      }

----

.. _post-apijobjobdisplayidpaymentachpaymentsession:

POST /api/job/{jobDisplayId}/payment/ACHPaymentSession
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
             "/api/job/{jobDisplayId}/payment/ACHPaymentSession"
         ,
             jobDisplayId="2000000"
         
         )
         
         # Process the response
         print(response)

   .. tab:: CLI

      .. code-block:: bash

         ab api raw post /api/job/{jobDisplayId}/payment/ACHPaymentSession \
             jobDisplayId=2000000

   .. tab:: curl

      .. code-block:: bash

         curl -X POST \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           -H 'Content-Type: application/json' \
           'https://api.abconnect.co/api/job/2000000/payment/ACHPaymentSession'

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

.. _post-apijobjobdisplayidpaymentachcredittransfer:

POST /api/job/{jobDisplayId}/payment/ACHCreditTransfer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
             "/api/job/{jobDisplayId}/payment/ACHCreditTransfer"
         ,
             jobDisplayId="2000000"
         
         )
         
         # Process the response
         print(response)

   .. tab:: CLI

      .. code-block:: bash

         ab api raw post /api/job/{jobDisplayId}/payment/ACHCreditTransfer \
             jobDisplayId=2000000

   .. tab:: curl

      .. code-block:: bash

         curl -X POST \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           -H 'Content-Type: application/json' \
           'https://api.abconnect.co/api/job/2000000/payment/ACHCreditTransfer'

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

.. _get-apijobjobdisplayidpayment:

GET /api/job/{jobDisplayId}/payment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Parameters:**

*Path Parameters:*

- `jobDisplayId` (string, path) *(required)*: No description available

*Query Parameters:*

- `jobSubKey` (string, query): No description available

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         
         # Initialize the API client
         api = ABConnectAPI()
         
         # Make the API call
         response = api.raw.get(
             "/api/job/{jobDisplayId}/payment"
         ,
             jobDisplayId="2000000"
         
         )
         
         # Process the response
         print(response)

   .. tab:: CLI

      .. code-block:: bash

         ab api raw get /api/job/{jobDisplayId}/payment \
             jobDisplayId=2000000

   .. tab:: curl

      .. code-block:: bash

         curl -X GET \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           'https://api.abconnect.co/api/job/2000000/payment'

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {
        "status": "success",
        "data": {}
      }

----

.. _post-apijobjobdisplayidpaymentattachcustomerbank:

POST /api/job/{jobDisplayId}/payment/attachCustomerBank
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
             "/api/job/{jobDisplayId}/payment/attachCustomerBank"
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

         ab api raw post /api/job/{jobDisplayId}/payment/attachCustomerBank \
             jobDisplayId=2000000

   .. tab:: curl

      .. code-block:: bash

         curl -X POST \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           -H 'Content-Type: application/json' \
           -d '{
               "example": "data"
           }' \
           'https://api.abconnect.co/api/job/2000000/payment/attachCustomerBank'

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

.. _post-apijobjobdisplayidpaymentverifyjobachsource:

POST /api/job/{jobDisplayId}/payment/verifyJobACHSource
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
             "/api/job/{jobDisplayId}/payment/verifyJobACHSource"
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

         ab api raw post /api/job/{jobDisplayId}/payment/verifyJobACHSource \
             jobDisplayId=2000000

   .. tab:: curl

      .. code-block:: bash

         curl -X POST \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           -H 'Content-Type: application/json' \
           -d '{
               "example": "data"
           }' \
           'https://api.abconnect.co/api/job/2000000/payment/verifyJobACHSource'

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

.. _post-apijobjobdisplayidpaymentcanceljobachverification:

POST /api/job/{jobDisplayId}/payment/cancelJobACHVerification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
             "/api/job/{jobDisplayId}/payment/cancelJobACHVerification"
         ,
             jobDisplayId="2000000"
         
         )
         
         # Process the response
         print(response)

   .. tab:: CLI

      .. code-block:: bash

         ab api raw post /api/job/{jobDisplayId}/payment/cancelJobACHVerification \
             jobDisplayId=2000000

   .. tab:: curl

      .. code-block:: bash

         curl -X POST \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           -H 'Content-Type: application/json' \
           'https://api.abconnect.co/api/job/2000000/payment/cancelJobACHVerification'

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

.. _get-apijobjobdisplayidpaymentsources:

GET /api/job/{jobDisplayId}/payment/sources
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
             "/api/job/{jobDisplayId}/payment/sources"
         ,
             jobDisplayId="2000000"
         
         )
         
         # Process the response
         print(response)

   .. tab:: CLI

      .. code-block:: bash

         ab api raw get /api/job/{jobDisplayId}/payment/sources \
             jobDisplayId=2000000

   .. tab:: curl

      .. code-block:: bash

         curl -X GET \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           'https://api.abconnect.co/api/job/2000000/payment/sources'

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      []

----

.. _post-apijobjobdisplayidpaymentbysource:

POST /api/job/{jobDisplayId}/payment/bysource
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
             "/api/job/{jobDisplayId}/payment/bysource"
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

         ab api raw post /api/job/{jobDisplayId}/payment/bysource \
             jobDisplayId=2000000

   .. tab:: curl

      .. code-block:: bash

         curl -X POST \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           -H 'Content-Type: application/json' \
           -d '{
               "example": "data"
           }' \
           'https://api.abconnect.co/api/job/2000000/payment/bysource'

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

.. _post-apijobjobdisplayidpaymentbanksource:

POST /api/job/{jobDisplayId}/payment/banksource
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
         response = api.raw.post(
             "/api/job/{jobDisplayId}/payment/banksource"
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

         ab api raw post /api/job/{jobDisplayId}/payment/banksource \
             jobDisplayId=2000000

   .. tab:: curl

      .. code-block:: bash

         curl -X POST \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           -H 'Content-Type: application/json' \
           -d '{
               "example": "data"
           }' \
           'https://api.abconnect.co/api/job/2000000/payment/banksource'

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {
        "id": "789e0123-e89b-12d3-a456-426614174002",
        "status": "created",
        "message": "Resource created successfully"
      }
