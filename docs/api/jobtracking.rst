JobTracking
===========

Track real-time status and location of shipments throughout the delivery process.

Quick Reference
---------------

.. list-table::
   :header-rows: 1
   :widths: 10 40 50

   * - Method
     - Endpoint
     - Description
   * - GET
     - /api/job/{jobDisplayId}/tracking
     - 
   * - GET
     - /api/job/{jobDisplayId}/tracking/shipment/{proNumber}
     - 


.. _get-apijobjobdisplayidtracking:

GET /api/job/{jobDisplayId}/tracking
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
             "/api/job/{jobDisplayId}/tracking"
         ,
             jobDisplayId="2000000"
         
         )
         
         # Process the response
         print(response)

   .. tab:: CLI

      .. code-block:: bash

         ab api raw get /api/job/{jobDisplayId}/tracking \
             jobDisplayId=2000000

   .. tab:: curl

      .. code-block:: bash

         curl -X GET \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           'https://api.abconnect.co/api/job/2000000/tracking'

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {
        "status": "success",
        "data": {}
      }

----

.. _get-apijobjobdisplayidtrackingshipmentpronumber:

GET /api/job/{jobDisplayId}/tracking/shipment/{proNumber}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Parameters:**

*Path Parameters:*

- `proNumber` (string, path) *(required)*: No description available
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
             "/api/job/{jobDisplayId}/tracking/shipment/{proNumber}"
         ,
             proNumber="example-value"
         ,
             jobDisplayId="2000000"
         
         )
         
         # Process the response
         print(response)

   .. tab:: CLI

      .. code-block:: bash

         ab api raw get /api/job/{jobDisplayId}/tracking/shipment/{proNumber} \
             proNumber=example-value \
             jobDisplayId=2000000

   .. tab:: curl

      .. code-block:: bash

         curl -X GET \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           'https://api.abconnect.co/api/job/2000000/tracking/shipment/example-value'

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {
        "status": "success",
        "data": {}
      }
