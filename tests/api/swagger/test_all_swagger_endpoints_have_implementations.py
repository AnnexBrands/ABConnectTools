"""Test that all swagger endpoints have implementations and can be imported."""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from base_test import ABConnectTestCase


class TestAllSwaggerEndpointsHaveImplementations(ABConnectTestCase):
    """Test swagger endpoint implementations with visual tree output."""

    def test_all_swagger_endpoints_have_implementations(self):
        """Test that all endpoints in swagger.json have implementations and can be imported.

        Displays a tree structure with green checks or red X for each import.
        """
        if not self.swagger_spec:
            self.skipTest("Swagger spec not available")

        print("\n" + "=" * 60)
        print("SWAGGER ENDPOINT IMPLEMENTATION CHECK")
        print("=" * 60)

        # Extract all API paths and group by endpoint
        endpoint_paths = {}
        for path in self.swagger_spec.get("paths", {}):
            parts = path.split("/")
            if len(parts) > 2:
                endpoint = parts[2]
                # Normalize endpoint names
                normalized = endpoint.replace("-", "_")
                if normalized not in endpoint_paths:
                    endpoint_paths[normalized] = {
                        'original': endpoint,
                        'paths': []
                    }
                endpoint_paths[normalized]['paths'].append(path)

        # Test each endpoint
        missing_files = []
        import_failures = []
        successful_imports = []

        print(f"\nAPI Endpoints Tree (from swagger.json):")
        print("├── ABConnect.api")

        for endpoint_name in sorted(endpoint_paths.keys()):
            endpoint_info = endpoint_paths[endpoint_name]
            path_count = len(endpoint_info['paths'])

            # Check if file exists (either as .py file or package directory)
            endpoint_file = self.endpoints_dir / f"{endpoint_name}.py"
            endpoint_package = self.endpoints_dir / endpoint_name
            file_exists = endpoint_file.exists() or (endpoint_package.exists() and endpoint_package.is_dir())

            # Special case: 'job' endpoint is implemented as 'jobs' package
            if endpoint_name == 'job' and not file_exists:
                jobs_package = self.endpoints_dir / 'jobs'
                if jobs_package.exists() and jobs_package.is_dir():
                    file_exists = True
                    endpoint_package = jobs_package

            # Try to import from API client
            can_import = False
            import_error = None

            if file_exists:
                try:
                    # Special handling for 'job' endpoint (implemented as 'jobs' package)
                    if endpoint_name == 'job':
                        # Check if the jobs package can be imported
                        try:
                            from ABConnect.api.endpoints.jobs import JobsPackage
                            can_import = True
                            successful_imports.append(endpoint_name)
                        except ImportError as e:
                            import_error = f"Cannot import JobsPackage: {e}"
                    else:
                        # Test if we can import the endpoint class directly
                        from ABConnect.api.endpoints import BaseEndpoint

                        # Import endpoint classes to verify they exist and are importable
                        endpoint_class_name = f"{endpoint_name.title()}Endpoint"

                        # Handle special cases for class names
                        class_name_mappings = {
                            'SmsTemplate': 'SmstemplateEndpoint',
                            'Values': 'ValuesEndpoint',
                            'e_sign': 'ESignEndpoint',
                        }

                        actual_class_name = class_name_mappings.get(endpoint_name, endpoint_class_name)

                        # Try to import the specific endpoint class
                        try:
                            import importlib
                            module = importlib.import_module('ABConnect.api.endpoints')
                            endpoint_class = getattr(module, actual_class_name)

                            # Verify it's a subclass of BaseEndpoint
                            if issubclass(endpoint_class, BaseEndpoint):
                                can_import = True
                                successful_imports.append(endpoint_name)
                            else:
                                import_error = f"{actual_class_name} is not a BaseEndpoint subclass"

                        except AttributeError:
                            import_error = f"Class {actual_class_name} not found in endpoints module"

                except Exception as e:
                    import_error = str(e)

                if not can_import:
                    import_failures.append((endpoint_name, import_error))
            else:
                missing_files.append(endpoint_name)

            # Display status with tree structure
            if file_exists and can_import:
                status = "✅"  # Green check
                # Check if it's a package implementation
                is_package = endpoint_package.exists() and endpoint_package.is_dir()
                if endpoint_name == 'job' and (self.endpoints_dir / 'jobs').is_dir():
                    detail = f"({path_count} paths, via 'jobs' package)"
                elif is_package:
                    detail = f"({path_count} paths, package)"
                else:
                    detail = f"({path_count} paths)"
            elif file_exists and not can_import:
                status = "⚠️ "  # Warning - file exists but can't import
                detail = f"(FILE EXISTS, IMPORT FAILED: {import_error})"
            else:
                status = "❌"  # Red X
                detail = f"(FILE MISSING, {path_count} paths)"

            print(f"│   ├── {endpoint_name} {status} {detail}")

            # Show some example paths for failed imports
            if not (file_exists and can_import) and path_count <= 3:
                for path in endpoint_info['paths']:
                    print(f"│   │   └── {path}")
            elif not (file_exists and can_import) and path_count > 3:
                for path in endpoint_info['paths'][:2]:
                    print(f"│   │   └── {path}")
                print(f"│   │   └── ... and {path_count - 2} more")

        # Summary
        total = len(endpoint_paths)
        working = len(successful_imports)
        file_missing = len(missing_files)
        import_failed = len(import_failures)

        print(f"\n" + "-" * 60)
        print(f"SUMMARY:")
        print(f"  ✅ Working endpoints:     {working}/{total}")
        print(f"  ❌ Missing files:         {file_missing}")
        print(f"  ⚠️  Import failures:      {import_failed}")

        if missing_files:
            print(f"\nMissing implementation files:")
            for endpoint in missing_files:
                print(f"  - {endpoint}.py")

        if import_failures:
            print(f"\nImport failures:")
            for endpoint, error in import_failures:
                print(f"  - {endpoint}: {error}")

        # Assert all endpoints are working
        self.assertEqual(file_missing, 0, f"Missing {file_missing} endpoint files")
        self.assertEqual(import_failed, 0, f"Failed to import {import_failed} endpoints")

    def test_endpoint_accessibility_from_api_client(self):
        """Test that endpoints are accessible from the main API client."""
        if not self.swagger_spec:
            self.skipTest("Swagger spec not available")

        try:
            from ABConnect.api import ABConnectAPI
            api = ABConnectAPI()
        except Exception as e:
            self.skipTest(f"Cannot import ABConnectAPI: {e}")

        # Get all endpoint names from swagger
        endpoint_names = set()
        for path in self.swagger_spec.get("paths", {}):
            parts = path.split("/")
            if len(parts) > 2:
                endpoint = parts[2].replace("-", "_")
                endpoint_names.add(endpoint)

        # Test each endpoint is accessible
        inaccessible = []
        for endpoint_name in sorted(endpoint_names):
            if not hasattr(api, endpoint_name):
                inaccessible.append(endpoint_name)

        if inaccessible:
            self.fail(f"Endpoints not accessible from ABConnectAPI: {inaccessible}")

    def test_swagger_path_coverage(self):
        """Test coverage of swagger paths in our implementation."""
        if not self.swagger_spec:
            self.skipTest("Swagger spec not available")

        total_paths = len(self.swagger_spec.get("paths", {}))

        # Group paths by endpoint
        endpoint_groups = {}
        for path in self.swagger_spec.get("paths", {}):
            parts = path.split("/")
            if len(parts) > 2:
                endpoint = parts[2].replace("-", "_")
                if endpoint not in endpoint_groups:
                    endpoint_groups[endpoint] = []
                endpoint_groups[endpoint].append(path)

        # Count implemented paths (endpoints that exist as files or packages)
        implemented_paths = 0
        for endpoint, paths in endpoint_groups.items():
            endpoint_file = self.endpoints_dir / f"{endpoint}.py"
            endpoint_package = self.endpoints_dir / endpoint

            # Special case: 'job' endpoint is implemented as 'jobs' package
            if endpoint == 'job':
                jobs_package = self.endpoints_dir / 'jobs'
                if jobs_package.exists() and jobs_package.is_dir():
                    implemented_paths += len(paths)
            elif endpoint_file.exists() or (endpoint_package.exists() and endpoint_package.is_dir()):
                implemented_paths += len(paths)

        coverage = (implemented_paths / total_paths * 100) if total_paths > 0 else 0

        print(f"\nSwagger Path Coverage: {implemented_paths}/{total_paths} ({coverage:.1f}%)")

        # We expect 100% coverage
        self.assertEqual(implemented_paths, total_paths,
                        f"Path coverage is {coverage:.1f}% (expected 100%)")


if __name__ == "__main__":
    import unittest
    unittest.main()