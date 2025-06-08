GridViews API
=============

This section covers the 8 endpoints related to GridViews.

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
     - /api/views/all
     - 
   * - GET
     - /api/views/{viewId}
     - 
   * - DELETE
     - /api/views/{viewId}
     - 
   * - GET
     - /api/views/{viewId}/accessinfo
     - 
   * - POST
     - /api/views
     - 
   * - PUT
     - /api/views/{viewId}/access
     - 
   * - GET
     - /api/views/datasetsps
     - 
   * - GET
     - /api/views/datasetsp/{spName}
     - 

Endpoints
---------

.. _get-apiviewsall:

GET /api/views/all
~~~~~~~~~~~~~~~~~~

****

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X GET \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/views/all'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/views/all

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

.. _get-apiviewsviewid:

GET /api/views/{viewId}
~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Path Parameters:*

- `viewId` (integer, path) *(required)*: No description available

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X GET \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/views/789e0123-e89b-12d3-a456-426614174002'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/views/{viewId} \
       viewId=789e0123-e89b-12d3-a456-426614174002

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

.. _delete-apiviewsviewid:

DELETE /api/views/{viewId}
~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Path Parameters:*

- `viewId` (integer, path) *(required)*: No description available

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X DELETE \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/views/789e0123-e89b-12d3-a456-426614174002'

Using AB CLI:

.. code-block:: bash

   ab api raw delete /api/views/{viewId} \
       viewId=789e0123-e89b-12d3-a456-426614174002

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {
        "status": "success",
        "message": "Resource deleted successfully"
      }

----

.. _get-apiviewsviewidaccessinfo:

GET /api/views/{viewId}/accessinfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Path Parameters:*

- `viewId` (integer, path) *(required)*: No description available

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X GET \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/views/789e0123-e89b-12d3-a456-426614174002/accessinfo'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/views/{viewId}/accessinfo \
       viewId=789e0123-e89b-12d3-a456-426614174002

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

.. _post-apiviews:

POST /api/views
~~~~~~~~~~~~~~~

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
     'https://api.abconnect.co/api/views'

Using AB CLI:

.. code-block:: bash

   ab api raw post /api/views

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

.. _put-apiviewsviewidaccess:

PUT /api/views/{viewId}/access
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Path Parameters:*

- `viewId` (integer, path) *(required)*: No description available

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
     'https://api.abconnect.co/api/views/789e0123-e89b-12d3-a456-426614174002/access'

Using AB CLI:

.. code-block:: bash

   ab api raw put /api/views/{viewId}/access \
       viewId=789e0123-e89b-12d3-a456-426614174002

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {
        "id": "123e4567-e89b-12d3-a456-426614174000",
        "status": "updated",
        "message": "Resource updated successfully",
        "modified_at": "2024-01-20T10:00:00Z"
      }

----

.. _get-apiviewsdatasetsps:

GET /api/views/datasetsps
~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X GET \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/views/datasetsps'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/views/datasetsps

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

.. _get-apiviewsdatasetspspname:

GET /api/views/datasetsp/{spName}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Path Parameters:*

- `spName` (string, path) *(required)*: No description available

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X GET \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/views/datasetsp/Example Name'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/views/datasetsp/{spName} \
       spName=Example Name

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
