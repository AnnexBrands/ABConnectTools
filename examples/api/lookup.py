"""
Lookup API Examples - Getting reference data

This example demonstrates getting various lookup/reference data.

Usage:
    python lookup.py                # Run all examples
    python lookup.py countries      # Run a single example
    python lookup.py help           # List available examples
"""

from _base import ExampleRunner
from _helpers import save_fixture


def to_serializable(obj):
    """Convert Pydantic models or lists of models to dicts."""
    if isinstance(obj, list):
        return [to_serializable(item) for item in obj]
    if hasattr(obj, 'model_dump'):
        return obj.model_dump(by_alias=True)
    return obj


class LookupExamples(ExampleRunner):
    def __init__(self):
        super().__init__("Lookup API", api_kwargs=dict(env='staging', username='instaquote'))
        self.add("countries", "Get countries", self.get_countries)
        self.add("contacttypes", "Get contact types", self.get_contact_types)
        self.add("documenttypes", "Get document types", self.get_document_types)
        self.add("accesskeys", "Get access keys", self.get_access_keys)
        self.add("densityclassmap", "Get density class map", self.get_density_class_map)
        self.add("parcelpackagetypes", "Get parcel package types", self.get_parcel_package_types)

    def _print_result(self, label, result, fixture_name):
        print(f"{label} type: {type(result)}")
        print(f"{label} count: {len(result) if isinstance(result, list) else 'N/A'}")
        save_fixture(to_serializable(result), fixture_name)

    def get_countries(self):
        self._print_result("Countries", self.api.lookup.get_countries(), "LookupCountries")

    def get_contact_types(self):
        self._print_result("Contact types", self.api.lookup.get_contacttypes(), "LookupContactTypes")

    def get_document_types(self):
        self._print_result("Document types", self.api.lookup.get_documenttypes(), "LookupDocumentTypes")

    def get_access_keys(self):
        self._print_result("Access keys", self.api.lookup.get_accesskeys(), "LookupAccessKeys")

    def get_density_class_map(self):
        self._print_result("Density class map", self.api.lookup.get_densityclassmap(), "LookupDensityClassMap")

    def get_parcel_package_types(self):
        self._print_result("Parcel package types", self.api.lookup.get_parcelpackagetypes(), "LookupParcelPackageTypes")


if __name__ == "__main__":
    LookupExamples().run()
