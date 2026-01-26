"""Job Timeline API endpoints.

Provides access to job timeline operations including status tracking,
task management, and job status increments.
"""

from typing import Optional, Dict, Any, List
from ABConnect.api.endpoints.base import BaseEndpoint
from ABConnect.api.routes import SCHEMA
from ABConnect.api.models import (
    CarrierTask,
    CompanyListItem,
    DeleteTaskResponse,
    SaveResponseModel,
    ServiceBaseResponse,
    TimelineResponse,
    TaskCodes,
)
from ABConnect.api.models.shared import (
    InTheFieldTaskModel,
    SimpleTaskModel,
    CarrierTaskModel,
)
from ABConnect.api.models.dashboard import (
    IncrementJobStatusResponseModel,
)


class JobTimelineEndpoint(BaseEndpoint):
    """Job Timeline API endpoint operations.

    Handles timeline tasks, status changes, and increment operations.
    """

    api_path = "job"
    routes = SCHEMA["JOB"]

    def get_timeline(self, jobDisplayId: str) -> TimelineResponse:
        """Get all timeline tasks for a job.

        Args:
            jobDisplayId: The job display ID (e.g., '2000000')

        Returns:
            TimelineResponse: Timeline data with tasks, on-holds, and job status
        """
        route = self.routes['GET_TIMELINE_LIST']
        route.params = {"jobDisplayId": str(jobDisplayId)}
        return self._make_request(route)

    # Map task codes to their request models
    _TASK_MODELS = {
        TaskCodes.PICKUP: InTheFieldTaskModel,      # PU - Field/Pickup tasks
        TaskCodes.PACKAGING: SimpleTaskModel,       # PK - Packaging tasks
        TaskCodes.STORAGE: SimpleTaskModel,         # ST - Storage tasks
        TaskCodes.CARRIER: CarrierTaskModel,        # CP - Carrier tasks
        TaskCodes.DELIVERY: CarrierTaskModel,       # DE - Delivery tasks
    }

    def post_timeline(
        self,
        jobDisplayId: str,
        create_email: Optional[str] = None,
        data: Optional[Dict[str, Any]] = None
    ):
        """Create or update a timeline task for a job.

        Args:
            jobDisplayId: The job display ID
            create_email: Optional email creation flag
            data: Task data dict with taskCode and task-specific fields

        Returns:
            The created/updated task validated against the appropriate model
            (InTheFieldTaskModel, SimpleTaskModel, or CarrierTaskModel)

        Raises:
            ValueError: If taskCode is missing or invalid
        """
        if data is None:
            raise ValueError("data is required for post_timeline")

        # Get task code to determine request/response model
        task_code = data.get("taskCode")
        if not task_code:
            raise ValueError("taskCode is required in timeline task data")

        model_class = self._TASK_MODELS.get(task_code)
        if model_class is None:
            raise ValueError(f"Unknown taskCode: {task_code}. Expected one of: {list(self._TASK_MODELS.keys())}")

        # Validate request data and serialize to JSON-compatible dict
        validated_request = model_class.model_validate(data)
        json_data = validated_request.model_dump(mode='json', by_alias=True, exclude_none=True)

        # Build request
        route = self.routes['POST_TIMELINE']
        url = route.path.format(jobDisplayId=jobDisplayId)
        params = {"createEmail": create_email} if create_email is not None else None

        # Make raw request (bypass automatic response validation)
        response = self._r.call(route.method, url, json=json_data, params=params)

        # Validate response against the same model (API returns the task)
        return model_class.model_validate(response)

    def patch_timeline(
        self,
        timelineTaskId: str,
        jobDisplayId: str,
        data: Optional[Dict[str, Any]] = None
    ) -> ServiceBaseResponse:
        """Update an existing timeline task.

        Args:
            timelineTaskId: The timeline task ID to update
            jobDisplayId: The job display ID
            data: UpdateTaskModel with updated task details

        Returns:
            ServiceBaseResponse: Confirmation of update
        """
        route = self.routes['PATCH_TIMELINE']
        route.params = {
            "jobDisplayId": str(jobDisplayId),
            "timelineTaskId": str(timelineTaskId)
        }
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def delete_timeline(self, timelineTaskId: str, jobDisplayId: str) -> DeleteTaskResponse:
        """Delete a timeline task.

        Args:
            timelineTaskId: The timeline task ID to delete
            jobDisplayId: The job display ID

        Returns:
            DeleteTaskResponse: Confirmation of deletion with success status
        """
        route = self.routes['DELETE_TIMELINE']
        route.params = {
            "jobDisplayId": str(jobDisplayId),
            "timelineTaskId": str(timelineTaskId)
        }
        return self._make_request(route)

    def get_timeline_task(
        self,
        timelineTaskIdentifier: str,
        jobDisplayId: str
    ) -> CarrierTask:
        """Get a specific timeline task by identifier.

        Args:
            timelineTaskIdentifier: The task identifier
            jobDisplayId: The job display ID

        Returns:
            CarrierTask: Task details
        """
        route = self.routes['GET_TIMELINE']
        route.params = {
            "jobDisplayId": str(jobDisplayId),
            "timelineTaskIdentifier": str(timelineTaskIdentifier)
        }
        return self._make_request(route)

    def get_timeline_agent(self, taskCode: str, jobDisplayId: str) -> CompanyListItem:
        """Get the agent assigned to a timeline task.

        Args:
            taskCode: The task code
            jobDisplayId: The job display ID

        Returns:
            CompanyListItem: Agent company info
        """
        route = self.routes['GET_TIMELINE_AGENT']
        route.params = {
            "jobDisplayId": str(jobDisplayId),
            "taskCode": str(taskCode)
        }
        return self._make_request(route)

    def post_incrementjobstatus(
        self,
        jobDisplayId: str,
        data: Optional[Dict[str, Any]] = None
    ) -> IncrementJobStatusResponseModel:
        """Increment the job status to the next stage.

        Advances the job through its workflow stages (e.g., Quote -> Booked).

        Args:
            jobDisplayId: The job display ID
            data: Optional IncrementJobStatusInputModel

        Returns:
            IncrementJobStatusResponseModel: Success status and new job state
        """
        route = self.routes['POST_TIMELINE_INCREMENTJOBSTATUS']
        route.params = {"jobDisplayId": str(jobDisplayId)}
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def post_undoincrementjobstatus(
        self,
        jobDisplayId: str,
        data: Optional[Dict[str, Any]] = None
    ) -> ServiceBaseResponse:
        """Undo the last job status increment.

        Reverts the job to its previous workflow stage.

        Args:
            jobDisplayId: The job display ID
            data: Optional request data

        Returns:
            ServiceBaseResponse: Confirmation of undo operation
        """
        route = self.routes['POST_TIMELINE_UNDOINCREMENTJOBSTATUS']
        route.params = {"jobDisplayId": str(jobDisplayId)}
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)
