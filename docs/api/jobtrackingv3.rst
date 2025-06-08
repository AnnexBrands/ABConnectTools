JobTrackingV3
=============

Quick Reference
---------------

.. list-table::
   :header-rows: 1
   :widths: 10 40 50

   * - Method
     - Endpoint
     - Description
   * - GET
     - /api/v3/job/{jobDisplayId}/tracking/{historyAmount}
     - 


.. _get-apiv3jobjobdisplayidtrackinghistoryamount:

GET /api/v3/job/{jobDisplayId}/tracking/{historyAmount}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Parameters:**

*Path Parameters:*

- `jobDisplayId` (string, path) *(required)*: No description available

*Query Parameters:*

- `historyAmount` (integer, query): No description available

**Example Request:**

.. tabs::

   .. tab:: Python

      .. code-block:: python

         from ABConnect import ABConnectAPI
         
         # Initialize the API client
         api = ABConnectAPI()
         
         # Make the API call
         response = api.raw.get(
             "/api/v3/job/{jobDisplayId}/tracking/{historyAmount}"
         ,
             jobDisplayId=2000000
         
         )
         
         # Process the response
         print(response)

   .. tab:: CLI

      .. code-block:: bash

         ab api raw get /api/v3/job/{jobDisplayId}/tracking/{historyAmount} \
             jobDisplayId=2000000

   .. tab:: curl

      .. code-block:: bash

         curl -X GET \
           -H 'Authorization: Bearer YOUR_API_TOKEN' \
           'https://api.abconnect.co/api/v3/job/2000000/tracking/{historyAmount}'

**Sample Response:**

.. toggle::

   .. code-block:: json
      :linenos:

      {
        "status": "success",
        "data": {}
      }
