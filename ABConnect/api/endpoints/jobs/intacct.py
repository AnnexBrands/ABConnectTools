"""Job Intacct API endpoints.

Provides access to Intacct integration operations for jobs
including invoice creation, drafts, and rebates.
"""

from typing import Optional, Dict, Any
from ABConnect.api.endpoints.base import BaseEndpoint
from ABConnect.api.routes import SCHEMA


class JobIntacctEndpoint(BaseEndpoint):
    """Job Intacct API endpoint operations.

    Handles Intacct ERP integration for job invoicing.
    """

    api_path = "jobintacct"
    routes = SCHEMA["JOBINTACCT"]

    def get_jobintacct(self, jobDisplayId: str) -> Dict[str, Any]:
        """Get Intacct invoice data for a job.

        Args:
            jobDisplayId: The job display ID

        Returns:
            CreateJobIntacctModel with invoice data
        """
        route = self.routes['GET']
        route.params = {"jobDisplayId": str(jobDisplayId)}
        return self._make_request(route)

    def post_jobintacct(
        self,
        jobDisplayId: str,
        data: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Create an Intacct invoice for a job.

        Args:
            jobDisplayId: The job display ID
            data: CreateJobIntacctModel with invoice details

        Returns:
            ServiceBaseResponse confirming creation
        """
        route = self.routes['POST']
        route.params = {"jobDisplayId": str(jobDisplayId)}
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def post_jobintacct_draft(
        self,
        jobDisplayId: str,
        data: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Create a draft Intacct invoice for a job.

        Args:
            jobDisplayId: The job display ID
            data: CreateJobIntacctModel with invoice details

        Returns:
            ServiceBaseResponse confirming draft creation
        """
        route = self.routes['DRAFT']
        route.params = {"jobDisplayId": str(jobDisplayId)}
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def delete_jobintacct(
        self,
        jobDisplayId: str,
        franchiseeId: str
    ) -> Dict[str, Any]:
        """Delete an Intacct invoice for a job.

        Args:
            jobDisplayId: The job display ID
            franchiseeId: The franchisee ID

        Returns:
            ServiceBaseResponse confirming deletion
        """
        route = self.routes['DELETE']
        route.params = {
            "jobDisplayId": str(jobDisplayId),
            "franchiseeId": str(franchiseeId)
        }
        return self._make_request(route)

    def post_jobintacct_applyRebate(
        self,
        jobDisplayId: str,
        data: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Apply a rebate to a job's Intacct invoice.

        Args:
            jobDisplayId: The job display ID
            data: Optional rebate parameters

        Returns:
            ServiceBaseResponse confirming rebate application
        """
        route = self.routes['APPLY_REBATE']
        route.params = {"jobDisplayId": str(jobDisplayId)}
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)
