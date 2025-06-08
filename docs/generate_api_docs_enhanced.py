#!/usr/bin/env python3
"""Generate enhanced API documentation from swagger specification.

This script creates comprehensive documentation for all API endpoints
organized by swagger tags with enhanced bash examples and collapsible outputs.
"""

import json
import os
from pathlib import Path
from collections import defaultdict
import re


def sanitize_filename(name):
    """Convert tag name to valid filename."""
    # Replace spaces and special characters
    name = re.sub(r'[^\w\s-]', '', name)
    name = re.sub(r'[-\s]+', '_', name)
    return name.lower()


def sanitize_anchor(text):
    """Convert text to valid anchor name."""
    # Remove special characters and convert to lowercase
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.lower()


def format_parameter(param):
    """Format a parameter for documentation."""
    name = param.get('name', '')
    required = param.get('required', False)
    param_in = param.get('in', '')
    description = param.get('description', 'No description available')
    schema = param.get('schema', {})
    param_type = schema.get('type', 'string')
    
    required_marker = ' *(required)*' if required else ''
    return f"- `{name}` ({param_type}, {param_in}){required_marker}: {description}"


def generate_realistic_example_value(param_name, param_type='string'):
    """Generate realistic example values based on parameter name and type."""
    param_lower = param_name.lower()
    
    # ID parameters
    if 'id' in param_lower:
        if 'display' in param_lower and 'job' in param_lower:
            # Use the actual test job display ID
            return '2000000'
        elif 'job' in param_lower:
            # For other job IDs, use a generic format
            return 'JOB-2024-001'
        elif 'company' in param_lower:
            # Use the actual test company ID
            return 'ed282b80-54fe-4f42-bf1b-69103ce1f76c'
        elif 'contact' in param_lower:
            return '456e7890-e89b-12d3-a456-426614174001'
        else:
            return '789e0123-e89b-12d3-a456-426614174002'
    
    # Code parameters
    elif 'code' in param_lower:
        if 'company' in param_lower:
            # Use the actual test company code
            return 'TRAINING'
        elif 'country' in param_lower:
            return 'US'
        else:
            return 'CODE-001'
    
    # Name parameters
    elif 'name' in param_lower:
        if 'first' in param_lower:
            return 'John'
        elif 'last' in param_lower:
            return 'Doe'
        elif 'company' in param_lower:
            return 'Acme Corporation'
        else:
            return 'Example Name'
    
    # Email parameters
    elif 'email' in param_lower:
        return 'user@example.com'
    
    # Phone parameters
    elif 'phone' in param_lower:
        return '+1-555-123-4567'
    
    # Date parameters
    elif 'date' in param_lower or 'time' in param_lower:
        if 'start' in param_lower:
            return '2024-01-01T09:00:00Z'
        elif 'end' in param_lower:
            return '2024-01-31T17:00:00Z'
        else:
            return '2024-01-15T12:00:00Z'
    
    # Boolean parameters
    elif param_type == 'boolean':
        return 'true'
    
    # Number parameters
    elif param_type in ['integer', 'number']:
        if 'page' in param_lower:
            return '1'
        elif 'per_page' in param_lower or 'perpage' in param_lower:
            return '20'
        elif 'count' in param_lower:
            return '10'
        else:
            return '100'
    
    # Default
    else:
        return 'example-value'


