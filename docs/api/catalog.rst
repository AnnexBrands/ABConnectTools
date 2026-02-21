Catalog
=======

The Catalog API manages auction catalogs, lots, and sellers via the
``catalog-api.abconnect.co`` service. It shares authentication with the
main ACPortal API.

Quick Reference
---------------

.. list-table::
   :header-rows: 1
   :widths: 10 40 50

   * - Method
     - Endpoint
     - Description
   * - GET
     - /api/Catalog
     - List catalogs (paginated)
   * - POST
     - /api/Catalog
     - Create a new catalog
   * - GET
     - /api/Catalog/{id}
     - Get catalog by ID
   * - PUT
     - /api/Catalog/{id}
     - Update a catalog
   * - DELETE
     - /api/Catalog/{id}
     - Delete a catalog
   * - GET
     - /api/Seller
     - List sellers (paginated)
   * - POST
     - /api/Seller
     - Create a new seller
   * - GET
     - /api/Seller/{id}
     - Get seller by ID
   * - PUT
     - /api/Seller/{id}
     - Update a seller
   * - DELETE
     - /api/Seller/{id}
     - Delete a seller
   * - GET
     - /api/Lot
     - List lots (paginated)
   * - POST
     - /api/Lot
     - Create a new lot
   * - GET
     - /api/Lot/{id}
     - Get lot by ID
   * - PUT
     - /api/Lot/{id}
     - Update a lot
   * - DELETE
     - /api/Lot/{id}
     - Delete a lot
   * - POST
     - /api/Lot/get-overrides
     - Get lot overrides
   * - POST
     - /api/Bulk/insert
     - Bulk insert catalogs, lots, and sellers

Catalogs
--------

.. _get-apicatalog:

GET /api/Catalog
~~~~~~~~~~~~~~~~

List catalogs with pagination. Start date and end date are range filters.

**Parameters:**

- ``page_number`` (int): Page number, default 1
- ``page_size`` (int): Items per page, default 10
- ``id`` (int, optional): Filter by catalog ID
- ``customer_catalog_id`` (str, optional): Filter by customer catalog ID
- ``agent`` (str, optional): Filter by agent name
- ``title`` (str, optional): Filter by catalog title
- ``start_date`` (datetime, optional): Filter by start date (range filter)
- ``end_date`` (datetime, optional): Filter by end date (range filter)
- ``is_completed`` (bool, optional): Filter by completion status
- ``seller_ids`` (list[int], optional): Filter by seller IDs

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI

         api = ABConnectAPI()

         # Basic listing
         result = api.catalog.catalogs.list(page_number=1, page_size=10)
         for catalog in result.items:
             print(f"{catalog.id}: {catalog.title}")

         # Filter by customer catalog ID
         result = api.catalog.catalogs.list(customer_catalog_id="CAT-001")

         # Filter by completion status and agent
         result = api.catalog.catalogs.list(is_completed=False, agent="MyAgent")

         # Filter by date range
         from datetime import datetime
         result = api.catalog.catalogs.list(
             start_date=datetime(2025, 1, 1),
             end_date=datetime(2025, 12, 31),
         )

   .. tab:: CLI

      .. code-block:: bash

         ab catalog catalogs list

   .. tab:: curl

      .. code-block:: bash

         curl -X GET \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           'https://catalog-api.abconnect.co/api/Catalog?PageNumber=1&PageSize=10'

         # With filters
         curl -X GET \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           'https://catalog-api.abconnect.co/api/Catalog?CustomerCatalogId=CAT-001&IsCompleted=false'

----

.. _post-apicatalog:

POST /api/Catalog
~~~~~~~~~~~~~~~~~

Create a new catalog.

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         from ABConnect.api.models.catalog import AddCatalogRequest
         from datetime import datetime

         api = ABConnectAPI()
         request = AddCatalogRequest(
             customer_catalog_id="CAT-001",
             title="My Catalog",
             start_date=datetime(2025, 1, 1),
             end_date=datetime(2025, 12, 31),
             seller_ids=[1, 2],
         )
         catalog = api.catalog.catalogs.create(request)
         print(catalog.id)

   .. tab:: curl

      .. code-block:: bash

         curl -X POST \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           -H 'Content-Type: application/json' \
           -d '{"customerCatalogId":"CAT-001","title":"My Catalog","startDate":"2025-01-01","endDate":"2025-12-31","sellerIds":[1,2]}' \
           'https://catalog-api.abconnect.co/api/Catalog'

