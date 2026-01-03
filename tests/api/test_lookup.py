import pytest


@pytest.mark.integration
def test_get_countries(api):
    """server returns countries list"""
    countries = api.lookup.get_countries()
    assert isinstance(countries, list), "api.lookup.get_countries should return a list"
    assert len(countries) > 0, "Should have at least one country"


def test_countries_fixture(LookupCountriesData):
    """fixture has expected structure"""
    assert isinstance(LookupCountriesData, list), "LookupCountries fixture should be a list"
    assert len(LookupCountriesData) > 0, "Should have at least one country"


@pytest.mark.integration
def test_get_contacttypes(api):
    """server returns contact types list"""
    contact_types = api.lookup.get_contacttypes()
    assert isinstance(contact_types, list), "api.lookup.get_contacttypes should return a list"
    assert len(contact_types) > 0, "Should have at least one contact type"


def test_contacttypes_fixture(LookupContactTypesData):
    """fixture has expected structure"""
    assert isinstance(LookupContactTypesData, list), "LookupContactTypes fixture should be a list"
    assert len(LookupContactTypesData) > 0, "Should have at least one contact type"


@pytest.mark.integration
def test_get_documenttypes(api):
    """server returns document types list"""
    document_types = api.lookup.get_documenttypes()
    assert isinstance(document_types, list), "api.lookup.get_documenttypes should return a list"
    assert len(document_types) > 0, "Should have at least one document type"


def test_documenttypes_fixture(LookupDocumentTypesData):
    """fixture has expected structure"""
    assert isinstance(LookupDocumentTypesData, list), "LookupDocumentTypes fixture should be a list"
    assert len(LookupDocumentTypesData) > 0, "Should have at least one document type"


@pytest.mark.integration
def test_get_accesskeys(api):
    """server returns access keys list"""
    access_keys = api.lookup.get_accesskeys()
    assert isinstance(access_keys, list), "api.lookup.get_accesskeys should return a list"
    assert len(access_keys) > 0, "Should have at least one access key"


def test_accesskeys_fixture(LookupAccessKeysData):
    """fixture has expected structure"""
    assert isinstance(LookupAccessKeysData, list), "LookupAccessKeys fixture should be a list"
    assert len(LookupAccessKeysData) > 0, "Should have at least one access key"


@pytest.mark.integration
def test_get_densityclassmap(api):
    """server returns density class map"""
    density_class_map = api.lookup.get_densityclassmap()
    assert isinstance(density_class_map, list), "api.lookup.get_densityclassmap should return a list"


def test_densityclassmap_fixture(LookupDensityClassMapData):
    """fixture has expected structure"""
    assert isinstance(LookupDensityClassMapData, list), "LookupDensityClassMap fixture should be a list"


@pytest.mark.integration
def test_get_parcelpackagetypes(api):
    """server returns parcel package types list"""
    parcel_package_types = api.lookup.get_parcelpackagetypes()
    assert isinstance(parcel_package_types, list), "api.lookup.get_parcelpackagetypes should return a list"
    assert len(parcel_package_types) > 0, "Should have at least one parcel package type"


def test_parcelpackagetypes_fixture(LookupParcelPackageTypesData):
    """fixture has expected structure"""
    assert isinstance(LookupParcelPackageTypesData, list), "LookupParcelPackageTypes fixture should be a list"
    assert len(LookupParcelPackageTypesData) > 0, "Should have at least one parcel package type"
