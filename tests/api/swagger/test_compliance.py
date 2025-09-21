"""Test swagger API compliance."""

try:
    import pytest
    HAS_PYTEST = True
except ImportError:
    HAS_PYTEST = False

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from base_test import ABConnectTestCase
from . import SwaggerEndpointChecker, check_swagger_compliance


def test_all_endpoints_can_be_imported():
    """Test that all endpoints defined in __init__.py can be imported."""
    checker = SwaggerEndpointChecker()
    results = checker.check_all_endpoints()

    # Check known implemented endpoints
    implemented = ['account', 'address', 'companies', 'contacts',
                   'documents', 'users']

    for endpoint in implemented:
        if endpoint in results:
            assert results[endpoint]['exists'], f"Expected {endpoint} to be importable"


def test_swagger_path_groups_extracted():
    """Test that we can extract API path groups from swagger."""
    checker = SwaggerEndpointChecker()
    groups = checker.get_api_path_groups()

    # Should have multiple API groups
    assert len(groups) > 0

    # Check some expected groups exist
    expected = ['account', 'companies', 'contacts', 'documents']
    for group in expected:
        assert group in groups, f"Expected {group} in API path groups"


def test_missing_endpoints_warning():
    """Test that missing endpoints generate warnings."""
    if HAS_PYTEST:
        with pytest.warns(UserWarning):
            checker = SwaggerEndpointChecker()
            results = checker.check_all_endpoints()

            # Some endpoints will be missing
            missing = [k for k, v in results.items() if not v['exists']]
            assert len(missing) > 0, "Expected some missing endpoints"
    else:
        # Run without pytest
        import warnings
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            checker = SwaggerEndpointChecker()
            results = checker.check_all_endpoints()

            # Some endpoints will be missing
            missing = [k for k, v in results.items() if not v['exists']]
            assert len(missing) > 0, "Expected some missing endpoints"
            assert len(w) > 0, "Expected warnings"


def test_compliance_check_output(capsys):
    """Test the compliance check output format."""
    results = check_swagger_compliance(verbose=True)
    captured = capsys.readouterr()

    # Should have header
    assert "SWAGGER API COMPLIANCE CHECK" in captured.out

    # Should show summary
    assert "Summary:" in captured.out

    # Should indicate missing endpoints if any
    if any(not v['exists'] for v in results.values()):
        assert "Missing endpoints:" in captured.out


def test_compliance_report():
    """Generate a compliance report showing missing endpoints."""
    results = check_swagger_compliance()

    missing_count = sum(1 for v in results.values() if not v['exists'])
    total_count = len(results)

    print(f"\n📊 Swagger Compliance: {total_count - missing_count}/{total_count} endpoints implemented")

    if missing_count > 0:
        print(f"⚠️  {missing_count} endpoints need implementation")
        missing = [k for k, v in results.items() if not v['exists']]
        for endpoint in missing[:5]:  # Show first 5
            print(f"   - {endpoint}: {results[endpoint]['path_count']} paths")
        if len(missing) > 5:
            print(f"   ... and {len(missing) - 5} more")


class TestSwaggerCompliance(ABConnectTestCase):
    """Test swagger compliance using base test standards."""

    def test_all_endpoints_have_files(self):
        """Test that all swagger endpoints have implementation files."""
        checker = SwaggerEndpointChecker()
        results = checker.check_all_endpoints()

        missing = [k for k, v in results.items() if not v['exists']]
        self.assertEqual(len(missing), 0,
                        f"Missing endpoint files: {', '.join(missing)}")

    def test_endpoint_coverage(self):
        """Test endpoint coverage metrics."""
        checker = SwaggerEndpointChecker()
        results = checker.check_all_endpoints()

        total = len(results)
        implemented = sum(1 for v in results.values() if v['exists'])
        coverage = (implemented / total * 100) if total > 0 else 0

        self.assertGreaterEqual(coverage, 100.0,
                               f"Endpoint coverage is {coverage:.1f}% (expected 100%)")

    def test_no_orphaned_endpoints(self):
        """Test that no endpoint files exist without swagger definitions."""
        checker = SwaggerEndpointChecker()
        swagger_endpoints = set(checker.get_api_path_groups())

        # Normalize names
        swagger_endpoints = {e.replace('-', '_') for e in swagger_endpoints}

        # Check actual endpoint files
        endpoints_dir = self.endpoints_dir
        actual_files = [f.stem for f in endpoints_dir.glob("*.py")
                       if f.stem not in ['__init__', 'base']]

        orphaned = [f for f in actual_files if f not in swagger_endpoints
                   and f not in ['SmsTemplate', 'Values', 'users', 'v2', 'v3', 'views', 'webhooks']]

        self.assertEqual(len(orphaned), 0,
                        f"Orphaned endpoint files (not in swagger): {', '.join(orphaned)}")


if __name__ == "__main__":
    # Run compliance check when module is executed
    import sys
    if "--verbose" in sys.argv:
        check_swagger_compliance(verbose=True)
    else:
        test_compliance_report()