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
     'https://api.abconnect.co/api/company/ed282b80-54fe-4f42-bf1b-69103ce1f76c/planner'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/company/{companyId}/planner \
       companyId=ed282b80-54fe-4f42-bf1b-69103ce1f76c

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
