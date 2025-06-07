Builder Module
==============

The Builder module provides functionality to dynamically construct API requests from static JSON templates.

.. automodule:: ABConnect.Builder
   :members:
   :undoc-members:
   :show-inheritance:

APIRequestBuilder
-----------------

.. autoclass:: ABConnect.Builder.APIRequestBuilder
   :members:
   :undoc-members:
   :show-inheritance:
   :special-members: __init__
   :noindex:

Usage Examples
--------------

Basic Request Building
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from ABConnect.Builder import APIRequestBuilder
   
   builder = APIRequestBuilder()
   
   # Build a regular job request
   request = builder.build(
       customer_id='CUST123',
       job_type='Regular',
       origin_address={
           'street': '123 Main St',
           'city': 'New York',
           'state': 'NY',
           'zip': '10001'
       },
       destination_address={
           'street': '456 Oak Ave',
           'city': 'Los Angeles',
           'state': 'CA',
           'zip': '90001'
       }
   )

3PL Job Request
~~~~~~~~~~~~~~~

.. code-block:: python

   # Build a 3PL job request with extra containers
   request = builder.build(
       customer_id='3PL_CUST',
       job_type='3PL',
       extra_containers=True,
       container_data={
           'type': 'special',
           'count': 2
       }
   )

Template Structure
------------------

The Builder uses JSON templates stored in the ``base/`` directory:

* ``simple_request.json`` - Default request template
* ``extra_containers.json`` - Additional container configurations for 3PL requests
* ``companies.json`` - Company reference data
* ``statuses.json`` - Status reference data