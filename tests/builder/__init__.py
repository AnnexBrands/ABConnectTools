"""Tests for ABConnect.Builder module."""

from ..base_test import ABConnectTestCase


class BuilderTestCase(ABConnectTestCase):
    """Base test class for Builder tests.

    Provides builder-specific test helpers.
    """

    @classmethod
    def setUpClass(cls):
        """Set up test class with builder resources."""
        super().setUpClass()
        cls.templates_dir = cls.project_root / "ABConnect" / "base"
        cls.simple_request_template = cls.templates_dir / "simple_request.json"
        cls.extra_containers_template = cls.templates_dir / "extra_containers.json"

    def load_template(self, template_name: str) -> dict:
        """Load a JSON template."""
        import json
        template_path = self.templates_dir / f"{template_name}.json"
        if template_path.exists():
            with open(template_path) as f:
                return json.load(f)
        return {}

    def assert_path_updated(self, data: dict, path: str, value):
        """Assert that a nested path in data has the expected value."""
        parts = path.split('.')
        current = data
        for part in parts[:-1]:
            self.assertIn(part, current)
            current = current[part]
        self.assertIn(parts[-1], current)
        self.assertEqual(current[parts[-1]], value)