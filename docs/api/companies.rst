Companies
=========

Manage company records including customers, vendors, carriers, and franchisees. Companies are the core entities in the system that can place orders, provide services, or act as shipping partners.

Quick Reference
---------------

.. list-table::
   :header-rows: 1
   :widths: 10 40 50

   * - Method
     - Endpoint
     - Description
   * - GET
     - /api/companies/{id}
     - Get company by ID
   * - GET
     - /api/companies/{companyId}/details
     - Get company details
   * - GET
     - /api/companies/availableByCurrentUser
     - Get companies available to current user
   * - GET
     - /api/companies/search
     - Search companies
   * - POST
     - /api/companies/search/v2
     - Advanced company search
   * - POST
     - /api/companies/list
     - 
   * - POST
     - /api/companies/simplelist
     - 
   * - GET
     - /api/companies/{companyId}/fulldetails
     - Get complete company information
   * - PUT
     - /api/companies/{companyId}/fulldetails
     - Update complete company information
   * - POST
     - /api/companies/fulldetails
     - 
   * - GET
     - /api/companies/infoFromKey
     - 
   * - GET
     - /api/companies/{companyId}/geosettings
     - 
   * - POST
     - /api/companies/{companyId}/geosettings
     - 
   * - GET
     - /api/companies/geosettings
     - 
   * - POST
     - /api/companies/filteredCustomers
     - 
   * - GET
     - /api/companies/{companyId}/carrierAcounts
     - 
   * - POST
     - /api/companies/{companyId}/carrierAcounts
     - 
   * - GET
     - /api/companies/{companyId}/capabilities
     - 
   * - POST
     - /api/companies/{companyId}/capabilities
     - 
   * - GET
     - /api/companies/{companyId}/packagingsettings
     - 
   * - POST
     - /api/companies/{companyId}/packagingsettings
     - 
   * - GET
     - /api/companies/{companyId}/inheritedPackagingTariffs
     - 
   * - GET
     - /api/companies/{companyId}/packaginglabor
     - 
   * - POST
     - /api/companies/{companyId}/packaginglabor
     - 
   * - GET
     - /api/companies/{companyId}/inheritedpackaginglabor
     - 
   * - GET
     - /api/companies/geoAreaCompanies
     - 
   * - GET
     - /api/companies/brands
     - 
   * - GET
     - /api/companies/brandstree
     - 
   * - GET
     - /api/companies/{companyId}/franchiseeAddresses
     - 


.. _get-apicompaniesid:

GET /api/companies/{id}
~~~~~~~~~~~~~~~~~~~~~~~

**Get company by ID**

Retrieves detailed information about a specific company using its unique identifier.

**Parameters:**

*Path Parameters:*

- `id` (string, path) *(required)*: No description available

**Response Type:**

:class:`~ABConnect.api.models.companies.CompanyBasic`

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
             "/api/companies/{id}"
         ,
             id="789e0123-e89b-12d3-a456-426614174002"
         
         )
         
         # Process the response
         print(response)

   .. tab:: CLI

      .. code-block:: bash

         ab api raw get /api/companies/{id} \
             id=789e0123-e89b-12d3-a456-426614174002

   .. tab:: curl

      .. code-block:: bash

         curl -X GET \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           'https://api.abconnect.co/api/companies/789e0123-e89b-12d3-a456-426614174002'

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {
        "id": "ed282b80-54fe-4f42-bf1b-69103ce1f76c",
        "code": "TRAINING",
        "name": "Training",
        "parentCompanyId": "5e2eefc1-d616-e911-b00c-00155d426802"
      }

----

.. _get-apicompaniescompanyiddetails:

GET /api/companies/{companyId}/details
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Get company details**

Retrieves comprehensive details about a company including contacts, addresses, settings, and financial information.

**Parameters:**

*Path Parameters:*

- `companyId` (string, path) *(required)*: No description available

**Response Type:**