----

.. _get-apicatalogid:

GET /api/Catalog/{id}
~~~~~~~~~~~~~~~~~~~~~

Get a catalog by ID, including its sellers and lots.

**Parameters:**

- ``catalog_id`` (int) *(required)*: Catalog ID

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI

         api = ABConnectAPI()
         catalog = api.catalog.catalogs.get(catalog_id=123)
         print(f"Title: {catalog.title}")
         print(f"Sellers: {len(catalog.sellers)}")
         print(f"Lots: {len(catalog.lots)}")

   .. tab:: curl

      .. code-block:: bash

         curl -X GET \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           'https://catalog-api.abconnect.co/api/Catalog/123'

----

.. _put-apicatalogid:

PUT /api/Catalog/{id}
~~~~~~~~~~~~~~~~~~~~~

Update an existing catalog.

**Parameters:**

- ``catalog_id`` (int) *(required)*: Catalog ID
- ``data`` (UpdateCatalogRequest) *(required)*: Updated catalog data

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         from ABConnect.api.models.catalog import UpdateCatalogRequest
         from datetime import datetime

         api = ABConnectAPI()
         request = UpdateCatalogRequest(
             customer_catalog_id="CAT-001",
             title="Updated Title",
             start_date=datetime(2025, 1, 1),
             end_date=datetime(2025, 12, 31),
         )
         catalog = api.catalog.catalogs.update(catalog_id=123, data=request)

   .. tab:: curl

      .. code-block:: bash

         curl -X PUT \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           -H 'Content-Type: application/json' \
           -d '{"customerCatalogId":"CAT-001","title":"Updated Title","startDate":"2025-01-01","endDate":"2025-12-31"}' \
           'https://catalog-api.abconnect.co/api/Catalog/123'

----

.. _delete-apicatalogid:

DELETE /api/Catalog/{id}
~~~~~~~~~~~~~~~~~~~~~~~~

Delete a catalog.

**Parameters:**

- ``catalog_id`` (int) *(required)*: Catalog ID

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI

         api = ABConnectAPI()
         api.catalog.catalogs.delete(catalog_id=123)

   .. tab:: curl

      .. code-block:: bash

         curl -X DELETE \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           'https://catalog-api.abconnect.co/api/Catalog/123'

----

Sellers
-------

.. _get-apiseller:

GET /api/Seller
~~~~~~~~~~~~~~~

List sellers with pagination.

**Parameters:**

- ``page_number`` (int): Page number, default 1
- ``page_size`` (int): Items per page, default 10
- ``id`` (int, optional): Filter by seller ID
- ``name`` (str, optional): Filter by seller name
- ``customer_display_id`` (int, optional): Filter by customer display ID
- ``is_active`` (bool, optional): Filter by active status

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI

         api = ABConnectAPI()

         # Basic listing
         result = api.catalog.sellers.list(page_number=1, page_size=10)
         for seller in result.items:
             print(f"{seller.id}: {seller.name} (active={seller.is_active})")

         # Filter by active status
         result = api.catalog.sellers.list(is_active=True)

         # Filter by name
         result = api.catalog.sellers.list(name="Smith")

   .. tab:: CLI

      .. code-block:: bash

         ab catalog sellers list

   .. tab:: curl

      .. code-block:: bash

         curl -X GET \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           'https://catalog-api.abconnect.co/api/Seller?PageNumber=1&PageSize=10'

         # With filters
         curl -X GET \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           'https://catalog-api.abconnect.co/api/Seller?IsActive=true&Name=Smith'

----

.. _post-apiseller:

POST /api/Seller
~~~~~~~~~~~~~~~~

Create a new seller.

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         from ABConnect.api.models.catalog import AddSellerRequest

         api = ABConnectAPI()
         request = AddSellerRequest(
             name="New Seller",
             customer_display_id=12345,
             is_active=True,
         )
         seller = api.catalog.sellers.create(request)
         print(seller.id)

   .. tab:: curl

      .. code-block:: bash

         curl -X POST \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           -H 'Content-Type: application/json' \
           -d '{"name":"New Seller","customerDisplayId":12345,"isActive":true}' \
           'https://catalog-api.abconnect.co/api/Seller'

----

.. _get-apisellerid:

