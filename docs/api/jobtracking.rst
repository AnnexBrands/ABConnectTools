JobTracking API
===============

This section covers the 2 endpoints related to JobTracking.

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
     - /api/job/{jobDisplayId}/tracking
     - 
   * - GET
     - /api/job/{jobDisplayId}/tracking/shipment/{proNumber}
     - 

Endpoints
---------

.. _get-apijobjobdisplayidtracking:

GET /api/job/{jobDisplayId}/tracking
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
     'https://api.abconnect.co/api/job/JOB-2024-001/tracking'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/job/{jobDisplayId}/tracking \
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

.. _get-apijobjobdisplayidtrackingshipmentpronumber:

GET /api/job/{jobDisplayId}/tracking/shipment/{proNumber}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Path Parameters:*

- `proNumber` (string, path) *(required)*: No description available
- `jobDisplayId` (string, path) *(required)*: No description available

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X GET \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/job/JOB-2024-001/tracking/shipment/example-value'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/job/{jobDisplayId}/tracking/shipment/{proNumber} \
       proNumber=example-value \
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
