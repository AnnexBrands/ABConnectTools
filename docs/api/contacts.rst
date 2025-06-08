Contacts
========

Manage contact information for individuals associated with companies. Contacts can have various roles such as primary contact, billing contact, or operations contact.

Quick Reference
---------------

.. list-table::
   :header-rows: 1
   :widths: 10 40 50

   * - Method
     - Endpoint
     - Description
   * - GET
     - /api/contacts/{id}
     - Get contact by ID
   * - GET
     - /api/contacts/user
     - 
   * - GET
     - /api/contacts/{contactId}/editdetails
     - 
   * - PUT
     - /api/contacts/{contactId}/editdetails
     - 
   * - POST
     - /api/contacts/editdetails
     - 
   * - POST
     - /api/contacts/search
     - 
   * - POST
     - /api/contacts/v2/search
     - 
   * - POST
     - /api/contacts/customers
     - 
   * - GET
     - /api/contacts/{contactId}/primarydetails
     - 


.. _get-apicontactsid:

GET /api/contacts/{id}
~~~~~~~~~~~~~~~~~~~~~~

**Get contact by ID**

Retrieves information about a specific contact.

**Parameters:**

*Path Parameters:*

- `id` (integer, path) *(required)*: No description available

**Response Type:**

:class:`~ABConnect.api.models.contacts.Contact`

See the model documentation for detailed field descriptions.

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         
         # Initialize the API client
         api = ABConnectAPI()
         
         # Make the API call
         response = api.raw.get(
             "/api/contacts/{id}"
         ,
             id=789e0123-e89b-12d3-a456-426614174002
         
         )
         
         # Process the response
         print(response)

   .. tab:: CLI

      .. code-block:: bash

         ab api raw get /api/contacts/{id} \
             id=789e0123-e89b-12d3-a456-426614174002

   .. tab:: curl

      .. code-block:: bash

         curl -X GET \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           'https://api.abconnect.co/api/contacts/789e0123-e89b-12d3-a456-426614174002'

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {
        "id": 266841,
        "contactDisplayId": "1",
        "fullName": "John Doe",
        "firstName": "John",
        "lastName": "Doe",
        "contactTypeId": 1,
        "companyId": "ed282b80-54fe-4f42-bf1b-69103ce1f76c",
        "isActive": true,
        "primaryEmail": "john.doe@example.com",
        "primaryPhone": "555-123-4567"
      }

----

.. _get-apicontactsuser:

GET /api/contacts/user
~~~~~~~~~~~~~~~~~~~~~~

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         
         # Initialize the API client
         api = ABConnectAPI()
         
         # Make the API call
         response = api.raw.get(
             "/api/contacts/user"
         
         )
         
         # Process the response
         print(response)

   .. tab:: CLI

      .. code-block:: bash

         ab api raw get /api/contacts/user

   .. tab:: curl

      .. code-block:: bash

         curl -X GET \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           'https://api.abconnect.co/api/contacts/user'

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {
        "status": "success",
        "data": {}
      }

----

.. _get-apicontactscontactideditdetails:

GET /api/contacts/{contactId}/editdetails
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Parameters:**

*Path Parameters:*

- `contactId` (integer, path) *(required)*: No description available

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         
         # Initialize the API client
         api = ABConnectAPI()
         
         # Make the API call
         response = api.raw.get(
             "/api/contacts/{contactId}/editdetails"
         ,
             contactId=456e7890-e89b-12d3-a456-426614174001
         
         )
         
         # Process the response
         print(response)

   .. tab:: CLI

      .. code-block:: bash

         ab api raw get /api/contacts/{contactId}/editdetails \
             contactId=456e7890-e89b-12d3-a456-426614174001

   .. tab:: curl

      .. code-block:: bash

         curl -X GET \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           'https://api.abconnect.co/api/contacts/456e7890-e89b-12d3-a456-426614174001/editdetails'

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      []

----

.. _put-apicontactscontactideditdetails:

PUT /api/contacts/{contactId}/editdetails
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Parameters:**

