"""Base endpoint class for all API endpoints.

This class provides the foundation for all API endpoint implementations.
It manages the HTTP request handler that is shared across all endpoints.

Attributes:
    _r: The HTTP request handler instance used for making API calls.

Example:
    All endpoint classes should inherit from BaseEndpoint::
    
        class MyEndpoint(BaseEndpoint):
            def get_resource(self, resource_id):
                return self._r('GET', f'/api/resource/{resource_id}')
"""


class BaseEndpoint:
    """Enhanced base class for all API endpoints.
    
    Maintains request handler inheritance while adding support for
    type-safe operations with Pydantic models.
    """
    
    _r = None
    api_path: str = ""
    
    def __init__(self):
        """Initialize endpoint instance."""
        if self._r is None:
            raise RuntimeError(
                "Request handler not set. Call BaseEndpoint.set_request_handler() first."
            )

    @classmethod
    def set_request_handler(cls, handler):
        """Set the HTTP request handler for all endpoints.
        
        This class method sets the request handler that will be used by all
        endpoint instances. It should be called once during API client
        initialization.
        
        Args:
            handler: The HTTP request handler callable. Should accept
                (method, path, **kwargs) and return the API response.
                
        Example:
            >>> from ABConnect.api.http_client import RequestHandler
            >>> handler = RequestHandler(base_url='https://api.example.com')
            >>> BaseEndpoint.set_request_handler(handler)
        """
        cls._r = handler
    
    def _make_request(self, method: str, path: str, **kwargs):
        """Make HTTP request using the shared request handler.
        
        Args:
            method: HTTP method (GET, POST, PUT, DELETE, etc.)
            path: API path (will be prefixed with api_path if relative)
            **kwargs: Additional arguments for the request
            
        Returns:
            API response data
        """
        # Handle relative vs absolute paths
        if not path.startswith('/api/'):
            path = f"{self.api_path.rstrip('/')}/{path.lstrip('/')}"
        
        return self._r(method, path, **kwargs)
