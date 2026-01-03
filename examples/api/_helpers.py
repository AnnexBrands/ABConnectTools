"""Helper utilities for API examples."""

import json
from pathlib import Path

FIXTURES_DIR = Path(__file__).parent.parent.parent / "tests" / "fixtures"


def save_fixture(obj, name: str) -> bool:
    """Save a Pydantic model as a fixture if it doesn't exist.

    Args:
        obj: Pydantic model instance
        name: Fixture name (without .json extension)

    Returns:
        True if fixture was saved, False if it already exists
    """
    fixture_path = FIXTURES_DIR / f"{name}.json"
    if fixture_path.exists():
        return False

    FIXTURES_DIR.mkdir(parents=True, exist_ok=True)
    fixture_path.write_text(
        json.dumps(obj.model_dump(by_alias=True), indent=2)
    )
    print(f"Saved fixture to {fixture_path}")
    return True