:class:`~ABConnect.api.models.companies.CompanyDetails`

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
             "/api/companies/{companyId}/details"
         ,
             companyId="ed282b80-54fe-4f42-bf1b-69103ce1f76c"
         
         )
         
         # Process the response
         print(response)

   .. tab:: CLI

      .. code-block:: bash

         ab api raw get /api/companies/{companyId}/details \
             companyId=ed282b80-54fe-4f42-bf1b-69103ce1f76c

   .. tab:: curl

      .. code-block:: bash

         curl -X GET \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           'https://api.abconnect.co/api/companies/ed282b80-54fe-4f42-bf1b-69103ce1f76c/details'

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {
        "companyID": "ed282b80-54fe-4f42-bf1b-69103ce1f76c",
        "companyName": "Training",
        "companyCode": "TRAINING",
        "companyEmail": "training@abconnect.co",
        "companyPhone": "8009814202",
        "mainAddress": {
          "id": 407491,
          "address1": "2534 Vista Dr",
          "city": "Castle Rock",
          "state": "CO",
          "zipCode": "80104",
          "latitude": 39.2942344,
          "longitude": -104.8221147
        },
        "companyInfo": {
          "companyId": "ed282b80-54fe-4f42-bf1b-69103ce1f76c",
          "companyName": "Training",
          "companyCode": "TRAINING",
          "isThirdParty": false,
          "isActive": true
        }
      }

----

.. _get-apicompaniesavailablebycurrentuser:

GET /api/companies/availableByCurrentUser
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Get companies available to current user**

Returns a list of companies that the currently authenticated user has permission to access.

**Response Type:**

Array of :class:`~ABConnect.api.models.companies.CompanyBasic` objects

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
             "/api/companies/availableByCurrentUser"
         
         )
         
         # Process the response
         print(response)

   .. tab:: CLI

      .. code-block:: bash

         ab api raw get /api/companies/availableByCurrentUser

   .. tab:: curl

      .. code-block:: bash

         curl -X GET \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           'https://api.abconnect.co/api/companies/availableByCurrentUser'

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      [
        {
          "id": "ed282b80-54fe-4f42-bf1b-69103ce1f76c",
          "code": "TRAINING",
          "name": "Training",
          "parentCompanyId": "5e2eefc1-d616-e911-b00c-00155d426802"
        }
      ]

----

.. _get-apicompaniessearch:

GET /api/companies/search
~~~~~~~~~~~~~~~~~~~~~~~~~

**Search companies**

Search for companies using various filters such as name, code, type, or location.

**Parameters:**

*Query Parameters:*

- `searchValue` (string, query): No description available

**Response Type:**

Array of :class:`~ABConnect.api.models.companies.CompanyBasic` objects

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
             "/api/companies/search"
         
         )
         
         # Process the response
         print(response)

   .. tab:: CLI

      .. code-block:: bash

         ab api raw get /api/companies/search

   .. tab:: curl

      .. code-block:: bash

         curl -X GET \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           'https://api.abconnect.co/api/companies/search'

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      []

----

.. _post-apicompaniessearchv2:

POST /api/companies/search/v2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Advanced company search**

Perform advanced searches on companies with complex filtering, sorting, and pagination options.

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         
         # Initialize the API client
         api = ABConnectAPI()
         
         # Make the API call
         response = api.raw.post(
             "/api/companies/search/v2"
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

         ab api raw post /api/companies/search/v2

   .. tab:: curl

      .. code-block:: bash

         curl -X POST \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           -H 'Content-Type: application/json' \
           -d '{
               "example": "data"
           }' \
           'https://api.abconnect.co/api/companies/search/v2'

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      []

----

.. _post-apicompanieslist:

POST /api/companies/list
~~~~~~~~~~~~~~~~~~~~~~~~

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         
         # Initialize the API client
         api = ABConnectAPI()
         
         # Make the API call
         response = api.raw.post(
             "/api/companies/list"
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

         ab api raw post /api/companies/list

   .. tab:: curl

      .. code-block:: bash

         curl -X POST \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           -H 'Content-Type: application/json' \
           -d '{
               "example": "data"
           }' \
           'https://api.abconnect.co/api/companies/list'

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

