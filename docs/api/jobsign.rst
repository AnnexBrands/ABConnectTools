JobSign API
===========

This section covers the 2 endpoints related to JobSign.

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
     - /api/e-sign/{jobDisplayId}/{bookingKey}
     - 
   * - GET
     - /api/e-sign/result
     - 

Endpoints
---------

.. _get-apie-signjobdisplayidbookingkey:

GET /api/e-sign/{jobDisplayId}/{bookingKey}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Path Parameters:*

- `jobDisplayId` (string, path) *(required)*: No description available
- `bookingKey` (string, path) *(required)*: No description available

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X GET \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/e-sign/JOB-2024-001/example-value'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/e-sign/{jobDisplayId}/{bookingKey} \
       jobDisplayId=JOB-2024-001 \
       bookingKey=example-value

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

.. _get-apie-signresult:

GET /api/e-sign/result
~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Query Parameters:*

- `envelope` (string, query): No description available
- `event` (string, query): No description available

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X GET \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/e-sign/result'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/e-sign/result

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
