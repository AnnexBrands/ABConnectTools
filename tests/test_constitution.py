"""Test that the codebase follows our constitution principles."""

import warnings
from pathlib import Path
from base_test import ABConnectTestCase


class TestConstitutionCompliance(ABConnectTestCase):
    """Test constitution compliance across the codebase."""

    def test_all_swagger_endpoints_have_implementations(self):
        """Test that all endpoints in swagger.json have implementations."""
        if not self.swagger_spec:
            self.skipTest("Swagger spec not available")

        # Extract unique endpoint prefixes
        endpoints = set()
        for path in self.swagger_spec.get("paths", {}):
            parts = path.split("/")
            if len(parts) > 2:
                endpoint = parts[2]
                # Normalize endpoint names
                if "-" in endpoint:
                    endpoint = endpoint.replace("-", "_")
                endpoints.add(endpoint)

        # Check each endpoint
        missing = []
        for endpoint in sorted(endpoints):
            endpoint_file = self.endpoints_dir / f"{endpoint}.py"
            if not endpoint_file.exists():
                missing.append(endpoint)

        if missing:
            warnings.warn(
                f"Missing endpoint implementations: {', '.join(missing)}",
                UserWarning
            )

        # We expect all endpoints to exist
        self.assertEqual(len(missing), 0,
                        f"Missing {len(missing)} endpoint implementations")

    def test_endpoint_model_pairing(self):
        """Test that endpoints have corresponding models."""
        endpoint_files = list(self.endpoints_dir.glob("*.py"))
        endpoint_files = [f for f in endpoint_files if f.name != "__init__.py" and f.name != "base.py"]

        endpoints_without_models = []

        for endpoint_file in endpoint_files:
            endpoint_name = endpoint_file.stem

            # Check if there's a corresponding model file or models in __init__
            model_file = self.models_dir / f"{endpoint_name}.py"

            if not model_file.exists():
                # Check if models are referenced in __init__
                models_init = self.models_dir / "__init__.py"
                if models_init.exists():
                    with open(models_init) as f:
                        content = f.read()
                        # Look for model references related to this endpoint
                        if endpoint_name not in content.lower():
                            endpoints_without_models.append(endpoint_name)

        if endpoints_without_models:
            warnings.warn(
                f"Endpoints without clear model associations: {', '.join(endpoints_without_models)}",
                UserWarning
            )

    def test_docs_tests_code_workflow(self):
        """Test that components follow docs -> tests -> code workflow."""
        # Check for key documentation files
        required_docs = [
            "index.rst",
            "api.rst",
            "quickstart.rst",
        ]

        missing_docs = []
        for doc in required_docs:
            doc_file = self.docs_dir / doc
            if not doc_file.exists():
                missing_docs.append(doc)

        if missing_docs:
            warnings.warn(
                f"Missing documentation files: {', '.join(missing_docs)}",
                UserWarning
            )

        # Check for test coverage
        test_dir = self.project_root / "tests"
        test_files = list(test_dir.glob("test_*.py"))

        # We should have tests for major components
        expected_test_patterns = [
            "test_api",
            "test_builder",
            "test_loader",
            "test_quoter"
        ]

        missing_tests = []
        for pattern in expected_test_patterns:
            if not any(pattern in f.name for f in test_files):
                missing_tests.append(pattern)

        if missing_tests:
            warnings.warn(
                f"Missing test files: {', '.join(missing_tests)}",
                UserWarning
            )

    def test_no_violating_enhanced_files(self):
        """Test that we don't have files violating the constitution.

        Enhanced files should not exist - functionality should be in
        the main endpoint files following 1:1 with swagger.
        """
        violations = []

        # Check for _enhanced files
        for endpoint_file in self.endpoints_dir.glob("*_enhanced.py"):
            violations.append(endpoint_file.name)

        # Check for duplicate endpoint implementations
        for endpoint_file in self.endpoints_dir.glob("*_v2.py"):
            violations.append(endpoint_file.name)

        self.assertEqual(len(violations), 0,
                        f"Found violating files: {', '.join(violations)}")

    def test_swagger_first_principle(self):
        """Test that endpoints are organized by API path from swagger."""
        if not self.swagger_spec:
            self.skipTest("Swagger spec not available")

        # Get all paths from swagger
        swagger_paths = self.swagger_spec.get("paths", {})

        # Group by endpoint prefix
        endpoint_paths = {}
        for path in swagger_paths:
            parts = path.split("/")
            if len(parts) > 2:
                endpoint = parts[2]
                if endpoint not in endpoint_paths:
                    endpoint_paths[endpoint] = []
                endpoint_paths[endpoint].append(path)

        # Each endpoint group should have a corresponding file
        for endpoint, paths in endpoint_paths.items():
            # Normalize name
            file_name = endpoint.replace("-", "_") + ".py"
            endpoint_file = self.endpoints_dir / file_name

            if not endpoint_file.exists():
                warnings.warn(
                    f"Endpoint {endpoint} has {len(paths)} paths in swagger but no implementation",
                    UserWarning
                )


if __name__ == "__main__":
    import unittest
    unittest.main()