#!/usr/bin/env python3
"""Generate schema_mappings.py from ACPortal_709_swagger.json.

This script parses the OpenAPI 3.0 swagger specification and extracts
request body and response schema mappings for all endpoints.

Usage:
    python generate_schema_mappings.py
"""

import json
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any


def extract_schema_ref(schema: Dict[str, Any]) -> Optional[str]:
    """Extract model name from schema reference.

    Args:
        schema: OpenAPI schema object

    Returns:
        Model name or None if no reference found
    """
    ref = schema.get('$ref', '')
    if ref:
        return ref.split('/')[-1]
    return None


def is_array_response(schema: Dict[str, Any]) -> bool:
    """Check if schema represents an array response.

    Args:
        schema: OpenAPI schema object

    Returns:
        True if schema is an array type
    """
    return schema.get('type') == 'array'


def get_array_item_ref(schema: Dict[str, Any]) -> Optional[str]:
    """Get the model name for array item schema.

    Args:
        schema: OpenAPI schema object with type=array

    Returns:
        Model name of array items or None
    """
    items = schema.get('items', {})
    return extract_schema_ref(items)


def parse_swagger(swagger_path: Path) -> Tuple[Dict, Dict]:
    """Parse swagger file and extract request/response mappings.

    Args:
        swagger_path: Path to swagger JSON file

    Returns:
        Tuple of (request_mappings, response_mappings)
    """
    with open(swagger_path, 'r') as f:
        swagger = json.load(f)

    request_mappings = {}
    response_mappings = {}

    for path, methods in swagger.get('paths', {}).items():
        for method, details in methods.items():
            if method not in ['get', 'post', 'put', 'delete', 'patch']:
                continue

            method_upper = method.upper()

            # Extract request body schema (OpenAPI 3.x format)
            request_body = details.get('requestBody', {})
            content = request_body.get('content', {})
            json_content = content.get('application/json', {})
            req_schema = json_content.get('schema', {})

            req_model = extract_schema_ref(req_schema)
            if req_model:
                request_mappings[(method_upper, path)] = req_model

            # Extract response schema (200 response)
            responses = details.get('responses', {})
            resp_200 = responses.get('200', {})
            resp_content = resp_200.get('content', {})
            resp_json = resp_content.get('application/json', {})
            resp_schema = resp_json.get('schema', {})

            if is_array_response(resp_schema):
                # Array response - wrap in list
                item_model = get_array_item_ref(resp_schema)
                if item_model:
                    response_mappings[(method_upper, path)] = [item_model]
            else:
                resp_model = extract_schema_ref(resp_schema)
                if resp_model:
                    response_mappings[(method_upper, path)] = resp_model

    return request_mappings, response_mappings


def generate_python_code(request_mappings: Dict, response_mappings: Dict) -> str:
    """Generate Python code for schema_mappings.py.

    Args:
        request_mappings: Dict of (method, path) -> model_name
        response_mappings: Dict of (method, path) -> model_name or [model_name]

    Returns:
        Python source code as string
    """
    lines = [
        '"""Schema mappings auto-generated from ACPortal_709_swagger.json.',
        '',
        'DO NOT EDIT MANUALLY - regenerate with:',
        '    python generate_schema_mappings.py',
        '',
        'This module provides mappings from API endpoints to their corresponding',
        'Pydantic model names for request validation and response casting.',
        '"""',
        '',
        'from typing import Dict, List, Tuple, Union',
        '',
        '',
        '# Request body schema mappings',
        '# Format: (HTTP_METHOD, path_pattern) -> model_name',
        'REQUEST_MAPPINGS: Dict[Tuple[str, str], str] = {',
    ]

    # Sort for consistent output
    for (method, path), model in sorted(request_mappings.items()):
        lines.append(f"    ('{method}', '{path}'): '{model}',")

    lines.extend([
        '}',
        '',
        '',
        '# Response schema mappings',
        '# Format: (HTTP_METHOD, path_pattern) -> model_name or [model_name] for arrays',
        'RESPONSE_MAPPINGS: Dict[Tuple[str, str], Union[str, List[str]]] = {',
    ])

    for (method, path), model in sorted(response_mappings.items()):
        if isinstance(model, list):
            lines.append(f"    ('{method}', '{path}'): {model},")
        else:
            lines.append(f"    ('{method}', '{path}'): '{model}',")

    lines.extend([
        '}',
        '',
        '',
        '# All models referenced in mappings (for validation)',
        'ALL_REFERENCED_MODELS = set()',
        'for model in REQUEST_MAPPINGS.values():',
        '    ALL_REFERENCED_MODELS.add(model)',
        'for model in RESPONSE_MAPPINGS.values():',
        '    if isinstance(model, list):',
        '        ALL_REFERENCED_MODELS.update(model)',
        '    else:',
        '        ALL_REFERENCED_MODELS.add(model)',
        '',
    ])

    return '\n'.join(lines)


def main():
    """Main entry point."""
    # Paths
    base_dir = Path(__file__).parent
    swagger_path = base_dir / 'ABConnect' / 'base' / 'ACPortal_709_swagger.json'
    output_path = base_dir / 'ABConnect' / 'api' / 'schema_mappings.py'

    print(f"Parsing swagger from: {swagger_path}")
    request_mappings, response_mappings = parse_swagger(swagger_path)

    print(f"Found {len(request_mappings)} request mappings")
    print(f"Found {len(response_mappings)} response mappings")

    # Generate Python code
    code = generate_python_code(request_mappings, response_mappings)

    # Write output
    output_path.write_text(code)
    print(f"Generated: {output_path}")

    # Summary
    print("\nSummary:")
    print(f"  Request models: {len(set(request_mappings.values()))}")
    print(f"  Response models: {len(set(str(v) for v in response_mappings.values()))}")


if __name__ == '__main__':
    main()
