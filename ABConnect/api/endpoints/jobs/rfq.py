"""Job Rfq API endpoints.

Auto-generated from swagger.json specification.
"""

from typing import List, Optional, Dict, Any
from ABConnect.api.endpoints.base import BaseEndpoint


class JobRfqEndpoint(BaseEndpoint):
    """JobRfq API endpoint operations.

    Total endpoints: 2
    """

    api_path = "job"

    def get_rfq(self, jobDisplayId: str, rfq_service_type: Optional[str] = None) -> Dict[str, Any]:
        """GET /api/job/{jobDisplayId}/rfq

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/rfq"
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        params = {}
        if rfq_service_type is not None:
            params["rfqServiceType"] = rfq_service_type
        if params:
            kwargs["params"] = params
        return self._make_request("GET", path, **kwargs)

    def get_rfq_statusof_forcompany(self, companyId: str, rfqServiceType: str, jobDisplayId: str) -> Dict[str, Any]:
        """GET /api/job/{jobDisplayId}/rfq/statusof/{rfqServiceType}/forcompany/{companyId}

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/rfq/statusof/{rfqServiceType}/forcompany/{companyId}"
        path = path.replace("{companyId}", str(companyId))
        path = path.replace("{rfqServiceType}", str(rfqServiceType))
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        return self._make_request("GET", path, **kwargs)
