import os
import tempfile
import unittest
import json
from openpyxl import Workbook

from ABConnect import FileLoader

class TestFileLoader(unittest.TestCase):
    def test_csv_loading(self):
        csv_content = "title,description\nTest Title,This is a test."
        with tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False) as tmp:
            tmp.write(csv_content)
            tmp_path = tmp.name
        try:
            loader = FileLoader(tmp_path, interactive=False)
            data = loader.to_list()
            self.assertEqual(len(data), 1)
            self.assertEqual(data[0]["title"], "Test Title")
            self.assertEqual(data[0]["description"], "This is a test.")
        finally:
            os.remove(tmp_path)

    def test_json_loading(self):
        json_data = {"key": "value", "list": [1, 2, 3]}
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as tmp:
            json.dump(json_data, tmp)
            tmp_path = tmp.name
        try:
            loader = FileLoader(tmp_path, interactive=False)
            self.assertEqual(loader.data, json_data)
        finally:
            os.remove(tmp_path)

    def test_xlsx_loading(self):
        # Create a temporary XLSX file using openpyxl
        tmp_path = tempfile.mktemp(suffix=".xlsx")
        workbook = Workbook()
        sheet = workbook.active
        # Write header row and one data row
        sheet.append(["header1", "header2"])
        sheet.append(["value1", "value2"])
        workbook.save(tmp_path)
        try:
            loader = FileLoader(tmp_path, interactive=False)
            data = loader.to_list()
            self.assertEqual(len(data), 1)
            self.assertEqual(data[0]["header1"], "value1")
            self.assertEqual(data[0]["header2"], "value2")
        finally:
            os.remove(tmp_path)

if __name__ == "__main__":
    unittest.main()
