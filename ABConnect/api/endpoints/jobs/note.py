"""Job Note API endpoints.

Provides access to job note operations including creation,
retrieval, and updates.
"""

from typing import Optional, Dict, Any
from ABConnect.api.endpoints.base import BaseEndpoint
from ABConnect.api.routes import SCHEMA


class JobNoteEndpoint(BaseEndpoint):
    """Job Note API endpoint operations.

    Handles note creation, retrieval, and updates for jobs.
    """

    api_path = "job"
    routes = SCHEMA["JOB"]

    def get_note_list(
        self,
        jobDisplayId: str,
        category: Optional[str] = None,
        task_code: Optional[str] = None
    ) -> Dict[str, Any]:
        """Get all notes for a job.

        Args:
            jobDisplayId: The job display ID
            category: Optional category filter
            task_code: Optional task code filter

        Returns:
            List[JobTaskNote] with all notes
        """
        route = self.routes['GET_NOTE_LIST']
        route.params = {"jobDisplayId": str(jobDisplayId)}
        kwargs = {}
        params = {}
        if category is not None:
            params["category"] = category
        if task_code is not None:
            params["taskCode"] = task_code
        if params:
            kwargs["params"] = params
        return self._make_request(route, **kwargs)

    def get_note(self, jobDisplayId: str) -> Dict[str, Any]:
        """Alias for get_note_list for backwards compatibility.

        Args:
            jobDisplayId: The job display ID

        Returns:
            List[JobTaskNote] with all notes
        """
        return self.get_note_list(jobDisplayId)

    def post_note(
        self,
        jobDisplayId: str,
        data: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Create a new note for a job.

        Args:
            jobDisplayId: The job display ID
            data: TaskNoteModel with note content

        Returns:
            JobTaskNote with created note
        """
        route = self.routes['POST_NOTE']
        route.params = {"jobDisplayId": str(jobDisplayId)}
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def get_note_by_id(self, id: str, jobDisplayId: str) -> Dict[str, Any]:
        """Get a specific note by ID.

        Args:
            id: The note ID
            jobDisplayId: The job display ID

        Returns:
            JobTaskNote with note details
        """
        route = self.routes['GET_NOTE']
        route.params = {
            "jobDisplayId": str(jobDisplayId),
            "id": str(id)
        }
        return self._make_request(route)

    def put_note(
        self,
        id: str,
        jobDisplayId: str,
        data: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Update an existing note.

        Args:
            id: The note ID to update
            jobDisplayId: The job display ID
            data: TaskNoteModel with updated content

        Returns:
            ServiceBaseResponse confirming update
        """
        route = self.routes['PUT_NOTE']
        route.params = {
            "jobDisplayId": str(jobDisplayId),
            "id": str(id)
        }
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)
