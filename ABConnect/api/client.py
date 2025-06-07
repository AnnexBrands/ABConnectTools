from typing import Optional, Dict, Type, Any, List
import logging
import os

from ABConnect.config import Config
from ABConnect.api.endpoints import (
    BaseEndpoint,
    CompaniesEndpoint,
    ContactsEndpoint,
    DocsEndpoint,
    FormsEndpoint,
    ItemsEndpoint,
    JobsEndpoint,
    TasksEndpoint,
    UsersEndpoint,
)

from .auth import FileTokenStorage, SessionTokenStorage
from .http import RequestHandler
from .swagger import SwaggerParser
from .builder import EndpointBuilder
from .generic import GenericEndpoint

logger = logging.getLogger(__name__)


class ABConnectAPI:
    """Main API client for ABConnect with automatic endpoint discovery.
    
    This client provides access to all API endpoints, both manually implemented
    and automatically generated from the OpenAPI specification.
    
    Attributes:
        users: User management endpoints
        companies: Company management endpoints
        contacts: Contact management endpoints
        docs: Document management endpoints
        forms: Form management endpoints
        items: Item management endpoints
        jobs: Job management endpoints
        tasks: Task management endpoints
        
    Additional endpoints are automatically discovered and available as attributes.
    """
    
    def __init__(self, request=None, enable_generic: bool = True, env: Optional[str] = None):
        """Initialize the API client.
        
        Args:
            request: Optional Django request object for session-based token storage
            enable_generic: Whether to enable automatic endpoint generation from swagger
            env: Environment to use ('staging' or 'production'). If not specified,
                 uses ABC_ENVIRONMENT from config or defaults to 'production'
        """
        # Handle environment configuration
        if env:
            # Temporarily set the environment
            os.environ['ABC_ENVIRONMENT'] = env
            # If already loaded from a staging env file, don't reload from default
            if not (Config._loaded and '.staging' in Config._env_file):
                Config._loaded = False  # Force config reload
                Config.load()  # Reload with new environment
        
        # Set up token storage
        token_storage = SessionTokenStorage(request) if request else FileTokenStorage()
        
        # Initialize request handler
        self._request_handler = RequestHandler(token_storage)
        BaseEndpoint.set_request_handler(self._request_handler)
        
        # Initialize manual endpoints
        self._init_manual_endpoints()
        
        # Initialize generic endpoints if enabled
        self._generic_endpoints: Dict[str, GenericEndpoint] = {}
        self._swagger_parser: Optional[SwaggerParser] = None
        self._endpoint_builder: Optional[EndpointBuilder] = None
        
        if enable_generic:
            try:
                self._init_generic_endpoints()
            except Exception as e:
                logger.warning(f"Failed to initialize generic endpoints: {e}")
                logger.info("Manual endpoints are still available")
    
    def _init_manual_endpoints(self):
        """Initialize manually implemented endpoints."""
        self.users = UsersEndpoint()
        self.companies = CompaniesEndpoint()
        self.contacts = ContactsEndpoint()
        self.docs = DocsEndpoint()
        self.forms = FormsEndpoint()
        self.items = ItemsEndpoint()
        self.jobs = JobsEndpoint()
        self.tasks = TasksEndpoint()
    
    def _init_generic_endpoints(self):
        """Initialize automatically generated endpoints from swagger."""
        try:
            # Parse swagger specification
            self._swagger_parser = SwaggerParser()
            
            # Build endpoint classes
            self._endpoint_builder = EndpointBuilder(self._swagger_parser)
            endpoint_classes = self._endpoint_builder.build_from_swagger()
            
            # Create instances
            for resource_name, endpoint_class in endpoint_classes.items():
                # Skip if we already have a manual implementation
                if hasattr(self, resource_name):
                    # Enhance manual endpoint with generic capabilities
                    manual_endpoint = getattr(self, resource_name)
                    # Store reference to swagger parser for dynamic methods
                    manual_endpoint._swagger_parser = self._swagger_parser
                    manual_endpoint._resource_name = resource_name
                    continue
                
                # Create generic endpoint instance
                endpoint_instance = endpoint_class(resource_name, self._swagger_parser)
                self._generic_endpoints[resource_name] = endpoint_instance
                
                # Make it available as an attribute
                setattr(self, resource_name, endpoint_instance)
                
            logger.info(f"Initialized {len(self._generic_endpoints)} generic endpoints")
            
        except Exception as e:
            logger.error(f"Error initializing generic endpoints: {e}")
            raise
    
    def __getattr__(self, name: str) -> Any:
        """Allow dynamic access to endpoints not explicitly defined.
        
        This enables access to any endpoint in the API specification,
        even if it wasn't discovered during initialization.
        
        Args:
            name: Endpoint or resource name
            
        Returns:
            Endpoint instance or raises AttributeError
        """
        # Check if it's in generic endpoints
        if name in self._generic_endpoints:
            return self._generic_endpoints[name]
        
        # Try to create it dynamically if we have swagger parser
        if self._swagger_parser and self._endpoint_builder:
            # Check if this resource exists in swagger
            all_resources = self._swagger_parser.parse()
            if name in all_resources:
                # Create endpoint class and instance
                endpoint_class = self._endpoint_builder.create_endpoint_class(
                    name, all_resources[name]
                )
                endpoint_instance = endpoint_class(name, self._swagger_parser)
                
                # Cache it
                self._generic_endpoints[name] = endpoint_instance
                setattr(self, name, endpoint_instance)
                
                return endpoint_instance
        
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")
    
    def raw(self, method: str, path: str, **kwargs) -> Any:
        """Execute a raw API request.
        
        This method provides direct access to any API endpoint without
        going through the endpoint classes.
        
        Args:
            method: HTTP method (GET, POST, PUT, DELETE, etc.)
            path: API path (e.g., '/api/companies/search')
            **kwargs: Additional request parameters
            
        Returns:
            API response data
            
        Example:
            >>> client.raw('GET', '/api/companies/search', params={'q': 'test'})
        """
        return self._request_handler.call(method.upper(), path, **kwargs)
    
    @property
    def available_endpoints(self) -> List[str]:
        """Get list of all available endpoints.
        
        Returns:
            List of endpoint names (both manual and generic)
        """
        endpoints = []
        
        # Manual endpoints
        manual = ['users', 'companies', 'contacts', 'docs', 'forms', 'items', 'jobs', 'tasks']
        endpoints.extend(manual)
        
        # Generic endpoints
        endpoints.extend(self._generic_endpoints.keys())
        
        return sorted(set(endpoints))
