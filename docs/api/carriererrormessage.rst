CarrierErrorMessage API
=======================

This section covers the 2 endpoints related to CarrierErrorMessage.

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
     - /api/admin/carriererrormessage/all
     - 
   * - POST
     - /api/admin/carriererrormessage
     - 

Endpoints
---------

.. _get-apiadmincarriererrormessageall:

GET /api/admin/carriererrormessage/all
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X GET \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/admin/carriererrormessage/all'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/admin/carriererrormessage/all

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

.. _post-apiadmincarriererrormessage:

POST /api/admin/carriererrormessage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
     'https://api.abconnect.co/api/admin/carriererrormessage'

Using AB CLI:

.. code-block:: bash

   ab api raw post /api/admin/carriererrormessage

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
