"""Values API endpoints.

Auto-generated from swagger.json specification.
Provides type-safe access to Values/* endpoints.
"""

from typing import Optional
from .base import BaseEndpoint


class ValuesEndpoint(BaseEndpoint):
    """Values API endpoint operations.
    
    Handles all API operations for /api/Values/* endpoints.
    Total endpoints: 1
    """
    
    api_path = "Values"

    def get_get(self, code: Optional[str] = None) -> dict:
        """GET /api/Values
        
        
        
        Returns:
            dict: API response data
        """
        path = "/"
        kwargs = {}
        params = {}
        if code is not None:
            params["code"] = code
        if params:
            kwargs["params"] = params
        return self._make_request("GET", path, **kwargs)
