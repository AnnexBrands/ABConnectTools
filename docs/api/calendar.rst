Calendar API
============

This section covers the 4 endpoints related to Calendar.

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
     - /api/company/{companyId}/calendar/{date}
     - 
   * - GET
     - /api/company/{companyId}/calendar/{date}/baseinfo
     - 
   * - GET
     - /api/company/{companyId}/calendar/{date}/startofday
     - 
   * - GET
     - /api/company/{companyId}/calendar/{date}/endofday
     - 

Endpoints
---------

.. _get-apicompanycompanyidcalendardate:

GET /api/company/{companyId}/calendar/{date}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Path Parameters:*

- `companyId` (string, path) *(required)*: No description available
- `date` (string, path) *(required)*: No description available

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X GET \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/company/ed282b80-54fe-4f42-bf1b-69103ce1f76c/calendar/2024-01-15T12:00:00Z'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/company/{companyId}/calendar/{date} \
       companyId=ed282b80-54fe-4f42-bf1b-69103ce1f76c \
       date=2024-01-15T12:00:00Z

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

.. _get-apicompanycompanyidcalendardatebaseinfo:

GET /api/company/{companyId}/calendar/{date}/baseinfo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Path Parameters:*

- `companyId` (string, path) *(required)*: No description available
- `date` (string, path) *(required)*: No description available

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X GET \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/company/ed282b80-54fe-4f42-bf1b-69103ce1f76c/calendar/2024-01-15T12:00:00Z/baseinfo'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/company/{companyId}/calendar/{date}/baseinfo \
       companyId=ed282b80-54fe-4f42-bf1b-69103ce1f76c \
       date=2024-01-15T12:00:00Z

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

.. _get-apicompanycompanyidcalendardatestartofday:

GET /api/company/{companyId}/calendar/{date}/startofday
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Path Parameters:*

- `companyId` (string, path) *(required)*: No description available
- `date` (string, path) *(required)*: No description available

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X GET \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/company/ed282b80-54fe-4f42-bf1b-69103ce1f76c/calendar/2024-01-15T12:00:00Z/startofday'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/company/{companyId}/calendar/{date}/startofday \
       companyId=ed282b80-54fe-4f42-bf1b-69103ce1f76c \
       date=2024-01-15T12:00:00Z

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

.. _get-apicompanycompanyidcalendardateendofday:

GET /api/company/{companyId}/calendar/{date}/endofday
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Path Parameters:*

- `companyId` (string, path) *(required)*: No description available
- `date` (string, path) *(required)*: No description available

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X GET \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/company/ed282b80-54fe-4f42-bf1b-69103ce1f76c/calendar/2024-01-15T12:00:00Z/endofday'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/company/{companyId}/calendar/{date}/endofday \
       companyId=ed282b80-54fe-4f42-bf1b-69103ce1f76c \
       date=2024-01-15T12:00:00Z

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
