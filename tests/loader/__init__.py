"""Tests for ABConnect.Loader module."""

from ..base_test import ABConnectTestCase
from pathlib import Path
import tempfile
import os


class LoaderTestCase(ABConnectTestCase):
    """Base test class for Loader tests.

    Provides loader-specific test helpers.
    """

    @classmethod
    def setUpClass(cls):
        """Set up test class with loader resources."""
        super().setUpClass()
        cls.loader_module_path = cls.project_root / "ABConnect" / "Loader.py"
        cls.test_data_dir = cls.project_root / "tests" / "test_data"

    def setUp(self):
        """Set up each test with temporary directory."""
        super().setUp()
        self.temp_dir = tempfile.mkdtemp()

    def tearDown(self):
        """Clean up temporary files."""
        import shutil
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)
        super().tearDown()

    def create_test_csv(self, filename: str, data: list) -> Path:
        """Create a test CSV file."""
        import csv
        file_path = Path(self.temp_dir) / filename
        with open(file_path, 'w', newline='') as f:
            if data:
                writer = csv.DictWriter(f, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)
        return file_path

    def create_test_json(self, filename: str, data: dict) -> Path:
        """Create a test JSON file."""
        import json
        file_path = Path(self.temp_dir) / filename
        with open(file_path, 'w') as f:
            json.dump(data, f)
        return file_path

    def create_test_xlsx(self, filename: str, data: list) -> Path:
        """Create a test XLSX file."""
        try:
            import pandas as pd
            file_path = Path(self.temp_dir) / filename
            df = pd.DataFrame(data)
            df.to_excel(file_path, index=False)
            return file_path
        except ImportError:
            self.skipTest("pandas not available for XLSX testing")

    def assert_loaded_data(self, data, expected_rows: int = None):
        """Assert that loaded data has expected structure."""
        self.assertIsNotNone(data)
        if expected_rows is not None:
            self.assertEqual(len(data), expected_rows)