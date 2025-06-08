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
        "userId": "00000000-0000-0000-0000-000000000000",
        "companyName": "Training",
        "contactName": null,
        "contactPhone": null,
        "companyType": null,
        "parcelOnly": null,
        "isThirdParty": false,
        "companyCode": "TRAINING",
        "parentCompanyName": "National Logistics Services",
        "companyTypeID": "e7f85166-34cf-429b-805d-261b44cb0c04",
        "parentCompanyID": "5e2eefc1-d616-e911-b00c-00155d426802",
        "companyPhone": "8009814202",
        "companyEmail": "training@abconnect.co",
        "companyFax": "",
        "companyWebSite": "http://abconnect.co/",
        "industryType": "6664ddb1-b7f1-e311-b7f5-000c298b59ee",
        "industryTypeName": null,
        "taxId": null,
        "customerCell": null,
        "companyCell": "6195087798",
        "pzCode": "PZ100",
        "referralCode": null,
        "companyLogo": "25d69a87-2146-4d67-8c92-843c2df302dd#NPS_230.gif",
        "letterHeadLogo": null,
        "thumbnailLogo": "7fc55a48-dc77-ee11-8393-16d570081145#NavisLogo.gif",
        "mapsMarkerImage": "7fc55a48-dc77-ee11-8393-16d570081145#NavisLogo.gif",
        "colorTheme": null,
        "franchiseeMaturityType": "50f7d54f-7023-4697-a187-8bcda433bad2",
        "pricingToUse": "4e8e4f3b-65f9-4625-bba0-fad6fa5e7d6e",
        "totalRows": null,
        "address": null,
        "companyInsurancePricing": null,
        "companyServicePricing": null,
        "companyTaxPricing": null,
        "wholeSaleMarkup": null,
        "baseMarkup": null,
        "mediumMarkup": null,
        "highMarkup": null,
        "miles": null,
        "insuranceType": "1e18bb08-25b2-e111-b36c-00155d6b2c30",
        "isGlobal": true,
        "isQbUser": false,
        "skipIntacct": true,
        "isAccess": null,
        "companyDisplayID": "694618",
        "depth": null,
        "franchiseeName": null,
        "isPrefered": true,
        "createdUser": null,
        "mappingLocations": null,
        "locationCount": null,
        "baseParent": null,
        "copyMaterialFrom": null,
        "isHide": true,
        "isDontUse": false,
        "mainAddress": {
          "id": 407491,
          "isValid": false,
          "dontValidate": false,
          "propertyType": null,
          "address1Value": "2534 Vista Dr",
          "address2Value": "",
          "countryName": null,
          "countryCode": null,
          "countryId": "daf9b34b-ce6a-4f2f-9207-15278c06b7d2",
          "latitude": 39.2942344,
          "longitude": -104.8221147,
          "fullCityLine": "Castle Rock, CO, 80104",
          "coordinates": {
            "latitude": 39.2942344,
            "longitude": -104.8221147
          },
          "address1": "2534 Vista Dr",
          "address2": null,
          "city": "Castle Rock",
          "state": "CO",
          "zipCode": "80104"
        },
        "accountManagerFranchiseeId": null,
        "accountManagerFranchiseeName": null,
        "carrierAccountsSourceCompanyId": null,
        "carrierAccountsSourceCompanyName": null,
        "autoPriceAPIEnableEmails": false,
        "autoPriceAPIEnableSMSs": false,
        "commercialCapabilities": 135,
        "primaryContactId": 338253,
        "payerContactId": 765896,
        "payerContactName": "Test Trainee",
        "totalJobs": 16,
        "totalJobsRevenue": 43225.58,
        "totalSales": 130,
        "totalSalesRevenue": 164486.74,
        "addressData": {
          "company": "Training",
          "firstLastName": "Training User",
          "addressLine1": "2534 Vista Dr",
          "addressLine2": null,
          "contactBOLNote": null,
          "city": "Castle Rock",
          "state": "CO",
          "stateCode": null,
          "zipCode": "80104",
          "countryName": null,
          "propertyType": null,
          "fullCityLine": "Castle Rock, CO, 80104",
          "phone": "(800) 981-4202",
          "cellPhone": null,
          "fax": "",
          "email": "training@abconnect.co",
          "addressLine2Visible": false,
          "companyVisible": true,
          "countryNameVisible": false,
          "phoneVisible": true,
          "emailVisible": true,
          "fullAddressLine": "2534 Vista Dr",
          "fullAddress": "2534 Vista Dr, Castle Rock CO 80104",
          "countryId": null
        },
        "overridableAddressData": {
          "company": {
            "defaultValue": "Training",
            "overrideValue": null,
            "forceEmpty": false,
            "value": "Training"
          },
          "firstLastName": {
            "defaultValue": "Training User",
            "overrideValue": null,
            "forceEmpty": false,
            "value": "Training User"
          },
          "addressLine1": {
            "defaultValue": "2534 Vista Dr",
            "overrideValue": null,
            "forceEmpty": false,
            "value": "2534 Vista Dr"
          },
          "addressLine2": {
            "defaultValue": null,
            "overrideValue": null,
            "forceEmpty": false,
            "value": null
          },
          "city": {
            "defaultValue": "Castle Rock",
            "overrideValue": null,
            "forceEmpty": false,
            "value": "Castle Rock"
          },
          "state": {
            "defaultValue": "CO",
            "overrideValue": null,
            "forceEmpty": false,
            "value": "CO"
          },
          "zipCode": {
            "defaultValue": "80104",
            "overrideValue": null,
            "forceEmpty": false,
            "value": "80104"
          },
          "phone": {
            "defaultValue": "(800) 981-4202",
            "overrideValue": null,
            "forceEmpty": false,
            "value": "(800) 981-4202"
          },
          "email": {
            "defaultValue": "training@abconnect.co",
            "overrideValue": null,
            "forceEmpty": false,
            "value": "training@abconnect.co"
          },
          "fullAddressLine": "2534 Vista Dr",
          "fullAddress": {
            "defaultValue": "2534 Vista Dr, Castle Rock CO 80104",
            "overrideValue": null,
            "forceEmpty": false,
            "value": "2534 Vista Dr, Castle Rock CO 80104"
          },
          "fullCityLine": {
            "defaultValue": "Castle Rock, CO, 80104",
            "overrideValue": null,
            "forceEmpty": false,
            "value": "Castle Rock, CO, 80104"
          }
        },
        "companyInfo": {
          "companyId": "ed282b80-54fe-4f42-bf1b-69103ce1f76c",
          "companyTypeId": "e7f85166-34cf-429b-805d-261b44cb0c04",
          "companyDisplayId": null,
          "companyName": "Training",
          "companyCode": "TRAINING",
          "companyEmail": "training@abconnect.co",
          "companyPhone": "8009814202",
          "thumbnailLogo": "7fc55a48-dc77-ee11-8393-16d570081145#NavisLogo.gif",
          "companyLogo": "25d69a87-2146-4d67-8c92-843c2df302dd#NPS_230.gif",
          "mapsMarkerImage": "7fc55a48-dc77-ee11-8393-16d570081145#NavisLogo.gif",
          "mainAddress": {
            "id": 407491,
            "isValid": false,
            "dontValidate": false,
            "propertyType": null,
            "address1Value": "2534 Vista Dr",
            "address2Value": "",
            "countryName": null,
            "countryCode": null,
            "countryId": "daf9b34b-ce6a-4f2f-9207-15278c06b7d2",
            "latitude": 39.2942344,
            "longitude": -104.8221147,
            "fullCityLine": "Castle Rock, CO, 80104",
            "coordinates": {
              "latitude": 39.2942344,
              "longitude": -104.8221147
            },
            "address1": "2534 Vista Dr",
            "address2": null,
            "city": "Castle Rock",
            "state": "CO",
            "zipCode": "80104"
          },
          "isThirdParty": false,
          "isActive": false,
          "isHidden": false
        },
        "companyID": "ed282b80-54fe-4f42-bf1b-69103ce1f76c",
        "addressID": null,
        "address1": null,
        "address2": null,
        "city": null,
        "state": null,
        "stateCode": null,
        "countryName": null,
        "countryCode": null,
        "countryID": null,
        "zipCode": null,
        "isActive": true,
        "createdDate": null,
        "createdBy": null,
        "modifiedDate": null,
        "modifiedBy": null,
        "latitude": null,
        "longitude": null,
        "result": null,
        "addressMappingID": null,
        "contactID": null,
        "userID": "00000000-0000-0000-0000-000000000000",
        "primaryCustomerName": "Training User",
        "contactInfo": null
      }

