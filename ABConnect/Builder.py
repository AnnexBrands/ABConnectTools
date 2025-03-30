from copy import deepcopy
from typing import Any, Dict, List, Optional, Union
from ABConnect.common import load_json_resource


class APIRequestBuilder:
    """
    Builder for API requests using static JSON configurations.
    """

    def __init__(
        self, req_type: str = "Regular", base_data: Optional[Dict[str, Any]] = None
    ):
        if base_data:
            self.data = deepcopy(base_data)
        elif req_type == "3PL":
            base = load_json_resource("simple_request.json")
            extracontainers = load_json_resource("extra_containers.json")
            self.data = {**base, **extracontainers}
        else:
            self.data = load_json_resource("simple_request.json")
        self.transformations = {}

    def load(self, base_data: Dict[str, Any]) -> "APIRequestBuilder":
        """
        Loads new base data into the builder.
        """
        self.data = deepcopy(base_data)
        return self

    def update(self, path: Union[str, List[str]], value: Any) -> "APIRequestBuilder":
        """
        Updates a nested dictionary or list structure by setting a value at the specified path.

        Args:
            path (Union[str, List[str]]): Dot-separated keys or list of keys/indexes.
            value (Any): The value to set.

        Returns:
            APIRequestBuilder: The updated instance.
        """
        if isinstance(path, str):
            path = path.split(".")

        current = self.data
        for i, key in enumerate(path[:-1]):
            if key.isdigit():
                key = int(key)
                if not isinstance(current, list):
                    current = []
                    self._set_nested_value(self.data, path[:i], current)
                while len(current) <= key:
                    current.append({})
            elif key not in current or not isinstance(current[key], (dict, list)):
                current[key] = {}
            current = current[key]

        last_key = path[-1]
        if last_key.isdigit():
            last_key = int(last_key)
            if not isinstance(current, list):
                current = []
                self._set_nested_value(self.data, path[:-1], current)
            while len(current) <= last_key:
                current.append({})
            if isinstance(value, dict) and isinstance(current[last_key], dict):
                current[last_key].update(value)
            else:
                current[last_key] = value
        else:
            if isinstance(value, dict) and isinstance(current.get(last_key), dict):
                current.setdefault(last_key, {}).update(value)
            else:
                current[last_key] = value

        return self

    def _set_nested_value(
        self, data: Dict[str, Any], path: List[str], value: Any
    ) -> None:
        """
        Sets a nested value in a dictionary based on a list of keys.
        """
        for key in path[:-1]:
            if key.isdigit():
                key = int(key)
                data = data.setdefault(key, {})
            else:
                data = data.setdefault(key, {})
        last_key = path[-1]
        if last_key.isdigit():
            last_key = int(last_key)
        data[last_key] = value

    def build(self) -> Dict[str, Any]:
        """
        Returns the built API request data.
        """
        return self.data
