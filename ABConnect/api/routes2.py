"""Auto-generated route definitions from swagger.json specification.

This module generates Route objects for all API endpoints discovered
in the OpenAPI specification, with proper request/response model mappings.
"""

import re
from typing import Dict, List, Optional, Tuple, Union

from .routes import Route
from .schema_mappings import REQUEST_MAPPINGS, RESPONSE_MAPPINGS
from .swagger import SwaggerParser


def _path_to_route_name(method: str, path: str) -> str:
    """Convert API path to route name.

    Examples:
        GET /api/contacts/{id} -> GET_CONTACTS_BY_ID
        POST /api/job/{jobDisplayId}/parcelitems -> POST_JOB_PARCELITEMS
        GET /api/job/{jobDisplayId}/parcelitems -> GET_JOB_PARCELITEMS
    """
    # Remove /api prefix
    clean_path = path.replace('/api/', '').replace('/api', '')

    # Split path into parts
    parts = clean_path.strip('/').split('/')

    # Process each part
    name_parts = [method.upper()]
    for part in parts:
        if part.startswith('{') and part.endswith('}'):
            # Path parameter - skip or add BY_ID indicator for final params
            continue
        else:
            # Convert camelCase/kebab-case to UPPER_SNAKE_CASE
            part = re.sub(r'[-]', '_', part)
            part = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', part)
            name_parts.append(part.upper())

    return '_'.join(name_parts)


def _normalize_path(path: str) -> str:
    """Normalize path by removing /api prefix for Route storage."""
    if path.startswith('/api/'):
        return path[4:]  # Remove '/api' prefix, keep leading slash
    return path


def _get_response_model(method: str, path: str) -> Optional[str]:
    """Get response model name from RESPONSE_MAPPINGS."""
    key = (method.upper(), path)
    model = RESPONSE_MAPPINGS.get(key)
    if model is None:
        return None
    if isinstance(model, list):
        return f"List[{model[0]}]"
    return model


def _get_request_model(method: str, path: str) -> Optional[str]:
    """Get request model name from REQUEST_MAPPINGS."""
    key = (method.upper(), path)
    return REQUEST_MAPPINGS.get(key)


def generate_schema() -> Dict[str, Route]:
    """Generate SCHEMA dict from swagger.json specification."""
    parser = SwaggerParser()
    endpoints = parser.get_endpoints()

    schema = {}

    for endpoint in endpoints:
        route_name = _path_to_route_name(endpoint.method, endpoint.path)

        # Get models from mappings
        request_model = _get_request_model(endpoint.method, endpoint.path)
        response_model = _get_response_model(endpoint.method, endpoint.path)

        # Normalize path (remove /api prefix)
        normalized_path = _normalize_path(endpoint.path)

        # Create Route
        route = Route(
            method=endpoint.method,
            path=normalized_path,
            request_model=request_model,
            response_model=response_model,
            params={}
        )

        schema[route_name] = route

    return schema


# Generate the schema at module load time
SCHEMA = generate_schema()


__all__ = ["SCHEMA", "generate_schema"]
