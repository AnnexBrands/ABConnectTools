import pytest
from tests.constants import COMPANY_ID


# ==============================================================================
# Parameterless GETs (working)
# ==============================================================================

@pytest.mark.integration
def test_get_company_by_id(api, models, schema):
    """server data validates against CompanySimple model"""
    CompanySimpleModelName = schema['COMPANIES']['GET'].response_model
    CompanySimpleClass = getattr(models, CompanySimpleModelName)
    company = api.companies.get_by_id(COMPANY_ID)
    assert isinstance(company, CompanySimpleClass), "api.companies.get_by_id should return a CompanySimple instance"
    assert company.name == "Training", "Company name should be 'Training'"
    assert company.code == "TRAINING", "Company code should be 'TRAINING'"


def test_company_simple_model(models, CompanySimpleData):
    """fixture validates against CompanySimple model"""
    models.CompanySimple.model_validate(CompanySimpleData)


@pytest.mark.integration
def test_get_brands(api):
    """server returns brands list"""
    brands = api.companies.get_brands()
    assert isinstance(brands, list), "api.companies.get_brands should return a list"


def test_brands_fixture(CompanyBrandsData):
    """fixture has expected structure"""
    assert isinstance(CompanyBrandsData, list), "CompanyBrands fixture should be a list"


@pytest.mark.integration
def test_get_brandstree(api):
    """server returns brands tree"""
    tree = api.companies.get_brandstree()
    assert tree is not None, "api.companies.get_brandstree should return data"


def test_brandstree_fixture(CompanyBrandsTreeData):
    """fixture has expected structure"""
    assert CompanyBrandsTreeData is not None, "CompanyBrandsTree fixture should have data"


@pytest.mark.integration
def test_get_availablebycurrentuser(api):
    """server returns companies available by current user"""
    available = api.companies.get_availablebycurrentuser()
    assert isinstance(available, list), "api.companies.get_availablebycurrentuser should return a list"


def test_availablebycurrentuser_fixture(CompanyAvailableByCurrentUserData):
    """fixture has expected structure"""
    assert isinstance(CompanyAvailableByCurrentUserData, list), "CompanyAvailableByCurrentUser fixture should be a list"


# ==============================================================================
# Parameterized GETs using COMPANY_ID from constants
# ==============================================================================

@pytest.mark.integration
def test_get_details(api, models):
    """get_details returns company details"""
    result = api.companies.get_details(COMPANY_ID)
    assert isinstance(result, models.Company)


@pytest.mark.integration
def test_get_fulldetails(api, models):
    """get_fulldetails returns full company details"""
    result = api.companies.get_fulldetails(COMPANY_ID)
    assert isinstance(result, models.CompanyDetails)


@pytest.mark.integration
def test_get_capabilities(api):
    """get_capabilities returns company capabilities"""
    result = api.companies.get_capabilities(COMPANY_ID)
    assert result is not None


@pytest.mark.integration
def test_get_carrieracounts(api):
    """get_carrieracounts returns carrier accounts for company"""
    result = api.companies.get_carrieracounts(COMPANY_ID)
    assert result is not None


@pytest.mark.integration
def test_get_franchiseeaddresses(api):
    """get_franchiseeaddresses returns franchisee addresses"""
    result = api.companies.get_franchiseeaddresses(COMPANY_ID)
    assert isinstance(result, list)


@pytest.mark.integration
def test_get_packagingsettings(api):
    """get_packagingsettings returns packaging settings"""
    result = api.companies.get_packagingsettings(COMPANY_ID)
    assert result is not None


@pytest.mark.integration
def test_get_packaginglabor(api):
    """get_packaginglabor returns packaging labor settings"""
    result = api.companies.get_packaginglabor(COMPANY_ID)
    assert result is not None


@pytest.mark.integration
def test_get_search(api):
    """get_search returns matching companies"""
    result = api.companies.get_search(search_value="Training")
    assert isinstance(result, list)


@pytest.mark.integration
def test_get_geosettings_search(api):
    """get_geosettings_search returns geo settings"""
    result = api.companies.get_geosettings_search()
    assert isinstance(result, list)


# ==============================================================================
# Known API errors
# ==============================================================================

@pytest.mark.integration
@pytest.mark.xfail(reason="API returns HTTP 500 for geoAreaCompanies endpoint.")
def test_get_geoareacompanies(api):
    """get_geoareacompanies returns geo area companies"""
    result = api.companies.get_geoareacompanies()
    assert result is not None


# ==============================================================================
# Write operations — xfail
# ==============================================================================

@pytest.mark.integration
@pytest.mark.xfail(reason="Human: Write op. POST /companies/fulldetails creates company data.")
def test_post_fulldetails(api):
    """post_fulldetails creates company details"""
    result = api.companies.post_fulldetails(data={})
    assert result is not None


@pytest.mark.integration
@pytest.mark.xfail(reason="Human: Write op. POST /companies/list requires WebApiDataSourceLoadOptions.")
def test_post_list(api):
    """post_list returns filtered company list"""
    result = api.companies.post_list(data={})
    assert result is not None
