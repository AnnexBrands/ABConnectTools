"""Tests for RequestMapper."""

import pytest
from pydantic import ValidationError

from tests.base_test import ABConnectTestCase
from ABConnect.api.request_mapper import RequestMapper, get_request_mapper
from ABConnect.api.schema_mappings import REQUEST_MAPPINGS


class TestRequestMapper(ABConnectTestCase):
    """Test suite for RequestMapper class."""

    def setUp(self):
        """Set up test fixtures."""
        self.mapper = RequestMapper()

    def test_singleton_pattern(self):
        """Test that get_request_mapper returns singleton instance."""
        mapper1 = get_request_mapper()
        mapper2 = get_request_mapper()
        self.assertIs(mapper1, mapper2)

    def test_mappings_loaded(self):
        """Test that endpoint mappings are loaded from schema_mappings."""
        self.assertGreater(len(self.mapper.endpoint_mappings), 0)
        self.assertEqual(len(self.mapper.endpoint_mappings), len(REQUEST_MAPPINGS))

    def test_path_matching_exact(self):
        """Test exact path matching."""
        self.assertTrue(self.mapper._match_path('/api/job', '/api/job'))
        self.assertTrue(self.mapper._match_path('/api/companies/fulldetails', '/api/companies/fulldetails'))
        self.assertFalse(self.mapper._match_path('/api/job', '/api/jobs'))

    def test_path_matching_with_placeholder(self):
        """Test path matching with placeholders."""
        self.assertTrue(
            self.mapper._match_path(
                '/api/job/123/changeAgent',
                '/api/job/{jobDisplayId}/changeAgent'
            )
        )
        self.assertTrue(
            self.mapper._match_path(
                '/api/companies/abc-123/fulldetails',
                '/api/companies/{companyId}/fulldetails'
            )
        )

    def test_path_matching_multiple_placeholders(self):
        """Test path matching with multiple placeholders."""
        self.assertTrue(
            self.mapper._match_path(
                '/api/job/123/freightproviders/0/ratequote',
                '/api/job/{jobDisplayId}/freightproviders/{optionIndex}/ratequote'
            )
        )

    def test_path_matching_different_lengths(self):
        """Test that paths with different segment counts don't match."""
        self.assertFalse(
            self.mapper._match_path(
                '/api/job/123',
                '/api/job/{jobDisplayId}/extra'
            )
        )

    def test_get_model_for_known_endpoint(self):
        """Test getting model class for a known endpoint."""
        # POST /api/job should use JobSaveRequestModel
        model_class = self.mapper.get_model_for_endpoint('POST', '/api/job')
        self.assertIsNotNone(model_class)
        self.assertEqual(model_class.__name__, 'JobSaveRequestModel')

    def test_get_model_for_unknown_endpoint(self):
        """Test getting model for an unknown endpoint returns None."""
        model_class = self.mapper.get_model_for_endpoint('GET', '/api/unknown/endpoint')
        self.assertIsNone(model_class)

    def test_validate_request_passthrough_no_model(self):
        """Test that data passes through unchanged for endpoints without models."""
        data = {'foo': 'bar', 'baz': 123}
        result = self.mapper.validate_request(data, 'GET', '/api/unknown/endpoint')
        self.assertEqual(result, data)

    def test_validate_request_none_passthrough(self):
        """Test that None data passes through unchanged."""
        result = self.mapper.validate_request(None, 'POST', '/api/job')
        self.assertIsNone(result)

    def test_validate_request_transforms_data(self):
        """Test that validation transforms data with proper aliases."""
        # ChangeJobAgentRequest has specific fields: agentId, serviceType, etc.
        data = {
            'agent_id': 'some-uuid',  # snake_case should transform to camelCase
            'recalculate_price': True
        }
        # This will validate against ChangeJobAgentRequest model
        # and return camelCase keys
        model_class = self.mapper.get_model_for_endpoint(
            'POST', '/api/job/123/changeAgent'
        )
        if model_class:
            # Should not raise
            result = model_class.json(data)
            self.assertIsInstance(result, dict)
            # Verify camelCase transformation
            self.assertIn('agentId', result)
            self.assertIn('recalculatePrice', result)


class TestRequestMapperIntegration(ABConnectTestCase):
    """Integration tests for request mapper with actual models."""

    def test_registration_model_validation(self):
        """Test validation against RegistrationModel."""
        mapper = get_request_mapper()

        # Valid registration data (matches RegistrationModel required fields)
        valid_data = {
            'userName': 'testuser',
            'password': 'securepass123',
            'fullName': 'Test User',
            'email': 'test@example.com'
        }

        model = mapper.get_model_for_endpoint('POST', '/api/account/register')
        if model:
            # Should validate without error
            result = mapper.validate_request(valid_data, 'POST', '/api/account/register')
            self.assertIsInstance(result, dict)
            self.assertEqual(result['userName'], 'testuser')

    def test_invalid_data_raises_validation_error(self):
        """Test that invalid data raises ValidationError."""
        mapper = get_request_mapper()

        # ConfirmEmailModel requires specific fields
        invalid_data = {
            'not_a_valid_field': 'random_value'
        }

        model = mapper.get_model_for_endpoint('POST', '/api/account/confirm')
        if model:
            # Should raise ValidationError due to extra="forbid" in ABConnectBaseModel
            with self.assertRaises(ValidationError):
                model.json(invalid_data)

    def test_job_save_request_validation(self):
        """Test validation against JobSaveRequestModel."""
        mapper = get_request_mapper()
        model = mapper.get_model_for_endpoint('POST', '/api/job')

        # Check that the model exists
        self.assertIsNotNone(model)
        self.assertEqual(model.__name__, 'JobSaveRequestModel')


class TestRequestMappingsContent(ABConnectTestCase):
    """Test the content of REQUEST_MAPPINGS."""

    def test_all_mappings_have_valid_model_names(self):
        """Test that all mapped model names are valid identifiers."""
        for (method, path), model_name in REQUEST_MAPPINGS.items():
            self.assertIsInstance(model_name, str)
            self.assertTrue(model_name[0].isupper(),
                f"Model name should be PascalCase: {model_name}")

    def test_all_methods_are_valid_http_methods(self):
        """Test that all mapped methods are valid HTTP methods."""
        valid_methods = {'GET', 'POST', 'PUT', 'DELETE', 'PATCH'}
        for (method, path), model_name in REQUEST_MAPPINGS.items():
            self.assertIn(method, valid_methods,
                f"Invalid HTTP method: {method}")

    def test_all_paths_start_with_api(self):
        """Test that all paths start with /api/."""
        for (method, path), model_name in REQUEST_MAPPINGS.items():
            self.assertTrue(path.startswith('/api/'),
                f"Path should start with /api/: {path}")

    def test_expected_endpoints_are_mapped(self):
        """Test that key expected endpoints are in the mappings."""
        expected = [
            ('POST', '/api/job'),
            ('POST', '/api/account/register'),
            ('POST', '/api/companies/fulldetails'),
            ('PUT', '/api/job/save'),
        ]
        for method, path in expected:
            self.assertIn((method, path), REQUEST_MAPPINGS,
                f"Expected endpoint not in mappings: {method} {path}")
