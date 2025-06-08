Planner API
===========

This section covers the 1 endpoints related to Planner.

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
     - /api/company/{companyId}/planner
     - 

Endpoints
---------

.. _get-apicompanycompanyidplanner:

GET /api/company/{companyId}/planner
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Path Parameters:*

- `companyId` (string, path) *(required)*: No description available

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X GET \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/company/123e4567-e89b-12d3-a456-426614174000/planner'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/company/{companyId}/planner \
       companyId=123e4567-e89b-12d3-a456-426614174000

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
