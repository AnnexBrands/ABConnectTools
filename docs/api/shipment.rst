Shipment API
============

This section covers the 3 endpoints related to Shipment.

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
     - /api/shipment
     - 
   * - GET
     - /api/shipment/accessorials
     - 
   * - GET
     - /api/shipment/document/{docId}
     - 

Endpoints
---------

.. _get-apishipment:

GET /api/shipment
~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Query Parameters:*

- `franchiseeId` (string, query): No description available
- `providerId` (string, query): No description available
- `proNumber` (string, query): No description available

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X GET \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/shipment'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/shipment

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

.. _get-apishipmentaccessorials:

GET /api/shipment/accessorials
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X GET \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/shipment/accessorials'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/shipment/accessorials

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      []

----

.. _get-apishipmentdocumentdocid:

GET /api/shipment/document/{docId}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Path Parameters:*

- `docId` (string, path) *(required)*: No description available

*Query Parameters:*

- `franchiseeId` (string, query): No description available

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X GET \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/shipment/document/789e0123-e89b-12d3-a456-426614174002'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/shipment/document/{docId} \
       docId=789e0123-e89b-12d3-a456-426614174002

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
