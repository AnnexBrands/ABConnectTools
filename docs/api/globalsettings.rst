GlobalSettings API
==================

This section covers the 5 endpoints related to GlobalSettings.

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
     - /api/admin/globalsettings/companyhierarchy
     - 
   * - GET
     - /api/admin/globalsettings/companyhierarchy/company/{companyId}
     - 
   * - POST
     - /api/admin/globalsettings/getinsuranceexceptions
     - 
   * - POST
     - /api/admin/globalsettings/approveinsuranceexception
     - 
   * - POST
     - /api/admin/globalsettings/intacct
     - 

Endpoints
---------

.. _get-apiadminglobalsettingscompanyhierarchy:

GET /api/admin/globalsettings/companyhierarchy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X GET \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/admin/globalsettings/companyhierarchy'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/admin/globalsettings/companyhierarchy

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

.. _get-apiadminglobalsettingscompanyhierarchycompanycompanyid:

GET /api/admin/globalsettings/companyhierarchy/company/{companyId}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
     'https://api.abconnect.co/api/admin/globalsettings/companyhierarchy/company/ed282b80-54fe-4f42-bf1b-69103ce1f76c'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/admin/globalsettings/companyhierarchy/company/{companyId} \
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

.. _post-apiadminglobalsettingsgetinsuranceexceptions:

POST /api/admin/globalsettings/getinsuranceexceptions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
     'https://api.abconnect.co/api/admin/globalsettings/getinsuranceexceptions'

Using AB CLI:

.. code-block:: bash

   ab api raw post /api/admin/globalsettings/getinsuranceexceptions

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

.. _post-apiadminglobalsettingsapproveinsuranceexception:

POST /api/admin/globalsettings/approveinsuranceexception
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Query Parameters:*

- `JobId` (string, query): No description available

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X POST \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     -H 'Content-Type: application/json' \
     'https://api.abconnect.co/api/admin/globalsettings/approveinsuranceexception'

Using AB CLI:

.. code-block:: bash

   ab api raw post /api/admin/globalsettings/approveinsuranceexception

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

.. _post-apiadminglobalsettingsintacct:

POST /api/admin/globalsettings/intacct
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
     'https://api.abconnect.co/api/admin/globalsettings/intacct'

Using AB CLI:

.. code-block:: bash

   ab api raw post /api/admin/globalsettings/intacct

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
