Address API
===========

This section covers the 4 endpoints related to Address.

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
     - /api/address/isvalid
     - 
   * - POST
     - /api/address/{addressId}/validated
     - 
   * - POST
     - /api/address/{addressId}/avoidValidation
     - 
   * - GET
     - /api/address/propertytype
     - 

Endpoints
---------

.. _get-apiaddressisvalid:

GET /api/address/isvalid
~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Query Parameters:*

- `Line1` (string, query): No description available
- `City` (string, query): No description available
- `State` (string, query): No description available
- `Zip` (string, query): No description available

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X GET \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/address/isvalid'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/address/isvalid

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

.. _post-apiaddressaddressidvalidated:

POST /api/address/{addressId}/validated
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Path Parameters:*

- `addressId` (integer, path) *(required)*: No description available

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
     'https://api.abconnect.co/api/address/789e0123-e89b-12d3-a456-426614174002/validated'

Using AB CLI:

.. code-block:: bash

   ab api raw post /api/address/{addressId}/validated \
       addressId=789e0123-e89b-12d3-a456-426614174002

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

.. _post-apiaddressaddressidavoidvalidation:

POST /api/address/{addressId}/avoidValidation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Path Parameters:*

- `addressId` (integer, path) *(required)*: No description available

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X POST \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     -H 'Content-Type: application/json' \
     'https://api.abconnect.co/api/address/789e0123-e89b-12d3-a456-426614174002/avoidValidation'

Using AB CLI:

.. code-block:: bash

   ab api raw post /api/address/{addressId}/avoidValidation \
       addressId=789e0123-e89b-12d3-a456-426614174002

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

.. _get-apiaddresspropertytype:

GET /api/address/propertytype
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Query Parameters:*

- `Address1` (string, query): No description available
- `Address2` (string, query): No description available
- `City` (string, query): No description available
- `State` (string, query): No description available
- `ZipCode` (string, query): No description available

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X GET \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/address/propertytype'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/address/propertytype

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
