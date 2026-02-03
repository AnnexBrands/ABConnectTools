import pytest

from tests.constants import JOB_DISPLAY_ID


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


# ==============================================================================
# Routes needing response_model defined (parameterless GETs, response_model=None)
# ==============================================================================

@pytest.mark.integration
@pytest.mark.xfail(reason=(
    "Human: Route COMON_INSURANCE has response_model=None. "
    "Call api.lookup.get_comoninsurance() manually, inspect the response, "
    "define a Pydantic model, update the route in routes.py, "
    "then save fixture via save_fixture(result, 'LookupComonInsurance')."
))
def test_get_comoninsurance(api):
    """get_comoninsurance returns insurance lookup data"""
    result = api.lookup.get_comoninsurance()
    assert result is not None


@pytest.mark.integration
@pytest.mark.xfail(reason=(
    "Human: Route PPCCAMPAIGNS has response_model=None. "
    "Call api.lookup.get_ppccampaigns() manually, inspect the response, "
    "define a Pydantic model, update the route in routes.py, "
    "then save fixture via save_fixture(result, 'LookupPPCCampaigns')."
))
def test_get_ppccampaigns(api):
    """get_ppccampaigns returns PPC campaign data"""
    result = api.lookup.get_ppccampaigns()
    assert result is not None


@pytest.mark.integration
@pytest.mark.xfail(reason=(
    "Human: Route REFER_CATEGORY has response_model=None. "
    "Call api.lookup.get_refercategory() manually, inspect the response, "
    "define a Pydantic model, update the route in routes.py, "
    "then save fixture via save_fixture(result, 'LookupReferCategory')."
))
def test_get_refercategory(api):
    """get_refercategory returns referral categories"""
    result = api.lookup.get_refercategory()
    assert result is not None


@pytest.mark.integration
@pytest.mark.xfail(reason=(
    "Human: Route REFER_CATEGORY_HEIRACHY has response_model=None. "
    "Call api.lookup.get_refercategoryheirachy() manually, inspect the response, "
    "define a Pydantic model, update the route in routes.py, "
    "then save fixture via save_fixture(result, 'LookupReferCategoryHierarchy')."
))
def test_get_refercategoryheirachy(api):
    """get_refercategoryheirachy returns referral category hierarchy"""
    result = api.lookup.get_refercategoryheirachy()
    assert result is not None


# ==============================================================================
# Routes needing parameters
# ==============================================================================

@pytest.mark.integration
@pytest.mark.xfail(reason=(
    "Human: Call api.lookup.get_lookup_value(masterConstantKey, valueId) "
    "with valid lookup key/value IDs. Save fixture via save_fixture(result, 'LookupValue')."
))
def test_get_lookup_value(api):
    """get_lookup_value returns a specific lookup entry"""
    result = api.lookup.get_lookup_value("NEED_VALID_KEY", "NEED_VALID_ID")
    assert result is not None


@pytest.mark.integration
@pytest.mark.xfail(reason=(
    "Human: Call api.lookup.get_accesskey(accessKey) with a valid access key "
    "from LookupAccessKeys fixture. Save fixture via save_fixture(result, 'LookupAccessKey')."
))
def test_get_accesskey(api):
    """get_accesskey returns a specific access key"""
    result = api.lookup.get_accesskey("NEED_VALID_KEY")
    assert result is not None


@pytest.mark.integration
@pytest.mark.xfail(reason=(
    "Human: Route ITEMS has response_model=None. "
    "Call api.lookup.get_items(job_display_id=JOB_DISPLAY_ID) manually, "
    "inspect the response, define a Pydantic model, update the route in routes.py, "
    "then save fixture via save_fixture(result, 'LookupItems')."
))
def test_get_items(api):
    """get_items returns item lookup data"""
    result = api.lookup.get_items(job_display_id=JOB_DISPLAY_ID)
    assert result is not None


# ==============================================================================
# Side-effecting route
# ==============================================================================

@pytest.mark.integration
@pytest.mark.xfail(reason=(
    "Human: Route RESET_MASTER_CONSTANT_CACHE has response_model=None and "
    "is side-effecting (resets cache). Only test if cache reset is safe in staging."
))
def test_resetmasterconstantcache(api):
    """get_resetmasterconstantcache resets the master constant cache"""
    result = api.lookup.get_resetmasterconstantcache()
    assert result is not None
