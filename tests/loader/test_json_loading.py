"""Tests for JSON file loading."""

from . import LoaderTestCase


class TestJSONLoading(LoaderTestCase):
    """Test suite for JSON file loading."""

    def test_load_simple_json(self):
        """Test loading a simple JSON file."""
        data = {"test": "data", "items": [1, 2, 3]}
        json_file = self.create_test_json("test.json", data)
        self.skipTest("FileLoader not yet imported")

    def test_load_nested_json(self):
        """Test loading nested JSON structures."""
        self.skipTest("Not yet implemented")

    def test_load_json_array(self):
        """Test loading JSON arrays."""
        self.skipTest("Not yet implemented")

    def test_load_malformed_json(self):
        """Test handling of malformed JSON files."""
        self.skipTest("Not yet implemented")