"""Helper utilities for API examples."""

import io
import json
from pathlib import Path

FIXTURES_DIR = Path(__file__).parent.parent.parent / "tests" / "fixtures"


def save_fixture(obj, name: str) -> bool:
    """Save a Pydantic model or dict as a fixture if it doesn't exist.

    Args:
        obj: Pydantic model instance or dict/list
        name: Fixture name (without .json extension)

    Returns:
        True if fixture was saved, False if it already exists
    """
    fixture_path = FIXTURES_DIR / f"{name}.json"
    if fixture_path.exists():
        return False

    FIXTURES_DIR.mkdir(parents=True, exist_ok=True)
    if hasattr(obj, 'model_dump'):
        data = obj.model_dump(by_alias=True)
    else:
        data = obj
    fixture_path.write_text(json.dumps(data, indent=2))
    print(f"Saved fixture to {fixture_path}")
    return True


def save_pdf_fixture(data: bytes, name: str) -> bool:
    """Save PDF bytes as a fixture if it doesn't exist.

    Args:
        data: PDF bytes
        name: Fixture name (without .pdf extension)

    Returns:
        True if fixture was saved, False if it already exists
    """
    fixture_path = FIXTURES_DIR / f"{name}.pdf"
    if fixture_path.exists():
        return False

    FIXTURES_DIR.mkdir(parents=True, exist_ok=True)
    fixture_path.write_bytes(data)
    print(f"Saved PDF fixture to {fixture_path}")
    return True


def is_valid_pdf(data: bytes) -> bool:
    """Check if bytes represent a valid PDF using pypdf.

    Args:
        data: Bytes to validate

    Returns:
        True if valid PDF, False otherwise
    """
    try:
        from pypdf import PdfReader
        reader = PdfReader(io.BytesIO(data))
        # Check we can read at least some metadata
        return len(reader.pages) >= 0
    except Exception:
        return False


def validate_pdf(data: bytes, name: str = "PDF") -> None:
    """Validate PDF bytes and raise AssertionError if invalid.

    Args:
        data: Bytes to validate
        name: Name for error messages

    Raises:
        AssertionError: If data is not valid PDF
    """
    assert isinstance(data, bytes), f"{name} should be bytes, got {type(data)}"
    assert len(data) > 0, f"{name} should not be empty"
    assert data[:4] == b'%PDF', f"{name} should start with PDF magic bytes"
    assert is_valid_pdf(data), f"{name} is not a valid PDF"
