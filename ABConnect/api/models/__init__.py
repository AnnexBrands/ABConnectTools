"""ABConnect API models package.

Auto-generated from swagger.json specification.
Contains Pydantic models for all API schemas.
"""

# Import base and enums first as they don't have dependencies
from .base import *
from .enums import *

# Lazy loading function to avoid circular imports
_MODELS = {}

def __getattr__(name):
    """Lazy load models to avoid circular imports."""
    if name in _MODELS:
        return _MODELS[name]

    # Map of model names to their modules
    module_map = {
        # Account models
        'ChangePasswordModel': 'account',
        'ForgotPasswordRequest': 'account',
        'LoginModel': 'account',
        'ResetPasswordRequest': 'account',
        'UserAccessProfileModel': 'account',

        # Address models
        'Address': 'address',
        'AddressData': 'address',
        'AddressDetails': 'address',
        'AddressModel': 'address',
        'OverridableAddressData': 'address',
        'PlannerAddress': 'address',

        # Company models
        'Company': 'companies',
        'CompanyAddressInfo': 'companies',
        'CompanyDetails': 'companies',
        'CompanyDetailsBaseInfo': 'companies',
        'CompanyDetailsFinalMileTariffItem': 'companies',
        'CompanyDetailsInsurancePricing': 'companies',
        'CompanyDetailsPreferences': 'companies',
        'CompanyDetailsServicePricings': 'companies',
        'CompanyDetailsTaxPricing': 'companies',
        'CompanyImageData': 'companies',
        'CompanyInfo': 'companies',
        'CompanyInsurancePricing': 'companies',
        'CompanyServicePricing': 'companies',
        'CompanyTaxPricing': 'companies',
        'ContactDetailsCompanyInfo': 'companies',
        'PackagingLaborSettings': 'companies',
        'PackagingTariffSettings': 'companies',
        'SaveGeoSettingModel': 'companies',
        'SearchCompanyDataSourceLoadOptions': 'companies',
        'SearchCompanyModel': 'companies',
        'SearchCompanyResponse': 'companies',
        'TagBoxDataSourceLoadOptions': 'companies',
        'UpdateCarrierAccountsModel': 'companies',
        'WebApiDataSourceLoadOptions': 'companies',

        # Contact models
        'BaseContactDetails': 'contacts',
        'CalendarContact': 'contacts',
        'Contact': 'contacts',
        'ContactDetails': 'contacts',
        'ContactModel': 'contacts',
        'ContactNote': 'contacts',
        'ContactResponse': 'contacts',
        'ContactSync': 'contacts',
        'CreateContactRequest': 'contacts',
        'CustomerInfo': 'contacts',
        'GetContactHistoryResponse': 'contacts',
        'MergeContact': 'contacts',
        'MergeContactRequest': 'contacts',
        'MergeContactResponse': 'contacts',
        'PreferredContact': 'contacts',
        'SmsContact': 'contacts',
        'UpdateContactRequest': 'contacts',

        # Job models
        'Job': 'job',
        'JobDetails': 'job',
        'JobFormAnswer': 'jobform',
        'JobFormQuestion': 'jobform',
        'JobPayment': 'jobpayment',
        'JobShipment': 'jobshipment',

        # Document models
        'DocumentUpdateModel': 'documents',
        'ItemPhotoUploadRequest': 'document_upload',
        'UploadedFile': 'document_upload',
        'ItemPhotoUploadResponse': 'document_upload',

        # Add more models as needed...
    }

    if name in module_map:
        module_name = module_map[name]
        # Import the module
        import importlib
        module = importlib.import_module(f'.{module_name}', package='ABConnect.api.models')
        # Get the model from the module
        model = getattr(module, name)
        # Cache it
        _MODELS[name] = model
        return model

    raise AttributeError(f"module 'ABConnect.api.models' has no attribute '{name}'")

# Rebuild models after all are defined (called when needed)
def rebuild_models():
    """Rebuild all Pydantic models to resolve forward references."""
    # Import all model modules
    import importlib
    modules_to_rebuild = [
        'account', 'address', 'companies', 'contacts', 'job',
        'jobform', 'jobpayment', 'jobshipment', 'documents',
        'users', 'dashboard', 'reports', 'lookup'
    ]

    for module_name in modules_to_rebuild:
        try:
            module = importlib.import_module(f'.{module_name}', package='ABConnect.api.models')
            # Call model_rebuild on all Pydantic models in the module
            for attr_name in dir(module):
                attr = getattr(module, attr_name)
                if hasattr(attr, 'model_rebuild'):
                    try:
                        attr.model_rebuild()
                    except:
                        pass  # Some models might not need rebuilding
        except ImportError:
            pass  # Module might not exist