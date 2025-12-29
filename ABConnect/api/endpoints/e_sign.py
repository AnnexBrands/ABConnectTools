"""ESign API endpoints.

Auto-generated from swagger.json specification.
Provides type-safe access to e-sign/* endpoints.
"""

from typing import Optional
from ABConnect.api.endpoints.base import BaseEndpoint


class ESignEndpoint(BaseEndpoint):
    """ESign API endpoint operations.
    
    Handles all API operations for /api/e-sign/* endpoints.
    Total endpoints: 2
    """
    
    api_path = "e-sign"

    def get_get(self, jobDisplayId: str, bookingKey: str) -> dict:
        """GET /api/e-sign/{jobDisplayId}/{bookingKey}
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/{bookingKey}"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        path = path.replace("{bookingKey}", bookingKey)
        kwargs = {}
        return self._make_request("GET", path, **kwargs)
    def get_result(self, envelope: Optional[str] = None, event: Optional[str] = None) -> dict:
        """GET /api/e-sign/result
        
        
        
        Returns:
            dict: API response data
        """
        path = "/result"
        kwargs = {}
        params = {}
        if envelope is not None:
            params["envelope"] = envelope
        if event is not None:
            params["event"] = event
        if params:
            kwargs["params"] = params
        return self._make_request("GET", path, **kwargs)
