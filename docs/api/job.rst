Job API
=======

This section covers the 18 endpoints related to Job.

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
   * - POST
     - /api/job/{jobDisplayId}/book
     - 
   * - GET
     - /api/job/{jobDisplayId}
     - 
   * - GET
     - /api/job/search
     - 
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

Endpoints
---------

.. _post-apijobjobdisplayidbook:

POST /api/job/{jobDisplayId}/book
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
     'https://api.abconnect.co/api/job/JOB-2024-001/book'

Using AB CLI:

.. code-block:: bash

   ab api raw post /api/job/{jobDisplayId}/book \
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

.. _get-apijobjobdisplayid:

GET /api/job/{jobDisplayId}
~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
     'https://api.abconnect.co/api/job/JOB-2024-001'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/job/{jobDisplayId} \
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

.. _get-apijobsearch:

GET /api/job/search
~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Query Parameters:*

- `jobDisplayId` (integer, query): No description available

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X GET \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/job/search'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/job/search

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      []

----

.. _post-apijobsearchbydetails:

POST /api/job/searchByDetails
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

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
     'https://api.abconnect.co/api/job/searchByDetails'

Using AB CLI:

.. code-block:: bash

   ab api raw post /api/job/searchByDetails

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      []

----

.. _get-apijobjobdisplayidcalendaritems:

GET /api/job/{jobDisplayId}/calendaritems
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Path Parameters:*

- `jobDisplayId` (integer, path) *(required)*: No description available

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X GET \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/job/JOB-2024-001/calendaritems'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/job/{jobDisplayId}/calendaritems \
       jobDisplayId=JOB-2024-001

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      []

----

.. _put-apijobsave:

PUT /api/job/save
~~~~~~~~~~~~~~~~~

****

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X PUT \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     -H 'Content-Type: application/json' \
     -d '{
         "example": "data"
     }' \
     'https://api.abconnect.co/api/job/save'

Using AB CLI:

.. code-block:: bash

   ab api raw put /api/job/save

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {
        "id": "123e4567-e89b-12d3-a456-426614174000",
        "status": "updated",
        "message": "Resource updated successfully",
        "modified_at": "2024-01-20T10:00:00Z"
      }

----

.. _post-apijob:

POST /api/job
~~~~~~~~~~~~~

****

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
     'https://api.abconnect.co/api/job'

Using AB CLI:

.. code-block:: bash

   ab api raw post /api/job

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

.. _get-apijobfeedbackjobdisplayid:

GET /api/job/feedback/{jobDisplayId}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
     'https://api.abconnect.co/api/job/feedback/JOB-2024-001'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/job/feedback/{jobDisplayId} \
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

.. _post-apijobfeedbackjobdisplayid:

POST /api/job/feedback/{jobDisplayId}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
     'https://api.abconnect.co/api/job/feedback/JOB-2024-001'

Using AB CLI:

.. code-block:: bash

   ab api raw post /api/job/feedback/{jobDisplayId} \
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

.. _post-apijobtransferjobdisplayid:

POST /api/job/transfer/{jobDisplayId}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
     'https://api.abconnect.co/api/job/transfer/JOB-2024-001'

Using AB CLI:

.. code-block:: bash

   ab api raw post /api/job/transfer/{jobDisplayId} \
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

.. _post-apijobjobdisplayidfreightitems:

POST /api/job/{jobDisplayId}/freightitems
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
     'https://api.abconnect.co/api/job/JOB-2024-001/freightitems'

Using AB CLI:

.. code-block:: bash

   ab api raw post /api/job/{jobDisplayId}/freightitems \
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

.. _get-apijobjobdisplayidsubmanagementstatus:

GET /api/job/{jobDisplayId}/submanagementstatus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
     'https://api.abconnect.co/api/job/JOB-2024-001/submanagementstatus'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/job/{jobDisplayId}/submanagementstatus \
       jobDisplayId=JOB-2024-001

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      []

----

.. _post-apijobjobdisplayiditemnotes:

POST /api/job/{jobDisplayId}/item/notes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
     'https://api.abconnect.co/api/job/JOB-2024-001/item/notes'

Using AB CLI:

.. code-block:: bash

   ab api raw post /api/job/{jobDisplayId}/item/notes \
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

.. _post-apijobjobdisplayidchangeagent:

POST /api/job/{jobDisplayId}/changeAgent
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
     'https://api.abconnect.co/api/job/JOB-2024-001/changeAgent'

Using AB CLI:

.. code-block:: bash

   ab api raw post /api/job/{jobDisplayId}/changeAgent \
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

.. _get-apijobjobdisplayidupdatepageconfig:

GET /api/job/{jobDisplayId}/updatePageConfig
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
     'https://api.abconnect.co/api/job/JOB-2024-001/updatePageConfig'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/job/{jobDisplayId}/updatePageConfig \
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

.. _get-apijobjobdisplayidprice:

GET /api/job/{jobDisplayId}/price
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
     'https://api.abconnect.co/api/job/JOB-2024-001/price'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/job/{jobDisplayId}/price \
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

.. _get-apijobjobaccesslevel:

GET /api/job/jobAccessLevel
~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Query Parameters:*

- `jobDisplayId` (string, query): No description available
- `jobItemId` (string, query): No description available

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X GET \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/job/jobAccessLevel'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/job/jobAccessLevel

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

.. _get-apijobdocumentconfig:

GET /api/job/documentConfig
~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X GET \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/job/documentConfig'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/job/documentConfig

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
