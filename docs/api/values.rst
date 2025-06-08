Values API
==========

This section covers the 1 endpoints related to Values.

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
     - /api/Values
     - 

Endpoints
---------

.. _get-apivalues:

GET /api/Values
~~~~~~~~~~~~~~~

****

**Parameters:**

*Query Parameters:*

- `code` (string, query): No description available

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X GET \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/Values'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/Values

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      []

----