.. _post-apicompaniessimplelist:

POST /api/companies/simplelist
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         
         # Initialize the API client
         api = ABConnectAPI()
         
         # Make the API call
         response = api.raw.post(
             "/api/companies/simplelist"
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

         ab api raw post /api/companies/simplelist

   .. tab:: curl

      .. code-block:: bash

         curl -X POST \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           -H 'Content-Type: application/json' \
           -d '{
               "example": "data"
           }' \
           'https://api.abconnect.co/api/companies/simplelist'

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

.. _get-apicompaniescompanyidfulldetails:

GET /api/companies/{companyId}/fulldetails
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Get complete company information**

Retrieves all available information about a company including details, preferences, capabilities, pricing, and insurance settings.

**Parameters:**

*Path Parameters:*

- `companyId` (string, path) *(required)*: No description available

**Response Type:**

:class:`~ABConnect.api.models.companies.CompanyFullDetails`

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
             "/api/companies/{companyId}/fulldetails"
         ,
             companyId="ed282b80-54fe-4f42-bf1b-69103ce1f76c"
         
         )
         
         # Process the response
         print(response)

   .. tab:: CLI

      .. code-block:: bash

         ab api raw get /api/companies/{companyId}/fulldetails \
             companyId=ed282b80-54fe-4f42-bf1b-69103ce1f76c

   .. tab:: curl

      .. code-block:: bash

         curl -X GET \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           'https://api.abconnect.co/api/companies/ed282b80-54fe-4f42-bf1b-69103ce1f76c/fulldetails'

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {
        "id": "ed282b80-54fe-4f42-bf1b-69103ce1f76c",
        "details": {
          "displayId": "694618",
          "name": "Training",
          "code": "TRAINING",
          "parentId": "5e2eefc1-d616-e911-b00c-00155d426802",
          "companyTypeId": "e7f85166-34cf-429b-805d-261b44cb0c04",
          "phone": "8009814202",
          "email": "training@abconnect.co",
          "isActive": true
        },
        "preferences": {
          "isQbUser": false,
          "skipIntacct": true,
          "pzCode": "PZ100"
        },
        "capabilities": 135,
        "address": {
          "id": 407491,
          "address1": "2534 Vista Dr",
          "city": "Castle Rock",
          "state": "CO",
          "zipCode": "80104"
        },
        "pricing": {
          "transportationCharge": {
            "baseTripFee": 100.0,
            "baseTripMile": 3000.0
          },
          "transportationMarkups": {
            "wholeSale": 1.0,
            "base": 1.25,
            "medium": 2.3,
            "high": 2.5
          }
        }
      }

----

.. _put-apicompaniescompanyidfulldetails:

PUT /api/companies/{companyId}/fulldetails
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Update complete company information**

Updates all company information including details, preferences, capabilities, pricing, and insurance settings.

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
         response = api.raw.put(
             "/api/companies/{companyId}/fulldetails"
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

         ab api raw put /api/companies/{companyId}/fulldetails \
             companyId=ed282b80-54fe-4f42-bf1b-69103ce1f76c

   .. tab:: curl

      .. code-block:: bash

         curl -X PUT \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           -H 'Content-Type: application/json' \
           -d '{
               "example": "data"
           }' \
           'https://api.abconnect.co/api/companies/ed282b80-54fe-4f42-bf1b-69103ce1f76c/fulldetails'

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {}

----

.. _post-apicompaniesfulldetails:

POST /api/companies/fulldetails
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         
         # Initialize the API client
         api = ABConnectAPI()
         
         # Make the API call
         response = api.raw.post(
             "/api/companies/fulldetails"
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

         ab api raw post /api/companies/fulldetails

   .. tab:: curl

      .. code-block:: bash

         curl -X POST \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           -H 'Content-Type: application/json' \
           -d '{
               "example": "data"
           }' \
           'https://api.abconnect.co/api/companies/fulldetails'

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {}

