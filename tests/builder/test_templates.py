"""Tests for JSON templates used by Builder."""

from . import BuilderTestCase


class TestTemplates(BuilderTestCase):
    """Test suite for JSON templates."""

    def test_simple_request_template_exists(self):
        """Test that simple_request.json exists."""
        self.assertTrue(self.simple_request_template.exists())

    def test_extra_containers_template_exists(self):
        """Test that extra_containers.json exists."""
        self.assertTrue(self.extra_containers_template.exists())

    def test_template_structure(self):
        """Test that templates have expected structure."""
        self.skipTest("Not yet implemented")

    def test_template_validation(self):
        """Test that templates are valid JSON."""
        import json
        if self.simple_request_template.exists():
            with open(self.simple_request_template) as f:
                data = json.load(f)
                self.assertIsInstance(data, dict)