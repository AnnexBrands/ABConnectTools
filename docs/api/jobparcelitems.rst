JobParcelItems
==============

Helper Methods
--------------

The ``ItemsHelper`` class provides convenient high-level methods for working with job items,
including parcel items, freight items, and calendar items. These methods automatically handle
Pydantic model casting for type safety.

Logged Delete Parcel Items
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Delete all parcel items for a job and automatically create a note logging the action.

**Method:** ``api.jobs.items.logged_delete_parcel_items(job_display_id)``

**Parameters:**

- ``job_display_id`` (int or str): The job display ID

**Returns:**

- ``bool``: True if all operations succeeded, False if any errors occurred

**Behavior:**

1. Gets the current username from authentication config (``ABCONNECT_USERNAME``)
2. Fetches all parcel items for the specified job
3. Creates a compact note listing the deleted items with their details (quantity, description, dimensions, weight)
4. Deletes each parcel item from the job
5. Logs all operations with appropriate error handling

**Note Format:** ``{username} deleted parcel items [{qty} {desc} {L}x{H}x{D} {W}lbs, ...]``

If no username is available, the note will be: ``Deleted parcel items [{qty} {desc} {L}x{H}x{D} {W}lbs, ...]``

**Example:**

.. code-block:: python

   from ABConnect.api import ABConnectAPI

   # Initialize the API client
   api = ABConnectAPI()

   # Delete all parcel items for a job with automatic logging
   success = api.jobs.items.logged_delete_parcel_items(4675060)

   if success:
       print("All parcel items deleted and logged successfully")
   else:
       print("Failed to delete parcel items - check logs for details")

**CLI Example:**

This helper method is designed for Python API use. For CLI operations, use the raw endpoints below.

**See Also:**

- :ref:`get-apijobjobdisplayidparcelitems` - Get parcel items for a job
- :ref:`delete-apijobjobdisplayidparcelitemsparcelitemid` - Delete individual parcel item
- :doc:`jobnote` - Note API for viewing created notes

----

Quick Reference
---------------

.. list-table::
   :header-rows: 1
   :widths: 10 40 50

   * - Method
     - Endpoint
     - Description
   * - GET
     - /api/job/{jobDisplayId}/parcelitems
     - 
   * - POST
     - /api/job/{jobDisplayId}/parcelitems
     - 
   * - PUT
     - /api/job/{jobDisplayId}/parcelitems/{parcelItemId}
     - 
   * - DELETE
     - /api/job/{jobDisplayId}/parcelitems/{parcelItemId}
     - 


.. _get-apijobjobdisplayidparcelitems:

GET /api/job/{jobDisplayId}/parcelitems
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Parameters:**

*Path Parameters:*

- `jobDisplayId` (string, path) *(required)*: No description available

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         
         # Initialize the API client
         api = ABConnectAPI()
         
         # Make the API call
         response = api.raw.get(
             "/api/job/{jobDisplayId}/parcelitems"
         ,
             jobDisplayId="2000000"
         
         )
         
         # Process the response
         print(response)

   .. tab:: CLI

      .. code-block:: bash

         ab api raw get /api/job/{jobDisplayId}/parcelitems \
             jobDisplayId=2000000

   .. tab:: curl

      .. code-block:: bash

         curl -X GET \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           'https://api.abconnect.co/api/job/2000000/parcelitems'

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      []

----

.. _post-apijobjobdisplayidparcelitems:

POST /api/job/{jobDisplayId}/parcelitems
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Parameters:**

*Path Parameters:*

- `jobDisplayId` (string, path) *(required)*: No description available

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         
         # Initialize the API client
         api = ABConnectAPI()
         
         # Make the API call
         response = api.raw.post(
             "/api/job/{jobDisplayId}/parcelitems"
         ,
             jobDisplayId="2000000"
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

         ab api raw post /api/job/{jobDisplayId}/parcelitems \
             jobDisplayId=2000000

   .. tab:: curl

      .. code-block:: bash

         curl -X POST \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           -H 'Content-Type: application/json' \
           -d '{
               "example": "data"
           }' \
           'https://api.abconnect.co/api/job/2000000/parcelitems'

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

.. _put-apijobjobdisplayidparcelitemsparcelitemid:

PUT /api/job/{jobDisplayId}/parcelitems/{parcelItemId}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Parameters:**

*Path Parameters:*

- `parcelItemId` (integer, path) *(required)*: No description available
- `jobDisplayId` (string, path) *(required)*: No description available

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         
         # Initialize the API client
         api = ABConnectAPI()
         
         # Make the API call
         response = api.raw.put(
             "/api/job/{jobDisplayId}/parcelitems/{parcelItemId}"
         ,
             parcelItemId="789e0123-e89b-12d3-a456-426614174002"
         ,
             jobDisplayId="2000000"
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

         ab api raw put /api/job/{jobDisplayId}/parcelitems/{parcelItemId} \
             parcelItemId=789e0123-e89b-12d3-a456-426614174002 \
             jobDisplayId=2000000

   .. tab:: curl

      .. code-block:: bash

         curl -X PUT \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           -H 'Content-Type: application/json' \
           -d '{
               "example": "data"
           }' \
           'https://api.abconnect.co/api/job/2000000/parcelitems/789e0123-e89b-12d3-a456-426614174002'

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {
        "id": "123e4567-e89b-12d3-a456-426614174000",
        "status": "updated",
        "message": "Resource updated successfully"
      }

----

.. _delete-apijobjobdisplayidparcelitemsparcelitemid:

DELETE /api/job/{jobDisplayId}/parcelitems/{parcelItemId}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Parameters:**

*Path Parameters:*

- `parcelItemId` (integer, path) *(required)*: No description available
- `jobDisplayId` (string, path) *(required)*: No description available

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         
         # Initialize the API client
         api = ABConnectAPI()
         
         # Make the API call
         response = api.raw.delete(
             "/api/job/{jobDisplayId}/parcelitems/{parcelItemId}"
         ,
             parcelItemId="789e0123-e89b-12d3-a456-426614174002"
         ,
             jobDisplayId="2000000"
         
         )
         
         # Process the response
         print(response)

   .. tab:: CLI

      .. code-block:: bash

         ab api raw delete /api/job/{jobDisplayId}/parcelitems/{parcelItemId} \
             parcelItemId=789e0123-e89b-12d3-a456-426614174002 \
             jobDisplayId=2000000

   .. tab:: curl

      .. code-block:: bash

         curl -X DELETE \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           'https://api.abconnect.co/api/job/2000000/parcelitems/789e0123-e89b-12d3-a456-426614174002'

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {
        "status": "success",
        "message": "Resource deleted successfully"
      }
