import io
from enum import Enum
from importlib import resources
import json
from pathlib import Path
import requests
from typing import Any, Dict, List, Optional, Union

from .config import Config


def load_json_resource(filename: str) -> Any:
    """
    Loads a JSON file from the package's 'base' directory using importlib.resources.

    Args:
        filename (str): The JSON file name.

    Returns:
        The parsed JSON object.
    """
    with resources.open_text("ABConnect.base", filename) as f:
        return json.load(f)

                                                                                                                
                                                                                                                
def sync_swagger() -> bool:
    """Sync local swagger.json with server version.
                                                                                                                
    Returns:
        bool: True if updated, False if already current
    """
    config = Config()
    swagger_url = config.get_swagger_url()
    local_path = Path(__file__).parent / "base" / "swagger.json"
                                                                                                                
    response = requests.get(swagger_url, timeout=30)
    response.raise_for_status()
    remote_swagger = response.json()
                                                                                                                
    if local_path.exists():
        with open(local_path, 'r') as f:
            local_swagger = json.load(f)
        if local_swagger == remote_swagger:
            return False
                                                                                                                
    with open(local_path, 'w') as f:
        json.dump(remote_swagger, f, indent=2)
                                                                                                                
    return True

def to_file_dict(response, job: int, form_name: str, filetype: str = "pdf") -> dict:
    file_name = f"{job}_{form_name}.{filetype}"
    bytes = io.BytesIO(response.content)
    return {file_name: bytes.getvalue()}

