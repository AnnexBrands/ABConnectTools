JobFreightProviders API
=======================

This section covers the 3 endpoints related to JobFreightProviders.

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
     - /api/job/{jobDisplayId}/freightproviders
     - 
   * - GET
     - /api/job/{jobDisplayId}/freightproviders
     - 
   * - POST
     - /api/job/{jobDisplayId}/freightproviders/{optionIndex}/ratequote
     - 

Endpoints
---------

.. _post-apijobjobdisplayidfreightproviders:

POST /api/job/{jobDisplayId}/freightproviders
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
     'https://api.abconnect.co/api/job/JOB-2024-001/freightproviders'

Using AB CLI:

.. code-block:: bash

   ab api raw post /api/job/{jobDisplayId}/freightproviders \
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

.. _get-apijobjobdisplayidfreightproviders:

GET /api/job/{jobDisplayId}/freightproviders
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Path Parameters:*

- `jobDisplayId` (string, path) *(required)*: No description available

*Query Parameters:*

- `ProviderIndexes` (array, query): No description available
- `ShipmentTypes` (array, query): No description available
- `OnlyActive` (boolean, query): No description available

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X GET \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/job/JOB-2024-001/freightproviders'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/job/{jobDisplayId}/freightproviders \
       jobDisplayId=JOB-2024-001

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {
        "data": [
          {
            "id": "123e4567-e89b-12d3-a456-426614174000",
            "name": "Example Item 1",
            "code": "ITEM-001",
            "status": "active",
            "created": "2024-01-01T00:00:00Z",
            "modified": "2024-01-15T12:30:00Z"
          },
          {
            "id": "456e7890-e89b-12d3-a456-426614174001",
            "name": "Example Item 2",
            "code": "ITEM-002",
            "status": "active",
            "created": "2024-01-02T00:00:00Z",
            "modified": "2024-01-16T14:45:00Z"
          }
        ],
        "pagination": {
          "page": 1,
          "per_page": 20,
          "total": 2,
          "total_pages": 1
        }
      }

----

.. _post-apijobjobdisplayidfreightprovidersoptionindexratequote:

POST /api/job/{jobDisplayId}/freightproviders/{optionIndex}/ratequote
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Path Parameters:*

- `optionIndex` (integer, path) *(required)*: No description available
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
     'https://api.abconnect.co/api/job/JOB-2024-001/freightproviders/100/ratequote'

Using AB CLI:

.. code-block:: bash

   ab api raw post /api/job/{jobDisplayId}/freightproviders/{optionIndex}/ratequote \
       optionIndex=100 \
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