----

.. _get-apicompaniesinfofromkey:

GET /api/companies/infoFromKey
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Parameters:**

*Query Parameters:*

- `key` (string, query): No description available

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         
         # Initialize the API client
         api = ABConnectAPI()
         
         # Make the API call
         response = api.raw.get(
             "/api/companies/infoFromKey"
         
         )
         
         # Process the response
         print(response)

   .. tab:: CLI

      .. code-block:: bash

         ab api raw get /api/companies/infoFromKey

   .. tab:: curl

      .. code-block:: bash

         curl -X GET \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           'https://api.abconnect.co/api/companies/infoFromKey'

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {
        "status": "success",
        "data": {}
      }

----

.. _get-apicompaniescompanyidgeosettings:

GET /api/companies/{companyId}/geosettings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
         response = api.raw.get(
             "/api/companies/{companyId}/geosettings"
         ,
             companyId="ed282b80-54fe-4f42-bf1b-69103ce1f76c"
         
         )
         
         # Process the response
         print(response)

   .. tab:: CLI

      .. code-block:: bash

         ab api raw get /api/companies/{companyId}/geosettings \
             companyId=ed282b80-54fe-4f42-bf1b-69103ce1f76c

   .. tab:: curl

      .. code-block:: bash

         curl -X GET \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           'https://api.abconnect.co/api/companies/ed282b80-54fe-4f42-bf1b-69103ce1f76c/geosettings'

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {
        "id": "ed282b80-54fe-4f42-bf1b-69103ce1f76c",
        "code": "TRAINING",
        "name": "Training",
        "parentCompanyId": "5e2eefc1-d616-e911-b00c-00155d426802"
      }

----

.. _post-apicompaniescompanyidgeosettings:

POST /api/companies/{companyId}/geosettings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
             "/api/companies/{companyId}/geosettings"
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

         ab api raw post /api/companies/{companyId}/geosettings \
             companyId=ed282b80-54fe-4f42-bf1b-69103ce1f76c

   .. tab:: curl

      .. code-block:: bash

         curl -X POST \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           -H 'Content-Type: application/json' \
           -d '{
               "example": "data"
           }' \
           'https://api.abconnect.co/api/companies/ed282b80-54fe-4f42-bf1b-69103ce1f76c/geosettings'

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

.. _get-apicompaniesgeosettings:

GET /api/companies/geosettings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Parameters:**

*Query Parameters:*

- `Latitude` (number, query): No description available
- `Longitude` (number, query): No description available
- `milesRadius` (integer, query): No description available

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         
         # Initialize the API client
         api = ABConnectAPI()
         
         # Make the API call
         response = api.raw.get(
             "/api/companies/geosettings"
         
         )
         
         # Process the response
         print(response)

   .. tab:: CLI

      .. code-block:: bash

         ab api raw get /api/companies/geosettings

   .. tab:: curl

      .. code-block:: bash

         curl -X GET \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           'https://api.abconnect.co/api/companies/geosettings'

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      []

----

.. _post-apicompaniesfilteredcustomers:

POST /api/companies/filteredCustomers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         
         # Initialize the API client
         api = ABConnectAPI()
         
         # Make the API call
         response = api.raw.post(
             "/api/companies/filteredCustomers"
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

         ab api raw post /api/companies/filteredCustomers

   .. tab:: curl

      .. code-block:: bash

         curl -X POST \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           -H 'Content-Type: application/json' \
           -d '{
               "example": "data"
           }' \
           'https://api.abconnect.co/api/companies/filteredCustomers'

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

.. _get-apicompaniescompanyidcarrieracounts:

