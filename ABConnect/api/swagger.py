"""OpenAPI/Swagger specification parser for dynamic endpoint generation.

This module provides functionality to parse OpenAPI 3.0 specifications
and extract endpoint definitions for automatic API method generation.
"""

import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union
from ABConnect.common import load_json_resource


@dataclass
class Parameter:
    """Represents an API parameter from OpenAPI specification."""
    name: str
    location: str  # 'path', 'query', 'header', 'cookie'
    required: bool = False
    schema: Dict[str, Any] = field(default_factory=dict)
    description: Optional[str] = None
    default: Optional[Any] = None
    
    @property
    def python_name(self) -> str:
        """Convert parameter name to valid Python identifier."""
        # Handle special cases and convert to snake_case
        name = self.name
        # Replace common separators with underscores
        name = re.sub(r'[-.\s]+', '_', name)
        # Convert camelCase to snake_case
        name = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', name)
        return name.lower()
    
    @property
    def python_type(self) -> str:
        """Get Python type hint from OpenAPI schema."""
        if not self.schema:
            return 'Any'
            
        schema_type = self.schema.get('type', 'string')
        schema_format = self.schema.get('format', '')
        
        type_mapping = {
            'string': 'str',
            'integer': 'int',
            'number': 'float',
            'boolean': 'bool',
            'array': 'List[Any]',
            'object': 'Dict[str, Any]'
        }
        
        # Handle special formats
        if schema_type == 'string' and schema_format == 'date-time':
            return 'str'  # Could be datetime with proper parsing
        elif schema_type == 'string' and schema_format == 'uuid':
            return 'str'  # Could be UUID with proper parsing
        elif schema_type == 'integer' and schema_format == 'int64':
            return 'int'
        elif schema_type == 'number' and schema_format == 'double':
            return 'float'
            
        return type_mapping.get(schema_type, 'Any')


@dataclass
class RequestBody:
    """Represents an API request body from OpenAPI specification."""
    content_types: Dict[str, Dict[str, Any]] = field(default_factory=dict)
    required: bool = False
    description: Optional[str] = None
    
    @property
    def primary_content_type(self) -> str:
        """Get the primary content type (prefer application/json)."""
        if 'application/json' in self.content_types:
            return 'application/json'
        return next(iter(self.content_types.keys()), 'application/json')
    
    @property
    def schema(self) -> Optional[Dict[str, Any]]:
        """Get the schema for the primary content type."""
        content = self.content_types.get(self.primary_content_type, {})
        return content.get('schema')


@dataclass
class EndpointDefinition:
    """Represents a single API endpoint definition."""
    path: str
    method: str
    operation_id: Optional[str] = None
    summary: Optional[str] = None
    description: Optional[str] = None
    tags: List[str] = field(default_factory=list)
    parameters: List[Parameter] = field(default_factory=list)
    request_body: Optional[RequestBody] = None
    responses: Dict[str, Dict[str, Any]] = field(default_factory=dict)
    deprecated: bool = False
    
    @property
    def resource_name(self) -> str:
        """Extract resource name from path or tags."""
        # Try to get from tags first
        if self.tags:
            return self.tags[0].lower().replace(' ', '_')
            
        # Extract from path
        parts = self.path.strip('/').split('/')
        # Skip 'api' prefix if present
        if parts and parts[0] == 'api':
            parts = parts[1:]
            
        if parts:
            # Return the first non-parameter part
            for part in parts:
                if not part.startswith('{'):
                    return part
                    
        return 'unknown'
    
    @property
    def method_name(self) -> str:
        """Generate a Python method name for this endpoint."""
        if self.operation_id:
            # Use operation ID if available
            name = self.operation_id
        else:
            # Generate from path and method
            parts = []
            path_parts = self.path.strip('/').split('/')
            
            # Skip 'api' prefix
            if path_parts and path_parts[0] == 'api':
                path_parts = path_parts[1:]
            
            # Add method prefix for non-GET methods
            if self.method.lower() != 'get':
                parts.append(self.method.lower())
            
            # Add path parts (skip parameters)
            for part in path_parts[1:]:  # Skip resource name
                if not part.startswith('{'):
                    parts.append(part)
            
            name = '_'.join(parts) if parts else 'list'
        
        # Convert to snake_case
        name = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', name)
        name = re.sub(r'[-.\s]+', '_', name)
        return name.lower()
    
    def get_path_parameters(self) -> List[Parameter]:
        """Get only path parameters."""
        return [p for p in self.parameters if p.location == 'path']
    
    def get_query_parameters(self) -> List[Parameter]:
        """Get only query parameters."""
        return [p for p in self.parameters if p.location == 'query']


