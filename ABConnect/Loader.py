import os
import json
import codecs
import logging
import chardet
import pandas as pd
import openpyxl
from bs4 import BeautifulSoup
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)


class FileLoader:
    """
    Loads data from CSV, JSON, or XLSX files while handling unsupported characters.

    Attributes:
        file_path (str): The path to the file.
        key (Optional[str]): Key to convert data into a dictionary form.
        data (List[Dict[str, Any]]): The loaded data.
    """

    def __init__(
        self, file_path: str, key: Optional[str] = None, interactive: bool = True
    ):
        self.file_path = file_path
        self.key = key
        self.data: List[Dict[str, Any]] = []
        self.interactive = interactive
        self.load()

    def load(self) -> None:
        file_extension = os.path.splitext(self.file_path)[1].lower()
        if file_extension == ".csv":
            self._read_csv()
        elif file_extension == ".json":
            self._read_json()
        elif file_extension in [".xlsx", ".xls"]:
            self._read_xlsx()
        else:
            raise ValueError(f"Unsupported file type: {file_extension}")

    def _read_csv(self) -> None:
        with open(self.file_path, "rb") as file:
            raw_data = file.read(10000)
            detected = chardet.detect(raw_data)

        encodings_to_try = [
            detected.get("encoding"),
            "utf-8",
            "utf-8-sig",
            "cp1252",
            "latin1",
            "iso-8859-1",
            "mbcs",
        ]

        results = []

        for encoding in encodings_to_try:
            if not encoding:
                continue
            try:
                # Read up to 5 lines (handle files with fewer than 5 lines)
                with codecs.open(self.file_path, "r", encoding=encoding) as f:
                    sample_lines = []
                    for _ in range(5):
                        try:
                            sample_lines.append(next(f))
                        except StopIteration:
                            break
                df = pd.read_csv(self.file_path, encoding=encoding, na_filter=False)
                df = df.fillna("")

                results.append(
                    {"encoding": encoding, "sample_lines": sample_lines, "df": df}
                )

                print(f"Successfully read file with encoding: {encoding}")
            except Exception as e:
                print(f"Error reading file with encoding {encoding}: {str(e)}")
                continue

        if not results:
            raise ValueError("Unable to read file with any encoding")

        # Select the first successful result if not interactive
        if self.interactive:
            print("\nAvailable Encodings:")
            for i, result in enumerate(results):
                print(f"{i}: {result['encoding']}")
                for line in result["sample_lines"]:
                    print(line.strip())
                print("-" * 40)
            choice = input(
                "\nEnter the number of the best encoding (or press Enter for the first successful one): "
            )
            chosen_result = results[int(choice)] if choice.strip() else results[0]
        else:
            chosen_result = results[0]

        df = chosen_result["df"]

        def clean_text(text):
            if pd.isna(text):
                return text
            text = str(text)
            replacements = {
                "Ã©": "é",
                "Ã¨": "è",
                "Ã¢": "â",
                "Ã": "à",
                "Å": "œ",
                "\x92": "'",
                "\x93": '"',
                "\x94": '"',
                "\ufeff": "",  # Remove BOM
            }
            for bad, good in replacements.items():
                text = text.replace(bad, good)
            soup = BeautifulSoup(text, "html.parser")
            return " ".join(soup.get_text().split()).strip()

        if "title" in df.columns:
            df["title"] = df["title"].apply(clean_text)

        self.df = df
        self.data = df.to_dict("records")

    def _read_json(self) -> None:
        with open(self.file_path, "r") as jsonfile:
            self.data = json.load(jsonfile)

    def _read_xlsx(self) -> None:
        workbook = openpyxl.load_workbook(self.file_path)
        sheet = workbook.active
        headers = [cell.value for cell in sheet[1]]
        self.data = []
        for row in sheet.iter_rows(min_row=2, values_only=True):
            self.data.append(dict(zip(headers, row)))

    def to_list(self) -> List[Dict[str, Any]]:
        """Returns the loaded data as a list of dictionaries."""
        return self.data

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the loaded data into a dictionary using self.key for keys.

        Raises:
            KeyError: If self.key is not found in a row.
        """
        if isinstance(self.data, dict):
            return self.data
        result = {}
        for row in self.data:
            if self.key not in row:
                raise KeyError(f"Key '{self.key}' not found in row: {row}")
            key_value = row.pop(self.key)
            if key_value in result:
                if isinstance(result[key_value], list):
                    result[key_value].append(row)
                else:
                    result[key_value] = [result[key_value], row]
            else:
                result[key_value] = row
        return result
