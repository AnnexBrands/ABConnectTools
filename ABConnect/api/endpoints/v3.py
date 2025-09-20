"""V3 API endpoints.

Auto-generated from swagger.json specification.
Provides type-safe access to v3/* endpoints.
"""

from typing import Optional
from .base import BaseEndpoint
# Model imports disabled
    # Model imports disabled


class V3Endpoint(BaseEndpoint):
    """V3 API endpoint operations.
    
    Handles all API operations for /api/v3/* endpoints.
    Total endpoints: 1
    """
    
    api_path = "v3"

    def get_job_tracking(self, jobDisplayId: str, historyAmount: str, history_amount: Optional[str] = None) -> dict:
        """GET /api/v3/job/{jobDisplayId}/tracking/{historyAmount}
        
        
        
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
