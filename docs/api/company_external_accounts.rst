Company External Accounts
=========================

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


.. _get-apicompanycompanyidaccountsstripeconnecturl:

GET /api/company/{companyId}/accounts/stripe/connecturl
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Parameters:**

*Path Parameters:*

- `companyId` (string, path) *(required)*: No description available

*Query Parameters:*

- `returnUri` (string, query): No description available

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         
         # Initialize the API client
         api = ABConnectAPI()
         
         # Make the API call
         response = api.raw.get(
             "/api/company/{companyId}/accounts/stripe/connecturl"
         ,
             companyId="ed282b80-54fe-4f42-bf1b-69103ce1f76c"
         
         )
         
         # Process the response
         print(response)

   .. tab:: CLI

      .. code-block:: bash

         ab api raw get /api/company/{companyId}/accounts/stripe/connecturl \
             companyId=ed282b80-54fe-4f42-bf1b-69103ce1f76c

   .. tab:: curl

      .. code-block:: bash

         curl -X GET \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           'https://api.abconnect.co/api/company/ed282b80-54fe-4f42-bf1b-69103ce1f76c/accounts/stripe/connecturl'

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {
        "status": "success",
        "data": {}
      }

----

.. _post-apicompanycompanyidaccountsstripecompleteconnection:

POST /api/company/{companyId}/accounts/stripe/completeconnection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Parameters:**

*Path Parameters:*

- `companyId` (string, path) *(required)*: No description available

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         
         # Initialize the API client
         api = ABConnectAPI()
         
         # Make the API call
         response = api.raw.post(
             "/api/company/{companyId}/accounts/stripe/completeconnection"
         ,
             companyId="ed282b80-54fe-4f42-bf1b-69103ce1f76c"
         ,
             data=
             {
                 "example": "data"
         }
         
         )
         
         # Process the response
         print(response)

   .. tab:: CLI

      .. code-block:: bash

         ab api raw post /api/company/{companyId}/accounts/stripe/completeconnection \
             companyId=ed282b80-54fe-4f42-bf1b-69103ce1f76c

   .. tab:: curl

      .. code-block:: bash

         curl -X POST \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           -H 'Content-Type: application/json' \
           -d '{
               "example": "data"
           }' \
           'https://api.abconnect.co/api/company/ed282b80-54fe-4f42-bf1b-69103ce1f76c/accounts/stripe/completeconnection'

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {
        "id": "789e0123-e89b-12d3-a456-426614174002",
        "status": "created",
        "message": "Resource created successfully"
      }

----

.. _delete-apicompanycompanyidaccountsstripe:

DELETE /api/company/{companyId}/accounts/stripe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Parameters:**

*Path Parameters:*

- `companyId` (string, path) *(required)*: No description available

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         
         # Initialize the API client
         api = ABConnectAPI()
         
         # Make the API call
         response = api.raw.delete(
             "/api/company/{companyId}/accounts/stripe"
         ,
             companyId="ed282b80-54fe-4f42-bf1b-69103ce1f76c"
         
         )
         
         # Process the response
         print(response)

   .. tab:: CLI

      .. code-block:: bash

         ab api raw delete /api/company/{companyId}/accounts/stripe \
             companyId=ed282b80-54fe-4f42-bf1b-69103ce1f76c

   .. tab:: curl

      .. code-block:: bash

         curl -X DELETE \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           'https://api.abconnect.co/api/company/ed282b80-54fe-4f42-bf1b-69103ce1f76c/accounts/stripe'

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {
        "status": "success",
        "message": "Resource deleted successfully"
      }
