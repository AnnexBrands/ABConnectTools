JobTrackingV3 API
=================

This section covers the 1 endpoints related to JobTrackingV3.

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
     - /api/v3/job/{jobDisplayId}/tracking/{historyAmount}
     - 

Endpoints
---------

.. _get-apiv3jobjobdisplayidtrackinghistoryamount:

GET /api/v3/job/{jobDisplayId}/tracking/{historyAmount}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Path Parameters:*

- `jobDisplayId` (string, path) *(required)*: No description available

*Query Parameters:*

- `historyAmount` (integer, query): No description available

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X GET \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/v3/job/JOB-2024-001/tracking/{historyAmount}'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/v3/job/{jobDisplayId}/tracking/{historyAmount} \
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
