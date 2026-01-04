"""Job Tracking API endpoints.

Provides access to job tracking operations including shipment
tracking and tracking history.
"""

from typing import Dict, Any
from ABConnect.api.endpoints.base import BaseEndpoint
from ABConnect.api.routes import SCHEMA


class JobTrackingEndpoint(BaseEndpoint):
    """Job Tracking API endpoint operations.

    Handles shipment tracking retrieval for jobs.
    """

    api_path = "job"
    routes = SCHEMA["JOB"]

    def get_tracking(self, jobDisplayId: str) -> Dict[str, Any]:
        """Get tracking information for a job.

        Args:
            jobDisplayId: The job display ID

        Returns:
            ShipmentTrackingDetails with tracking info
        """
        route = self.routes['GET_TRACKING']
        route.params = {"jobDisplayId": str(jobDisplayId)}
        return self._make_request(route)

    def get_tracking_shipment(
        self,
        proNumber: str,
        jobDisplayId: str
    ) -> Dict[str, Any]:
        """Get tracking information for a specific shipment.

        Args:
            proNumber: The PRO number of the shipment
            jobDisplayId: The job display ID

        Returns:
            ShipmentTrackingDetails for the specific shipment
        """
        route = self.routes['GET_TRACKING_SHIPMENT']
        route.params = {
            "jobDisplayId": str(jobDisplayId),
            "proNumber": str(proNumber)
        }
        return self._make_request(route)
