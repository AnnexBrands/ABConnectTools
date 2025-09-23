"""Job Tracking API endpoints.

Auto-generated from swagger.json specification.
"""

from typing import List, Optional, Dict, Any
from ABConnect.api.endpoints.base import BaseEndpoint


class JobTrackingEndpoint(BaseEndpoint):
    """JobTracking API endpoint operations.

    Total endpoints: 2
    """

    api_path = "job"

    def get_tracking(self, jobDisplayId: str) -> Dict[str, Any]:
        """GET /api/job/{jobDisplayId}/tracking

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/tracking"
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        return self._make_request("GET", path, **kwargs)

    def get_tracking_shipment(self, proNumber: str, jobDisplayId: str) -> Dict[str, Any]:
        """GET /api/job/{jobDisplayId}/tracking/shipment/{proNumber}

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/tracking/shipment/{proNumber}"
        path = path.replace("{proNumber}", str(proNumber))
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        return self._make_request("GET", path, **kwargs)
