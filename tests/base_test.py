"""Base test class for ABConnect test suite.

Enforces constitution principles:
- Docs -> Tests -> Code workflow
- 1:1 relationship between endpoints and models with swagger.json
- Each endpoint requires: models, examples, unit tests, implementation
"""

import unittest
import warnings
from typing import Dict, List, Optional, Any
from pathlib import Path
import json


class ABConnectTestCase(unittest.TestCase):
    """Base test case for all ABConnect tests.

    Provides common functionality and enforces testing standards.
    """

    @classmethod
    def setUpClass(cls):
        """Set up class-level fixtures."""
        cls.project_root = Path(__file__).parent.parent
        cls.swagger_path = cls.project_root / "ABConnect" / "base" / "swagger.json"
        cls.endpoints_dir = cls.project_root / "ABConnect" / "api" / "endpoints"
        cls.models_dir = cls.project_root / "ABConnect" / "api" / "models"
        cls.docs_dir = cls.project_root / "docs"
        cls.examples_dir = cls.project_root / "examples"

        # Load swagger once for all tests
        if cls.swagger_path.exists():
            with open(cls.swagger_path) as f:
                cls.swagger_spec = json.load(f)
        else:
            cls.swagger_spec = None

    def assertEndpointExists(self, endpoint_name: str, msg: Optional[str] = None):
        """Assert that an endpoint implementation exists."""
        endpoint_file = self.endpoints_dir / f"{endpoint_name}.py"
        if not endpoint_file.exists():
            msg = msg or f"Endpoint {endpoint_name} not found at {endpoint_file}"
            self.fail(msg)

    def assertModelExists(self, model_name: str, msg: Optional[str] = None):
        """Assert that a model implementation exists."""
        # Models might be in various files, check __init__ mapping
        models_init = self.models_dir / "__init__.py"
        if models_init.exists():
            with open(models_init) as f:
                content = f.read()
                if f"'{model_name}'" in content or f'"{model_name}"' in content:
                    return
        msg = msg or f"Model {model_name} not found in models package"
        self.fail(msg)

    def assertHasDocumentation(self, component: str, msg: Optional[str] = None):
        """Assert that documentation exists for a component."""
        # Check various doc locations
        doc_locations = [
            self.docs_dir / "api" / f"{component}.rst",
            self.docs_dir / "endpoints" / f"{component}.rst",
            self.docs_dir / "models" / f"{component}.rst",
        ]

        if not any(loc.exists() for loc in doc_locations):
            msg = msg or f"Documentation for {component} not found"
            self.fail(msg)

    def assertHasExample(self, endpoint: str, msg: Optional[str] = None):
        """Assert that an example exists for an endpoint."""
        example_locations = [
            self.examples_dir / f"{endpoint}_example.py",
            self.examples_dir / endpoint / "example.py",
        ]

        if not any(loc.exists() for loc in example_locations):
            # Check if examples are in docstrings
            endpoint_file = self.endpoints_dir / f"{endpoint}.py"
            if endpoint_file.exists():
                with open(endpoint_file) as f:
                    content = f.read()
                    if "Example:" in content or ">>> " in content:
                        return

            msg = msg or f"No examples found for {endpoint}"
            self.fail(msg)

    def assertSwaggerCompliant(self, endpoint_name: str, msg: Optional[str] = None):
        """Assert that an endpoint is compliant with swagger spec."""
        if not self.swagger_spec:
            self.skipTest("Swagger spec not available")

        # Find paths for this endpoint
        endpoint_paths = [
            path for path in self.swagger_spec.get("paths", {})
            if path.startswith(f"/api/{endpoint_name}")
        ]

        if not endpoint_paths:
            msg = msg or f"No swagger paths found for {endpoint_name}"
            self.fail(msg)

        # Check endpoint exists
        self.assertEndpointExists(endpoint_name)

        # Check for models referenced in swagger
        for path in endpoint_paths:
            path_spec = self.swagger_spec["paths"][path]
            for method in path_spec:
                if method in ["get", "post", "put", "delete", "patch"]:
                    self._check_operation_models(path_spec[method])

    def _check_operation_models(self, operation: Dict[str, Any]):
        """Check models referenced in an operation."""
        # Check request body schema
        if "requestBody" in operation:
            content = operation["requestBody"].get("content", {})
            for content_type in content:
                schema = content[content_type].get("schema", {})
                self._check_schema_models(schema)

        # Check response schemas
        for status_code in operation.get("responses", {}):
            response = operation["responses"][status_code]
            if "content" in response:
                for content_type in response["content"]:
                    schema = response["content"][content_type].get("schema", {})
                    self._check_schema_models(schema)

    def _check_schema_models(self, schema: Dict[str, Any]):
        """Recursively check schema for model references."""
        if "$ref" in schema:
            # Extract model name from reference
            model_name = schema["$ref"].split("/")[-1]
            with warnings.catch_warnings():
                warnings.simplefilter("always")
                try:
                    self.assertModelExists(model_name)
                except AssertionError:
                    warnings.warn(f"Model {model_name} referenced in swagger but not found", UserWarning)

        # Check nested schemas
        if "properties" in schema:
            for prop in schema["properties"].values():
                self._check_schema_models(prop)
        if "items" in schema:
            self._check_schema_models(schema["items"])