def format_bash_example(endpoint, base_url="https://api.abconnect.co"):
    """Generate enhanced bash example for an endpoint."""
    path = endpoint['path']
    method = endpoint['method']
    params = endpoint.get('parameters', [])
    request_body = endpoint.get('requestBody', {})
    
    # Replace path parameters with example values
    example_path = path
    path_params = []
    query_params = []
    
    for param in params:
        param_name = param.get('name', '')
        param_in = param.get('in', '')
        schema = param.get('schema', {})
        param_type = schema.get('type', 'string')
        
        if param_in == 'path':
            example_value = generate_realistic_example_value(param_name, param_type)
            example_path = example_path.replace(f'{{{param_name}}}', example_value)
            path_params.append((param_name, example_value))
            
        elif param_in == 'query' and (param.get('required', False) or param_name in ['page', 'per_page', 'perPage']):
            example_value = generate_realistic_example_value(param_name, param_type)
            query_params.append(f'{param_name}={example_value}')
    
    # Build the curl command with proper formatting
    curl_lines = [f"curl -X {method} \\"]
    curl_lines.append("  -H 'Authorization: Bearer YOUR_API_TOKEN' \\")
    
    if method in ['POST', 'PUT', 'PATCH']:
        curl_lines.append("  -H 'Content-Type: application/json' \\")
        
        # Generate sample request body
        content = request_body.get('content', {})
        if 'application/json' in content:
            schema = content['application/json'].get('schema', {})
            sample_body = generate_sample_request_body(schema)
            curl_lines.append("  -d '{")
            body_lines = json.dumps(sample_body, indent=2).split('\n')
            for i, line in enumerate(body_lines[1:-1]):  # Skip first { and last }
                if i == len(body_lines) - 3:  # Last line
                    curl_lines.append(f"    {line}")
                else:
                    curl_lines.append(f"    {line}")
            curl_lines.append("  }' \\")
    
    # Add URL with query parameters
    url = f"{base_url}{example_path}"
    if query_params:
        url += "?" + "&".join(query_params)
    
    curl_lines.append(f"  '{url}'")
    curl_cmd = '\n'.join(curl_lines)
    
    # Also add ab CLI example with realistic values
    ab_cmd = f"ab api raw {method.lower()} {path}"
    if path_params:
        ab_cmd += " \\\n    "
        ab_cmd += " \\\n    ".join(f"{name}={value}" for name, value in path_params)
    if query_params:
        if path_params:
            ab_cmd += " \\\n    "
        else:
            ab_cmd += " \\\n    "
        ab_cmd += " \\\n    ".join(query_params)
    
    return curl_cmd, ab_cmd


def generate_sample_request_body(schema):
    """Generate a realistic sample request body based on schema."""
    if not schema:
        return {"example": "data"}
    
    # Common request patterns
    properties = schema.get('properties', {})
    
    sample = {}
    for prop_name, prop_schema in properties.items():
        prop_type = prop_schema.get('type', 'string')
        sample[prop_name] = generate_realistic_example_value(prop_name, prop_type)
    
    return sample if sample else {"example": "data"}


def load_response_examples():
    """Load response examples from the response_examples.json file."""
    response_examples_path = Path(__file__).parent / "api" / "response_examples.json"
    if response_examples_path.exists():
        with open(response_examples_path, 'r') as f:
            return json.load(f)
    return {}


# Global variable to store response examples
RESPONSE_EXAMPLES = None


def get_endpoint_key(path, method):
    """Generate a key for looking up response examples."""
    # Normalize path for lookup
    # Remove path parameters
    normalized_path = re.sub(r'\{[^}]+\}', '{}', path)
    
    # Common endpoint patterns
    if '/companies/{}/details' in normalized_path:
        return 'companies.get_company_details'
    elif '/companies/{}/fulldetails' in normalized_path and method == 'GET':
        return 'companies.get_company_fulldetails'
    elif '/companies/{}' in normalized_path and method == 'GET':
        return 'companies.get_company_by_id'
    elif '/companies/search' in normalized_path:
        return 'companies.get_companies_search'
    elif '/companies/availableByCurrentUser' in normalized_path:
        return 'companies.get_companies_availableByCurrentUser'
    
    # Default key based on path
    tag = path.split('/')[2] if len(path.split('/')) > 2 else 'generic'
    operation = path.split('/')[-1].replace('{', '').replace('}', '')
    return f"{tag}.{method.lower()}_{operation}"