----

.. _get-apicompaniesavailablebycurrentuser:

GET /api/companies/availableByCurrentUser
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Get companies available to current user**

Returns a list of companies that the currently authenticated user has permission to access.

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

      [
        {
          "id": "ed282b80-54fe-4f42-bf1b-69103ce1f76c",
          "code": "TRAINING",
          "name": "Training",
          "parentCompanyId": "5e2eefc1-d616-e911-b00c-00155d426802"
        }
      ]

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

      [
        {
          "id": "ed282b80-54fe-4f42-bf1b-69103ce1f76c",
          "code": "TRAINING",
          "name": "Training",
          "parentCompanyId": "5e2eefc1-d616-e911-b00c-00155d426802"
        }
      ]

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
          "taxId": null,
          "code": "TRAINING",
          "parentId": "5e2eefc1-d616-e911-b00c-00155d426802",
          "franchiseeId": null,
          "companyTypeId": "e7f85166-34cf-429b-805d-261b44cb0c04",
          "industryTypeId": "6664ddb1-b7f1-e311-b7f5-000c298b59ee",
          "cellPhone": "6195087798",
          "phone": "8009814202",
          "fax": "",
          "email": "training@abconnect.co",
          "website": "http://abconnect.co/",
          "isActive": true,
          "isHidden": true,
          "isGlobal": true,
          "isNotUsed": false,
          "isPreferred": true,
          "payerContactId": 765896,
          "payerContactName": "Test Trainee"
        },
        "preferences": {
          "companyHeaderLogo": {
            "filePath": "\\Uploads\\CompanyHeaderLogo\\25d69a87-2146-4d67-8c92-843c2df302dd#NPS_230.gif",
            "newFile": null
          },
          "thumbnailLogo": {
            "filePath": "\\Uploads\\ThumbnailLogo\\7fc55a48-dc77-ee11-8393-16d570081145#NavisLogo.gif",
            "newFile": null
          },
          "letterHeadLogo": {
            "filePath": null,
            "newFile": null
          },
          "mapsMarker": {
            "filePath": "\\Uploads\\MapsMarkerImage\\7fc55a48-dc77-ee11-8393-16d570081145#NavisLogo.gif",
            "newFile": null
          },
          "isQbUser": false,
          "skipIntacct": true,
          "pricingToUse": "4e8e4f3b-65f9-4625-bba0-fad6fa5e7d6e",
          "pzCode": "PZ100",
          "insuranceTypeId": "1e18bb08-25b2-e111-b36c-00155d6b2c30",
          "franchiseeMaturityTypeId": "50f7d54f-7023-4697-a187-8bcda433bad2",
          "isCompanyUsedAsCarrierSource": false,
          "carrierAccountsSourceCompanyId": null,
          "carrierAccountsSourceCompanyName": null,
          "accountManagerFranchiseeId": null,
          "accountManagerFranchiseeName": null,
          "autoPriceAPIEnableEmails": false,
          "autoPriceAPIEnableSMSs": false,
          "copyMaterials": 0
        },
        "capabilities": 135,
        "address": {
          "id": 407491,
          "isValid": false,
          "dontValidate": false,
          "propertyType": null,
          "address1Value": "2534 Vista Dr",
          "address2Value": "",
          "countryName": "United States",
          "countryCode": "US",
          "countryId": "daf9b34b-ce6a-4f2f-9207-15278c06b7d2",
          "latitude": 39.2942344,
          "longitude": -104.8221147,
          "fullCityLine": "Castle Rock, CO, 80104",
          "coordinates": {
            "latitude": 39.2942344,
            "longitude": -104.8221147
          },
          "address1": "2534 Vista Dr",
          "address2": null,
          "city": "Castle Rock",
          "state": "CO",
          "zipCode": "80104"
        },
        "pricing": {
          "transportationCharge": {
            "baseTripFee": 100.0,
            "baseTripMile": 3000.0,
            "extraFee": 0.0,
            "fuelSurcharge": 0.0
          },
          "transportationMarkups": {
            "wholeSale": 1.0,
            "base": 1.25,
            "medium": 2.3,
            "high": 2.5
          },
          "carrierFreightMarkups": {
            "wholeSale": 1.98,
            "base": 2.36,
            "medium": 2.7,
            "high": 2.9
          }
        },
        "insurance": {
          "isp": {
            "insuranceSlabId": "88424802-9559-489c-a69a-3e8958cafc65",
            "option": 1,
            "sellPrice": 2.0
          },
          "nsp": {
            "insuranceSlabId": "88424802-9559-489c-a69a-3e8958cafc69",
            "option": 2,
            "sellPrice": 2.0
          },
          "ltl": {
            "insuranceSlabId": "88424802-9559-489c-a69a-3e8958cafc67",
            "option": 2,
            "sellPrice": 2.0
          }
        },
        "readOnlyAccess": false
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

----
