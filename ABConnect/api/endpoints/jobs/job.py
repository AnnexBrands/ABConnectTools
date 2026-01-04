"""Job API endpoints.

Provides access to core job operations including creation, retrieval,
search, and updates for shipping jobs in the ABConnect system.
"""

from typing import Optional, Dict, Any
from ABConnect.api.endpoints.base import BaseEndpoint
from ABConnect.api.routes import SCHEMA


class JobEndpoint(BaseEndpoint):
    """Core Job API operations.

    Handles job creation, retrieval, search, booking, and updates.
    """

    api_path = "job"
    routes = SCHEMA["JOB"]

    def get(self, jobDisplayId: str) -> Dict[str, Any]:
        """Retrieve a job by display ID.

        Args:
            jobDisplayId: The job display ID (e.g., '2000000')

        Returns:
            CalendarJob with full job details
        """
        route = self.routes['GET']
        route.params = {"jobDisplayId": str(jobDisplayId)}
        return self._make_request(route)

    def post(self, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Create a new job.

        Args:
            data: JobSaveRequestModel with job details

        Returns:
            ServiceBaseResponse with created job info
        """
        route = self.routes['POST']
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def put_save(self, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Save/update an existing job.

        Args:
            data: JobSaveRequest with updated job details

        Returns:
            ServiceBaseResponse with save confirmation
        """
        route = self.routes['PUT_SAVE']
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def post_book(self, jobDisplayId: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Book a job for shipping.

        Args:
            jobDisplayId: The job display ID
            data: Optional booking parameters

        Returns:
            ServiceBaseResponse with booking confirmation
        """
        route = self.routes['POST_BOOK']
        route.params = {"jobDisplayId": str(jobDisplayId)}
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def get_search(self, job_display_id: Optional[str] = None) -> Dict[str, Any]:
        """Search for jobs.

        Args:
            job_display_id: Optional job display ID filter

        Returns:
            List[SearchJobInfo] matching the search criteria
        """
        route = self.routes['GET_SEARCH']
        if job_display_id is not None:
            route.params = {"jobDisplayId": job_display_id}
        return self._make_request(route)

    def post_searchByDetails(self, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Search for jobs by detailed criteria.

        Args:
            data: SearchJobFilter with search parameters

        Returns:
            ServiceBaseResponse with matching jobs
        """
        route = self.routes['POST_SEARCH_BY_DETAILS']
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def get_calendaritems(self, jobDisplayId: str) -> Dict[str, Any]:
        """Get calendar items for a job.

        Args:
            jobDisplayId: The job display ID

        Returns:
            List[CalendarItem] for the job
        """
        route = self.routes['GET_CALENDARITEMS']
        route.params = {"jobDisplayId": str(jobDisplayId)}
        return self._make_request(route)

    def get_feedback(self, jobDisplayId: str) -> Dict[str, Any]:
        """Get feedback for a job.

        Args:
            jobDisplayId: The job display ID

        Returns:
            FeedbackSaveModel with job feedback
        """
        route = self.routes['GET_FEEDBACK']
        route.params = {"jobDisplayId": str(jobDisplayId)}
        return self._make_request(route)

    def post_feedback(self, jobDisplayId: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Submit feedback for a job.

        Args:
            jobDisplayId: The job display ID
            data: FeedbackSaveModel with feedback content

        Returns:
            ServiceBaseResponse confirming feedback submission
        """
        route = self.routes['POST_FEEDBACK']
        route.params = {"jobDisplayId": str(jobDisplayId)}
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def post_transfer(self, jobDisplayId: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Transfer a job to another agent/company.

        Args:
            jobDisplayId: The job display ID
            data: TransferModel with transfer details

        Returns:
            ServiceBaseResponse confirming transfer
        """
        route = self.routes['POST_TRANSFER']
        route.params = {"jobDisplayId": str(jobDisplayId)}
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def post_freightitems(self, jobDisplayId: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Save freight items for a job.

        Args:
            jobDisplayId: The job display ID
            data: SaveAllFreightItemsRequest with freight item details

        Returns:
            ServiceBaseResponse confirming save
        """
        route = self.routes['POST_FREIGHTITEMS']
        route.params = {"jobDisplayId": str(jobDisplayId)}
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def get_submanagementstatus(self, jobDisplayId: str) -> Dict[str, Any]:
        """Get sub-management status for a job.

        Args:
            jobDisplayId: The job display ID

        Returns:
            Sub-management status data
        """
        route = self.routes['GET_SUBMANAGEMENTSTATUS']
        route.params = {"jobDisplayId": str(jobDisplayId)}
        return self._make_request(route)

    def post_item_notes(self, jobDisplayId: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Add notes to job items.

        Args:
            jobDisplayId: The job display ID
            data: JobItemNotesData with note content

        Returns:
            ServiceBaseResponse confirming note creation
        """
        route = self.routes['POST_ITEM_NOTES']
        route.params = {"jobDisplayId": str(jobDisplayId)}
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def post_changeAgent(self, jobDisplayId: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Change the assigned agent for a job.

        Args:
            jobDisplayId: The job display ID
            data: ChangeJobAgentRequest with new agent info

        Returns:
            ServiceBaseResponse confirming agent change
        """
        route = self.routes['POST_CHANGE_AGENT']
        route.params = {"jobDisplayId": str(jobDisplayId)}
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def get_updatePageConfig(self, jobDisplayId: str) -> Dict[str, Any]:
        """Get page configuration for updating a job.

        Args:
            jobDisplayId: The job display ID

        Returns:
            JobUpdatePageConfig with UI configuration
        """
        route = self.routes['GET_UPDATE_PAGE_CONFIG']
        route.params = {"jobDisplayId": str(jobDisplayId)}
        return self._make_request(route)

    def get_price(self, jobDisplayId: str) -> Dict[str, Any]:
        """Get pricing information for a job.

        Args:
            jobDisplayId: The job display ID

        Returns:
            Price details for the job
        """
        route = self.routes['GET_PRICE']
        route.params = {"jobDisplayId": str(jobDisplayId)}
        return self._make_request(route)

    def get_jobAccessLevel(self, job_display_id: Optional[str] = None, job_item_id: Optional[str] = None) -> Dict[str, Any]:
        """Get access level for a job.

        Args:
            job_display_id: Optional job display ID
            job_item_id: Optional job item ID

        Returns:
            JobAccessLevel with permission details
        """
        route = self.routes['GET_JOB_ACCESS_LEVEL']
        params = {}
        if job_display_id is not None:
            params["jobDisplayId"] = job_display_id
        if job_item_id is not None:
            params["jobItemId"] = job_item_id
        if params:
            route.params = params
        return self._make_request(route)

    def get_documentConfig(self) -> Dict[str, Any]:
        """Get document configuration settings.

        Returns:
            Document configuration options
        """
        route = self.routes['GET_DOCUMENT_CONFIG']
        return self._make_request(route)

    def get_packagingcontainers(self, jobDisplayId: str) -> Dict[str, Any]:
        """Get packaging containers for a job.

        Args:
            jobDisplayId: The job display ID

        Returns:
            List[Packaging] with container details
        """
        route = self.routes['GET_PACKAGINGCONTAINERS']
        route.params = {"jobDisplayId": str(jobDisplayId)}
        return self._make_request(route)

    def put_item(self, jobDisplayId: str, itemId: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Update a job item.

        Args:
            jobDisplayId: The job display ID
            itemId: The item UUID to update
            data: JobItemInfoData with updated item details

        Returns:
            ServiceBaseResponse confirming update
        """
        route = self.routes['PUT_ITEM']
        route.params = {"jobDisplayId": str(jobDisplayId), "itemId": itemId}
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def post_status_quote(self, jobDisplayId: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Set job status to quote.

        Args:
            jobDisplayId: The job display ID
            data: Optional status data

        Returns:
            ServiceBaseResponse confirming status change
        """
        route = self.routes['POST_STATUS_QUOTE']
        route.params = {"jobDisplayId": str(jobDisplayId)}
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)
