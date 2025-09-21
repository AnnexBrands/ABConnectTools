"""Swagger API compliance tests package.

This package ensures that all API endpoints defined in swagger.json
have corresponding implementations in the ABConnect.api.endpoints module.
Each API path group has its own submodule for testing.
"""

import json
import warnings
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple
import importlib
import sys

# Add parent directory to path for base_test import
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from base_test import ABConnectTestCase


class SwaggerEndpointChecker:
    """Check API endpoints against swagger specification."""

    def __init__(self):
        self.swagger_path = Path(__file__).parent.parent.parent / "ABConnect" / "base" / "swagger.json"
        self.endpoints_module = "ABConnect.api.endpoints"
        self.swagger_data = self._load_swagger()
        self.api_paths = self._extract_api_paths()

    def _load_swagger(self) -> dict:
        """Load swagger.json specification."""
        with open(self.swagger_path, 'r') as f:
            return json.load(f)

    def _extract_api_paths(self) -> Dict[str, List[str]]:
        """Extract and group API paths by their prefix."""
        api_paths = {}
        for path in self.swagger_data['paths'].keys():
            parts = path.split('/')
            if len(parts) > 2:
                prefix = parts[2]  # e.g., 'companies', 'contacts', etc.
                if prefix not in api_paths:
                    api_paths[prefix] = []
                api_paths[prefix].append(path)
        return api_paths

    def check_endpoint_exists(self, endpoint_name: str) -> Tuple[bool, Optional[str]]:
        """Check if an endpoint module exists and can be imported.

        Args:
            endpoint_name: Name of the endpoint (e.g., 'companies', 'contacts')

        Returns:
            Tuple of (exists, error_message)
        """
        # Handle special cases for endpoint names
        module_name = endpoint_name

        # Map hyphenated names to underscores
        if '-' in module_name:
            module_name = module_name.replace('-', '_')

        # SmsTemplate -> SmsTemplate (case preserved)
        # Values -> Values (case preserved)

        # Check if the file exists first (doesn't require imports)
        from pathlib import Path
        endpoints_dir = Path(__file__).parent.parent.parent / "ABConnect" / "api" / "endpoints"
        module_file = endpoints_dir / f"{module_name}.py"

        if module_file.exists():
            return True, None
        else:
            return False, f"File {module_file.name} not found"

    def check_all_endpoints(self) -> Dict[str, Dict]:
        """Check all endpoints defined in swagger against implementations.

        Returns:
            Dictionary mapping endpoint names to their status and paths
        """
        results = {}

        for prefix, paths in self.api_paths.items():
            exists, error = self.check_endpoint_exists(prefix)
            results[prefix] = {
                'exists': exists,
                'error': error,
                'paths': paths,
                'path_count': len(paths)
            }

            if not exists:
                warnings.warn(
                    f"Missing endpoint implementation for '{prefix}' "
                    f"({len(paths)} paths in swagger.json)",
                    UserWarning
                )

        return results

    def get_api_path_groups(self) -> List[str]:
        """Get sorted list of API path groups."""
        return sorted(self.api_paths.keys())

    def get_paths_for_group(self, group: str) -> List[str]:
        """Get all paths for a specific API group."""
        return self.api_paths.get(group, [])


# Define the expected API path groups from swagger.json
API_PATH_GROUPS = [
    "account",
    "address",
    "admin",
    "companies",
    "company",
    "contacts",
    "dashboard",
    "documents",
    "e-sign",
    "email",
    "job",
    "jobintacct",
    "lookup",
    "note",
    "notifications",
    "reports",
    "rfq",
    "shipment",
    "smstemplate",
    "values"
]

def check_swagger_compliance(verbose=False):
    """Main function to check swagger compliance."""
    checker = SwaggerEndpointChecker()
    results = checker.check_all_endpoints()

    missing = []
    implemented = []

    for endpoint, status in sorted(results.items()):
        if status['exists']:
            implemented.append(endpoint)
        else:
            missing.append(endpoint)

    if verbose:
        print("=" * 60)
        print("SWAGGER API COMPLIANCE CHECK")
        print("=" * 60)

        for endpoint, status in sorted(results.items()):
            if status['exists']:
                print(f"✓ {endpoint}: {status['path_count']} paths")
            else:
                print(f"✗ {endpoint}: {status['path_count']} paths (MISSING)")

        print("\n" + "-" * 60)
        print(f"Summary: {len(implemented)}/{len(results)} endpoints implemented")

        if missing:
            print(f"\nMissing endpoints: {', '.join(missing)}")
            print("\nThese endpoints need manual implementation in ABConnect.api.endpoints")

    return results