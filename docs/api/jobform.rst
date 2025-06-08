JobForm API
===========

This section covers the 2 endpoints related to JobForm.

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
     - /api/job/{jobDisplayId}/form/shipments
     - 
   * - GET
     - /api/job/{jobDisplayId}/form/{formid}
     - 

Endpoints
---------

.. _get-apijobjobdisplayidformshipments:

GET /api/job/{jobDisplayId}/form/shipments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
     'https://api.abconnect.co/api/job/JOB-2024-001/form/shipments'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/job/{jobDisplayId}/form/shipments \
       jobDisplayId=JOB-2024-001

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      []

----

.. _get-apijobjobdisplayidformformid:

GET /api/job/{jobDisplayId}/form/{formid}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Path Parameters:*

- `formId` (string, path) *(required)*: No description available
- `jobDisplayId` (string, path) *(required)*: No description available

*Query Parameters:*

- `type` (string, query): No description available
- `shipmentPlanID` (string, query): No description available

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X GET \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/job/JOB-2024-001/form/{formid}'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/job/{jobDisplayId}/form/{formid} \
       formId=789e0123-e89b-12d3-a456-426614174002 \
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
