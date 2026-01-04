"""Job RFQ API endpoints.

Provides access to job RFQ (Request for Quote) operations
including retrieval and status checking.
"""

from typing import Optional, Dict, Any
from ABConnect.api.endpoints.base import BaseEndpoint
from ABConnect.api.routes import SCHEMA


class JobRfqEndpoint(BaseEndpoint):
    """Job RFQ API endpoint operations.

    Handles RFQ retrieval and status operations for jobs.
    """

    api_path = "job"
    routes = SCHEMA["JOB"]

    def get_rfq(
        self,
        jobDisplayId: str,
        rfq_service_type: Optional[str] = None
    ) -> Dict[str, Any]:
        """Get RFQ information for a job.

        Args:
            jobDisplayId: The job display ID
            rfq_service_type: Optional service type filter

        Returns:
            List[QuoteRequestDisplayInfo] with RFQ details
        """
        route = self.routes['GET_RFQ']
        route.params = {"jobDisplayId": str(jobDisplayId)}
        kwargs = {}
        if rfq_service_type is not None:
            kwargs["params"] = {"rfqServiceType": rfq_service_type}
        return self._make_request(route, **kwargs)

    def get_rfq_statusof_forcompany(
        self,
        companyId: str,
        rfqServiceType: str,
        jobDisplayId: str
    ) -> Dict[str, Any]:
        """Get RFQ status for a specific company.

        Args:
            companyId: The company ID
            rfqServiceType: The RFQ service type
            jobDisplayId: The job display ID

        Returns:
            QuoteRequestStatus with status details
        """
        route = self.routes['GET_RFQ_STATUSOF_FORCOMPANY']
        route.params = {
            "jobDisplayId": str(jobDisplayId),
            "rfqServiceType": str(rfqServiceType),
            "companyId": str(companyId)
        }
        return self._make_request(route)
