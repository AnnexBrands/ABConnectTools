"""Endpoint builder for dynamically creating API endpoint classes.

This module provides functionality to automatically generate endpoint classes
from OpenAPI/Swagger specifications.
"""

import re
from typing import Any, Dict, List, Type, Optional
from types import ModuleType

from ABConnect.api.generic import GenericEndpoint
from ABConnect.api.swagger import SwaggerParser, EndpointDefinition


class EndpointBuilder:
    """Builds endpoint classes dynamically from OpenAPI specifications."""
    
    def __init__(self, swagger_parser: SwaggerParser):
        """Initialize the endpoint builder.
        
        Args:
            swagger_parser: Initialized SwaggerParser instance
        """
        self.swagger_parser = swagger_parser
        self._endpoint_cache: Dict[str, Type[GenericEndpoint]] = {}
    
    def build_from_swagger(self) -> Dict[str, Type[GenericEndpoint]]:
        """Build endpoint classes for all resources in the swagger spec.
        
        Returns:
            Dictionary mapping resource names to their endpoint classes
        """
        endpoints_by_resource = self.swagger_parser.parse()
        endpoint_classes = {}
        
        for resource_name, endpoints in endpoints_by_resource.items():
            # Create or get cached endpoint class
            if resource_name in self._endpoint_cache:
                endpoint_class = self._endpoint_cache[resource_name]
            else:
                endpoint_class = self.create_endpoint_class(resource_name, endpoints)
                self._endpoint_cache[resource_name] = endpoint_class
            
            endpoint_classes[resource_name] = endpoint_class
        
        return endpoint_classes
    
    def create_endpoint_class(self, resource: str, 
                            endpoints: List[EndpointDefinition]) -> Type[GenericEndpoint]:
        """Create a dynamic endpoint class for a resource.
        
        Args:
            resource: Resource name (e.g., 'companies', 'jobs')
            endpoints: List of endpoint definitions for this resource
            
        Returns:
            Dynamically created endpoint class
        """
        # Create class name
        class_name = self._resource_to_class_name(resource)
        
        # Create class docstring
        docstring = self._generate_class_docstring(resource, endpoints)
        
        # Create class attributes
        class_attrs = {
            '__doc__': docstring,
            '__module__': 'ABConnect.api.endpoints.dynamic',
            '_resource_name': resource,
            '_endpoints': endpoints,
        }
        
        # Add convenience methods for common operations
        for endpoint in endpoints:
            method_name = self.generate_method_name(
                endpoint.operation_id, 
                endpoint.path, 
                endpoint.method
            )
            
            # Skip if it would override a base class method
            if method_name in ['get', 'list', 'create', 'update', 'delete', 'patch']:
                continue
            
            # Create a wrapper method
            method = self._create_endpoint_method(endpoint)
            class_attrs[method_name] = method
        
        # Create the class dynamically
        endpoint_class = type(class_name, (GenericEndpoint,), class_attrs)
        
        return endpoint_class
    
    def generate_method_name(self, operation_id: Optional[str], 
                           path: str, method: str) -> str:
        """Generate a Python method name from endpoint information.
        
        Args:
            operation_id: OpenAPI operation ID if available
            path: API endpoint path
            method: HTTP method
            
        Returns:
            Valid Python method name
        """
        if operation_id:
            # Use operation ID if available
            name = operation_id
        else:
            # Generate from path and method
            parts = []
            
            # Add method prefix for non-GET
            if method.lower() != 'get':
                parts.append(method.lower())
            
            # Extract meaningful parts from path
            path_parts = path.strip('/').split('/')
            
            # Skip 'api' prefix
            if path_parts and path_parts[0] == 'api':
                path_parts = path_parts[1:]
            
            # Skip the resource name (first part)
            if len(path_parts) > 1:
                path_parts = path_parts[1:]
            
            # Add non-parameter parts
            for part in path_parts:
                if not part.startswith('{') and part not in ['v1', 'v2', 'api']:
                    # Convert part to snake_case
                    part = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', part)
                    parts.append(part.lower())
            
            # Default names for common patterns
            if not parts:
                if method.lower() == 'get':
                    name = 'list' if not any('{' in p for p in path_parts) else 'get_by_id'
                else:
                    name = method.lower()
            else:
                name = '_'.join(parts)
        
        # Clean up the name
        name = re.sub(r'[^a-zA-Z0-9_]', '_', name)  # Replace invalid chars
        name = re.sub(r'_+', '_', name)  # Remove duplicate underscores
        name = name.strip('_')  # Remove leading/trailing underscores
        
        # Ensure it doesn't start with a number
        if name and name[0].isdigit():
            name = f'method_{name}'
        
        # Convert to snake_case
        name = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', name)
        
        return name.lower()
    
    def _resource_to_class_name(self, resource: str) -> str:
        """Convert resource name to a proper class name.
        
        Args:
            resource: Resource name (e.g., 'companies', 'job_items')
            
        Returns:
            Class name (e.g., 'CompaniesEndpoint', 'JobItemsEndpoint')
        """
        # Split by underscore and capitalize each part
        parts = resource.split('_')
        
        # Handle plural forms
        if parts[-1].endswith('ies'):
            # companies -> Company
            parts[-1] = parts[-1][:-3] + 'y'
        elif parts[-1].endswith('es'):
            # addresses -> Address
            parts[-1] = parts[-1][:-2]
        elif parts[-1].endswith('s') and len(parts[-1]) > 1:
            # jobs -> Job (but not 's' alone)
            parts[-1] = parts[-1][:-1]
        
        # Capitalize and join
        class_name = ''.join(part.capitalize() for part in parts)
        
        return f"{class_name}Endpoint"
    
    def _generate_class_docstring(self, resource: str, 
                                 endpoints: List[EndpointDefinition]) -> str:
        """Generate a docstring for the endpoint class.
        
        Args:
            resource: Resource name
            endpoints: List of endpoints for this resource
            
        Returns:
            Class docstring
        """
        lines = [
            f"Auto-generated endpoint for {resource} resource.",
            "",
            "This endpoint provides the following operations:",
            ""
        ]
        
        # Group endpoints by operation type
        operations = {}
        for endpoint in endpoints:
            key = f"{endpoint.method} {endpoint.path}"
            if endpoint.summary:
                operations[key] = endpoint.summary
            elif endpoint.description:
                operations[key] = endpoint.description.split('\n')[0]
            else:
                operations[key] = f"{endpoint.method} operation"
        
        # Add operations to docstring
        for operation, description in sorted(operations.items()):
            lines.append(f"- {operation}: {description}")
        
        return '\n'.join(lines)
    
    def _create_endpoint_method(self, endpoint: EndpointDefinition):
        """Create a method for a specific endpoint.
        
        Args:
            endpoint: EndpointDefinition to create method for
            
        Returns:
            Method function
        """
        def endpoint_method(self, **kwargs):
            """Execute the endpoint with given parameters."""
            return self._execute_endpoint(endpoint, **kwargs)
        
        # Set method metadata
        endpoint_method.__name__ = endpoint.method_name
        endpoint_method.__doc__ = self._generate_method_docstring(endpoint)
        
        return endpoint_method
    
    def _generate_method_docstring(self, endpoint: EndpointDefinition) -> str:
        """Generate docstring for an endpoint method.
        
        Args:
            endpoint: EndpointDefinition to document
            
        Returns:
            Method docstring
        """
        lines = []
        
        # Add summary/description
        if endpoint.summary:
            lines.append(endpoint.summary)
            if endpoint.description:
                lines.append("")
                lines.append(endpoint.description)
        elif endpoint.description:
            lines.append(endpoint.description)
        else:
            lines.append(f"{endpoint.method} {endpoint.path}")
        
        lines.append("")
        
        # Document parameters
        if endpoint.parameters or endpoint.request_body:
            lines.append("Args:")
            
            # Path and query parameters
            for param in endpoint.parameters:
                param_doc = f"    {param.python_name}"
                
                # Add type hint
                if param.python_type != 'Any':
                    param_doc += f" ({param.python_type})"
                
                param_doc += ": "
                
                # Add description
                if param.description:
                    param_doc += param.description
                else:
                    param_doc += f"{param.location} parameter"
                
                # Mark if required
                if param.required:
                    param_doc += " (required)"
                elif param.default is not None:
                    param_doc += f" (default: {param.default})"
                
                lines.append(param_doc)
            
            # Request body
            if endpoint.request_body:
                body_doc = "    data (dict): Request body"
                if endpoint.request_body.description:
                    body_doc += f" - {endpoint.request_body.description}"
                if endpoint.request_body.required:
                    body_doc += " (required)"
                lines.append(body_doc)
            
            lines.append("")
        
        # Document return value
        lines.append("Returns:")
        
        # Check for documented responses
        success_response = None
        for status_code in ['200', '201', '202', '204']:
            if status_code in endpoint.responses:
                success_response = endpoint.responses[status_code]
                break
        
        if success_response and 'description' in success_response:
            lines.append(f"    {success_response['description']}")
        else:
            lines.append("    API response data")
        
        # Add example if we can generate one
        example = self._generate_example(endpoint)
        if example:
            lines.append("")
            lines.append("Example:")
            lines.append(f"    >>> {example}")
        
        return '\n'.join(lines)
    
    def _generate_example(self, endpoint: EndpointDefinition) -> Optional[str]:
        """Generate an example method call.
        
        Args:
            endpoint: EndpointDefinition to create example for
            
        Returns:
            Example string or None
        """
        parts = [f"endpoint.{endpoint.method_name}("]
        args = []
        
        # Add required parameters
        for param in endpoint.parameters:
            if param.required:
                if param.python_type == 'str':
                    value = f"'{param.name}_value'"
                elif param.python_type == 'int':
                    value = "123"
                elif param.python_type == 'bool':
                    value = "True"
                else:
                    value = f"<{param.python_type}>"
                
                args.append(f"{param.python_name}={value}")
        
        # Add body if required
        if endpoint.request_body and endpoint.request_body.required:
            args.append("data={...}")
        
        if args:
            parts.append(", ".join(args))
        
        parts.append(")")
        
        return "".join(parts) if args else None