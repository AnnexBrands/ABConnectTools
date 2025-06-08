#!/usr/bin/env python3
"""Generate API documentation from swagger specification.

This script creates comprehensive documentation for all API endpoints
organized by swagger tags.
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


def format_bash_example(endpoint, base_url="https://api.abconnect.co"):
    """Generate bash example for an endpoint."""
    path = endpoint['path']
    method = endpoint['method']
    params = endpoint.get('parameters', [])
    
    # Replace path parameters with example values
    example_path = path
    path_params = []
    query_params = []
    
    for param in params:
        param_name = param.get('name', '')
        param_in = param.get('in', '')
        
        if param_in == 'path':
            # Use example values for common parameters
            if 'id' in param_name.lower():
                example_value = '123e4567-e89b-12d3-a456-426614174000'
            elif 'displayid' in param_name.lower():
                example_value = 'JOB-2024-001'
            elif 'code' in param_name.lower():
                example_value = 'ABC123'
            else:
                example_value = 'example-value'
            
            example_path = example_path.replace(f'{{{param_name}}}', example_value)
            path_params.append((param_name, example_value))
            
        elif param_in == 'query':
            # Add common query parameters
            if param_name == 'page':
                query_params.append(f'{param_name}=1')
            elif param_name == 'per_page' or param_name == 'perPage':
                query_params.append(f'{param_name}=20')
            elif param.get('required', False):
                query_params.append(f'{param_name}=value')
    
    # Build the curl command
    curl_cmd = f"curl -X {method}"
    
    # Add headers
    curl_cmd += " \\\n  -H 'Authorization: Bearer YOUR_TOKEN'"
    
    if method in ['POST', 'PUT', 'PATCH']:
        curl_cmd += " \\\n  -H 'Content-Type: application/json'"
        curl_cmd += " \\\n  -d '{"
        curl_cmd += "\n    \"key\": \"value\""
        curl_cmd += "\n  }'"
    
    # Add URL with query parameters
    url = f"{base_url}{example_path}"
    if query_params:
        url += "?" + "&".join(query_params)
    
    curl_cmd += f" \\\n  '{url}'"
    
    # Also add ab CLI example
    ab_cmd = f"ab api raw {method.lower()} {path}"
    if path_params:
        for name, value in path_params:
            ab_cmd += f" {name}={value}"
    if query_params:
        ab_cmd += " " + " ".join(query_params)
    
    return curl_cmd, ab_cmd


def generate_sample_response(endpoint):
    """Generate a sample response based on endpoint details."""
    # This is a simplified version - in reality you'd want to use the schema
    responses = endpoint.get('responses', {})
    
    if '200' in responses:
        response = responses['200']
        content = response.get('content', {})
        
        if 'application/json' in content:
            schema = content['application/json'].get('schema', {})
            
            # Generate sample based on common patterns
            if 'array' in str(schema):
                return json.dumps([
                    {
                        "id": "123e4567-e89b-12d3-a456-426614174000",
                        "name": "Example Item",
                        "created": "2024-01-01T00:00:00Z"
                    }
                ], indent=2)
            else:
                return json.dumps({
                    "id": "123e4567-e89b-12d3-a456-426614174000",
                    "status": "success",
                    "data": {
                        "example": "response"
                    }
                }, indent=2)
    
    return json.dumps({"message": "Success"}, indent=2)


def generate_tag_documentation(tag_name, endpoints, tag_description=""):
    """Generate RST documentation for a tag."""
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
    
    # Process each endpoint
    for endpoint in endpoints:
        operation_id = endpoint.get('operationId', '')
        summary = endpoint.get('summary', 'No summary available')
        description = endpoint.get('description', '')
        path = endpoint['path']
        method = endpoint['method']
        parameters = endpoint.get('parameters', [])
        
        # Endpoint title
        endpoint_title = f"{method} {path}"
        doc.append(endpoint_title)
        doc.append("-" * len(endpoint_title))
        doc.append("")
        
        # Summary and description
        doc.append(summary)
        if description and description != summary:
            doc.append("")
            doc.append(description)
        doc.append("")
        
        # Parameters
        if parameters:
            doc.append("**Parameters:**")
            doc.append("")
            for param in parameters:
                doc.append(format_parameter(param))
            doc.append("")
        
        # Request example
        doc.append("**Example Request:**")
        doc.append("")
        
        # Generate bash examples
        curl_example, ab_example = format_bash_example(endpoint)
        
        # Curl example with copy button
        doc.append(".. code-block:: bash")
        doc.append("   :caption: Using curl")
        doc.append("")
        for line in curl_example.split('\n'):
            doc.append(f"   {line}")
        doc.append("")
        
        # AB CLI example
        doc.append(".. code-block:: bash")
        doc.append("   :caption: Using AB CLI")
        doc.append("")
        doc.append(f"   {ab_example}")
        doc.append("")
        
        # Sample response (collapsible)
        doc.append("**Sample Response:**")
        doc.append("")
        doc.append(".. toggle::")
        doc.append("")
        doc.append("   .. code-block:: json")
        doc.append("")
        
        sample_response = generate_sample_response(endpoint)
        for line in sample_response.split('\n'):
            doc.append(f"      {line}")
        doc.append("")
        doc.append("")
    
    return "\n".join(doc)


def main():
    """Generate API documentation."""
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
        index_content.append(f"   api/{filename}")
        
        print(f"Generated documentation for {tag} ({len(endpoints)} endpoints)")
    
    # Save index file
    index_path = Path(__file__).parent / "api" / "index.rst"
    with open(index_path, 'w') as f:
        f.write("\n".join(index_content))
    
    print(f"\nGenerated documentation for {len(tag_groups)} tags")
    print(f"Documentation saved in: {api_dir}")


if __name__ == "__main__":
    main()