GET /api/companies/{companyId}/carrierAcounts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
         response = api.raw.get(
             "/api/companies/{companyId}/carrierAcounts"
         ,
             companyId="ed282b80-54fe-4f42-bf1b-69103ce1f76c"
         
         )
         
         # Process the response
         print(response)

   .. tab:: CLI

      .. code-block:: bash

         ab api raw get /api/companies/{companyId}/carrierAcounts \
             companyId=ed282b80-54fe-4f42-bf1b-69103ce1f76c

   .. tab:: curl

      .. code-block:: bash

         curl -X GET \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           'https://api.abconnect.co/api/companies/ed282b80-54fe-4f42-bf1b-69103ce1f76c/carrierAcounts'

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {
        "id": "ed282b80-54fe-4f42-bf1b-69103ce1f76c",
        "code": "TRAINING",
        "name": "Training",
        "parentCompanyId": "5e2eefc1-d616-e911-b00c-00155d426802"
      }

----

.. _post-apicompaniescompanyidcarrieracounts:

POST /api/companies/{companyId}/carrierAcounts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
             "/api/companies/{companyId}/carrierAcounts"
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

         ab api raw post /api/companies/{companyId}/carrierAcounts \
             companyId=ed282b80-54fe-4f42-bf1b-69103ce1f76c

   .. tab:: curl

      .. code-block:: bash

         curl -X POST \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           -H 'Content-Type: application/json' \
           -d '{
               "example": "data"
           }' \
           'https://api.abconnect.co/api/companies/ed282b80-54fe-4f42-bf1b-69103ce1f76c/carrierAcounts'

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

.. _get-apicompaniescompanyidcapabilities:

GET /api/companies/{companyId}/capabilities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
         response = api.raw.get(
             "/api/companies/{companyId}/capabilities"
         ,
             companyId="ed282b80-54fe-4f42-bf1b-69103ce1f76c"
         
         )
         
         # Process the response
         print(response)

   .. tab:: CLI

      .. code-block:: bash

         ab api raw get /api/companies/{companyId}/capabilities \
             companyId=ed282b80-54fe-4f42-bf1b-69103ce1f76c

   .. tab:: curl

      .. code-block:: bash

         curl -X GET \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           'https://api.abconnect.co/api/companies/ed282b80-54fe-4f42-bf1b-69103ce1f76c/capabilities'

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {
        "id": "ed282b80-54fe-4f42-bf1b-69103ce1f76c",
        "code": "TRAINING",
        "name": "Training",
        "parentCompanyId": "5e2eefc1-d616-e911-b00c-00155d426802"
      }

----

.. _post-apicompaniescompanyidcapabilities:

POST /api/companies/{companyId}/capabilities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
             "/api/companies/{companyId}/capabilities"
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

         ab api raw post /api/companies/{companyId}/capabilities \
             companyId=ed282b80-54fe-4f42-bf1b-69103ce1f76c

   .. tab:: curl

      .. code-block:: bash

         curl -X POST \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           -H 'Content-Type: application/json' \
           -d '{
               "example": "data"
           }' \
           'https://api.abconnect.co/api/companies/ed282b80-54fe-4f42-bf1b-69103ce1f76c/capabilities'

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

.. _get-apicompaniescompanyidpackagingsettings:

GET /api/companies/{companyId}/packagingsettings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
         response = api.raw.get(
             "/api/companies/{companyId}/packagingsettings"
         ,
             companyId="ed282b80-54fe-4f42-bf1b-69103ce1f76c"
         
         )
         
         # Process the response
         print(response)

   .. tab:: CLI

      .. code-block:: bash

         ab api raw get /api/companies/{companyId}/packagingsettings \
             companyId=ed282b80-54fe-4f42-bf1b-69103ce1f76c

   .. tab:: curl

      .. code-block:: bash

         curl -X GET \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           'https://api.abconnect.co/api/companies/ed282b80-54fe-4f42-bf1b-69103ce1f76c/packagingsettings'

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {
        "id": "ed282b80-54fe-4f42-bf1b-69103ce1f76c",
        "code": "TRAINING",
        "name": "Training",
        "parentCompanyId": "5e2eefc1-d616-e911-b00c-00155d426802"
      }

