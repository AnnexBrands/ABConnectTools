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
     'https://api.abconnect.co/api/company/ed282b80-54fe-4f42-bf1b-69103ce1f76c/containerthicknessinches'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/company/{companyId}/containerthicknessinches \
       companyId=ed282b80-54fe-4f42-bf1b-69103ce1f76c

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      []

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
     'https://api.abconnect.co/api/company/ed282b80-54fe-4f42-bf1b-69103ce1f76c/containerthicknessinches'

Using AB CLI:

.. code-block:: bash

   ab api raw post /api/company/{companyId}/containerthicknessinches \
       companyId=ed282b80-54fe-4f42-bf1b-69103ce1f76c

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
     'https://api.abconnect.co/api/company/ed282b80-54fe-4f42-bf1b-69103ce1f76c/containerthicknessinches'

Using AB CLI:

.. code-block:: bash

   ab api raw delete /api/company/{companyId}/containerthicknessinches \
       companyId=ed282b80-54fe-4f42-bf1b-69103ce1f76c

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {
        "status": "success",
        "message": "Resource deleted successfully"
      }

----
