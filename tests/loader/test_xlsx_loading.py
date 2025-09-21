"""Tests for XLSX file loading."""

from . import LoaderTestCase


class TestXLSXLoading(LoaderTestCase):
    """Test suite for XLSX file loading."""

    def test_load_simple_xlsx(self):
        """Test loading a simple XLSX file."""
        data = [
            {"name": "John", "age": 30, "city": "New York"},
            {"name": "Jane", "age": 25, "city": "Los Angeles"}
        ]
        try:
            xlsx_file = self.create_test_xlsx("test.xlsx", data)
            self.skipTest("FileLoader not yet imported")
        except ImportError:
            self.skipTest("pandas not available")

    def test_load_xlsx_multiple_sheets(self):
        """Test loading XLSX with multiple sheets."""
        self.skipTest("Not yet implemented")

    def test_load_xlsx_with_formulas(self):
        """Test loading XLSX files with formulas."""
        self.skipTest("Not yet implemented")

    def test_load_xlsx_with_formatting(self):
        """Test loading XLSX files with cell formatting."""
        self.skipTest("Not yet implemented")