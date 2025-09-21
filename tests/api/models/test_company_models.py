"""Tests for company-related models."""

from .base_model_test import BaseModelTest


class TestCompanyModel(BaseModelTest):
    """Test suite for Company model."""

    model_name = "Company"
    # model_class will be set when imports are available
    sample_data = {
        "id": "test-id",
        "name": "Test Company",
        "code": "TEST"
    }


class TestCompanyDetailsModel(BaseModelTest):
    """Test suite for CompanyDetails model."""

    model_name = "CompanyDetails"
    sample_data = {
        "id": "test-id",
        "name": "Test Company",
        "code": "TEST",
        "address": "123 Test St"
    }