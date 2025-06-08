JobPayment API
==============

This section covers the 10 endpoints related to JobPayment.

.. contents::
   :local:
   :depth: 2

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

Endpoints
---------

.. _get-apijobjobdisplayidpaymentcreate:

GET /api/job/{jobDisplayId}/payment/create
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Path Parameters:*

- `jobDisplayId` (string, path) *(required)*: No description available

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X GET \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/job/JOB-2024-001/payment/create'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/job/{jobDisplayId}/payment/create \
       jobDisplayId=JOB-2024-001

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {
        "status": "success",
        "data": {
          "message": "Operation completed successfully"
        }
      }

----

.. _post-apijobjobdisplayidpaymentachpaymentsession:

POST /api/job/{jobDisplayId}/payment/ACHPaymentSession
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Path Parameters:*

- `jobDisplayId` (string, path) *(required)*: No description available

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X POST \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     -H 'Content-Type: application/json' \
     'https://api.abconnect.co/api/job/JOB-2024-001/payment/ACHPaymentSession'

Using AB CLI:

.. code-block:: bash

   ab api raw post /api/job/{jobDisplayId}/payment/ACHPaymentSession \
       jobDisplayId=JOB-2024-001

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {
        "id": "789e0123-e89b-12d3-a456-426614174002",
        "status": "created",
        "message": "Resource created successfully",
        "data": {
          "id": "789e0123-e89b-12d3-a456-426614174002",
          "created_at": "2024-01-20T10:00:00Z"
        }
      }

----

.. _post-apijobjobdisplayidpaymentachcredittransfer:

POST /api/job/{jobDisplayId}/payment/ACHCreditTransfer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Path Parameters:*

- `jobDisplayId` (string, path) *(required)*: No description available

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X POST \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     -H 'Content-Type: application/json' \
     'https://api.abconnect.co/api/job/JOB-2024-001/payment/ACHCreditTransfer'

Using AB CLI:

.. code-block:: bash

   ab api raw post /api/job/{jobDisplayId}/payment/ACHCreditTransfer \
       jobDisplayId=JOB-2024-001

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {
        "id": "789e0123-e89b-12d3-a456-426614174002",
        "status": "created",
        "message": "Resource created successfully",
        "data": {
          "id": "789e0123-e89b-12d3-a456-426614174002",
          "created_at": "2024-01-20T10:00:00Z"
        }
      }

----

.. _get-apijobjobdisplayidpayment:

GET /api/job/{jobDisplayId}/payment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Path Parameters:*

- `jobDisplayId` (string, path) *(required)*: No description available

*Query Parameters:*

- `jobSubKey` (string, query): No description available

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X GET \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/job/JOB-2024-001/payment'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/job/{jobDisplayId}/payment \
       jobDisplayId=JOB-2024-001

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {
        "status": "success",
        "data": {
          "message": "Operation completed successfully"
        }
      }

----

.. _post-apijobjobdisplayidpaymentattachcustomerbank:

POST /api/job/{jobDisplayId}/payment/attachCustomerBank
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Path Parameters:*

- `jobDisplayId` (string, path) *(required)*: No description available

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X POST \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     -H 'Content-Type: application/json' \
     -d '{
         "example": "data"
     }' \
     'https://api.abconnect.co/api/job/JOB-2024-001/payment/attachCustomerBank'

Using AB CLI:

.. code-block:: bash

   ab api raw post /api/job/{jobDisplayId}/payment/attachCustomerBank \
       jobDisplayId=JOB-2024-001

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {
        "id": "789e0123-e89b-12d3-a456-426614174002",
        "status": "created",
        "message": "Resource created successfully",
        "data": {
          "id": "789e0123-e89b-12d3-a456-426614174002",
          "created_at": "2024-01-20T10:00:00Z"
        }
      }

----

.. _post-apijobjobdisplayidpaymentverifyjobachsource:

POST /api/job/{jobDisplayId}/payment/verifyJobACHSource
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Path Parameters:*

- `jobDisplayId` (string, path) *(required)*: No description available

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X POST \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     -H 'Content-Type: application/json' \
     -d '{
         "example": "data"
     }' \
     'https://api.abconnect.co/api/job/JOB-2024-001/payment/verifyJobACHSource'

Using AB CLI:

.. code-block:: bash

   ab api raw post /api/job/{jobDisplayId}/payment/verifyJobACHSource \
       jobDisplayId=JOB-2024-001

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {
        "id": "789e0123-e89b-12d3-a456-426614174002",
        "status": "created",
        "message": "Resource created successfully",
        "data": {
          "id": "789e0123-e89b-12d3-a456-426614174002",
          "created_at": "2024-01-20T10:00:00Z"
        }
      }

----

.. _post-apijobjobdisplayidpaymentcanceljobachverification:

POST /api/job/{jobDisplayId}/payment/cancelJobACHVerification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Path Parameters:*

- `jobDisplayId` (string, path) *(required)*: No description available

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X POST \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     -H 'Content-Type: application/json' \
     'https://api.abconnect.co/api/job/JOB-2024-001/payment/cancelJobACHVerification'

Using AB CLI:

.. code-block:: bash

   ab api raw post /api/job/{jobDisplayId}/payment/cancelJobACHVerification \
       jobDisplayId=JOB-2024-001

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {
        "id": "789e0123-e89b-12d3-a456-426614174002",
        "status": "created",
        "message": "Resource created successfully",
        "data": {
          "id": "789e0123-e89b-12d3-a456-426614174002",
          "created_at": "2024-01-20T10:00:00Z"
        }
      }

----

.. _get-apijobjobdisplayidpaymentsources:

GET /api/job/{jobDisplayId}/payment/sources
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Path Parameters:*

- `jobDisplayId` (string, path) *(required)*: No description available

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X GET \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/job/JOB-2024-001/payment/sources'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/job/{jobDisplayId}/payment/sources \
       jobDisplayId=JOB-2024-001

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      []

----

.. _post-apijobjobdisplayidpaymentbysource:

POST /api/job/{jobDisplayId}/payment/bysource
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Path Parameters:*

- `jobDisplayId` (string, path) *(required)*: No description available

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X POST \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     -H 'Content-Type: application/json' \
     -d '{
         "example": "data"
     }' \
     'https://api.abconnect.co/api/job/JOB-2024-001/payment/bysource'

Using AB CLI:

.. code-block:: bash

   ab api raw post /api/job/{jobDisplayId}/payment/bysource \
       jobDisplayId=JOB-2024-001

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {
        "id": "789e0123-e89b-12d3-a456-426614174002",
        "status": "created",
        "message": "Resource created successfully",
        "data": {
          "id": "789e0123-e89b-12d3-a456-426614174002",
          "created_at": "2024-01-20T10:00:00Z"
        }
      }

----

.. _post-apijobjobdisplayidpaymentbanksource:

POST /api/job/{jobDisplayId}/payment/banksource
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Path Parameters:*

- `jobDisplayId` (string, path) *(required)*: No description available

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X POST \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     -H 'Content-Type: application/json' \
     -d '{
         "example": "data"
     }' \
     'https://api.abconnect.co/api/job/JOB-2024-001/payment/banksource'

Using AB CLI:

.. code-block:: bash

   ab api raw post /api/job/{jobDisplayId}/payment/banksource \
       jobDisplayId=JOB-2024-001

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {
        "id": "789e0123-e89b-12d3-a456-426614174002",
        "status": "created",
        "message": "Resource created successfully",
        "data": {
          "id": "789e0123-e89b-12d3-a456-426614174002",
          "created_at": "2024-01-20T10:00:00Z"
        }
      }

----
