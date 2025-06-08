JobNote API
===========

This section covers the 4 endpoints related to JobNote.

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
     - /api/job/{jobDisplayId}/note
     - 
   * - POST
     - /api/job/{jobDisplayId}/note
     - 
   * - GET
     - /api/job/{jobDisplayId}/note/{id}
     - 
   * - PUT
     - /api/job/{jobDisplayId}/note/{id}
     - 

Endpoints
---------

.. _get-apijobjobdisplayidnote:

GET /api/job/{jobDisplayId}/note
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Path Parameters:*

- `jobDisplayId` (string, path) *(required)*: No description available

*Query Parameters:*

- `category` (string, query): No description available
- `taskCode` (string, query): No description available

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X GET \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/job/JOB-2024-001/note'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/job/{jobDisplayId}/note \
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

.. _post-apijobjobdisplayidnote:

POST /api/job/{jobDisplayId}/note
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
     -d '{
         "example": "data"
     }' \
     'https://api.abconnect.co/api/job/JOB-2024-001/note'

Using AB CLI:

.. code-block:: bash

   ab api raw post /api/job/{jobDisplayId}/note \
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

.. _get-apijobjobdisplayidnoteid:

GET /api/job/{jobDisplayId}/note/{id}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Path Parameters:*

- `id` (integer, path) *(required)*: No description available
- `jobDisplayId` (string, path) *(required)*: No description available

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X GET \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/job/JOB-2024-001/note/789e0123-e89b-12d3-a456-426614174002'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/job/{jobDisplayId}/note/{id} \
       id=789e0123-e89b-12d3-a456-426614174002 \
       jobDisplayId=JOB-2024-001

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {}

----

.. _put-apijobjobdisplayidnoteid:

PUT /api/job/{jobDisplayId}/note/{id}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Path Parameters:*

- `id` (integer, path) *(required)*: No description available
- `jobDisplayId` (string, path) *(required)*: No description available

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
     'https://api.abconnect.co/api/job/JOB-2024-001/note/789e0123-e89b-12d3-a456-426614174002'

Using AB CLI:

.. code-block:: bash

   ab api raw put /api/job/{jobDisplayId}/note/{id} \
       id=789e0123-e89b-12d3-a456-426614174002 \
       jobDisplayId=JOB-2024-001

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {}

----
