Job Models
==========

.. currentmodule:: ABConnect.api.models.jobs

Models for job-related API responses.

Core Job Model
--------------

.. autoclass:: Job
   :members:
   :undoc-members:
   :show-inheritance:
   :inherited-members:
   
   The main Job model represents a shipping/logistics job with all its details including:
   
   - Job identification (jobDisplayId, jobId)
   - Status and workflow information
   - Customer and contact details
   - Origin and destination addresses
   - Items being shipped
   - Pricing and billing information
   - Tracking and timeline data

   **Example Response Structure:**

   .. code-block:: json

      {
        "jobDisplayId": "2000000",
        "bookedDate": "2024-08-13T14:04:04",
        "ownerCompanyId": "ed282b80-54fe-4f42-bf1b-69103ce1f76c",
        "customerContact": {
          "id": 3473290,
          "contact": {
            "id": 266841,
            "fullName": "Training",
            "company": {
              "companyName": "Training",
              "companyCode": "TRAINING"
            }
          }
        },
        "items": [
          {
            "description": "Widget",
            "quantity": 1,
            "weight": 10.5
          }
        ]
      }

Supporting Models
-----------------

.. autoclass:: JobItem
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: JobAddress
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: JobContact
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: JobPricing
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: JobTimeline
   :members:
   :undoc-members:
   :show-inheritance:

Usage Examples
--------------

**Accessing nested data:**

.. code-block:: python

    from ABConnect import ABConnectAPI
    
    api = ABConnectAPI()
    job = api.jobs.get("2000000")
    
    # Access customer information
    customer_name = job.customerContact.contact.fullName
    company_code = job.customerContact.contact.company.companyCode
    
    # Iterate through items
    total_weight = sum(item.weight for item in job.items)
    
    # Check job status
    if job.jobStatusName == "Booked":
        print(f"Job {job.jobDisplayId} is ready for shipping")

**Creating a new job:**

.. code-block:: python

    from ABConnect.api.models.jobs import Job, JobItem
    
    # Create job data
    job_data = {
        "customerContactId": 12345,
        "items": [
            {"description": "Box 1", "quantity": 2, "weight": 5.0},
            {"description": "Box 2", "quantity": 1, "weight": 10.0}
        ],
        "origin": {
            "address1": "123 Main St",
            "city": "Denver",
            "state": "CO",
            "zipCode": "80202"
        },
        "destination": {
            "address1": "456 Oak Ave", 
            "city": "Los Angeles",
            "state": "CA",
            "zipCode": "90001"
        }
    }
    
    # Validate with Pydantic model
    job = Job.model_validate(job_data)
    
    # Create via API
    created_job = api.jobs.create(job.model_dump())

See Also
--------

- :class:`~ABConnect.api.models.companies.CompanyBasic` - Company information in jobs
- :class:`~ABConnect.api.models.contacts.Contact` - Contact details in jobs
- :class:`~ABConnect.api.models.addresses.Address` - Address validation