def generate_sample_response(endpoint):
    """Generate a sample response using actual API responses when available."""
    global RESPONSE_EXAMPLES
    if RESPONSE_EXAMPLES is None:
        RESPONSE_EXAMPLES = load_response_examples()
    
    path = endpoint['path']
    method = endpoint['method']
    
    # Try to find a real response example
    endpoint_key = get_endpoint_key(path, method)
    
    # Check for exact match first
    for tag, endpoints in RESPONSE_EXAMPLES.items():
        if tag == 'generic':
            continue
        for key, example in endpoints.items():
            if example.get('endpoint') == path and example.get('method') == method:
                response = example.get('response', {})
                return json.dumps(response, indent=2)
    
    # Check for pattern match
    parts = endpoint_key.split('.')
    if len(parts) == 2:
        tag, operation = parts
        if tag in RESPONSE_EXAMPLES and operation in RESPONSE_EXAMPLES[tag]:
            response = RESPONSE_EXAMPLES[tag][operation].get('response', {})
            return json.dumps(response, indent=2)
    
    # Fallback to generic responses based on endpoint patterns
    responses = endpoint.get('responses', {})
    
    # Common response patterns based on endpoint
    if 'search' in path.lower() or (method == 'GET' and path.endswith('s')):
        # List response - check if we have a generic empty list
        if 'generic' in RESPONSE_EXAMPLES and 'empty_list' in RESPONSE_EXAMPLES['generic']:
            return json.dumps(RESPONSE_EXAMPLES['generic']['empty_list'], indent=2)
        return json.dumps([], indent=2)
    
    elif '{id}' in path or 'details' in path:
        # Single item response - check for generic empty object
        if 'generic' in RESPONSE_EXAMPLES and 'empty_object' in RESPONSE_EXAMPLES['generic']:
            return json.dumps(RESPONSE_EXAMPLES['generic']['empty_object'], indent=2)
        return json.dumps({}, indent=2)
    
    elif method == 'POST':
        # Create response
        return json.dumps({
            "id": "789e0123-e89b-12d3-a456-426614174002",
            "status": "created",
            "message": "Resource created successfully",
            "data": {
                "id": "789e0123-e89b-12d3-a456-426614174002",
                "created_at": "2024-01-20T10:00:00Z"
            }
        }, indent=2)
    
    elif method in ['PUT', 'PATCH']:
        # Update response
        return json.dumps({
            "id": "123e4567-e89b-12d3-a456-426614174000",
            "status": "updated",
            "message": "Resource updated successfully",
            "modified_at": "2024-01-20T10:00:00Z"
        }, indent=2)
    
    elif method == 'DELETE':
        # Delete response
        return json.dumps({
            "status": "success",
            "message": "Resource deleted successfully"
        }, indent=2)
    
    else:
        # Generic success response
        return json.dumps({
            "status": "success",
            "data": {
                "message": "Operation completed successfully"
            }
        }, indent=2)


def generate_tag_documentation(tag_name, endpoints, tag_description=""):
    """Generate enhanced RST documentation for a tag."""
    doc = []
    
    # Title
    title = f"{tag_name} API"
    doc.append(title)
    doc.append("=" * len(title))
    doc.append("")
    
    # Description
    if tag_description:
        doc.append(tag_description)
        doc.append("")
    
    doc.append(f"This section covers the {len(endpoints)} endpoints related to {tag_name}.")
    doc.append("")
    
    # Table of contents
    doc.append(".. contents::")
    doc.append("   :local:")
    doc.append("   :depth: 2")
    doc.append("")
    
    # Quick reference table
    doc.append("Quick Reference")
    doc.append("---------------")
    doc.append("")
    doc.append(".. list-table::")
    doc.append("   :header-rows: 1")
    doc.append("   :widths: 10 40 50")
    doc.append("")
    doc.append("   * - Method")
    doc.append("     - Endpoint")
    doc.append("     - Description")
    
    for endpoint in endpoints:
        method = endpoint['method']
        path = endpoint['path']
        summary = endpoint.get('summary', 'No summary available')
        doc.append(f"   * - {method}")
        doc.append(f"     - {path}")
        doc.append(f"     - {summary}")
    
    doc.append("")
    doc.append("Endpoints")
    doc.append("---------")
    doc.append("")
    
    # Process each endpoint
    for endpoint in endpoints:
        operation_id = endpoint.get('operationId', '')
        summary = endpoint.get('summary', 'No summary available')
        description = endpoint.get('description', '')
        path = endpoint['path']
        method = endpoint['method']
        parameters = endpoint.get('parameters', [])
        
        # Create anchor ID for cross-referencing
        anchor_id = sanitize_anchor(f"{method}-{path}")
        
        # Endpoint title with anchor
        doc.append(f".. _{anchor_id}:")
        doc.append("")
        endpoint_title = f"{method} {path}"
        doc.append(endpoint_title)
        doc.append("~" * len(endpoint_title))
        doc.append("")
        
        # Summary and description
        doc.append(f"**{summary}**")
        if description and description != summary:
            doc.append("")
            doc.append(description)
        doc.append("")
        
        # Parameters
        if parameters:
            doc.append("**Parameters:**")
            doc.append("")
            
            # Group parameters by type
            path_params = [p for p in parameters if p.get('in') == 'path']
            query_params = [p for p in parameters if p.get('in') == 'query']
            header_params = [p for p in parameters if p.get('in') == 'header']
            
            if path_params:
                doc.append("*Path Parameters:*")
                doc.append("")
                for param in path_params:
                    doc.append(format_parameter(param))
                doc.append("")
            
            if query_params:
                doc.append("*Query Parameters:*")
                doc.append("")
                for param in query_params:
                    doc.append(format_parameter(param))
                doc.append("")
            
            if header_params:
                doc.append("*Header Parameters:*")
                doc.append("")
                for param in header_params:
                    doc.append(format_parameter(param))
                doc.append("")
        
        # Request example
        doc.append("**Example Request:**")
        doc.append("")
        
        # Generate bash examples
        curl_example, ab_example = format_bash_example(endpoint)
        
        # Curl example with copy button
        doc.append("Using curl:")
        doc.append("")
        doc.append(".. code-block:: bash")
        doc.append("   :linenos:")
        doc.append("")
        for line in curl_example.split('\n'):
            doc.append(f"   {line}")
        doc.append("")
        
        # AB CLI example
        doc.append("Using AB CLI:")
        doc.append("")
        doc.append(".. code-block:: bash")
        doc.append("")
        for line in ab_example.split('\n'):
            doc.append(f"   {line}")
        doc.append("")
        
        # Sample response (collapsible)
        doc.append("**Sample Response:**")
        doc.append("")
        doc.append(".. toggle::")
        doc.append("")
        doc.append("   .. code-block:: json")
        doc.append("      :linenos:")
        doc.append("")
        
        sample_response = generate_sample_response(endpoint)
        for line in sample_response.split('\n'):
            doc.append(f"      {line}")
        doc.append("")
        
        # Add a separator between endpoints
        doc.append("----")
        doc.append("")
    
    return "\n".join(doc)


