#!/usr/bin/env python3
"""Generate enhanced API documentation from swagger specification.

This script creates comprehensive documentation for all API endpoints
organized by swagger tags with tabbed examples and descriptions.
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
            return '2000000'
        elif 'job' in param_lower:
            return 'JOB-2024-001'
        elif 'company' in param_lower:
            return 'ed282b80-54fe-4f42-bf1b-69103ce1f76c'
        elif 'contact' in param_lower:
            return '456e7890-e89b-12d3-a456-426614174001'
        else:
            return '789e0123-e89b-12d3-a456-426614174002'
    
    # Code parameters
    elif 'code' in param_lower:
        if 'company' in param_lower:
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


def format_python_example(endpoint):
    """Generate Python code example for an endpoint."""
    path = endpoint['path']
    method = endpoint['method']
    params = endpoint.get('parameters', [])
    request_body = endpoint.get('requestBody', {})
    
    # Build the code
    code_lines = []
    
    # Import statement
    code_lines.append("from ABConnect import ABConnectAPI")
    code_lines.append("")
    code_lines.append("# Initialize the API client")
    code_lines.append("api = ABConnectAPI()")
    code_lines.append("")
    
    # Prepare parameters
    path_params = []
    query_params = []
    
    for param in params:
        param_name = param.get('name', '')
        param_in = param.get('in', '')
        schema = param.get('schema', {})
        param_type = schema.get('type', 'string')
        
        if param_in == 'path':
            example_value = generate_realistic_example_value(param_name, param_type)
            path_params.append((param_name, example_value))
        elif param_in == 'query' and (param.get('required', False) or param_name in ['page', 'per_page', 'perPage']):
            example_value = generate_realistic_example_value(param_name, param_type)
            query_params.append((param_name, example_value))
    
    # Build the API call
    code_lines.append("# Make the API call")
    code_lines.append(f"response = api.raw.{method.lower()}(")
    code_lines.append(f'    "{path}"')
    
    # Add path parameters
    for param_name, value in path_params:
        if param_type == 'string':
            code_lines.append(f',\n    {param_name}="{value}"')
        else:
            code_lines.append(f',\n    {param_name}={value}')
    
    # Add query parameters
    for param_name, value in query_params:
        if param_type == 'string':
            code_lines.append(f',\n    {param_name}="{value}"')
        else:
            code_lines.append(f',\n    {param_name}={value}')
    
    # Add request body for POST/PUT/PATCH
    if method in ['POST', 'PUT', 'PATCH']:
        content = request_body.get('content', {})
        if 'application/json' in content:
            schema = content['application/json'].get('schema', {})
            sample_body = generate_sample_request_body(schema)
            code_lines.append(',\n    data=')
            body_lines = json.dumps(sample_body, indent=8).split('\n')
            for i, line in enumerate(body_lines):
                if i == 0:
                    code_lines.append(f'    {line}')
                else:
                    code_lines.append(line)
    
    code_lines.append("\n)")
    code_lines.append("")
    code_lines.append("# Process the response")
    code_lines.append("print(response)")
    
    return '\n'.join(code_lines)


def format_cli_example(endpoint):
    """Generate AB CLI example for an endpoint."""
    path = endpoint['path']
    method = endpoint['method']
    params = endpoint.get('parameters', [])
    
    # Build the command
    cmd_parts = [f"ab api raw {method.lower()} {path}"]
    
    path_params = []
    query_params = []
    
    for param in params:
        param_name = param.get('name', '')
        param_in = param.get('in', '')
        schema = param.get('schema', {})
        param_type = schema.get('type', 'string')
        
        if param_in == 'path':
            example_value = generate_realistic_example_value(param_name, param_type)
            path_params.append(f"{param_name}={example_value}")
        elif param_in == 'query' and (param.get('required', False) or param_name in ['page', 'per_page', 'perPage']):
            example_value = generate_realistic_example_value(param_name, param_type)
            query_params.append(f"{param_name}={example_value}")
    
    # Add parameters
    all_params = path_params + query_params
    if all_params:
        cmd_parts.extend([f"    {param}" for param in all_params])
    
    return ' \\\n'.join(cmd_parts)


def format_curl_example(endpoint, base_url="https://api.abconnect.co"):
    """Generate curl example for an endpoint."""
    path = endpoint['path']
    method = endpoint['method']
    params = endpoint.get('parameters', [])
    request_body = endpoint.get('requestBody', {})
    
    # Replace path parameters with example values
    example_path = path
    query_params = []
    
    for param in params:
        param_name = param.get('name', '')
        param_in = param.get('in', '')
        schema = param.get('schema', {})
        param_type = schema.get('type', 'string')
        
        if param_in == 'path':
            example_value = generate_realistic_example_value(param_name, param_type)
            example_path = example_path.replace(f'{{{param_name}}}', example_value)
        elif param_in == 'query' and (param.get('required', False) or param_name in ['page', 'per_page', 'perPage']):
            example_value = generate_realistic_example_value(param_name, param_type)
            query_params.append(f'{param_name}={example_value}')
    
    # Build the curl command
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
    
    return '\n'.join(curl_lines)


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


def load_endpoint_descriptions():
    """Load endpoint descriptions from the endpoint_descriptions.json file."""
    descriptions_path = Path(__file__).parent / "api" / "endpoint_descriptions.json"
    if descriptions_path.exists():
        with open(descriptions_path, 'r') as f:
            return json.load(f)
    return {"endpoints": {}, "tags": {}}


# Global variables
RESPONSE_EXAMPLES = None
ENDPOINT_DESCRIPTIONS = None


def get_endpoint_description(path, method):
    """Get description for a specific endpoint."""
    global ENDPOINT_DESCRIPTIONS
    if ENDPOINT_DESCRIPTIONS is None:
        ENDPOINT_DESCRIPTIONS = load_endpoint_descriptions()
    
    endpoints = ENDPOINT_DESCRIPTIONS.get('endpoints', {})
    endpoint_data = endpoints.get(path, {}).get(method.lower(), {})
    
    return endpoint_data.get('summary', ''), endpoint_data.get('description', '')


def get_tag_description(tag):
    """Get description for a tag."""
    global ENDPOINT_DESCRIPTIONS
    if ENDPOINT_DESCRIPTIONS is None:
        ENDPOINT_DESCRIPTIONS = load_endpoint_descriptions()
    
    tags = ENDPOINT_DESCRIPTIONS.get('tags', {})
    return tags.get(tag, '')


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
    
    # Map specific endpoints to response examples
    endpoint_mappings = {
        ('/api/job/{jobDisplayId}', 'GET'): ('job', 'get_job_by_display_id'),
        ('/api/companies/{id}', 'GET'): ('companies', 'get_company_by_id'),
        ('/api/companies/{companyId}/details', 'GET'): ('companies', 'get_company_details'),
        ('/api/companies/{companyId}/fulldetails', 'GET'): ('companies', 'get_company_fulldetails'),
        ('/api/companies/availableByCurrentUser', 'GET'): ('companies', 'get_companies_available'),
        ('/api/contacts/{id}', 'GET'): ('contacts', 'get_contact_by_id'),
        ('/api/users/{id}', 'GET'): ('users', 'get_user_by_id'),
        ('/api/users', 'GET'): ('users', 'get_users_list'),
        ('/api/lookup/{masterConstantKey}', 'GET'): ('lookups', 'get_lookup_values'),
    }
    
    # Check if we have a specific example for this endpoint
    if (path, method) in endpoint_mappings:
        tag, key = endpoint_mappings[(path, method)]
        if tag in RESPONSE_EXAMPLES and key in RESPONSE_EXAMPLES[tag]:
            response = RESPONSE_EXAMPLES[tag][key].get('response', {})
            return json.dumps(response, indent=2)
    
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
    
    # Fallback to generic responses based on endpoint
    responses = endpoint.get('responses', {})
    
    # Common response patterns based on endpoint
    if 'search' in path.lower() or (method == 'GET' and path.endswith('s')):
        # List response
        if 'generic' in RESPONSE_EXAMPLES and 'empty_list' in RESPONSE_EXAMPLES['generic']:
            return json.dumps(RESPONSE_EXAMPLES['generic']['empty_list'], indent=2)
        return json.dumps([], indent=2)
    
    elif '{id}' in path or 'details' in path:
        # Single item response
        if 'generic' in RESPONSE_EXAMPLES and 'empty_object' in RESPONSE_EXAMPLES['generic']:
            return json.dumps(RESPONSE_EXAMPLES['generic']['empty_object'], indent=2)
        return json.dumps({}, indent=2)
    
    elif method == 'POST':
        # Create response
        return json.dumps({
            "id": "789e0123-e89b-12d3-a456-426614174002",
            "status": "created",
            "message": "Resource created successfully"
        }, indent=2)
    
    elif method in ['PUT', 'PATCH']:
        # Update response
        return json.dumps({
            "id": "123e4567-e89b-12d3-a456-426614174000",
            "status": "updated",
            "message": "Resource updated successfully"
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
            "data": {}
        }, indent=2)


def get_pydantic_models():
    """Load Pydantic model mappings for endpoints."""
    # Define endpoint to model mappings
    return {
        # Job endpoints
        ('/api/job/{jobDisplayId}', 'GET'): {
            'model': 'Job',
            'module': 'jobs'
        },
        ('/api/job/search', 'GET'): {
            'model': 'List[Job]',
            'module': 'jobs'
        },
        ('/api/job/{jobDisplayId}/book', 'POST'): {
            'model': 'Job',
            'module': 'jobs'
        },
        
        # Company endpoints
        ('/api/companies/{id}', 'GET'): {
            'model': 'CompanyBasic',
            'module': 'companies'
        },
        ('/api/companies/{companyId}/details', 'GET'): {
            'model': 'CompanyDetails', 
            'module': 'companies'
        },
        ('/api/companies/{companyId}/fulldetails', 'GET'): {
            'model': 'CompanyFullDetails',
            'module': 'companies'
        },
        ('/api/companies/availableByCurrentUser', 'GET'): {
            'model': 'List[CompanyBasic]',
            'module': 'companies'
        },
        ('/api/companies/search', 'GET'): {
            'model': 'List[CompanyBasic]',
            'module': 'companies'
        },
        
        # Contact endpoints
        ('/api/contacts/{id}', 'GET'): {
            'model': 'Contact',
            'module': 'contacts'
        },
        ('/api/contacts', 'POST'): {
            'model': 'Contact',
            'module': 'contacts'
        },
        
        # User endpoints
        ('/api/users', 'GET'): {
            'model': 'List[User]',
            'module': 'users'
        },
        ('/api/users/{id}', 'GET'): {
            'model': 'User',
            'module': 'users'
        },
        
        # Lookup endpoints
        ('/api/lookup/{masterConstantKey}', 'GET'): {
            'model': 'List[LookupValue]',
            'module': 'lookups'
        },
    }


def format_response_model(endpoint_path, method):
    """Get the response model documentation for an endpoint."""
    model_mappings = get_pydantic_models()
    model_info = model_mappings.get((endpoint_path, method))
    
    if not model_info:
        return None
        
    model_name = model_info['model']
    module_name = model_info['module']
    
    # Format the response type section
    lines = []
    lines.append("**Response Type:**")
    lines.append("")
    
    if model_name.startswith('List['):
        inner_model = model_name[5:-1]
        lines.append(f"Array of :class:`~ABConnect.api.models.{module_name}.{inner_model}` objects")
    else:
        lines.append(f":class:`~ABConnect.api.models.{module_name}.{model_name}`")
    
    lines.append("")
    lines.append("See the model documentation for detailed field descriptions.")
    lines.append("")
    
    return lines


def generate_tag_documentation(tag_name, endpoints, tag_description=""):
    """Generate enhanced RST documentation for a tag."""
    doc = []
    
    # Title (without 'API' suffix)
    title = tag_name
    doc.append(title)
    doc.append("=" * len(title))
    doc.append("")
    
    # Tag description
    custom_description = get_tag_description(tag_name)
    if custom_description:
        doc.append(custom_description)
        doc.append("")
    elif tag_description:
        doc.append(tag_description)
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
        
        # Get custom summary or use swagger summary
        custom_summary, _ = get_endpoint_description(path, method)
        summary = custom_summary or endpoint.get('summary', '')
        
        doc.append(f"   * - {method}")
        doc.append(f"     - {path}")
        doc.append(f"     - {summary}")
    
    doc.append("")
    doc.append("")
    
    # Process each endpoint
    for endpoint in endpoints:
        operation_id = endpoint.get('operationId', '')
        path = endpoint['path']
        method = endpoint['method']
        parameters = endpoint.get('parameters', [])
        
        # Get custom descriptions
        custom_summary, custom_description = get_endpoint_description(path, method)
        summary = custom_summary or endpoint.get('summary', '')
        description = custom_description or endpoint.get('description', '')
        
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
        if summary:
            doc.append(f"**{summary}**")
            doc.append("")
        
        if description:
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
        
        # Response Model (if available)
        response_model_lines = format_response_model(path, method)
        if response_model_lines:
            doc.extend(response_model_lines)
        
        # Example Request with tabs
        doc.append("**Example Request:**")
        doc.append("")
        doc.append(".. tabs::")
        doc.append("")
        
        # Python tab
        doc.append("   .. tab:: Python")
        doc.append("")
        doc.append("      .. code-block:: python")
        doc.append("")
        python_example = format_python_example(endpoint)
        for line in python_example.split('\n'):
            doc.append(f"         {line}")
        doc.append("")
        
        # CLI tab
        doc.append("   .. tab:: CLI")
        doc.append("")
        doc.append("      .. code-block:: bash")
        doc.append("")
        cli_example = format_cli_example(endpoint)
        for line in cli_example.split('\n'):
            doc.append(f"         {line}")
        doc.append("")
        
        # Curl tab
        doc.append("   .. tab:: curl")
        doc.append("")
        doc.append("      .. code-block:: bash")
        doc.append("")
        curl_example = format_curl_example(endpoint)
        for line in curl_example.split('\n'):
            doc.append(f"         {line}")
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
        
        # Add a separator between endpoints (except for the last one)
        if endpoint != endpoints[-1]:
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
    
    # Get tag descriptions from swagger
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
    index_content.append("Endpoint Reference")
    index_content.append("==================")
    index_content.append("")
    index_content.append("Complete API endpoint reference organized by resource type.")
    index_content.append("")
    index_content.append("")
    index_content.append("Available Resources")
    index_content.append("-------------------")
    index_content.append("")
    
    # Add a table of resources with descriptions
    descriptions = load_endpoint_descriptions()
    tag_descs = descriptions.get('tags', {})
    
    index_content.append(".. list-table::")
    index_content.append("   :header-rows: 1")
    index_content.append("   :widths: 20 80")
    index_content.append("")
    index_content.append("   * - Resource")
    index_content.append("     - Description")
    
    for tag in sorted(tag_groups.keys()):
        desc = tag_descs.get(tag, tag_descriptions.get(tag, ''))
        index_content.append(f"   * - :doc:`{sanitize_filename(tag)}`")
        index_content.append(f"     - {desc}")
    
    index_content.append("")
    index_content.append(".. toctree::")
    index_content.append("   :maxdepth: 2")
    index_content.append("   :hidden:")
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
        
        print(f"Generated documentation for {tag} ({len(endpoints)} endpoints)")
    
    # Save index file
    index_path = api_dir / "index.rst"
    with open(index_path, 'w') as f:
        f.write("\n".join(index_content))
    
    print(f"\nGenerated enhanced documentation for {len(tag_groups)} tags")
    print(f"Documentation saved in: {api_dir}")


if __name__ == "__main__":
    main()