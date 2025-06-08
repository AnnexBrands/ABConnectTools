RfQ API
=======

This section covers the 7 endpoints related to RfQ.

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

Endpoints
---------

.. _get-apirfqrfqid:

GET /api/rfq/{rfqId}
~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Path Parameters:*

- `rfqId` (integer, path) *(required)*: No description available

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X GET \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/rfq/789e0123-e89b-12d3-a456-426614174002'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/rfq/{rfqId} \
       rfqId=789e0123-e89b-12d3-a456-426614174002

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

.. _post-apirfqrfqidaccept:

POST /api/rfq/{rfqId}/accept
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Path Parameters:*

- `rfqId` (integer, path) *(required)*: No description available

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
     'https://api.abconnect.co/api/rfq/789e0123-e89b-12d3-a456-426614174002/accept'

Using AB CLI:

.. code-block:: bash

   ab api raw post /api/rfq/{rfqId}/accept \
       rfqId=789e0123-e89b-12d3-a456-426614174002

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

.. _post-apirfqrfqiddecline:

POST /api/rfq/{rfqId}/decline
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Path Parameters:*

- `rfqId` (integer, path) *(required)*: No description available

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X POST \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     -H 'Content-Type: application/json' \
     'https://api.abconnect.co/api/rfq/789e0123-e89b-12d3-a456-426614174002/decline'

Using AB CLI:

.. code-block:: bash

   ab api raw post /api/rfq/{rfqId}/decline \
       rfqId=789e0123-e89b-12d3-a456-426614174002

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

.. _post-apirfqrfqidcancel:

POST /api/rfq/{rfqId}/cancel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Path Parameters:*

- `rfqId` (integer, path) *(required)*: No description available

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X POST \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     -H 'Content-Type: application/json' \
     'https://api.abconnect.co/api/rfq/789e0123-e89b-12d3-a456-426614174002/cancel'

Using AB CLI:

.. code-block:: bash

   ab api raw post /api/rfq/{rfqId}/cancel \
       rfqId=789e0123-e89b-12d3-a456-426614174002

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

.. _post-apirfqrfqidacceptwinner:

POST /api/rfq/{rfqId}/acceptwinner
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Path Parameters:*

- `rfqId` (integer, path) *(required)*: No description available

*Query Parameters:*

- `finalAmount` (number, query): No description available

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X POST \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     -H 'Content-Type: application/json' \
     'https://api.abconnect.co/api/rfq/789e0123-e89b-12d3-a456-426614174002/acceptwinner'

Using AB CLI:

.. code-block:: bash

   ab api raw post /api/rfq/{rfqId}/acceptwinner \
       rfqId=789e0123-e89b-12d3-a456-426614174002

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

.. _post-apirfqrfqidcomment:

POST /api/rfq/{rfqId}/comment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Path Parameters:*

- `rfqId` (integer, path) *(required)*: No description available

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
     'https://api.abconnect.co/api/rfq/789e0123-e89b-12d3-a456-426614174002/comment'

Using AB CLI:

.. code-block:: bash

   ab api raw post /api/rfq/{rfqId}/comment \
       rfqId=789e0123-e89b-12d3-a456-426614174002

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

.. _get-apirfqforjobjobid:

GET /api/rfq/forjob/{jobId}
~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Path Parameters:*

- `jobId` (integer, path) *(required)*: No description available

*Query Parameters:*

- `companyId` (string, query): No description available

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X GET \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/rfq/forjob/JOB-2024-001'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/rfq/forjob/{jobId} \
       jobId=JOB-2024-001

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
