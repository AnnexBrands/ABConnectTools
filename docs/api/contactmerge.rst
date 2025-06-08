ContactMerge API
================

This section covers the 2 endpoints related to ContactMerge.

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
     - /api/contacts/{mergeToId}/merge/preview
     - 
   * - PUT
     - /api/contacts/{mergeToId}/merge
     - 

Endpoints
---------

.. _post-apicontactsmergetoidmergepreview:

POST /api/contacts/{mergeToId}/merge/preview
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Path Parameters:*

- `mergeToId` (integer, path) *(required)*: No description available

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
     'https://api.abconnect.co/api/contacts/789e0123-e89b-12d3-a456-426614174002/merge/preview'

Using AB CLI:

.. code-block:: bash

   ab api raw post /api/contacts/{mergeToId}/merge/preview \
       mergeToId=789e0123-e89b-12d3-a456-426614174002

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

.. _put-apicontactsmergetoidmerge:

PUT /api/contacts/{mergeToId}/merge
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Path Parameters:*

- `mergeToId` (integer, path) *(required)*: No description available

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
     'https://api.abconnect.co/api/contacts/789e0123-e89b-12d3-a456-426614174002/merge'

Using AB CLI:

.. code-block:: bash

   ab api raw put /api/contacts/{mergeToId}/merge \
       mergeToId=789e0123-e89b-12d3-a456-426614174002

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
