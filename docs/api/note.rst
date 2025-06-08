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

      {}

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

      []

----
