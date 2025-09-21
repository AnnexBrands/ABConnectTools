"""Tests for FileLoader main class."""

from . import LoaderTestCase
from ABConnect import FileLoader


class TestFileLoader(LoaderTestCase):
    """Test suite for FileLoader class."""

    def test_loader_initialization(self):
        """Test loader initialization."""
        # Test with a simple CSV file
        data = [{"title": "Test", "description": "Test description"}]
        csv_file = self.create_test_csv("test.csv", data)

        loader = FileLoader(str(csv_file), interactive=False)
        self.assertIsNotNone(loader)

    def test_csv_loading(self):
        """Test CSV file loading."""
        csv_content_data = [
            {"title": "Test Title", "description": "This is a test."}
        ]
        csv_file = self.create_test_csv("test.csv", csv_content_data)

        loader = FileLoader(str(csv_file), interactive=False)
        data = loader.to_list()

        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["title"], "Test Title")
        self.assertEqual(data[0]["description"], "This is a test.")

    def test_json_loading(self):
        """Test JSON file loading."""
        json_data = {"key": "value", "list": [1, 2, 3]}
        json_file = self.create_test_json("test.json", json_data)

        loader = FileLoader(str(json_file), interactive=False)
        self.assertEqual(loader.data, json_data)

    def test_xlsx_loading(self):
        """Test XLSX file loading."""
        try:
            data = [
                {"header1": "value1", "header2": "value2"}
            ]
            xlsx_file = self.create_test_xlsx("test.xlsx", data)

            loader = FileLoader(str(xlsx_file), interactive=False)
            loaded_data = loader.to_list()

            self.assertEqual(len(loaded_data), 1)
            self.assertEqual(loaded_data[0]["header1"], "value1")
            self.assertEqual(loaded_data[0]["header2"], "value2")
        except ImportError:
            self.skipTest("openpyxl not available for XLSX testing")

    def test_encoding_detection(self):
        """Test automatic encoding detection."""
        self.skipTest("Not yet implemented - requires chardet testing")

    def test_unsupported_character_handling(self):
        """Test handling of unsupported characters."""
        self.skipTest("Not yet implemented")

    def test_interactive_mode(self):
        """Test interactive mode functionality."""
        # Interactive mode is hard to test in unit tests
        self.skipTest("Interactive mode requires user input")

    def test_file_format_detection(self):
        """Test automatic file format detection."""
        # Test CSV detection
        csv_data = [{"test": "data"}]
        csv_file = self.create_test_csv("test.csv", csv_data)
        loader = FileLoader(str(csv_file), interactive=False)
        self.assertIsNotNone(loader.data)

        # Test JSON detection
        json_data = {"test": "data"}
        json_file = self.create_test_json("test.json", json_data)
        loader = FileLoader(str(json_file), interactive=False)
        self.assertEqual(loader.data, json_data)