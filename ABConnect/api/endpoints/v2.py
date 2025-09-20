"""V2 API endpoints.

Auto-generated from swagger.json specification.
Provides type-safe access to v2/* endpoints.
"""

from typing import Optional
from .base import BaseEndpoint


class V2Endpoint(BaseEndpoint):
    """V2 API endpoint operations.
    
    Handles all API operations for /api/v2/* endpoints.
    Total endpoints: 1
    """
    
    api_path = "v2"

    def get_job_tracking(self, jobDisplayId: str, historyAmount: str, history_amount: Optional[str] = None) -> dict:
        """GET /api/v2/job/{jobDisplayId}/tracking/{historyAmount}
        
        
        
        Returns:
            dict: API response data
        """
        path = "/job/{jobDisplayId}/tracking/{historyAmount}"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        path = path.replace("{historyAmount}", historyAmount)
        kwargs = {}
        params = {}
        if history_amount is not None:
            params["historyAmount"] = history_amount
        if params:
            kwargs["params"] = params
        return self._make_request("GET", path, **kwargs)
