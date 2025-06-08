Company Models
==============

.. currentmodule:: ABConnect.api.models.companies

Models for company-related API responses with inheritance hierarchy.

Base Models
-----------

.. autoclass:: CompanyBase
   :members:
   :undoc-members:
   :show-inheritance:
   
   Base model with fields common to all company responses.

.. autoclass:: CompanyBasic
   :members:
   :undoc-members:
   :show-inheritance:
   
   Basic company information returned by most endpoints.
   
   **Example Response:**
   
   .. code-block:: json
   
      {
        "id": "ed282b80-54fe-4f42-bf1b-69103ce1f76c",
        "code": "TRAINING",
        "name": "Training",
        "parentCompanyId": "5e2eefc1-d616-e911-b00c-00155d426802"
      }

Detailed Models
---------------

.. autoclass:: CompanyDetails
   :members:
   :undoc-members:
   :show-inheritance:
   
   Extended company information including addresses and contacts.
   
   **Example Response Structure:**
   
   .. code-block:: json
   
      {
        "companyID": "ed282b80-54fe-4f42-bf1b-69103ce1f76c",
        "companyName": "Training",
        "companyCode": "TRAINING",
        "companyEmail": "training@abconnect.co",
        "companyPhone": "8009814202",
        "mainAddress": {
          "address1": "2534 Vista Dr",
          "city": "Castle Rock",
          "state": "CO",
          "zipCode": "80104"
        },
        "companyInfo": {
          "isThirdParty": false,
          "isActive": true
        }
      }

.. autoclass:: CompanyFullDetails
   :members:
   :undoc-members:
   :show-inheritance:
   
   Complete company information including preferences, pricing, and capabilities.

Supporting Models
-----------------

.. autoclass:: CompanyAddress
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: CompanyPreferences
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: CompanyPricing
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: CompanyInsurance
   :members:
   :undoc-members:
   :show-inheritance:

Usage Examples
--------------

**Working with company hierarchy:**

.. code-block:: python

    from ABConnect import ABConnectAPI
    
    api = ABConnectAPI()
    
    # Get basic company info
    company = api.companies.get("ed282b80-54fe-4f42-bf1b-69103ce1f76c")
    print(f"{company.name} ({company.code})")
    
    # Get detailed information
    details = api.companies.get_details(company.id)
    print(f"Email: {details.companyEmail}")
    print(f"Phone: {details.companyPhone}")
    print(f"Address: {details.mainAddress.address1}")
    
    # Get full details including pricing
    full = api.companies.get_full_details(company.id)
    print(f"Base markup: {full.pricing.transportationMarkups.base}")

**Searching for companies:**

.. code-block:: python

    # Get all available companies
    companies = api.companies.get_available()
    
    for company in companies:
        print(f"{company.name} - {company.code}")
        
        # Check if it has a parent company
        if company.parentCompanyId:
            parent = api.companies.get(company.parentCompanyId)
            print(f"  Parent: {parent.name}")

Model Inheritance
-----------------

The company models use inheritance to avoid duplication:

1. **CompanyBase** - Common fields (id, code, name, parentCompanyId)
2. **CompanyBasic** - Inherits from CompanyBase, used for simple listings
3. **CompanyDetails** - Adds contact info, addresses, and settings
4. **CompanyFullDetails** - Adds pricing, insurance, and capabilities

This allows consistent field names across all company endpoints while providing
appropriate levels of detail for each use case.

See Also
--------

- :doc:`contacts` - Contact models associated with companies
- :doc:`addresses` - Address models used in company details
- :class:`~ABConnect.api.models.lookups.CompanyType` - Company type enumeration