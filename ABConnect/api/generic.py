"""Generic endpoint base class for dynamic API method generation.

This module provides a base class that can dynamically generate API methods
from OpenAPI/Swagger specifications, enabling automatic endpoint coverage.
"""

import re
from typing import Any, Callable, Dict, List, Optional, Union
from urllib.parse import urlencode

from ABConnect.api.endpoints.base import BaseEndpoint
from ABConnect.api.swagger import EndpointDefinition, Parameter, SwaggerParser
from ABConnect.exceptions import ABConnectError
from ABConnect.api.query import QueryBuilder


class GenericEndpoint(BaseEndpoint):
    """Base class for dynamically generated API endpoints.
    
    This class provides standard REST methods and can dynamically generate
    additional methods based on OpenAPI specifications.
    """
    
    def __init__(self, resource_name: str, swagger_parser: Optional[SwaggerParser] = None):
        """Initialize generic endpoint.
        
        Args:
            resource_name: Name of the API resource (e.g., 'companies', 'jobs')
            swagger_parser: Optional SwaggerParser instance for dynamic method generation
        """
        super().__init__()
        self.resource_name = resource_name
        self.swagger_parser = swagger_parser
        self._endpoints: List[EndpointDefinition] = []
        
        if swagger_parser:
            self._load_endpoints()
            self._generate_methods()
    
    def _load_endpoints(self) -> None:
        """Load endpoint definitions for this resource."""
        all_endpoints = self.swagger_parser.parse()
        self._endpoints = all_endpoints.get(self.resource_name, [])
    
    def _generate_methods(self) -> None:
        """Dynamically generate methods from endpoint definitions."""
        for endpoint in self._endpoints:
            method_name = endpoint.method_name
            
            # Skip if method already exists (allows manual override)
            if hasattr(self, method_name):
                continue
                
            # Create the method
            method = self._create_method(endpoint)
            setattr(self, method_name, method)
    
    def _create_method(self, endpoint: EndpointDefinition) -> Callable:
        """Create a method for an endpoint definition."""
        def dynamic_method(**kwargs):
            return self._execute_endpoint(endpoint, **kwargs)
        
        # Set method metadata
        dynamic_method.__name__ = endpoint.method_name
        dynamic_method.__doc__ = self._generate_docstring(endpoint)
        
        # Add type hints (simplified for now)
        dynamic_method.__annotations__ = self._generate_type_hints(endpoint)
        
        return dynamic_method
    
    def _execute_endpoint(self, endpoint: EndpointDefinition, **kwargs) -> Any:
        """Execute an API endpoint with given parameters."""
        # Build the path with path parameters
        path = self._build_path(endpoint, **kwargs)
        
        # Separate parameters by type
        query_params = {}
        body_data = None
        
        # Process parameters
        for param in endpoint.parameters:
            value = kwargs.get(param.python_name)
            
            if value is None and param.required:
                raise ABConnectError(f"Required parameter '{param.name}' not provided")
            
            if value is not None:
                if param.location == 'query':
                    query_params[param.name] = value
                elif param.location == 'path':
                    # Already handled in _build_path
                    pass
                # Note: header and cookie parameters could be added here
        
        # Handle request body
        if endpoint.request_body:
            # Look for common body parameter names
            for body_param in ['data', 'body', 'json', 'payload']:
                if body_param in kwargs:
                    body_data = kwargs[body_param]
                    break
        
        # Build the request
        request_kwargs = {}
        if query_params:
            request_kwargs['params'] = query_params
        if body_data is not None:
            request_kwargs['json'] = body_data
            
        # Execute the request
        return self._r.call(endpoint.method, path, **request_kwargs)
    
    def _build_path(self, endpoint: EndpointDefinition, **kwargs) -> str:
        """Build the request path with path parameters."""
        path = endpoint.path
        
        # Replace path parameters
        for param in endpoint.get_path_parameters():
            value = kwargs.get(param.python_name)
            if value is None:
                raise ABConnectError(f"Path parameter '{param.name}' is required")
            
            # Replace {paramName} with actual value
            path = path.replace(f'{{{param.name}}}', str(value))
        
        return path
    
    def _generate_docstring(self, endpoint: EndpointDefinition) -> str:
        """Generate a docstring for a dynamic method."""
        lines = []
        
        # Summary
        if endpoint.summary:
            lines.append(endpoint.summary)
            lines.append("")
        elif endpoint.description:
            lines.append(endpoint.description.split('\n')[0])
            lines.append("")
        
        # Description
        if endpoint.description and endpoint.summary:
            lines.append(endpoint.description)
            lines.append("")
        
        # Parameters
        if endpoint.parameters or endpoint.request_body:
            lines.append("Args:")
            
            for param in endpoint.parameters:
                param_line = f"    {param.python_name}"
                if param.python_type != 'Any':
                    param_line += f" ({param.python_type})"
                param_line += ": "
                if param.description:
                    param_line += param.description
                if param.required:
                    param_line += " (required)"
                lines.append(param_line)
            
            if endpoint.request_body:
                lines.append("    data (dict): Request body data")
            
            lines.append("")
        
        # Returns
        lines.append("Returns:")
        lines.append("    API response data")
        
        return '\n'.join(lines)
    
    def _generate_type_hints(self, endpoint: EndpointDefinition) -> Dict[str, Any]:
        """Generate type hints for a dynamic method."""
        hints = {}
        
        # Add parameter type hints
        for param in endpoint.parameters:
            param_type = param.python_type
            if not param.required:
                param_type = f"Optional[{param_type}]"
            hints[param.python_name] = eval(param_type)
        
        # Add body parameter if needed
        if endpoint.request_body:
            hints['data'] = Dict[str, Any]
        
        # Return type
        hints['return'] = Any
        
        return hints
    
    # Standard REST methods
    
    def get(self, id: Optional[str] = None, **kwargs) -> Dict[str, Any]:
        """Get a resource by ID or list resources.
        
        Args:
            id: Optional resource ID. If provided, gets a single resource.
                If None, lists resources.
            **kwargs: Additional parameters (filters, pagination, etc.)
            
        Returns:
            Single resource dict if id provided, list of resources otherwise
        """
        if id:
            # Get single resource
            path = f"{self.resource_name}/{id}"
            return self._r.call('GET', path, params=kwargs)
        else:
            # List resources
            return self.list(**kwargs)
    
    def list(self, page: int = 1, per_page: int = 50, **kwargs) -> Dict[str, Any]:
        """List resources with optional filtering and pagination.
        
        Args:
            page: Page number (1-based)
            per_page: Number of items per page
            **kwargs: Additional filters and parameters
            
        Returns:
            Dict containing list of resources and pagination info
        """
        params = {
            'page': page,
            'perPage': per_page,
            **kwargs
        }
        
        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}
        
        return self._r.call('GET', self.resource_name, params=params)
    
    def create(self, data: Dict[str, Any], **kwargs) -> Dict[str, Any]:
        """Create a new resource.
        
        Args:
            data: Resource data to create
            **kwargs: Additional parameters
            
        Returns:
            Created resource data
        """
        return self._r.call('POST', self.resource_name, json=data, params=kwargs)
    
    def update(self, id: str, data: Dict[str, Any], **kwargs) -> Dict[str, Any]:
        """Update an existing resource.
        
        Args:
            id: Resource ID to update
            data: Updated resource data
            **kwargs: Additional parameters
            
        Returns:
            Updated resource data
        """
        path = f"{self.resource_name}/{id}"
        return self._r.call('PUT', path, json=data, params=kwargs)
    
    def patch(self, id: str, data: Dict[str, Any], **kwargs) -> Dict[str, Any]:
        """Partially update an existing resource.
        
        Args:
            id: Resource ID to update
            data: Partial resource data to update
            **kwargs: Additional parameters
            
        Returns:
            Updated resource data
        """
        path = f"{self.resource_name}/{id}"
        return self._r.call('PATCH', path, json=data, params=kwargs)
    
    def delete(self, id: str, **kwargs) -> Dict[str, Any]:
        """Delete a resource.
        
        Args:
            id: Resource ID to delete
            **kwargs: Additional parameters
            
        Returns:
            Deletion confirmation or empty response
        """
        path = f"{self.resource_name}/{id}"
        return self._r.call('DELETE', path, params=kwargs)
    
    def query(self) -> QueryBuilder:
        """Create a query builder for this endpoint.
        
        Returns:
            QueryBuilder instance for fluent query construction
            
        Example:
            >>> results = endpoint.query()
            ...     .filter(status='active')
            ...     .sort('created', 'desc')
            ...     .page(2)
            ...     .execute()
        """
        return QueryBuilder(self)
    
    def raw(self, method: str, path: str, **kwargs) -> Any:
        """Execute a raw API request.
        
        This method allows direct API access for cases not covered by
        standard methods or when you need full control.
        
        Args:
            method: HTTP method (GET, POST, PUT, DELETE, etc.)
            path: API path (can be relative or absolute)
            **kwargs: Additional request parameters (params, json, headers, etc.)
            
        Returns:
            API response data
            
        Example:
            >>> endpoint.raw('GET', '/custom/endpoint', params={'filter': 'active'})
        """
        # Ensure path starts with /
        if not path.startswith('/'):
            path = f'/{path}'
            
        return self._r.call(method.upper(), path, **kwargs)
    
    def __getattr__(self, name: str) -> Callable:
        """Allow dynamic method calls for any endpoint.
        
        This enables calling methods that weren't generated at initialization
        or accessing nested resources.
        
        Args:
            name: Method or resource name
            
        Returns:
            Callable method or nested endpoint
        """
        # Check if it's a known endpoint method
        for endpoint in self._endpoints:
            if endpoint.method_name == name:
                return self._create_method(endpoint)
        
        # Otherwise, assume it's a nested resource
        def nested_resource(**kwargs):
            path = f"{self.resource_name}/{name}"
            method = kwargs.pop('_method', 'GET')
            return self._r.call(method, path, **kwargs)
        
        return nested_resource