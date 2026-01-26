"""Tests for companies endpoints with proper type validation.

All List responses must validate each element is the expected type.
"""
import pytest

# Training company ID (from fixture data)
TRAINING_COMPANY_ID = "ed282b80-54fe-4f42-bf1b-69103ce1f76c"


# =============================================================================
# GET /companies/{id} -> CompanySimple
# =============================================================================

@pytest.mark.integration
def test_get_company_by_id(api, models, schema):
    """server data validates against CompanySimple model"""
    CompanySimpleModelName = schema['COMPANIES']['GET'].response_model
    CompanySimpleClass = getattr(models, CompanySimpleModelName)
    company = api.companies.get_by_id(TRAINING_COMPANY_ID)
    assert isinstance(company, CompanySimpleClass), f"Expected CompanySimple, got {type(company)}"
    assert company.name == "Training", "Company name should be 'Training'"
    assert company.code == "TRAINING", "Company code should be 'TRAINING'"


def test_company_simple_model(models, CompanySimpleData):
    """fixture validates against CompanySimple model"""
    result = models.CompanySimple.model_validate(CompanySimpleData)
    assert isinstance(result, models.CompanySimple)


# =============================================================================
# GET /companies/brands -> List[CompanyBrandTreeNode]
# =============================================================================

@pytest.mark.integration
def test_get_brands(api, models, schema):
    """server returns List[CompanyBrandTreeNode] - each element must be correct type"""
    response_model = schema['COMPANIES']['GET_BRANDS'].response_model
    assert response_model == "List[CompanyBrandTreeNode]", f"Expected List[CompanyBrandTreeNode], schema says {response_model}"

    brands = api.companies.get_brands()
    assert isinstance(brands, list), f"Expected list, got {type(brands)}"
    assert len(brands) > 0, "Expected at least one brand"

    for i, brand in enumerate(brands):
        assert isinstance(brand, models.CompanyBrandTreeNode), \
            f"Element {i} is {type(brand)}, expected CompanyBrandTreeNode"


def test_brands_fixture(models, CompanyBrandsData):
    """fixture validates - each element must be CompanyBrandTreeNode"""
    assert isinstance(CompanyBrandsData, list), "CompanyBrands fixture should be a list"
    assert len(CompanyBrandsData) > 0, "Expected at least one brand in fixture"

    for i, item in enumerate(CompanyBrandsData):
        result = models.CompanyBrandTreeNode.model_validate(item)
        assert isinstance(result, models.CompanyBrandTreeNode), \
            f"Element {i} failed to validate as CompanyBrandTreeNode"


# =============================================================================
# GET /companies/brandstree -> List[CompanyBrandTreeNode]
# =============================================================================

@pytest.mark.integration
def test_get_brandstree(api, models, schema):
    """server returns List[CompanyBrandTreeNode] - each element must be correct type"""
    response_model = schema['COMPANIES']['GET_BRANDSTREE'].response_model
    assert response_model == "List[CompanyBrandTreeNode]", f"Expected List[CompanyBrandTreeNode], schema says {response_model}"

    tree = api.companies.get_brandstree()
    assert isinstance(tree, list), f"Expected list, got {type(tree)}"

    for i, node in enumerate(tree):
        assert isinstance(node, models.CompanyBrandTreeNode), \
            f"Element {i} is {type(node)}, expected CompanyBrandTreeNode"


def test_brandstree_fixture(models, CompanyBrandsTreeData):
    """fixture validates - each element must be CompanyBrandTreeNode"""
    assert isinstance(CompanyBrandsTreeData, list), "CompanyBrandsTree fixture should be a list"

    for i, item in enumerate(CompanyBrandsTreeData):
        result = models.CompanyBrandTreeNode.model_validate(item)
        assert isinstance(result, models.CompanyBrandTreeNode), \
            f"Element {i} failed to validate as CompanyBrandTreeNode"


# =============================================================================
# GET /companies/availableByCurrentUser -> List[CompanySimple]
# =============================================================================

@pytest.mark.integration
def test_get_availablebycurrentuser(api, models, schema):
    """server returns List[CompanySimple] - each element must be correct type"""
    response_model = schema['COMPANIES']['GET_AVAILABLE_BY_CURRENT_USER'].response_model
    assert response_model == "List[CompanySimple]", f"Expected List[CompanySimple], schema says {response_model}"

    available = api.companies.get_availablebycurrentuser()
    assert isinstance(available, list), f"Expected list, got {type(available)}"
    assert len(available) > 0, "Expected at least one company available to current user"

    for i, company in enumerate(available):
        assert isinstance(company, models.CompanySimple), \
            f"Element {i} is {type(company)}, expected CompanySimple"


def test_availablebycurrentuser_fixture(models, CompanyAvailableByCurrentUserData):
    """fixture validates - each element must be CompanySimple"""
    assert isinstance(CompanyAvailableByCurrentUserData, list), "CompanyAvailableByCurrentUser fixture should be a list"
    assert len(CompanyAvailableByCurrentUserData) > 0, "Expected at least one company in fixture"

    for i, item in enumerate(CompanyAvailableByCurrentUserData):
        result = models.CompanySimple.model_validate(item)
        assert isinstance(result, models.CompanySimple), \
            f"Element {i} failed to validate as CompanySimple"


# =============================================================================
# GET /companies/search -> List[SearchCompanyResponse]
# =============================================================================

@pytest.mark.integration
def test_get_search(api, models, schema):
    """server returns List[SearchCompanyResponse] - each element must be correct type"""
    response_model = schema['COMPANIES']['GET_SEARCH'].response_model
    assert response_model == "List[SearchCompanyResponse]", f"Expected List[SearchCompanyResponse], schema says {response_model}"

    # Must provide search_value to avoid HTTP 500
    results = api.companies.get_search(search_value="Training")
    assert isinstance(results, list), f"Expected list, got {type(results)}"

    for i, company in enumerate(results):
        assert isinstance(company, models.SearchCompanyResponse), \
            f"Element {i} is {type(company)}, expected SearchCompanyResponse"


# =============================================================================
# GET /companies/geoAreaCompanies -> List[CompanyGeoAreaCompanies]
# =============================================================================

@pytest.mark.integration
@pytest.mark.xfail(reason="HTTP 500 from API")
def test_get_geoareacompanies(api, models, schema):
    """server returns List[CompanyGeoAreaCompanies] - each element must be correct type"""
    response_model = schema['COMPANIES']['GET_GEO_AREA_COMPANIES'].response_model
    assert response_model == "List[CompanyGeoAreaCompanies]", f"Expected List[CompanyGeoAreaCompanies], schema says {response_model}"

    companies = api.companies.get_geoareacompanies()
    assert isinstance(companies, list), f"Expected list, got {type(companies)}"

    for i, company in enumerate(companies):
        assert isinstance(company, models.CompanyGeoAreaCompanies), \
            f"Element {i} is {type(company)}, expected CompanyGeoAreaCompanies"
