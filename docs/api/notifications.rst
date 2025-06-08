Notifications API
=================

This section covers the 1 endpoints related to Notifications.

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
     - /api/notifications
     - 

Endpoints
---------

.. _get-apinotifications:

GET /api/notifications
~~~~~~~~~~~~~~~~~~~~~~

****

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X GET \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/notifications'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/notifications

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      []

----
