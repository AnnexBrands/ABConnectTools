"""
Lookup API Examples - Getting reference data

This example demonstrates getting various lookup/reference data.
"""

from ABConnect.api import ABConnectAPI
from _helpers import save_fixture


def to_serializable(obj):
    """Convert Pydantic models or lists of models to dicts."""
    if isinstance(obj, list):
        return [to_serializable(item) for item in obj]
    if hasattr(obj, 'model_dump'):
        return obj.model_dump(by_alias=True)
    return obj


api = ABConnectAPI(env='staging', username='instaquote')

# Get countries
countries = api.lookup.get_countries()
print(f"Countries type: {type(countries)}")
print(f"Countries count: {len(countries) if isinstance(countries, list) else 'N/A'}")
save_fixture(to_serializable(countries), "LookupCountries")

# Get contact types
contact_types = api.lookup.get_contacttypes()
print(f"Contact types type: {type(contact_types)}")
print(f"Contact types count: {len(contact_types) if isinstance(contact_types, list) else 'N/A'}")
save_fixture(to_serializable(contact_types), "LookupContactTypes")

# Get document types
document_types = api.lookup.get_documenttypes()
print(f"Document types type: {type(document_types)}")
print(f"Document types count: {len(document_types) if isinstance(document_types, list) else 'N/A'}")
save_fixture(to_serializable(document_types), "LookupDocumentTypes")

# Get access keys
access_keys = api.lookup.get_accesskeys()
print(f"Access keys type: {type(access_keys)}")
print(f"Access keys count: {len(access_keys) if isinstance(access_keys, list) else 'N/A'}")
save_fixture(to_serializable(access_keys), "LookupAccessKeys")

# Get density class map
density_class_map = api.lookup.get_densityclassmap()
print(f"Density class map type: {type(density_class_map)}")
print(f"Density class map count: {len(density_class_map) if isinstance(density_class_map, list) else 'N/A'}")
save_fixture(to_serializable(density_class_map), "LookupDensityClassMap")

# Get parcel package types
parcel_package_types = api.lookup.get_parcelpackagetypes()
print(f"Parcel package types type: {type(parcel_package_types)}")
print(f"Parcel package types count: {len(parcel_package_types) if isinstance(parcel_package_types, list) else 'N/A'}")
save_fixture(to_serializable(parcel_package_types), "LookupParcelPackageTypes")
