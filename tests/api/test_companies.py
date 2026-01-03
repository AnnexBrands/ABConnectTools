import pytest

# Training company ID (from fixture data)
TRAINING_COMPANY_ID = "ed282b80-54fe-4f42-bf1b-69103ce1f76c"


@pytest.mark.integration
def test_get_company_by_id(api, models, schema):
    """server data validates against CompanySimple model"""
    CompanySimpleModelName = schema['COMPANIES']['GET'].response_model
    CompanySimpleClass = getattr(models, CompanySimpleModelName)
    company = api.companies.get_by_id(TRAINING_COMPANY_ID)
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
