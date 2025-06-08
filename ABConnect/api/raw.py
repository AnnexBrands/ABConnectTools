"""Raw endpoint access layer for direct API calls.

This module provides direct access to API endpoints without any abstraction,
allowing users to make raw HTTP calls to any endpoint in the API.
"""

from typing import Any, Dict, Optional, Union
import re


class RawEndpoint:
    """Direct access to API endpoints without abstraction.
    
    This class provides a way to call any API endpoint directly using
    the exact path and HTTP method from the swagger specification.
    
    Examples:
        >>> raw = RawEndpoint(request_handler)
        >>> raw.get('/api/companies/{id}/details', id='uuid-123')
        >>> raw.post('/api/job/{jobDisplayId}/book', jobDisplayId='123', data={...})
    """
    
    def __init__(self, request_handler):
        """Initialize raw endpoint.
        
        Args:
            request_handler: HTTP request handler instance
        """
        self._request_handler = request_handler
        
    def _substitute_path_params(self, path: str, **kwargs) -> tuple[str, dict]:
        """Substitute path parameters in the URL.
        
        Args:
            path: URL path with {param} placeholders
            **kwargs: All parameters including path params
            
        Returns:
            Tuple of (formatted_path, remaining_kwargs)
        """
        # Remove /api/ prefix if present (request handler adds base URL)
        if path.startswith('/api/'):
            path = path[5:]  # Remove '/api/'
        elif path.startswith('api/'):
            path = path[4:]  # Remove 'api/'
        
        # Find all path parameters
        path_params = re.findall(r'\{(\w+)\}', path)
        
        # Substitute path parameters
        formatted_path = path
        remaining_kwargs = kwargs.copy()
        
        for param in path_params:
            if param in kwargs:
                formatted_path = formatted_path.replace(
                    f'{{{param}}}', 
                    str(kwargs[param])
                )
                remaining_kwargs.pop(param)
        
        return formatted_path, remaining_kwargs
        
    def get(self, path: str, **kwargs) -> Any:
        """Make a GET request to the specified path.
        
        Args:
            path: API path (e.g., '/api/companies/{id}/details')
            **kwargs: Path parameters and query parameters
            
        Returns:
            API response
        """
        formatted_path, params = self._substitute_path_params(path, **kwargs)
        return self._request_handler.call('GET', formatted_path, params=params)
        
    def post(self, path: str, data: Optional[Dict] = None, **kwargs) -> Any:
        """Make a POST request to the specified path.
        
        Args:
            path: API path
            data: Request body data
            **kwargs: Path parameters and query parameters
            
        Returns:
            API response
        """
        formatted_path, params = self._substitute_path_params(path, **kwargs)
        return self._request_handler.call('POST', formatted_path, json=data, params=params)
        
    def put(self, path: str, data: Optional[Dict] = None, **kwargs) -> Any:
        """Make a PUT request to the specified path.
        
        Args:
            path: API path
            data: Request body data
            **kwargs: Path parameters and query parameters
            
        Returns:
            API response
        """
        formatted_path, params = self._substitute_path_params(path, **kwargs)
        return self._request_handler.call('PUT', formatted_path, json=data, params=params)
        
    def patch(self, path: str, data: Optional[Dict] = None, **kwargs) -> Any:
        """Make a PATCH request to the specified path.
        
        Args:
            path: API path
            data: Request body data
            **kwargs: Path parameters and query parameters
            
        Returns:
            API response
        """
        formatted_path, params = self._substitute_path_params(path, **kwargs)
        return self._request_handler.call('PATCH', formatted_path, json=data, params=params)
        
    def delete(self, path: str, **kwargs) -> Any:
        """Make a DELETE request to the specified path.
        
        Args:
            path: API path
            **kwargs: Path parameters and query parameters
            
        Returns:
            API response
        """
        formatted_path, params = self._substitute_path_params(path, **kwargs)
        return self._request_handler.call('DELETE', formatted_path, params=params)
        
    def call(self, method: str, path: str, data: Optional[Dict] = None, **kwargs) -> Any:
        """Make a request with any HTTP method.
        
        Args:
            method: HTTP method (GET, POST, PUT, PATCH, DELETE)
            path: API path
            data: Request body data (for POST, PUT, PATCH)
            **kwargs: Path parameters and query parameters
            
        Returns:
            API response
        """
        if method is None:
            raise ValueError("HTTP method is required")
            
        method = method.upper()
        if method == 'GET':
            return self.get(path, **kwargs)
        elif method == 'POST':
            return self.post(path, data=data, **kwargs)
        elif method == 'PUT':
            return self.put(path, data=data, **kwargs)
        elif method == 'PATCH':
            return self.patch(path, data=data, **kwargs)
        elif method == 'DELETE':
            return self.delete(path, **kwargs)
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")