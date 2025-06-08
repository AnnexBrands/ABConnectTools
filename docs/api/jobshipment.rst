JobShipment API
===============

This section covers the 11 endpoints related to JobShipment.

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
     - /api/job/{jobDisplayId}/shipment/book
     - 
   * - DELETE
     - /api/job/{jobDisplayId}/shipment
     - 
   * - GET
     - /api/job/{jobDisplayId}/shipment/ratequotes
     - 
   * - POST
     - /api/job/{jobDisplayId}/shipment/ratequotes
     - 
   * - GET
     - /api/job/{jobDisplayId}/shipment/origindestination
     - 
   * - GET
     - /api/job/{jobDisplayId}/shipment/accessorials
     - 
   * - POST
     - /api/job/{jobDisplayId}/shipment/accessorial
     - 
   * - DELETE
     - /api/job/{jobDisplayId}/shipment/accessorial/{addOnId}
     - 
   * - GET
     - /api/job/{jobDisplayId}/shipment/ratesstate
     - 
   * - GET
     - /api/job/{jobDisplayId}/shipment/exportdata
     - 
   * - POST
     - /api/job/{jobDisplayId}/shipment/exportdata
     - 

Endpoints
---------

.. _post-apijobjobdisplayidshipmentbook:

POST /api/job/{jobDisplayId}/shipment/book
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
     -d '{
         "example": "data"
     }' \
     'https://api.abconnect.co/api/job/JOB-2024-001/shipment/book'

Using AB CLI:

.. code-block:: bash

   ab api raw post /api/job/{jobDisplayId}/shipment/book \
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

.. _delete-apijobjobdisplayidshipment:

DELETE /api/job/{jobDisplayId}/shipment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Path Parameters:*

- `jobDisplayId` (string, path) *(required)*: No description available

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X DELETE \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/job/JOB-2024-001/shipment'

Using AB CLI:

.. code-block:: bash

   ab api raw delete /api/job/{jobDisplayId}/shipment \
       jobDisplayId=JOB-2024-001

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {
        "status": "success",
        "message": "Resource deleted successfully"
      }

----

.. _get-apijobjobdisplayidshipmentratequotes:

GET /api/job/{jobDisplayId}/shipment/ratequotes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Path Parameters:*

- `jobDisplayId` (string, path) *(required)*: No description available

*Query Parameters:*

- `ShipOutDate` (string, query): No description available
- `RatesSources` (array, query): No description available
- `SettingsKey` (string, query): No description available

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X GET \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/job/JOB-2024-001/shipment/ratequotes'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/job/{jobDisplayId}/shipment/ratequotes \
       jobDisplayId=JOB-2024-001

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      []

----

.. _post-apijobjobdisplayidshipmentratequotes:

POST /api/job/{jobDisplayId}/shipment/ratequotes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
     -d '{
         "example": "data"
     }' \
     'https://api.abconnect.co/api/job/JOB-2024-001/shipment/ratequotes'

Using AB CLI:

.. code-block:: bash

   ab api raw post /api/job/{jobDisplayId}/shipment/ratequotes \
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

.. _get-apijobjobdisplayidshipmentorigindestination:

GET /api/job/{jobDisplayId}/shipment/origindestination
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
     'https://api.abconnect.co/api/job/JOB-2024-001/shipment/origindestination'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/job/{jobDisplayId}/shipment/origindestination \
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

.. _get-apijobjobdisplayidshipmentaccessorials:

GET /api/job/{jobDisplayId}/shipment/accessorials
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
     'https://api.abconnect.co/api/job/JOB-2024-001/shipment/accessorials'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/job/{jobDisplayId}/shipment/accessorials \
       jobDisplayId=JOB-2024-001

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      []

----

.. _post-apijobjobdisplayidshipmentaccessorial:

POST /api/job/{jobDisplayId}/shipment/accessorial
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
     -d '{
         "example": "data"
     }' \
     'https://api.abconnect.co/api/job/JOB-2024-001/shipment/accessorial'

Using AB CLI:

.. code-block:: bash

   ab api raw post /api/job/{jobDisplayId}/shipment/accessorial \
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

.. _delete-apijobjobdisplayidshipmentaccessorialaddonid:

DELETE /api/job/{jobDisplayId}/shipment/accessorial/{addOnId}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Path Parameters:*

- `addOnId` (integer, path) *(required)*: No description available
- `jobDisplayId` (string, path) *(required)*: No description available

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X DELETE \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/job/JOB-2024-001/shipment/accessorial/789e0123-e89b-12d3-a456-426614174002'

Using AB CLI:

.. code-block:: bash

   ab api raw delete /api/job/{jobDisplayId}/shipment/accessorial/{addOnId} \
       addOnId=789e0123-e89b-12d3-a456-426614174002 \
       jobDisplayId=JOB-2024-001

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {
        "status": "success",
        "message": "Resource deleted successfully"
      }

----

.. _get-apijobjobdisplayidshipmentratesstate:

GET /api/job/{jobDisplayId}/shipment/ratesstate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
     'https://api.abconnect.co/api/job/JOB-2024-001/shipment/ratesstate'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/job/{jobDisplayId}/shipment/ratesstate \
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

.. _get-apijobjobdisplayidshipmentexportdata:

GET /api/job/{jobDisplayId}/shipment/exportdata
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
     'https://api.abconnect.co/api/job/JOB-2024-001/shipment/exportdata'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/job/{jobDisplayId}/shipment/exportdata \
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

.. _post-apijobjobdisplayidshipmentexportdata:

POST /api/job/{jobDisplayId}/shipment/exportdata
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
     -d '{
         "example": "data"
     }' \
     'https://api.abconnect.co/api/job/JOB-2024-001/shipment/exportdata'

Using AB CLI:

.. code-block:: bash

   ab api raw post /api/job/{jobDisplayId}/shipment/exportdata \
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