GET /api/Seller/{id}
~~~~~~~~~~~~~~~~~~~~

Get a seller by ID, including associated catalogs.

**Parameters:**

- ``seller_id`` (int) *(required)*: Seller ID

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI

         api = ABConnectAPI()
         seller = api.catalog.sellers.get(seller_id=42)
         print(f"Name: {seller.name}")
         print(f"Catalogs: {len(seller.catalogs)}")

   .. tab:: curl

      .. code-block:: bash

         curl -X GET \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           'https://catalog-api.abconnect.co/api/Seller/42'

----

.. _put-apisellerid:

PUT /api/Seller/{id}
~~~~~~~~~~~~~~~~~~~~

Update an existing seller.

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         from ABConnect.api.models.catalog import UpdateSellerRequest

         api = ABConnectAPI()
         request = UpdateSellerRequest(
             name="Updated Seller",
             customer_display_id=12345,
             is_active=True,
         )
         seller = api.catalog.sellers.update(seller_id=42, data=request)

   .. tab:: curl

      .. code-block:: bash

         curl -X PUT \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           -H 'Content-Type: application/json' \
           -d '{"name":"Updated Seller","customerDisplayId":12345,"isActive":true}' \
           'https://catalog-api.abconnect.co/api/Seller/42'

----

.. _delete-apisellerid:

DELETE /api/Seller/{id}
~~~~~~~~~~~~~~~~~~~~~~~

Delete a seller.

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI

         api = ABConnectAPI()
         api.catalog.sellers.delete(seller_id=42)

   .. tab:: curl

      .. code-block:: bash

         curl -X DELETE \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           'https://catalog-api.abconnect.co/api/Seller/42'

----

Lots
----

.. _get-apilot:

GET /api/Lot
~~~~~~~~~~~~

List lots with pagination.

**Parameters:**

- ``page_number`` (int): Page number, default 1
- ``page_size`` (int): Items per page, default 10
- ``id`` (int, optional): Filter by lot ID
- ``customer_item_id`` (str, optional): Filter by customer item ID
- ``lot_number`` (str, optional): Filter by lot number
- ``customer_catalog_id`` (str, optional): Filter by customer catalog ID

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI

         api = ABConnectAPI()

         # Basic listing
         result = api.catalog.lots.list(page_number=1, page_size=10)
         for lot in result.items:
             print(f"{lot.id}: {lot.customer_item_id}")

         # Filter by customer item ID
         result = api.catalog.lots.list(customer_item_id="ITEM-001")

         # Filter by lot number
         result = api.catalog.lots.list(lot_number="LOT-001")

         # Filter by customer catalog ID
         result = api.catalog.lots.list(customer_catalog_id="400160")

   .. tab:: CLI

      .. code-block:: bash

         ab catalog lots list

   .. tab:: curl

      .. code-block:: bash

         curl -X GET \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           'https://catalog-api.abconnect.co/api/Lot?PageNumber=1&PageSize=10'

         # With filters
         curl -X GET \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           'https://catalog-api.abconnect.co/api/Lot?CustomerItemId=ITEM-001&LotNumber=LOT-001'

----

.. _post-apilot:

POST /api/Lot
~~~~~~~~~~~~~

Create a new lot.

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         from ABConnect.api.models.catalog import AddLotRequest, LotDataDto, LotCatalogDto

         api = ABConnectAPI()
         request = AddLotRequest(
             customer_item_id="ITEM-001",
             initial_data=LotDataDto(
                 qty=1,
                 l=24.0, w=18.0, h=12.0,
                 wgt=50.0,
                 description="Antique chair",
             ),
             catalogs=[LotCatalogDto(catalog_id=1, lot_number="LOT-001")],
         )
         lot = api.catalog.lots.create(request)
         print(lot.id)

   .. tab:: curl

      .. code-block:: bash

         curl -X POST \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           -H 'Content-Type: application/json' \
           -d '{"customerItemId":"ITEM-001","initialData":{"Qty":1,"L":24.0,"W":18.0,"H":12.0,"Wgt":50.0,"Description":"Antique chair"},"catalogs":[{"catalogId":1,"lotNumber":"LOT-001"}],"imageLinks":[]}' \
           'https://catalog-api.abconnect.co/api/Lot'

----

.. _get-apilotid:

GET /api/Lot/{id}
~~~~~~~~~~~~~~~~~