class SwaggerParser:
    """Parser for OpenAPI/Swagger specifications."""
    
    def __init__(self, swagger_path: Optional[str] = None):
        """Initialize parser with swagger specification.
        
        Args:
            swagger_path: Path to swagger.json file. If None, uses the bundled swagger.json
        """
        if swagger_path:
            with open(swagger_path, 'r') as f:
                self.spec = json.load(f)
        else:
            # Use the bundled swagger.json
            self.spec = load_json_resource('swagger.json')
            
        self.paths = self.spec.get('paths', {})
        self.components = self.spec.get('components', {})
        self.schemas = self.components.get('schemas', {})
        
    def parse(self) -> Dict[str, List[EndpointDefinition]]:
        """Parse all endpoints and group by resource.
        
        Returns:
            Dictionary mapping resource names to their endpoint definitions
        """
        endpoints_by_resource = {}
        
        for path, path_item in self.paths.items():
            # Skip parameter definitions
            if 'parameters' in path_item:
                path_parameters = self._parse_parameters(path_item['parameters'])
            else:
                path_parameters = []
            
            # Process each HTTP method
            for method in ['get', 'post', 'put', 'patch', 'delete', 'head', 'options']:
                if method not in path_item:
                    continue
                    
                operation = path_item[method]
                endpoint = self._parse_endpoint(path, method, operation, path_parameters)
                
                # Group by resource
                resource = endpoint.resource_name
                if resource not in endpoints_by_resource:
                    endpoints_by_resource[resource] = []
                endpoints_by_resource[resource].append(endpoint)
        
        return endpoints_by_resource
    
    def _parse_endpoint(self, path: str, method: str, operation: Dict[str, Any], 
                       path_parameters: List[Parameter]) -> EndpointDefinition:
        """Parse a single endpoint definition."""
        # Parse parameters
        parameters = path_parameters.copy()
        if 'parameters' in operation:
            parameters.extend(self._parse_parameters(operation['parameters']))
        
        # Parse request body
        request_body = None
        if 'requestBody' in operation:
            request_body = self._parse_request_body(operation['requestBody'])
        
        return EndpointDefinition(
            path=path,
            method=method.upper(),
            operation_id=operation.get('operationId'),
            summary=operation.get('summary'),
            description=operation.get('description'),
            tags=operation.get('tags', []),
            parameters=parameters,
            request_body=request_body,
            responses=operation.get('responses', {}),
            deprecated=operation.get('deprecated', False)
        )
    
    def _parse_parameters(self, parameters: List[Dict[str, Any]]) -> List[Parameter]:
        """Parse parameter definitions."""
        parsed = []
        for param in parameters:
            # Handle $ref
            if '$ref' in param:
                param = self.resolve_ref(param['$ref'])
                
            parsed.append(Parameter(
                name=param['name'],
                location=param['in'],
                required=param.get('required', False),
                schema=param.get('schema', {}),
                description=param.get('description'),
                default=param.get('default')
            ))
        return parsed
    
    def _parse_request_body(self, request_body: Dict[str, Any]) -> RequestBody:
        """Parse request body definition."""
        # Handle $ref
        if '$ref' in request_body:
            request_body = self.resolve_ref(request_body['$ref'])
            
        return RequestBody(
            content_types=request_body.get('content', {}),
            required=request_body.get('required', False),
            description=request_body.get('description')
        )
    
    def resolve_ref(self, ref: str) -> Dict[str, Any]:
        """Resolve a $ref reference.
        
        Args:
            ref: Reference string like '#/components/schemas/CompanyDetails'
            
        Returns:
            The resolved object
        """
        if not ref.startswith('#/'):
            raise ValueError(f"Only local references are supported, got: {ref}")
            
        parts = ref[2:].split('/')
        current = self.spec
        
        for part in parts:
            if part in current:
                current = current[part]
            else:
                raise ValueError(f"Could not resolve reference: {ref}")
                
        return current
    
    def get_endpoints(self) -> List[EndpointDefinition]:
        """Get all endpoint definitions as a flat list."""
        all_endpoints = []
        for endpoints in self.parse().values():
            all_endpoints.extend(endpoints)
        return all_endpoints
    
    def parse_by_tags(self) -> Dict[str, List[EndpointDefinition]]:
        """Parse all endpoints and group by their tags.
        
        Returns:
            Dictionary mapping tag names to their endpoint definitions
        """
        endpoints_by_tag = {}
        
        for path, path_item in self.paths.items():
            # Skip parameter definitions
            if 'parameters' in path_item:
                path_parameters = self._parse_parameters(path_item['parameters'])
            else:
                path_parameters = []
            
            # Process each HTTP method
            for method in ['get', 'post', 'put', 'patch', 'delete', 'head', 'options']:
                if method not in path_item:
                    continue
                    
                operation = path_item[method]
                
                # Build endpoint definition
                endpoint = EndpointDefinition(
                    path=path,
                    method=method.upper(),
                    operation_id=operation.get('operationId'),
                    summary=operation.get('summary'),
                    description=operation.get('description'),
                    tags=operation.get('tags', ['Untagged']),
                    parameters=path_parameters + self._parse_parameters(
                        operation.get('parameters', [])
                    ),
                    request_body=self._parse_request_body(
                        operation.get('requestBody')
                    ) if 'requestBody' in operation else None,
                    responses=operation.get('responses', {})
                )
                
                # Group by tags
                for tag in endpoint.tags:
                    if tag not in endpoints_by_tag:
                        endpoints_by_tag[tag] = []
                    endpoints_by_tag[tag].append(endpoint)
        
        return endpoints_by_tag
    
    def get_schemas(self) -> Dict[str, Dict[str, Any]]:
        """Get all schema definitions."""
        return self.schemas.copy()
    
    def get_endpoint_by_operation_id(self, operation_id: str) -> Optional[EndpointDefinition]:
        """Find an endpoint by its operation ID."""
        for endpoint in self.get_endpoints():
            if endpoint.operation_id == operation_id:
                return endpoint
        return None