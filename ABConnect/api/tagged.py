"""Tag-based resource builder for grouping endpoints by swagger tags.

This module provides functionality to build resource classes based on
swagger tags, providing a more organized API structure.
"""

from typing import Any, Dict, List, Optional, Type, Callable
import re
from functools import wraps
from ABConnect.api.swagger import EndpointDefinition, SwaggerParser


class TaggedResource:
    """Base class for tag-based API resources.
    
    This class is extended dynamically with methods based on swagger endpoints
    that share the same tag.
    """
    
    def __init__(self, tag: str, request_handler):
        """Initialize tagged resource.
        
        Args:
            tag: The swagger tag this resource represents
            request_handler: HTTP request handler instance
        """
        self._tag = tag
        self._request_handler = request_handler
        self._endpoints: List[EndpointDefinition] = []
        
    def _call(self, method: str, path: str, **kwargs) -> Any:
        """Make an API call.
        
        Args:
            method: HTTP method
            path: API path with {param} placeholders
            **kwargs: Path parameters, query parameters, and data
            
        Returns:
            API response
        """
        # Separate path params, data, and query params
        path_params = {}
        query_params = {}
        data = kwargs.pop('data', None)
        json_data = kwargs.pop('json', data)
        
        # Extract path parameters
        import re
        path_param_names = re.findall(r'\{(\w+)\}', path)
        
        for param_name in path_param_names:
            if param_name in kwargs:
                path_params[param_name] = kwargs.pop(param_name)
        
        # Remaining kwargs are query parameters
        query_params = kwargs
        
        # Substitute path parameters
        formatted_path = path
        for param_name, param_value in path_params.items():
            formatted_path = formatted_path.replace(
                f'{{{param_name}}}', 
                str(param_value)
            )
        
        # Make the request
        if method in ['GET', 'DELETE']:
            return self._request_handler.call(
                method, 
                formatted_path, 
                params=query_params
            )
        else:
            return self._request_handler.call(
                method, 
                formatted_path, 
                json=json_data, 
                params=query_params
            )


def sanitize_name(name: str) -> str:
    """Convert a name to a valid Python identifier.
    
    Args:
        name: Original name (e.g., operation ID or path)
        
    Returns:
        Valid Python identifier
    """
    # Remove leading/trailing slashes and api prefix
    name = name.strip('/')
    if name.startswith('api/'):
        name = name[4:]
    
    # Replace path parameters with descriptive names
    name = re.sub(r'\{(\w+)\}', r'by_\1', name)
    
    # Replace special characters
    name = re.sub(r'[^a-zA-Z0-9_]', '_', name)
    
    # Remove consecutive underscores
    name = re.sub(r'_+', '_', name)
    
    # Remove leading/trailing underscores
    name = name.strip('_')
    
    # Ensure it starts with a letter
    if name and name[0].isdigit():
        name = 'op_' + name
    
    return name.lower()


def create_method(endpoint: EndpointDefinition) -> Callable:
    """Create a method for an endpoint definition.
    
    Args:
        endpoint: Endpoint definition from swagger
        
    Returns:
        Method that can be attached to a class
    """
    def method(self, **kwargs):
        """Auto-generated method from swagger endpoint."""
        return self._call(endpoint.method, endpoint.path, **kwargs)
    
    # Create a proper docstring
    docstring_parts = []
    
    if endpoint.summary:
        docstring_parts.append(endpoint.summary)
    
    if endpoint.description:
        docstring_parts.append("")
        docstring_parts.append(endpoint.description)
    
    # Document parameters
    if endpoint.parameters:
        docstring_parts.append("")
        docstring_parts.append("Args:")
        
        for param in endpoint.parameters:
            param_desc = f"    {param.name}: "
            if param.description:
                param_desc += param.description
            if param.required:
                param_desc += " (required)"
            if param.default is not None:
                param_desc += f" (default: {param.default})"
            docstring_parts.append(param_desc)
    
    if endpoint.request_body:
        if not endpoint.parameters:
            docstring_parts.append("")
            docstring_parts.append("Args:")
        docstring_parts.append("    data: Request body data")
        if endpoint.request_body.description:
            docstring_parts.append(f"        {endpoint.request_body.description}")
    
    docstring_parts.append("")
    docstring_parts.append("Returns:")
    docstring_parts.append("    API response")
    
    method.__doc__ = "\n".join(docstring_parts)
    method.__name__ = sanitize_name(endpoint.operation_id or endpoint.path)
    
    return method