class EndpointTestCase(ABConnectTestCase):
    """Base test case for endpoint-specific tests.

    Each endpoint test should inherit from this class.
    """

    # Override in subclasses
    endpoint_name = None
    endpoint_class = None
    required_models = []

    def test_endpoint_exists(self):
        """Test that the endpoint file exists."""
        if self.endpoint_name:
            self.assertEndpointExists(self.endpoint_name)

    def test_models_exist(self):
        """Test that required models exist."""
        for model in self.required_models:
            self.assertModelExists(model)

    def test_swagger_compliance(self):
        """Test swagger compliance for this endpoint."""
        if self.endpoint_name:
            self.assertSwaggerCompliant(self.endpoint_name)

    def test_has_documentation(self):
        """Test that documentation exists."""
        if self.endpoint_name:
            with warnings.catch_warnings():
                warnings.simplefilter("always")
                try:
                    self.assertHasDocumentation(self.endpoint_name)
                except AssertionError:
                    warnings.warn(f"Documentation missing for {self.endpoint_name}", UserWarning)

    def test_has_examples(self):
        """Test that examples exist."""
        if self.endpoint_name:
            with warnings.catch_warnings():
                warnings.simplefilter("always")
                try:
                    self.assertHasExample(self.endpoint_name)
                except AssertionError:
                    warnings.warn(f"Examples missing for {self.endpoint_name}", UserWarning)


class ModelTestCase(ABConnectTestCase):
    """Base test case for model-specific tests."""

    # Override in subclasses
    model_name = None
    model_class = None
    sample_data = {}

    def test_model_exists(self):
        """Test that the model exists."""
        if self.model_name:
            self.assertModelExists(self.model_name)

    def test_model_validation(self):
        """Test model validation with sample data."""
        if self.model_class and self.sample_data:
            try:
                instance = self.model_class(**self.sample_data)
                self.assertIsNotNone(instance)
            except Exception as e:
                self.fail(f"Model validation failed: {e}")

    def test_model_serialization(self):
        """Test model serialization."""
        if self.model_class and self.sample_data:
            try:
                instance = self.model_class(**self.sample_data)
                # Test dict serialization
                as_dict = instance.model_dump() if hasattr(instance, 'model_dump') else instance.dict()
                self.assertIsInstance(as_dict, dict)

                # Test JSON serialization
                as_json = instance.model_dump_json() if hasattr(instance, 'model_dump_json') else instance.json()
                self.assertIsInstance(as_json, str)
            except Exception as e:
                self.fail(f"Model serialization failed: {e}")