JobSmsTemplate API
==================

This section covers the 6 endpoints related to JobSmsTemplate.

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
     - /api/SmsTemplate/notificationTokens
     - 
   * - GET
     - /api/SmsTemplate/jobStatuses
     - 
   * - GET
     - /api/SmsTemplate/list
     - 
   * - GET
     - /api/SmsTemplate/{templateId}
     - 
   * - DELETE
     - /api/SmsTemplate/{templateId}
     - 
   * - POST
     - /api/SmsTemplate/save
     - 

Endpoints
---------

.. _get-apismstemplatenotificationtokens:

GET /api/SmsTemplate/notificationTokens
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X GET \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/SmsTemplate/notificationTokens'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/SmsTemplate/notificationTokens

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      []

----

.. _get-apismstemplatejobstatuses:

GET /api/SmsTemplate/jobStatuses
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X GET \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/SmsTemplate/jobStatuses'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/SmsTemplate/jobStatuses

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      []

----

.. _get-apismstemplatelist:

GET /api/SmsTemplate/list
~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Query Parameters:*

- `companyId` (string, query): No description available

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X GET \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/SmsTemplate/list'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/SmsTemplate/list

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

.. _get-apismstemplatetemplateid:

GET /api/SmsTemplate/{templateId}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Path Parameters:*

- `templateId` (integer, path) *(required)*: No description available

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X GET \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/SmsTemplate/789e0123-e89b-12d3-a456-426614174002'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/SmsTemplate/{templateId} \
       templateId=789e0123-e89b-12d3-a456-426614174002

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

.. _delete-apismstemplatetemplateid:

DELETE /api/SmsTemplate/{templateId}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Path Parameters:*

- `templateId` (integer, path) *(required)*: No description available

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X DELETE \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/SmsTemplate/789e0123-e89b-12d3-a456-426614174002'

Using AB CLI:

.. code-block:: bash

   ab api raw delete /api/SmsTemplate/{templateId} \
       templateId=789e0123-e89b-12d3-a456-426614174002

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {
        "status": "success",
        "message": "Resource deleted successfully"
      }

----

.. _post-apismstemplatesave:

POST /api/SmsTemplate/save
~~~~~~~~~~~~~~~~~~~~~~~~~~

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
     'https://api.abconnect.co/api/SmsTemplate/save'

Using AB CLI:

.. code-block:: bash

   ab api raw post /api/SmsTemplate/save

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
