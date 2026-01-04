"""Job OnHold API endpoints.

Provides access to job on-hold operations including creation, resolution,
and follow-up user management.
"""

from typing import Optional, Dict, Any
from ABConnect.api.endpoints.base import BaseEndpoint
from ABConnect.api.routes import SCHEMA


class JobOnHoldEndpoint(BaseEndpoint):
    """Job OnHold API endpoint operations.

    Handles on-hold creation, updates, resolution, and comments.
    """

    api_path = "job"
    routes = SCHEMA["JOB"]

    def get_onhold_list(self, jobDisplayId: str) -> Dict[str, Any]:
        """Get all on-hold items for a job.

        Args:
            jobDisplayId: The job display ID

        Returns:
            List[OnHoldDetails] with all on-hold items
        """
        route = self.routes['GET_ONHOLD_LIST']
        route.params = {"jobDisplayId": str(jobDisplayId)}
        return self._make_request(route)

    def get_onhold(self, jobDisplayId: str, id: str) -> Dict[str, Any]:
        """Get a specific on-hold item by ID.

        Args:
            jobDisplayId: The job display ID
            id: The on-hold item ID

        Returns:
            OnHoldDetails for the specified on-hold
        """
        route = self.routes['GET_ONHOLD']
        route.params = {"jobDisplayId": str(jobDisplayId), "id": str(id)}
        return self._make_request(route)

    def post_onhold(
        self,
        jobDisplayId: str,
        data: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Create a new on-hold item for a job.

        Args:
            jobDisplayId: The job display ID
            data: SaveOnHoldRequest with on-hold details

        Returns:
            SaveOnHoldResponse with created on-hold info
        """
        route = self.routes['POST_ONHOLD']
        route.params = {"jobDisplayId": str(jobDisplayId)}
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def delete_onhold(self, jobDisplayId: str) -> Dict[str, Any]:
        """Delete an on-hold item from a job.

        Args:
            jobDisplayId: The job display ID

        Returns:
            ServiceBaseResponse confirming deletion
        """
        route = self.routes['DELETE_ONHOLD']
        route.params = {"jobDisplayId": str(jobDisplayId)}
        return self._make_request(route)

    def put_onhold(
        self,
        jobDisplayId: str,
        onHoldId: str,
        data: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Update an existing on-hold item.

        Args:
            jobDisplayId: The job display ID
            onHoldId: The on-hold item ID to update
            data: SaveOnHoldRequest with updated details

        Returns:
            SaveOnHoldResponse confirming update
        """
        route = self.routes['PUT_ONHOLD']
        route.params = {
            "jobDisplayId": str(jobDisplayId),
            "onHoldId": str(onHoldId)
        }
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def put_onhold_resolve(
        self,
        jobDisplayId: str,
        onHoldId: str,
        data: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Resolve an on-hold item.

        Args:
            jobDisplayId: The job display ID
            onHoldId: The on-hold item ID to resolve
            data: SaveOnHoldRequest with resolution details

        Returns:
            ResolveJobOnHoldResponse confirming resolution
        """
        route = self.routes['PUT_ONHOLD_RESOLVE']
        route.params = {
            "jobDisplayId": str(jobDisplayId),
            "onHoldId": str(onHoldId)
        }
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def post_onhold_comment(
        self,
        jobDisplayId: str,
        onHoldId: str,
        data: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Add a comment to an on-hold item.

        Args:
            jobDisplayId: The job display ID
            onHoldId: The on-hold item ID
            data: Comment content

        Returns:
            OnHoldNoteDetails with created comment
        """
        route = self.routes['POST_ONHOLD_COMMENT']
        route.params = {
            "jobDisplayId": str(jobDisplayId),
            "onHoldId": str(onHoldId)
        }
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def get_onhold_followupusers(self, jobDisplayId: str) -> Dict[str, Any]:
        """Get all follow-up users for on-hold items.

        Args:
            jobDisplayId: The job display ID

        Returns:
            List[OnHoldUser] with available follow-up users
        """
        route = self.routes['GET_ONHOLD_FOLLOWUPUSERS']
        route.params = {"jobDisplayId": str(jobDisplayId)}
        return self._make_request(route)

    def get_onhold_followupuser(
        self,
        jobDisplayId: str,
        contactId: str
    ) -> Dict[str, Any]:
        """Get a specific follow-up user by contact ID.

        Args:
            jobDisplayId: The job display ID
            contactId: The contact ID of the follow-up user

        Returns:
            OnHoldUser details
        """
        route = self.routes['GET_ONHOLD_FOLLOWUPUSER']
        route.params = {
            "jobDisplayId": str(jobDisplayId),
            "contactId": str(contactId)
        }
        return self._make_request(route)

    def put_onhold_dates(
        self,
        jobDisplayId: str,
        onHoldId: str,
        data: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Update dates for an on-hold item.

        Args:
            jobDisplayId: The job display ID
            onHoldId: The on-hold item ID
            data: SaveOnHoldDatesModel with date updates

        Returns:
            ResolveJobOnHoldResponse confirming update
        """
        route = self.routes['PUT_ONHOLD_DATES']
        route.params = {
            "jobDisplayId": str(jobDisplayId),
            "onHoldId": str(onHoldId)
        }
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)