*Path Parameters:*

- `contactId` (integer, path) *(required)*: No description available

*Query Parameters:*

- `franchiseeId` (string, query): No description available

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         
         # Initialize the API client
         api = ABConnectAPI()
         
         # Make the API call
         response = api.raw.put(
             "/api/contacts/{contactId}/editdetails"
         ,
             contactId="456e7890-e89b-12d3-a456-426614174001"
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

         ab api raw put /api/contacts/{contactId}/editdetails \
             contactId=456e7890-e89b-12d3-a456-426614174001

   .. tab:: curl

      .. code-block:: bash

         curl -X PUT \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           -H 'Content-Type: application/json' \
           -d '{
               "example": "data"
           }' \
           'https://api.abconnect.co/api/contacts/456e7890-e89b-12d3-a456-426614174001/editdetails'

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {}

----

.. _post-apicontactseditdetails:

POST /api/contacts/editdetails
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Parameters:**

*Query Parameters:*

- `franchiseeId` (string, query): No description available

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         
         # Initialize the API client
         api = ABConnectAPI()
         
         # Make the API call
         response = api.raw.post(
             "/api/contacts/editdetails"
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

         ab api raw post /api/contacts/editdetails

   .. tab:: curl

      .. code-block:: bash

         curl -X POST \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           -H 'Content-Type: application/json' \
           -d '{
               "example": "data"
           }' \
           'https://api.abconnect.co/api/contacts/editdetails'

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {}

----

.. _post-apicontactssearch:

POST /api/contacts/search
~~~~~~~~~~~~~~~~~~~~~~~~~

**Parameters:**

*Query Parameters:*

- `companyId` (string, query): No description available

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         
         # Initialize the API client
         api = ABConnectAPI()
         
         # Make the API call
         response = api.raw.post(
             "/api/contacts/search"
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

         ab api raw post /api/contacts/search

   .. tab:: curl

      .. code-block:: bash

         curl -X POST \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           -H 'Content-Type: application/json' \
           -d '{
               "example": "data"
           }' \
           'https://api.abconnect.co/api/contacts/search'

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      []

----

.. _post-apicontactsv2search:

POST /api/contacts/v2/search
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         
         # Initialize the API client
         api = ABConnectAPI()
         
         # Make the API call
         response = api.raw.post(
             "/api/contacts/v2/search"
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

         ab api raw post /api/contacts/v2/search

   .. tab:: curl

      .. code-block:: bash

         curl -X POST \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           -H 'Content-Type: application/json' \
           -d '{
               "example": "data"
           }' \
           'https://api.abconnect.co/api/contacts/v2/search'

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      []

----

.. _post-apicontactscustomers:

POST /api/contacts/customers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         
         # Initialize the API client
         api = ABConnectAPI()
         
         # Make the API call
         response = api.raw.post(
             "/api/contacts/customers"
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

         ab api raw post /api/contacts/customers

   .. tab:: curl

      .. code-block:: bash

         curl -X POST \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           -H 'Content-Type: application/json' \
           -d '{
               "example": "data"
           }' \
           'https://api.abconnect.co/api/contacts/customers'

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

.. _get-apicontactscontactidprimarydetails:

GET /api/contacts/{contactId}/primarydetails
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Parameters:**

*Path Parameters:*

- `contactId` (integer, path) *(required)*: No description available

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         
         # Initialize the API client
         api = ABConnectAPI()
         
         # Make the API call
         response = api.raw.get(
             "/api/contacts/{contactId}/primarydetails"
         ,
             contactId=456e7890-e89b-12d3-a456-426614174001
         
         )
         
         # Process the response
         print(response)

   .. tab:: CLI

      .. code-block:: bash

         ab api raw get /api/contacts/{contactId}/primarydetails \
             contactId=456e7890-e89b-12d3-a456-426614174001

   .. tab:: curl

      .. code-block:: bash

         curl -X GET \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           'https://api.abconnect.co/api/contacts/456e7890-e89b-12d3-a456-426614174001/primarydetails'

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      []
