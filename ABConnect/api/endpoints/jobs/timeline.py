"""Job Timeline API endpoints.

Auto-generated from swagger.json specification.
"""

from typing import List, Optional, Dict, Any
from ABConnect.api.endpoints.base import BaseEndpoint


class JobTimelineEndpoint(BaseEndpoint):
    """JobTimeline API endpoint operations.

    Total endpoints: 6
    """

    api_path = "job"

    def get_timeline(self, jobDisplayId: str) -> Dict[str, Any]:
        """GET /api/job/{jobDisplayId}/timeline

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/timeline"
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        return self._make_request("GET", path, **kwargs)

    def post_timeline(self, jobDisplayId: str, create_email: Optional[str] = None, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """POST /api/job/{jobDisplayId}/timeline

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/timeline"
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        params = {}
        if create_email is not None:
            params["createEmail"] = create_email
        if params:
            kwargs["params"] = params
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)

    def patch_timeline(self, timelineTaskId: str, jobDisplayId: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """PATCH /api/job/{jobDisplayId}/timeline/{timelineTaskId}

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/timeline/{timelineTaskId}"
        path = path.replace("{timelineTaskId}", str(timelineTaskId))
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("PATCH", path, **kwargs)

    def delete_timeline(self, timelineTaskId: str, jobDisplayId: str) -> Dict[str, Any]:
        """DELETE /api/job/{jobDisplayId}/timeline/{timelineTaskId}

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/timeline/{timelineTaskId}"
        path = path.replace("{timelineTaskId}", str(timelineTaskId))
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        return self._make_request("DELETE", path, **kwargs)

    def get_timeline_task(self, timelineTaskIdentifier: str, jobDisplayId: str) -> Dict[str, Any]:
        """GET /api/job/{jobDisplayId}/timeline/{timelineTaskIdentifier}

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/timeline/{timelineTaskIdentifier}"
        path = path.replace("{timelineTaskIdentifier}", str(timelineTaskIdentifier))
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        return self._make_request("GET", path, **kwargs)

    def get_timeline_agent(self, taskCode: str, jobDisplayId: str) -> Dict[str, Any]:
        """GET /api/job/{jobDisplayId}/timeline/{taskCode}/agent

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/timeline/{taskCode}/agent"
        path = path.replace("{taskCode}", str(taskCode))
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        return self._make_request("GET", path, **kwargs)
