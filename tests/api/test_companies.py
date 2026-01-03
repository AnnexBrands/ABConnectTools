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
