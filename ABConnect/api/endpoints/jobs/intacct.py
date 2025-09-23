"""Job Intacct API endpoints.

Auto-generated from swagger.json specification.
"""

from typing import List, Optional, Dict, Any
from ABConnect.api.endpoints.base import BaseEndpoint


class JobIntacctEndpoint(BaseEndpoint):
    """JobIntacct API endpoint operations.

    Total endpoints: 5
    """

    api_path = "job"

    def get_jobintacct(self, jobDisplayId: str) -> Dict[str, Any]:
        """GET /api/jobintacct/{jobDisplayId}

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "intacct/{jobDisplayId}"
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        return self._make_request("GET", path, **kwargs)

    def post_jobintacct(self, jobDisplayId: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """POST /api/jobintacct/{jobDisplayId}

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "intacct/{jobDisplayId}"
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)

    def post_jobintacct_draft(self, jobDisplayId: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """POST /api/jobintacct/{jobDisplayId}/draft

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "intacct/{jobDisplayId}/draft"
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)

    def delete_jobintacct(self, jobDisplayId: str, franchiseeId: str) -> Dict[str, Any]:
        """DELETE /api/jobintacct/{jobDisplayId}/{franchiseeId}

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "intacct/{jobDisplayId}/{franchiseeId}"
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        path = path.replace("{franchiseeId}", str(franchiseeId))
        kwargs = {}
        return self._make_request("DELETE", path, **kwargs)

    def post_jobintacct_applyRebate(self, jobDisplayId: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """POST /api/jobintacct/{jobDisplayId}/applyRebate

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "intacct/{jobDisplayId}/applyRebate"
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
