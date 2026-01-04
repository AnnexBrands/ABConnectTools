"""Job Timeline API endpoints.

Provides access to job timeline operations including status tracking,
task management, and job status increments.
"""

from typing import Optional, Dict, Any
from ABConnect.api.endpoints.base import BaseEndpoint
from ABConnect.api.routes import SCHEMA


class JobTimelineEndpoint(BaseEndpoint):
    """Job Timeline API endpoint operations.

    Handles timeline tasks, status changes, and increment operations.
    """

    api_path = "job"
    routes = SCHEMA["JOB"]

    def get_timeline(self, jobDisplayId: str) -> Dict[str, Any]:
        """Get all timeline tasks for a job.

        Args:
            jobDisplayId: The job display ID (e.g., '2000000')

        Returns:
            List[CarrierTask] with all timeline tasks
        """
        route = self.routes['GET_TIMELINE_LIST']
        route.params = {"jobDisplayId": str(jobDisplayId)}
        return self._make_request(route)

    def post_timeline(
        self,
        jobDisplayId: str,
        create_email: Optional[str] = None,
        data: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Create a new timeline task for a job.

        Args:
            jobDisplayId: The job display ID
            create_email: Optional email creation flag
            data: TimelineTaskInput with task details

        Returns:
            SaveResponseModel with created task info
        """
        route = self.routes['POST_TIMELINE']
        route.params = {"jobDisplayId": str(jobDisplayId)}
        kwargs = {}
        if create_email is not None:
            kwargs["params"] = {"createEmail": create_email}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def patch_timeline(
        self,
        timelineTaskId: str,
        jobDisplayId: str,
        data: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Update an existing timeline task.

        Args:
            timelineTaskId: The timeline task ID to update
            jobDisplayId: The job display ID
            data: UpdateTaskModel with updated task details

        Returns:
            ServiceBaseResponse confirming update
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

    def delete_timeline(self, timelineTaskId: str, jobDisplayId: str) -> Dict[str, Any]:
        """Delete a timeline task.

        Args:
            timelineTaskId: The timeline task ID to delete
            jobDisplayId: The job display ID

        Returns:
            DeleteTaskResponse confirming deletion
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
    ) -> Dict[str, Any]:
        """Get a specific timeline task by identifier.

        Args:
            timelineTaskIdentifier: The task identifier
            jobDisplayId: The job display ID

        Returns:
            CarrierTask with task details
        """
        route = self.routes['GET_TIMELINE']
        route.params = {
            "jobDisplayId": str(jobDisplayId),
            "timelineTaskIdentifier": str(timelineTaskIdentifier)
        }
        return self._make_request(route)

    def get_timeline_agent(self, taskCode: str, jobDisplayId: str) -> Dict[str, Any]:
        """Get the agent assigned to a timeline task.

        Args:
            taskCode: The task code
            jobDisplayId: The job display ID

        Returns:
            CompanyListItem with agent company info
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
    ) -> Dict[str, Any]:
        """Increment the job status to the next stage.

        Advances the job through its workflow stages (e.g., Quote -> Booked).

        Args:
            jobDisplayId: The job display ID
            data: Optional IncrementJobStatusInputModel

        Returns:
            IncrementJobStatusResponseModel with success status
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
    ) -> Dict[str, Any]:
        """Undo the last job status increment.

        Reverts the job to its previous workflow stage.

        Args:
            jobDisplayId: The job display ID
            data: Optional request data

        Returns:
            ServiceBaseResponse confirming undo
        """
        route = self.routes['POST_TIMELINE_UNDOINCREMENTJOBSTATUS']
        route.params = {"jobDisplayId": str(jobDisplayId)}
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)