class TaggedResourceBuilder:
    """Builder for creating tagged resource classes from swagger."""
    
    def __init__(self, swagger_parser: SwaggerParser):
        """Initialize the builder.
        
        Args:
            swagger_parser: Swagger parser instance
        """
        self.parser = swagger_parser
        self._resource_classes: Dict[str, Type[TaggedResource]] = {}
        
    def build(self) -> Dict[str, Type[TaggedResource]]:
        """Build resource classes for all tags.
        
        Returns:
            Dictionary mapping tag names to resource classes
        """
        endpoints_by_tag = self.parser.parse_by_tags()
        
        for tag, endpoints in endpoints_by_tag.items():
            # Create a sanitized class name
            class_name = self._tag_to_class_name(tag)
            
            # Create a new class inheriting from TaggedResource
            resource_class = type(
                class_name,
                (TaggedResource,),
                {
                    '__doc__': f"Auto-generated resource for tag: {tag}",
                    '_tag_name': tag,
                    '_endpoints': endpoints
                }
            )
            
            # Add methods for each endpoint
            for endpoint in endpoints:
                method_name = self._get_method_name(endpoint)
                if method_name and not hasattr(resource_class, method_name):
                    method = create_method(endpoint)
                    setattr(resource_class, method_name, method)
            
            self._resource_classes[self._tag_to_attribute_name(tag)] = resource_class
        
        return self._resource_classes
    
    def _tag_to_class_name(self, tag: str) -> str:
        """Convert tag to a class name.
        
        Args:
            tag: Swagger tag name
            
        Returns:
            Valid Python class name
        """
        # Remove spaces and special characters
        name = re.sub(r'[^a-zA-Z0-9]', '', tag)
        # Ensure it starts with uppercase
        return name[0].upper() + name[1:] + 'Resource' if name else 'UnknownResource'
    
    def _tag_to_attribute_name(self, tag: str) -> str:
        """Convert tag to an attribute name.
        
        Args:
            tag: Swagger tag name
            
        Returns:
            Valid Python attribute name (e.g., job_timeline)
        """
        # Convert to snake_case
        name = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1_\2', tag)
        name = re.sub(r'([a-z\d])([A-Z])', r'\1_\2', name)
        name = name.replace(' ', '_').replace('-', '_')
        return name.lower()
    
    def _get_method_name(self, endpoint: EndpointDefinition) -> Optional[str]:
        """Get a method name for an endpoint.
        
        Args:
            endpoint: Endpoint definition
            
        Returns:
            Method name or None if it can't be determined
        """
        # Prefer operation ID
        if endpoint.operation_id:
            return sanitize_name(endpoint.operation_id)
        
        # Fall back to path + method
        path_parts = endpoint.path.strip('/').split('/')
        # Remove 'api' prefix
        if path_parts and path_parts[0] == 'api':
            path_parts = path_parts[1:]
        
        # Remove tag-related parts
        if endpoint.tags:
            tag_parts = endpoint.tags[0].lower().split()
            path_parts = [p for p in path_parts if p.lower() not in tag_parts]
        
        # Create method name
        if not path_parts:
            return endpoint.method.lower()
        
        # Handle special cases
        if len(path_parts) == 1 and path_parts[0].startswith('{'):
            return f"{endpoint.method.lower()}_by_id"
        
        method_name = '_'.join(path_parts)
        if endpoint.method != 'GET':
            method_name = f"{endpoint.method.lower()}_{method_name}"
        
        return sanitize_name(method_name)