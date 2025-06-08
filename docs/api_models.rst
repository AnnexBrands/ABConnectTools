API Models
==========

Complete reference for all API request and response models.

.. toctree::
   :maxdepth: 2
   :caption: Model Categories

   models/addresses
   models/companies
   models/contacts
   models/documents
   models/forms
   models/jobs
   models/lookups
   models/users

Overview
--------

All API responses are validated using Pydantic models to ensure data consistency and type safety. 
The models are organized by their API tags and provide:

- Field validation and type checking
- Automatic JSON serialization/deserialization
- Clear documentation of expected data structures
- Support for nested models and relationships

Model Categories
----------------

**Core Models**

- :doc:`models/companies` - Company entities including customers, vendors, and carriers
- :doc:`models/contacts` - Contact information for individuals and businesses
- :doc:`models/jobs` - Shipping and logistics job models
- :doc:`models/users` - User accounts and authentication

**Supporting Models**

- :doc:`models/addresses` - Physical address models with validation
- :doc:`models/documents` - Document and file attachment models
- :doc:`models/forms` - Form data and submissions
- :doc:`models/lookups` - Reference data and configuration values

Usage Example
-------------

When you call an API endpoint, the response is automatically validated against the corresponding Pydantic model:

.. code-block:: python

    from ABConnect import ABConnectAPI
    from ABConnect.api.models.jobs import Job
    
    api = ABConnectAPI()
    
    # Get a job - response is validated as a Job model
    job = api.jobs.get("2000000")
    
    # Access typed fields
    print(job.jobDisplayId)  # "2000000"
    print(job.customerContact.contact.fullName)  # "Training"
    
    # Models provide IDE autocomplete and type hints
    for item in job.items:
        print(f"{item.description}: {item.weight} lbs")

Cross-References
----------------

Throughout the API documentation, you'll see references to these models in the **Response Type** sections.
Click on any model reference to see its complete field documentation.