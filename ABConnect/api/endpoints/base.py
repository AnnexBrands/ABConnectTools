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
    _r = None

    @classmethod
    def set_request_handler(cls, handler):
        """Set the HTTP request handler for all endpoints.
        
        This class method sets the request handler that will be used by all
        endpoint instances. It should be called once during API client
        initialization.
        
        Args:
            handler: The HTTP request handler callable. Should accept
                (method, path, **kwargs) and return the API response.
                
        Returns:
            None
            
        Example:
            >>> from ABConnect.api.http import HTTPClient
            >>> http_client = HTTPClient(base_url='https://api.example.com')
            >>> BaseEndpoint.set_request_handler(http_client.request)
        """
        cls._r = handler
