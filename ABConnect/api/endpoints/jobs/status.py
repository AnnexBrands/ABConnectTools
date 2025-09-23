"""Job Status API endpoints.

Auto-generated from swagger.json specification.
"""

from typing import List, Optional, Dict, Any
from ABConnect.api.endpoints.base import BaseEndpoint


class JobStatusEndpoint(BaseEndpoint):
    """JobStatus API endpoint operations.

    Total endpoints: 1
    """

    api_path = "job"

    def post_status_quote(self, jobDisplayId: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """POST /api/job/{jobDisplayId}/status/quote

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/status/quote"
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
