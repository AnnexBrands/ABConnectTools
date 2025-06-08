ContactHistory API
==================

This section covers the 3 endpoints related to ContactHistory.

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
     - /api/contacts/{contactId}/history
     - 
   * - GET
     - /api/contacts/{contactId}/history/aggregated
     - 
   * - GET
     - /api/contacts/{contactId}/history/graphdata
     - 

Endpoints
---------

.. _post-apicontactscontactidhistory:

POST /api/contacts/{contactId}/history
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Path Parameters:*

- `contactId` (integer, path) *(required)*: No description available

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
     'https://api.abconnect.co/api/contacts/456e7890-e89b-12d3-a456-426614174001/history'

Using AB CLI:

.. code-block:: bash

   ab api raw post /api/contacts/{contactId}/history \
       contactId=456e7890-e89b-12d3-a456-426614174001

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

.. _get-apicontactscontactidhistoryaggregated:

GET /api/contacts/{contactId}/history/aggregated
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Path Parameters:*

- `contactId` (integer, path) *(required)*: No description available

*Query Parameters:*

- `statuses` (array, query): No description available

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X GET \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/contacts/456e7890-e89b-12d3-a456-426614174001/history/aggregated'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/contacts/{contactId}/history/aggregated \
       contactId=456e7890-e89b-12d3-a456-426614174001

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

.. _get-apicontactscontactidhistorygraphdata:

GET /api/contacts/{contactId}/history/graphdata
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Path Parameters:*

- `contactId` (integer, path) *(required)*: No description available

*Query Parameters:*

- `statuses` (array, query): No description available

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X GET \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/contacts/456e7890-e89b-12d3-a456-426614174001/history/graphdata'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/contacts/{contactId}/history/graphdata \
       contactId=456e7890-e89b-12d3-a456-426614174001

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
