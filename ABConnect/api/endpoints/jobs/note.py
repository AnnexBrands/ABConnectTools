"""Job Note API endpoints.

Auto-generated from swagger.json specification.
"""

from typing import List, Optional, Dict, Any
from ABConnect.api.endpoints.base import BaseEndpoint


class JobNoteEndpoint(BaseEndpoint):
    """JobNote API endpoint operations.

    Total endpoints: 4
    """

    api_path = "job"

    def get_note(self, jobDisplayId: str, category: Optional[str] = None, task_code: Optional[str] = None) -> Dict[str, Any]:
        """GET /api/job/{jobDisplayId}/note

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/note"
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        params = {}
        if category is not None:
            params["category"] = category
        if task_code is not None:
            params["taskCode"] = task_code
        if params:
            kwargs["params"] = params
        return self._make_request("GET", path, **kwargs)

    def post_note(self, jobDisplayId: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """POST /api/job/{jobDisplayId}/note

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/note"
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)

    def get_note_by_id(self, id: str, jobDisplayId: str) -> Dict[str, Any]:
        """GET /api/job/{jobDisplayId}/note/{id}

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/note/{id}"
        path = path.replace("{id}", str(id))
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        return self._make_request("GET", path, **kwargs)

    def put_note(self, id: str, jobDisplayId: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """PUT /api/job/{jobDisplayId}/note/{id}

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/note/{id}"
        path = path.replace("{id}", str(id))
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("PUT", path, **kwargs)
