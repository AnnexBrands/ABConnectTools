Note API
========

This section covers the 4 endpoints related to Note.

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
     - /api/note
     - 
   * - POST
     - /api/note
     - 
   * - PUT
     - /api/note/{id}
     - 
   * - GET
     - /api/note/suggestUsers
     - 

Endpoints
---------

.. _get-apinote:

GET /api/note
~~~~~~~~~~~~~

****

**Parameters:**

*Query Parameters:*

- `category` (array, query): No description available
- `jobId` (string, query): No description available
- `contactId` (integer, query): No description available
- `companyId` (string, query): No description available

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X GET \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/note'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/note

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

.. _post-apinote:

POST /api/note
~~~~~~~~~~~~~~

****

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
     'https://api.abconnect.co/api/note'

Using AB CLI:

.. code-block:: bash

   ab api raw post /api/note

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

.. _put-apinoteid:

PUT /api/note/{id}
~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Path Parameters:*

- `id` (integer, path) *(required)*: No description available

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X PUT \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     -H 'Content-Type: application/json' \
     -d '{
         "example": "data"
     }' \
     'https://api.abconnect.co/api/note/789e0123-e89b-12d3-a456-426614174002'

Using AB CLI:

.. code-block:: bash

   ab api raw put /api/note/{id} \
       id=789e0123-e89b-12d3-a456-426614174002

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {
        "id": "123e4567-e89b-12d3-a456-426614174000",
        "name": "Example Item",
        "code": "ITEM-001",
        "description": "This is a detailed example item",
        "status": "active",
        "type": "standard",
        "metadata": {
          "created_by": "user@example.com",
          "created_at": "2024-01-01T00:00:00Z",
          "updated_at": "2024-01-15T12:30:00Z"
        },
        "settings": {
          "notifications": true,
          "auto_update": false
        }
      }

----

.. _get-apinotesuggestusers:

GET /api/note/suggestUsers
~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Query Parameters:*

- `SearchKey` (string, query) *(required)*: No description available
- `JobFranchiseeId` (string, query): No description available
- `CompanyId` (string, query): No description available

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X GET \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/note/suggestUsers?SearchKey=example-value'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/note/suggestUsers \
       SearchKey=example-value

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
