"""Query builder for fluent API interactions.

This module provides a query builder pattern for constructing complex
API queries with filtering, sorting, and pagination.
"""

from typing import Any, Dict, List, Optional, Union, TYPE_CHECKING
from urllib.parse import urlencode

if TYPE_CHECKING:
    from ABConnect.api.generic import GenericEndpoint


class QueryBuilder:
    """Fluent query builder for API requests.
    
    Enables method chaining to build complex queries with filters,
    sorting, pagination, and field selection.
    
    Example:
        >>> results = (api.companies.query()
        ...     .filter(type='Customer', active=True)
        ...     .sort('name', order='desc')
        ...     .page(2, per_page=50)
        ...     .select('id', 'name', 'type')
        ...     .execute())
    """
    
    def __init__(self, endpoint: 'GenericEndpoint'):
        """Initialize query builder.
        
        Args:
            endpoint: The endpoint to query against
        """
        self._endpoint = endpoint
        self._filters: Dict[str, Any] = {}
        self._sort_fields: List[str] = []
        self._page_num: int = 1
        self._per_page: int = 50
        self._selected_fields: List[str] = []
        self._expanded_relations: List[str] = []
        self._search_query: Optional[str] = None
        self._custom_params: Dict[str, Any] = {}
    
    def filter(self, **kwargs) -> 'QueryBuilder':
        """Add filters to the query.
        
        Multiple calls to filter() are combined with AND logic.
        
        Args:
            **kwargs: Field-value pairs to filter by
            
        Returns:
            Self for method chaining
            
        Example:
            >>> query.filter(status='active', type='Customer')
        """
        self._filters.update(kwargs)
        return self
    
    def where(self, field: str, operator: str, value: Any) -> 'QueryBuilder':
        """Add a filter with a specific operator.
        
        Args:
            field: Field name to filter on
            operator: Comparison operator (eq, ne, gt, gte, lt, lte, like, in)
            value: Value to compare against
            
        Returns:
            Self for method chaining
            
        Example:
            >>> query.where('created', 'gte', '2024-01-01')
            >>> query.where('status', 'in', ['active', 'pending'])
        """
        if operator == 'eq':
            self._filters[field] = value
        else:
            # Store with operator notation
            filter_key = f"{field}__{operator}"
            self._filters[filter_key] = value
        return self
    
    def search(self, query: str) -> 'QueryBuilder':
        """Add a search query.
        
        Args:
            query: Search string
            
        Returns:
            Self for method chaining
            
        Example:
            >>> query.search('john doe')
        """
        self._search_query = query
        return self
    
    def sort(self, field: str, order: str = 'asc') -> 'QueryBuilder':
        """Add sorting to the query.
        
        Multiple calls to sort() create multi-level sorting.
        
        Args:
            field: Field name to sort by
            order: Sort order ('asc' or 'desc')
            
        Returns:
            Self for method chaining
            
        Example:
            >>> query.sort('name').sort('created', 'desc')
        """
        if order.lower() == 'desc':
            self._sort_fields.append(f"-{field}")
        else:
            self._sort_fields.append(field)
        return self
    
    def order_by(self, *fields: str) -> 'QueryBuilder':
        """Alternative sorting method accepting multiple fields.
        
        Args:
            *fields: Field names to sort by. Prefix with '-' for descending
            
        Returns:
            Self for method chaining
            
        Example:
            >>> query.order_by('name', '-created')
        """
        self._sort_fields.extend(fields)
        return self
    
    def page(self, page: int, per_page: Optional[int] = None) -> 'QueryBuilder':
        """Set pagination parameters.
        
        Args:
            page: Page number (1-based)
            per_page: Items per page (optional)
            
        Returns:
            Self for method chaining
            
        Example:
            >>> query.page(3, per_page=25)
        """
        self._page_num = max(1, page)
        if per_page is not None:
            self._per_page = max(1, per_page)
        return self
    
    def limit(self, limit: int) -> 'QueryBuilder':
        """Set the maximum number of results.
        
        Args:
            limit: Maximum number of results
            
        Returns:
            Self for method chaining
            
        Example:
            >>> query.limit(10)
        """
        self._per_page = limit
        return self
    
    def offset(self, offset: int) -> 'QueryBuilder':
        """Set the result offset.
        
        Args:
            offset: Number of results to skip
            
        Returns:
            Self for method chaining
            
        Example:
            >>> query.offset(100)
        """
        # Convert offset to page number
        if self._per_page > 0:
            self._page_num = (offset // self._per_page) + 1
        return self
    
    def select(self, *fields: str) -> 'QueryBuilder':
        """Select specific fields to return.
        
        Args:
            *fields: Field names to include
            
        Returns:
            Self for method chaining
            
        Example:
            >>> query.select('id', 'name', 'email')
        """
        self._selected_fields.extend(fields)
        return self
    
    def expand(self, *relations: str) -> 'QueryBuilder':
        """Expand related resources.
        
        Args:
            *relations: Relation names to expand
            
        Returns:
            Self for method chaining
            
        Example:
            >>> query.expand('addresses', 'contacts')
        """
        self._expanded_relations.extend(relations)
        return self
    
    def param(self, name: str, value: Any) -> 'QueryBuilder':
        """Add a custom query parameter.
        
        Args:
            name: Parameter name
            value: Parameter value
            
        Returns:
            Self for method chaining
            
        Example:
            >>> query.param('include_deleted', True)
        """
        self._custom_params[name] = value
        return self
    
    def build(self) -> Dict[str, Any]:
        """Build the query parameters.
        
        Returns:
            Dictionary of query parameters
        """
        params = {}
        
        # Add filters
        params.update(self._filters)
        
        # Add search query
        if self._search_query:
            params['q'] = self._search_query
        
        # Add sorting
        if self._sort_fields:
            params['sort'] = ','.join(self._sort_fields)
        
        # Add pagination
        params['page'] = self._page_num
        params['per_page'] = self._per_page
        
        # Add field selection
        if self._selected_fields:
            params['fields'] = ','.join(self._selected_fields)
        
        # Add expansions
        if self._expanded_relations:
            params['expand'] = ','.join(self._expanded_relations)
        
        # Add custom parameters
        params.update(self._custom_params)
        
        # Remove None values
        return {k: v for k, v in params.items() if v is not None}
    
    def execute(self) -> Dict[str, Any]:
        """Execute the query and return results.
        
        Returns:
            API response data
            
        Raises:
            ABConnectError: If the query fails
        """
        params = self.build()
        return self._endpoint.list(**params)
    
    def first(self) -> Optional[Dict[str, Any]]:
        """Execute the query and return the first result.
        
        Returns:
            First result or None if no results
        """
        self.limit(1)
        results = self.execute()
        
        # Handle different response formats
        if isinstance(results, list):
            return results[0] if results else None
        elif isinstance(results, dict):
            # Check for common response formats
            if 'data' in results:
                data = results['data']
                return data[0] if data else None
            elif 'items' in results:
                items = results['items']
                return items[0] if items else None
            elif 'results' in results:
                results_list = results['results']
                return results_list[0] if results_list else None
        
        return None
    
    def count(self) -> int:
        """Get the count of results without fetching them.
        
        Returns:
            Number of results matching the query
        """
        # Add count-only parameter
        self.param('count_only', True).limit(1)
        response = self.execute()
        
        # Try to extract count from response
        if isinstance(response, dict):
            # Common count field names
            for field in ['total', 'count', 'total_count', 'totalCount']:
                if field in response:
                    return int(response[field])
        
        # Fallback: execute full query and count
        self.param('count_only', False)  # Remove count-only
        results = self.execute()
        if isinstance(results, list):
            return len(results)
        elif isinstance(results, dict) and 'data' in results:
            return len(results['data'])
        
        return 0
    
    def exists(self) -> bool:
        """Check if any results exist for the query.
        
        Returns:
            True if results exist, False otherwise
        """
        return self.count() > 0
    
    def __iter__(self):
        """Make the query builder iterable.
        
        Yields:
            Individual results from the query
        """
        current_page = 1
        while True:
            self.page(current_page)
            results = self.execute()
            
            # Extract items from response
            items = []
            if isinstance(results, list):
                items = results
            elif isinstance(results, dict):
                if 'data' in results:
                    items = results['data']
                elif 'items' in results:
                    items = results['items']
                elif 'results' in results:
                    items = results['results']
            
            # Yield items
            for item in items:
                yield item
            
            # Check if there are more pages
            if not items or len(items) < self._per_page:
                break
                
            current_page += 1
    
    def __repr__(self) -> str:
        """String representation of the query."""
        params = self.build()
        return f"QueryBuilder({self._endpoint.resource_name}, params={params})"