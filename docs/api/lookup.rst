Lookup API
==========

This section covers the 14 endpoints related to Lookup.

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
     - /api/lookup/{masterConstantKey}
     - 
   * - GET
     - /api/lookup/{masterConstantKey}/{valueId}
     - 
   * - GET
     - /api/lookup/countries
     - 
   * - GET
     - /api/lookup/resetMasterConstantCache
     - 
   * - GET
     - /api/lookup/accessKeys
     - 
   * - GET
     - /api/lookup/accessKey/{accessKey}
     - 
   * - GET
     - /api/lookup/documentTypes
     - 
   * - GET
     - /api/lookup/items
     - 
   * - GET
     - /api/lookup/referCategory
     - 
   * - GET
     - /api/lookup/referCategoryHeirachy
     - 
   * - GET
     - /api/lookup/PPCCampaigns
     - 
   * - GET
     - /api/lookup/parcelPackageTypes
     - 
   * - GET
     - /api/lookup/comonInsurance
     - 
   * - GET
     - /api/lookup/contactTypes
     - 

Endpoints
---------

.. _get-apilookupmasterconstantkey:

GET /api/lookup/{masterConstantKey}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Path Parameters:*

- `masterConstantKey` (string, path) *(required)*: No description available

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X GET \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/lookup/example-value'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/lookup/{masterConstantKey} \
       masterConstantKey=example-value

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

.. _get-apilookupmasterconstantkeyvalueid:

GET /api/lookup/{masterConstantKey}/{valueId}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Path Parameters:*

- `masterConstantKey` (string, path) *(required)*: No description available
- `valueId` (string, path) *(required)*: No description available

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X GET \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/lookup/example-value/789e0123-e89b-12d3-a456-426614174002'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/lookup/{masterConstantKey}/{valueId} \
       masterConstantKey=example-value \
       valueId=789e0123-e89b-12d3-a456-426614174002

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

.. _get-apilookupcountries:

GET /api/lookup/countries
~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X GET \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/lookup/countries'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/lookup/countries

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      []

----

.. _get-apilookupresetmasterconstantcache:

GET /api/lookup/resetMasterConstantCache
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X GET \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/lookup/resetMasterConstantCache'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/lookup/resetMasterConstantCache

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

.. _get-apilookupaccesskeys:

GET /api/lookup/accessKeys
~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X GET \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/lookup/accessKeys'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/lookup/accessKeys

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      []

----

.. _get-apilookupaccesskeyaccesskey:

GET /api/lookup/accessKey/{accessKey}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Path Parameters:*

- `accessKey` (string, path) *(required)*: No description available

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X GET \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/lookup/accessKey/example-value'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/lookup/accessKey/{accessKey} \
       accessKey=example-value

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

.. _get-apilookupdocumenttypes:

GET /api/lookup/documentTypes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Query Parameters:*

- `documentSource` (string, query): No description available

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X GET \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/lookup/documentTypes'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/lookup/documentTypes

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      []

----

.. _get-apilookupitems:

GET /api/lookup/items
~~~~~~~~~~~~~~~~~~~~~

****

**Parameters:**

*Query Parameters:*

- `jobDisplayId` (string, query): No description available
- `jobItemId` (string, query): No description available

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X GET \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/lookup/items'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/lookup/items

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      []

----

.. _get-apilookuprefercategory:

GET /api/lookup/referCategory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X GET \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/lookup/referCategory'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/lookup/referCategory

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

.. _get-apilookuprefercategoryheirachy:

GET /api/lookup/referCategoryHeirachy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X GET \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/lookup/referCategoryHeirachy'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/lookup/referCategoryHeirachy

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

.. _get-apilookupppccampaigns:

GET /api/lookup/PPCCampaigns
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X GET \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/lookup/PPCCampaigns'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/lookup/PPCCampaigns

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      []

----

.. _get-apilookupparcelpackagetypes:

GET /api/lookup/parcelPackageTypes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X GET \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/lookup/parcelPackageTypes'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/lookup/parcelPackageTypes

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      []

----

.. _get-apilookupcomoninsurance:

GET /api/lookup/comonInsurance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X GET \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/lookup/comonInsurance'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/lookup/comonInsurance

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

.. _get-apilookupcontacttypes:

GET /api/lookup/contactTypes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

****

**Example Request:**

Using curl:

.. code-block:: bash
   :linenos:

   curl -X GET \
     -H 'Authorization: Bearer YOUR_API_TOKEN' \
     'https://api.abconnect.co/api/lookup/contactTypes'

Using AB CLI:

.. code-block:: bash

   ab api raw get /api/lookup/contactTypes

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      []

----
