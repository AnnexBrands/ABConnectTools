Contacts API
============

This section covers the 9 endpoints related to Contacts.

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
     - /api/contacts/{id}
     - 
   * - GET
     - /api/contacts/user
     - 
   * - GET
     - /api/contacts/{contactId}/editdetails
     - 
   * - PUT
     - /api/contacts/{contactId}/editdetails
     - 
   * - POST
     - /api/contacts/editdetails
     - 
   * - POST
     - /api/contacts/search
     - 
   * - POST
     - /api/contacts/v2/search
     - 
   * - POST
     - /api/contacts/customers
     - 
   * - GET
     - /api/contacts/{contactId}/primarydetails
     - 

Endpoints
---------

.. _get-apicontactsid:

GET /api/contacts/{id}
~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Path Parameters:*

- `id` (integer, path) *(required)*: No description available

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X GET \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/contacts/789e0123-e89b-12d3-a456-426614174002'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/contacts/{id} \
       id=789e0123-e89b-12d3-a456-426614174002

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {}

----

.. _get-apicontactsuser:

GET /api/contacts/user
~~~~~~~~~~~~~~~~~~~~~~

****

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X GET \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/contacts/user'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/contacts/user

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

.. _get-apicontactscontactideditdetails:

GET /api/contacts/{contactId}/editdetails
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Path Parameters:*

- `contactId` (integer, path) *(required)*: No description available

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X GET \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/contacts/456e7890-e89b-12d3-a456-426614174001/editdetails'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/contacts/{contactId}/editdetails \
       contactId=456e7890-e89b-12d3-a456-426614174001

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      []

----

.. _put-apicontactscontactideditdetails:

PUT /api/contacts/{contactId}/editdetails
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Path Parameters:*

- `contactId` (integer, path) *(required)*: No description available

*Query Parameters:*

- `franchiseeId` (string, query): No description available

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
     'https://api.abconnect.co/api/contacts/456e7890-e89b-12d3-a456-426614174001/editdetails'

Using AB CLI:

.. code-block:: bash

   ab api raw put /api/contacts/{contactId}/editdetails \
       contactId=456e7890-e89b-12d3-a456-426614174001

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {}

----

.. _post-apicontactseditdetails:

POST /api/contacts/editdetails
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Query Parameters:*

- `franchiseeId` (string, query): No description available

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
     'https://api.abconnect.co/api/contacts/editdetails'

Using AB CLI:

.. code-block:: bash

   ab api raw post /api/contacts/editdetails

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {}

----

.. _post-apicontactssearch:

POST /api/contacts/search
~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Query Parameters:*

- `companyId` (string, query): No description available

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
     'https://api.abconnect.co/api/contacts/search'

Using AB CLI:

.. code-block:: bash

   ab api raw post /api/contacts/search

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      []

----

.. _post-apicontactsv2search:

POST /api/contacts/v2/search
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
     'https://api.abconnect.co/api/contacts/v2/search'

Using AB CLI:

.. code-block:: bash

   ab api raw post /api/contacts/v2/search

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      []

----

.. _post-apicontactscustomers:

POST /api/contacts/customers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
     'https://api.abconnect.co/api/contacts/customers'

Using AB CLI:

.. code-block:: bash

   ab api raw post /api/contacts/customers

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

.. _get-apicontactscontactidprimarydetails:

GET /api/contacts/{contactId}/primarydetails
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Path Parameters:*

- `contactId` (integer, path) *(required)*: No description available

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X GET \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/contacts/456e7890-e89b-12d3-a456-426614174001/primarydetails'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/contacts/{contactId}/primarydetails \
       contactId=456e7890-e89b-12d3-a456-426614174001

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      []

----
