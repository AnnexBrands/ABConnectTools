ContainerThicknessInches API
============================

This section covers the 3 endpoints related to ContainerThicknessInches.

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
     - /api/company/{companyId}/containerthicknessinches
     - 
   * - POST
     - /api/company/{companyId}/containerthicknessinches
     - 
   * - DELETE
     - /api/company/{companyId}/containerthicknessinches
     - 

Endpoints
---------

.. _get-apicompanycompanyidcontainerthicknessinches:

GET /api/company/{companyId}/containerthicknessinches
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
     'https://api.abconnect.co/api/company/123e4567-e89b-12d3-a456-426614174000/containerthicknessinches'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/company/{companyId}/containerthicknessinches \
       companyId=123e4567-e89b-12d3-a456-426614174000

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

.. _post-apicompanycompanyidcontainerthicknessinches:

POST /api/company/{companyId}/containerthicknessinches
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Path Parameters:*

- `companyId` (string, path) *(required)*: No description available

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
     'https://api.abconnect.co/api/company/123e4567-e89b-12d3-a456-426614174000/containerthicknessinches'

Using AB CLI:

.. code-block:: bash

   ab api raw post /api/company/{companyId}/containerthicknessinches \
       companyId=123e4567-e89b-12d3-a456-426614174000

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

.. _delete-apicompanycompanyidcontainerthicknessinches:

DELETE /api/company/{companyId}/containerthicknessinches
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Path Parameters:*

- `companyId` (string, path) *(required)*: No description available

*Query Parameters:*

- `containerId` (integer, query): No description available

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X DELETE \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/company/123e4567-e89b-12d3-a456-426614174000/containerthicknessinches'

Using AB CLI:

.. code-block:: bash

   ab api raw delete /api/company/{companyId}/containerthicknessinches \
       companyId=123e4567-e89b-12d3-a456-426614174000

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {
        "status": "success",
        "message": "Resource deleted successfully"
      }

----
