JobRfq API
==========

This section covers the 2 endpoints related to JobRfq.

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
     - /api/job/{jobDisplayId}/rfq
     - 
   * - GET
     - /api/job/{jobDisplayId}/rfq/statusof/{rfqServiceType}/forcompany/{companyId}
     - 

Endpoints
---------

.. _get-apijobjobdisplayidrfq:

GET /api/job/{jobDisplayId}/rfq
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Path Parameters:*

- `jobDisplayId` (string, path) *(required)*: No description available

*Query Parameters:*

- `rfqServiceType` (string, query): No description available

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X GET \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/job/JOB-2024-001/rfq'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/job/{jobDisplayId}/rfq \
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

.. _get-apijobjobdisplayidrfqstatusofrfqservicetypeforcompanycompanyid:

GET /api/job/{jobDisplayId}/rfq/statusof/{rfqServiceType}/forcompany/{companyId}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Path Parameters:*

- `companyId` (string, path) *(required)*: No description available
- `rfqServiceType` (string, path) *(required)*: No description available
- `jobDisplayId` (string, path) *(required)*: No description available

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X GET \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/job/JOB-2024-001/rfq/statusof/example-value/forcompany/ed282b80-54fe-4f42-bf1b-69103ce1f76c'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/job/{jobDisplayId}/rfq/statusof/{rfqServiceType}/forcompany/{companyId} \
       companyId=ed282b80-54fe-4f42-bf1b-69103ce1f76c \
       rfqServiceType=example-value \
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