Get a lot by ID.

**Parameters:**

- ``lot_id`` (int) *(required)*: Lot ID

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI

         api = ABConnectAPI()
         lot = api.catalog.lots.get(lot_id=99)
         print(f"Item: {lot.customer_item_id}")
         print(f"Dimensions: {lot.initial_data.l}x{lot.initial_data.w}x{lot.initial_data.h}")

   .. tab:: curl

      .. code-block:: bash

         curl -X GET \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           'https://catalog-api.abconnect.co/api/Lot/99'

----

.. _put-apilotid:

PUT /api/Lot/{id}
~~~~~~~~~~~~~~~~~

Update an existing lot.

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         from ABConnect.api.models.catalog import UpdateLotRequest

         api = ABConnectAPI()
         request = UpdateLotRequest(
             customer_item_id="ITEM-001-UPDATED",
         )
         lot = api.catalog.lots.update(lot_id=99, data=request)

   .. tab:: curl

      .. code-block:: bash

         curl -X PUT \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           -H 'Content-Type: application/json' \
           -d '{"customerItemId":"ITEM-001-UPDATED"}' \
           'https://catalog-api.abconnect.co/api/Lot/99'

----

.. _delete-apilotid:

DELETE /api/Lot/{id}
~~~~~~~~~~~~~~~~~~~~

Delete a lot.

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI

         api = ABConnectAPI()
         api.catalog.lots.delete(lot_id=99)

   .. tab:: curl

      .. code-block:: bash

         curl -X DELETE \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           'https://catalog-api.abconnect.co/api/Lot/99'

----

.. _post-apilotgetoverrides:

POST /api/Lot/get-overrides
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Get lot overrides for specific customer item IDs.

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         from ABConnect.api.models.catalog import GetLotsOverridesQuery

         api = ABConnectAPI()
         query = GetLotsOverridesQuery(
             customer_item_ids=["ITEM-001", "ITEM-002"],
         )
         overrides = api.catalog.lots.get_overrides(query)
         for override in overrides:
             print(f"{override.customer_item_id}: {override.description}")

   .. tab:: curl

      .. code-block:: bash

         curl -X POST \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           -H 'Content-Type: application/json' \
           -d '{"customerItemIds":["ITEM-001","ITEM-002"]}' \
           'https://catalog-api.abconnect.co/api/Lot/get-overrides'

----

Bulk Operations
---------------

.. _post-apibulkinsert:

POST /api/Bulk/insert
~~~~~~~~~~~~~~~~~~~~~

Bulk insert catalogs with their associated lots and sellers in a single request.

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         from ABConnect.api.models.catalog import (
             BulkInsertRequest,
             BulkInsertCatalogRequest,
             BulkInsertLotRequest,
             BulkInsertSellerRequest,
             LotDataDto,
         )
         from datetime import datetime

         api = ABConnectAPI()
         request = BulkInsertRequest(
             catalogs=[
                 BulkInsertCatalogRequest(
                     customer_catalog_id="BULK-CAT-001",
                     agent="AgentName",
                     title="Bulk Catalog",
                     start_date=datetime(2025, 1, 1),
                     end_date=datetime(2025, 12, 31),
                     lots=[
                         BulkInsertLotRequest(
                             customer_item_id="ITEM-001",
                             lot_number="LOT-001",
                             initial_data=LotDataDto(
                                 qty=1, description="Bulk item",
                             ),
                         ),
                     ],
                     sellers=[
                         BulkInsertSellerRequest(
                             name="Bulk Seller",
                             customer_display_id=12345,
                             is_active=True,
                         ),
                     ],
                 ),
             ],
         )
         api.catalog.bulk.insert(request)

   .. tab:: curl

      .. code-block:: bash

         curl -X POST \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           -H 'Content-Type: application/json' \
           -d '{"catalogs":[{"customerCatalogId":"BULK-CAT-001","agent":"AgentName","title":"Bulk Catalog","startDate":"2025-01-01","endDate":"2025-12-31","lots":[{"customerItemId":"ITEM-001","lotNumber":"LOT-001","initialData":{"Qty":1,"Description":"Bulk item"},"imageLinks":[],"overridenData":[]}],"sellers":[{"name":"Bulk Seller","customerDisplayId":12345,"isActive":true}]}]}' \
           'https://catalog-api.abconnect.co/api/Bulk/insert'
