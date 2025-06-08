TwilioWebhook API
=================

This section covers the 1 endpoints related to TwilioWebhook.

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
     - /api/webhooks/twilio/smsStatusCallback
     - 

Endpoints
---------

.. _post-apiwebhookstwiliosmsstatuscallback:

POST /api/webhooks/twilio/smsStatusCallback
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
     'https://api.abconnect.co/api/webhooks/twilio/smsStatusCallback'

Using AB CLI:

.. code-block:: bash

   ab api raw post /api/webhooks/twilio/smsStatusCallback

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
