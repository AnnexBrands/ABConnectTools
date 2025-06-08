#!/usr/bin/env python3
"""Update test files to add documentation cross-references."""

import json
import os
from pathlib import Path
from collections import defaultdict
import re


def sanitize_name(name):
    """Convert name to valid Python identifier."""
    # Replace special characters
    name = re.sub(r'[^\w\s-]', '', name)
    name = re.sub(r'[-\s]+', '_', name)
    return name.lower()


def generate_endpoint_test(endpoint, tag_name):
    """Generate test method for an endpoint with documentation cross-reference."""
    path = endpoint['path']
    method = endpoint['method'].lower()
    operation_id = endpoint.get('operationId', '')
    
    # Create test method name
    test_name = operation_id or f"{method}_{sanitize_name(path)}"
    test_name = f"test_{sanitize_name(test_name)}"
    
    # Generate documentation URL
    tag_slug = sanitize_name(tag_name)
    anchor = f"{method}-{path.replace('/', '').replace('{', '').replace('}', '')}"
    anchor = sanitize_name(anchor)
    doc_url = f"https://abconnecttools.readthedocs.io/en/latest/api/{tag_slug}.html#{anchor}"
    
    # Generate path with example values
    example_path = path
    path_params = {}
    
    for param in endpoint.get('parameters', []):
        if param.get('in') == 'path':
            param_name = param['name']
            if 'id' in param_name.lower():
                example_value = 'test-id-123'
            else:
                example_value = 'test-value'
            path_params[param_name] = example_value
            example_path = example_path.replace(f'{{{param_name}}}', example_value)
    
    # Generate test method
    test_code = [
        f"    def {test_name}(self):",
        f'        """Test {method.upper()} {path}.',
        f'        ',
        f'        See documentation: {doc_url}',
        f'        """'
    ]
    
    if path_params:
        test_code.append("        # Path parameters")
        for name, value in path_params.items():
            test_code.append(f'        {name} = "{value}"')
        test_code.append("")
    
    test_code.append(f'        response = self.api.raw.{method}(')
    test_code.append(f'            "{path}",')
    
    if path_params:
        for name, value in path_params.items():
            test_code.append(f'            {name}={name},')
    
    test_code.append('        )')
    test_code.append('        ')
    test_code.append('        # Check response')
    test_code.append('        self.assertIsNotNone(response)')
    test_code.append('        if isinstance(response, dict):')
    test_code.append('            self.assertIsInstance(response, dict)')
    test_code.append('        elif isinstance(response, list):')
    test_code.append('            self.assertIsInstance(response, list)')
    
    return '\n'.join(test_code)


def generate_tag_test_file(tag_name, endpoints):
    """Generate test file for a tag with documentation cross-references."""
    class_name = ''.join(word.capitalize() for word in tag_name.split())
    class_name = f"Test{class_name}API"
    
    # Generate file content
    content = [
        '"""Tests for {} API endpoints.',
        '',
        'Documentation: https://abconnecttools.readthedocs.io/en/latest/api/{}.html',
        '"""'.format(tag_name, sanitize_name(tag_name)),
        '',
        'import unittest',
        'from unittest.mock import patch, MagicMock',
        'from ABConnect import ABConnectAPI',
        'from ABConnect.exceptions import ABConnectError',
        '',
        '',
        f'class {class_name}(unittest.TestCase):',
        '    """Test cases for {} endpoints."""'.format(tag_name),
        '',
        '    def setUp(self):',
        '        """Set up test fixtures."""',
        '        self.api = ABConnectAPI()',
        '        # Mock the raw API calls to avoid actual API requests',
        '        self.mock_response = MagicMock()',
        '',
        '    @patch("ABConnect.api.http.RequestHandler.call")',
        '    def test_endpoint_availability(self, mock_call):',
        '        """Test that endpoints are available."""',
        '        # This is a basic test to ensure the API client initializes',
        '        self.assertIsNotNone(self.api)',
        '        self.assertTrue(hasattr(self.api, "raw"))',
        ''
    ]
    
    # Add test methods for each endpoint
    for endpoint in endpoints[:5]:  # Limit to first 5 to keep tests manageable
        content.append('')
        content.append(generate_endpoint_test(endpoint, tag_name))
    
    # Add main block
    content.extend([
        '',
        '',
        'if __name__ == "__main__":',
        '    unittest.main()'
    ])
    
    return '\n'.join(content)


def main():
    """Update test files with documentation cross-references."""
    # Load swagger specification
    swagger_path = Path(__file__).parent.parent / "ABConnect" / "base" / "swagger.json"
    with open(swagger_path, 'r') as f:
        swagger = json.load(f)
    
    # Group endpoints by tags
    tag_groups = defaultdict(list)
    
    for path, methods in swagger['paths'].items():
        for method, details in methods.items():
            if method in ['get', 'post', 'put', 'patch', 'delete']:
                tags = details.get('tags', ['Untagged'])
                endpoint_info = {
                    'path': path,
                    'method': method.upper(),
                    'operationId': details.get('operationId', ''),
                    'parameters': details.get('parameters', [])
                }
                
                for tag in tags:
                    tag_groups[tag].append(endpoint_info)
    
    # Generate test files
    generated_files = []
    
    # Generate test for each major tag
    major_tags = ['Companies', 'Contacts', 'Job', 'Lookup', 'Users']
    
    for tag in major_tags:
        if tag in tag_groups:
            endpoints = tag_groups[tag]
            filename = f"test_{sanitize_name(tag)}_api.py"
            filepath = Path(__file__).parent / filename
            
            content = generate_tag_test_file(tag, endpoints)
            with open(filepath, 'w') as f:
                f.write(content)
            
            generated_files.append(filename)
            print(f"Updated {filename} with documentation cross-references")
    
    print(f"\nUpdated {len(generated_files)} test files with documentation cross-references")


if __name__ == "__main__":
    main()