----

.. _post-apicompaniescompanyidpackagingsettings:

POST /api/companies/{companyId}/packagingsettings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
             "/api/companies/{companyId}/packagingsettings"
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

         ab api raw post /api/companies/{companyId}/packagingsettings \
             companyId=ed282b80-54fe-4f42-bf1b-69103ce1f76c

   .. tab:: curl

      .. code-block:: bash

         curl -X POST \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           -H 'Content-Type: application/json' \
           -d '{
               "example": "data"
           }' \
           'https://api.abconnect.co/api/companies/ed282b80-54fe-4f42-bf1b-69103ce1f76c/packagingsettings'

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

.. _get-apicompaniescompanyidinheritedpackagingtariffs:

GET /api/companies/{companyId}/inheritedPackagingTariffs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Parameters:**

*Path Parameters:*

- `companyId` (string, path) *(required)*: No description available

*Query Parameters:*

- `inheritFrom` (string, query): No description available

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         
         # Initialize the API client
         api = ABConnectAPI()
         
         # Make the API call
         response = api.raw.get(
             "/api/companies/{companyId}/inheritedPackagingTariffs"
         ,
             companyId="ed282b80-54fe-4f42-bf1b-69103ce1f76c"
         
         )
         
         # Process the response
         print(response)

   .. tab:: CLI

      .. code-block:: bash

         ab api raw get /api/companies/{companyId}/inheritedPackagingTariffs \
             companyId=ed282b80-54fe-4f42-bf1b-69103ce1f76c

   .. tab:: curl

      .. code-block:: bash

         curl -X GET \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           'https://api.abconnect.co/api/companies/ed282b80-54fe-4f42-bf1b-69103ce1f76c/inheritedPackagingTariffs'

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {
        "id": "ed282b80-54fe-4f42-bf1b-69103ce1f76c",
        "code": "TRAINING",
        "name": "Training",
        "parentCompanyId": "5e2eefc1-d616-e911-b00c-00155d426802"
      }

----

.. _get-apicompaniescompanyidpackaginglabor:

GET /api/companies/{companyId}/packaginglabor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
         response = api.raw.get(
             "/api/companies/{companyId}/packaginglabor"
         ,
             companyId="ed282b80-54fe-4f42-bf1b-69103ce1f76c"
         
         )
         
         # Process the response
         print(response)

   .. tab:: CLI

      .. code-block:: bash

         ab api raw get /api/companies/{companyId}/packaginglabor \
             companyId=ed282b80-54fe-4f42-bf1b-69103ce1f76c

   .. tab:: curl

      .. code-block:: bash

         curl -X GET \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           'https://api.abconnect.co/api/companies/ed282b80-54fe-4f42-bf1b-69103ce1f76c/packaginglabor'

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {
        "id": "ed282b80-54fe-4f42-bf1b-69103ce1f76c",
        "code": "TRAINING",
        "name": "Training",
        "parentCompanyId": "5e2eefc1-d616-e911-b00c-00155d426802"
      }

----

.. _post-apicompaniescompanyidpackaginglabor:

POST /api/companies/{companyId}/packaginglabor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
             "/api/companies/{companyId}/packaginglabor"
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

         ab api raw post /api/companies/{companyId}/packaginglabor \
             companyId=ed282b80-54fe-4f42-bf1b-69103ce1f76c

   .. tab:: curl

      .. code-block:: bash

         curl -X POST \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           -H 'Content-Type: application/json' \
           -d '{
               "example": "data"
           }' \
           'https://api.abconnect.co/api/companies/ed282b80-54fe-4f42-bf1b-69103ce1f76c/packaginglabor'

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

.. _get-apicompaniescompanyidinheritedpackaginglabor:

GET /api/companies/{companyId}/inheritedpackaginglabor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Parameters:**

*Path Parameters:*

