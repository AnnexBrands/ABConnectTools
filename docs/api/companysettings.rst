CompanySettings API
===================

This section covers the 1 endpoints related to CompanySettings.

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
     - /api/company/{companyId}/setupdata
     - 

Endpoints
---------

.. _get-apicompanycompanyidsetupdata:

GET /api/company/{companyId}/setupdata
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
     'https://api.abconnect.co/api/company/123e4567-e89b-12d3-a456-426614174000/setupdata'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/company/{companyId}/setupdata \
       companyId=123e4567-e89b-12d3-a456-426614174000

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
