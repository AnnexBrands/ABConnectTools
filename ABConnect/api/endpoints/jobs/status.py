"""Job Status API endpoints.

Provides access to job status operations including
changing job status to quote.
"""

from typing import Optional, Dict, Any
from ABConnect.api.endpoints.base import BaseEndpoint
from ABConnect.api.routes import SCHEMA


class JobStatusEndpoint(BaseEndpoint):
    """Job Status API endpoint operations.

    Handles job status changes.
    """

    api_path = "job"
    routes = SCHEMA["JOB"]

    def post_status_quote(
        self,
        jobDisplayId: str,
        data: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Set job status to quote.

        Args:
            jobDisplayId: The job display ID
            data: Optional status change parameters

        Returns:
            ServiceBaseResponse confirming status change
        """
        route = self.routes['POST_STATUS_QUOTE']
        route.params = {"jobDisplayId": str(jobDisplayId)}
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)