- `companyId` (string, path) *(required)*: No description available

*Query Parameters:*

- `inheritFrom` (string, query): No description available

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         
         # Initialize the API client
         api = ABConnectAPI()
         
         # Make the API call
         response = api.raw.get(
             "/api/companies/{companyId}/inheritedpackaginglabor"
         ,
             companyId="ed282b80-54fe-4f42-bf1b-69103ce1f76c"
         
         )
         
         # Process the response
         print(response)

   .. tab:: CLI

      .. code-block:: bash

         ab api raw get /api/companies/{companyId}/inheritedpackaginglabor \
             companyId=ed282b80-54fe-4f42-bf1b-69103ce1f76c

   .. tab:: curl

      .. code-block:: bash

         curl -X GET \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           'https://api.abconnect.co/api/companies/ed282b80-54fe-4f42-bf1b-69103ce1f76c/inheritedpackaginglabor'

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {
        "id": "ed282b80-54fe-4f42-bf1b-69103ce1f76c",
        "code": "TRAINING",
        "name": "Training",
        "parentCompanyId": "5e2eefc1-d616-e911-b00c-00155d426802"
      }

----

.. _get-apicompaniesgeoareacompanies:

GET /api/companies/geoAreaCompanies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         
         # Initialize the API client
         api = ABConnectAPI()
         
         # Make the API call
         response = api.raw.get(
             "/api/companies/geoAreaCompanies"
         
         )
         
         # Process the response
         print(response)

   .. tab:: CLI

      .. code-block:: bash

         ab api raw get /api/companies/geoAreaCompanies

   .. tab:: curl

      .. code-block:: bash

         curl -X GET \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           'https://api.abconnect.co/api/companies/geoAreaCompanies'

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      []

----

.. _get-apicompaniesbrands:

GET /api/companies/brands
~~~~~~~~~~~~~~~~~~~~~~~~~

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         
         # Initialize the API client
         api = ABConnectAPI()
         
         # Make the API call
         response = api.raw.get(
             "/api/companies/brands"
         
         )
         
         # Process the response
         print(response)

   .. tab:: CLI

      .. code-block:: bash

         ab api raw get /api/companies/brands

   .. tab:: curl

      .. code-block:: bash

         curl -X GET \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           'https://api.abconnect.co/api/companies/brands'

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      []

----

.. _get-apicompaniesbrandstree:

GET /api/companies/brandstree
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         
         # Initialize the API client
         api = ABConnectAPI()
         
         # Make the API call
         response = api.raw.get(
             "/api/companies/brandstree"
         
         )
         
         # Process the response
         print(response)

   .. tab:: CLI

      .. code-block:: bash

         ab api raw get /api/companies/brandstree

   .. tab:: curl

      .. code-block:: bash

         curl -X GET \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           'https://api.abconnect.co/api/companies/brandstree'

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {
        "status": "success",
        "data": {}
      }

----

.. _get-apicompaniescompanyidfranchiseeaddresses:

GET /api/companies/{companyId}/franchiseeAddresses
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
         response = api.raw.get(
             "/api/companies/{companyId}/franchiseeAddresses"
         ,
             companyId="ed282b80-54fe-4f42-bf1b-69103ce1f76c"
         
         )
         
         # Process the response
         print(response)

   .. tab:: CLI

      .. code-block:: bash

         ab api raw get /api/companies/{companyId}/franchiseeAddresses \
             companyId=ed282b80-54fe-4f42-bf1b-69103ce1f76c

   .. tab:: curl

      .. code-block:: bash

         curl -X GET \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           'https://api.abconnect.co/api/companies/ed282b80-54fe-4f42-bf1b-69103ce1f76c/franchiseeAddresses'

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {
        "id": "ed282b80-54fe-4f42-bf1b-69103ce1f76c",
        "code": "TRAINING",
        "name": "Training",
        "parentCompanyId": "5e2eefc1-d616-e911-b00c-00155d426802"
      }
