JobParcelItems API
==================

This section covers the 4 endpoints related to JobParcelItems.

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
     - /api/job/{jobDisplayId}/parcelitems
     - 
   * - POST
     - /api/job/{jobDisplayId}/parcelitems
     - 
   * - PUT
     - /api/job/{jobDisplayId}/parcelitems/{parcelItemId}
     - 
   * - DELETE
     - /api/job/{jobDisplayId}/parcelitems/{parcelItemId}
     - 

Endpoints
---------

.. _get-apijobjobdisplayidparcelitems:

GET /api/job/{jobDisplayId}/parcelitems
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
     'https://api.abconnect.co/api/job/JOB-2024-001/parcelitems'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/job/{jobDisplayId}/parcelitems \
       jobDisplayId=JOB-2024-001

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      []

----

.. _post-apijobjobdisplayidparcelitems:

POST /api/job/{jobDisplayId}/parcelitems
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
     'https://api.abconnect.co/api/job/JOB-2024-001/parcelitems'

Using AB CLI:

.. code-block:: bash

   ab api raw post /api/job/{jobDisplayId}/parcelitems \
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

.. _put-apijobjobdisplayidparcelitemsparcelitemid:

PUT /api/job/{jobDisplayId}/parcelitems/{parcelItemId}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Path Parameters:*

- `parcelItemId` (integer, path) *(required)*: No description available
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
     'https://api.abconnect.co/api/job/JOB-2024-001/parcelitems/789e0123-e89b-12d3-a456-426614174002'

Using AB CLI:

.. code-block:: bash

   ab api raw put /api/job/{jobDisplayId}/parcelitems/{parcelItemId} \
       parcelItemId=789e0123-e89b-12d3-a456-426614174002 \
       jobDisplayId=JOB-2024-001

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

.. _delete-apijobjobdisplayidparcelitemsparcelitemid:

DELETE /api/job/{jobDisplayId}/parcelitems/{parcelItemId}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Path Parameters:*

- `parcelItemId` (integer, path) *(required)*: No description available
- `jobDisplayId` (string, path) *(required)*: No description available

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X DELETE \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/job/JOB-2024-001/parcelitems/789e0123-e89b-12d3-a456-426614174002'

Using AB CLI:

.. code-block:: bash

   ab api raw delete /api/job/{jobDisplayId}/parcelitems/{parcelItemId} \
       parcelItemId=789e0123-e89b-12d3-a456-426614174002 \
       jobDisplayId=JOB-2024-001

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {
        "status": "success",
        "message": "Resource deleted successfully"
      }

----