def main():
    """Generate enhanced API documentation."""
    # Load swagger specification
    swagger_path = Path(__file__).parent.parent / "ABConnect" / "base" / "swagger.json"
    with open(swagger_path, 'r') as f:
        swagger = json.load(f)
    
    # Create api directory if it doesn't exist
    api_dir = Path(__file__).parent / "api"
    api_dir.mkdir(exist_ok=True)
    
    # Group endpoints by tags
    tag_groups = defaultdict(list)
    tag_descriptions = {}
    
    # Get tag descriptions
    if 'tags' in swagger:
        for tag in swagger['tags']:
            tag_descriptions[tag['name']] = tag.get('description', '')
    
    # Group paths by tags
    for path, methods in swagger['paths'].items():
        for method, details in methods.items():
            if method in ['get', 'post', 'put', 'patch', 'delete']:
                tags = details.get('tags', ['Untagged'])
                endpoint_info = {
                    'path': path,
                    'method': method.upper(),
                    'summary': details.get('summary', ''),
                    'description': details.get('description', ''),
                    'operationId': details.get('operationId', ''),
                    'parameters': details.get('parameters', []),
                    'requestBody': details.get('requestBody', {}),
                    'responses': details.get('responses', {})
                }
                
                for tag in tags:
                    tag_groups[tag].append(endpoint_info)
    
    # Generate index file
    index_content = []
    index_content.append("API Reference")
    index_content.append("=============")
    index_content.append("")
    index_content.append("Complete API reference organized by resource type.")
    index_content.append("")
    index_content.append(".. toctree::")
    index_content.append("   :maxdepth: 2")
    index_content.append("   :caption: API Endpoints:")
    index_content.append("")
    
    # Generate documentation for each tag
    for tag in sorted(tag_groups.keys()):
        endpoints = tag_groups[tag]
        description = tag_descriptions.get(tag, '')
        
        # Generate documentation
        doc_content = generate_tag_documentation(tag, endpoints, description)
        
        # Save to file
        filename = sanitize_filename(tag)
        filepath = api_dir / f"{filename}.rst"
        with open(filepath, 'w') as f:
            f.write(doc_content)
        
        # Add to index
        index_content.append(f"   {filename}")
        
        print(f"Generated enhanced documentation for {tag} ({len(endpoints)} endpoints)")
    
    # Save index file
    index_path = api_dir / "index.rst"
    with open(index_path, 'w') as f:
        f.write("\n".join(index_content))
    
    print(f"\nGenerated enhanced documentation for {len(tag_groups)} tags")
    print(f"Documentation saved in: {api_dir}")


if __name__ == "__main__":
    main()