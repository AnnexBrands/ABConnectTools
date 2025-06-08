Email API
=========

This section covers the 1 endpoints related to Email.

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
     - /api/email/{jobDisplayId}/labelrequest
     - 

Endpoints
---------

.. _post-apiemailjobdisplayidlabelrequest:

POST /api/email/{jobDisplayId}/labelrequest
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
     'https://api.abconnect.co/api/email/JOB-2024-001/labelrequest'

Using AB CLI:

.. code-block:: bash

   ab api raw post /api/email/{jobDisplayId}/labelrequest \
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
