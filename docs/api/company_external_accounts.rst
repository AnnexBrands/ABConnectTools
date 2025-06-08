Company External Accounts API
=============================

This section covers the 3 endpoints related to Company External Accounts.

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
     - /api/company/{companyId}/accounts/stripe/connecturl
     - 
   * - POST
     - /api/company/{companyId}/accounts/stripe/completeconnection
     - 
   * - DELETE
     - /api/company/{companyId}/accounts/stripe
     - 

Endpoints
---------

.. _get-apicompanycompanyidaccountsstripeconnecturl:

GET /api/company/{companyId}/accounts/stripe/connecturl
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Path Parameters:*

- `companyId` (string, path) *(required)*: No description available

*Query Parameters:*

- `returnUri` (string, query): No description available

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X GET \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/company/ed282b80-54fe-4f42-bf1b-69103ce1f76c/accounts/stripe/connecturl'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/company/{companyId}/accounts/stripe/connecturl \
       companyId=ed282b80-54fe-4f42-bf1b-69103ce1f76c

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

.. _post-apicompanycompanyidaccountsstripecompleteconnection:

POST /api/company/{companyId}/accounts/stripe/completeconnection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
     'https://api.abconnect.co/api/company/ed282b80-54fe-4f42-bf1b-69103ce1f76c/accounts/stripe/completeconnection'

Using AB CLI:

.. code-block:: bash

   ab api raw post /api/company/{companyId}/accounts/stripe/completeconnection \
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

.. _delete-apicompanycompanyidaccountsstripe:

DELETE /api/company/{companyId}/accounts/stripe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Path Parameters:*

- `companyId` (string, path) *(required)*: No description available

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X DELETE \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/company/ed282b80-54fe-4f42-bf1b-69103ce1f76c/accounts/stripe'

Using AB CLI:

.. code-block:: bash

   ab api raw delete /api/company/{companyId}/accounts/stripe \
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
