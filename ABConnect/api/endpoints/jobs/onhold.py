"""Job Onhold API endpoints.

Auto-generated from swagger.json specification.
"""

from typing import List, Optional, Dict, Any
from ABConnect.api.endpoints.base import BaseEndpoint


class JobOnHoldEndpoint(BaseEndpoint):
    """JobOnHold API endpoint operations.

    Total endpoints: 10
    """

    api_path = "job"

    def get_onhold(self, jobDisplayId: str) -> Dict[str, Any]:
        """GET /api/job/{jobDisplayId}/onhold

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/onhold"
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        return self._make_request("GET", path, **kwargs)

    def post_onhold(self, jobDisplayId: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """POST /api/job/{jobDisplayId}/onhold

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/onhold"
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)

    def delete_onhold(self, jobDisplayId: str) -> Dict[str, Any]:
        """DELETE /api/job/{jobDisplayId}/onhold

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/onhold"
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        return self._make_request("DELETE", path, **kwargs)

    def get_onhold(self, jobDisplayId: str, id: str) -> Dict[str, Any]:
        """GET /api/job/{jobDisplayId}/onhold/{id}

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/onhold/{id}"
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        path = path.replace("{id}", str(id))
        kwargs = {}
        return self._make_request("GET", path, **kwargs)

    def put_onhold(self, jobDisplayId: str, onHoldId: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """PUT /api/job/{jobDisplayId}/onhold/{onHoldId}

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/onhold/{onHoldId}"
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        path = path.replace("{onHoldId}", str(onHoldId))
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("PUT", path, **kwargs)

    def put_onhold_resolve(self, jobDisplayId: str, onHoldId: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """PUT /api/job/{jobDisplayId}/onhold/{onHoldId}/resolve

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/onhold/{onHoldId}/resolve"
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        path = path.replace("{onHoldId}", str(onHoldId))
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("PUT", path, **kwargs)

    def post_onhold_comment(self, jobDisplayId: str, onHoldId: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """POST /api/job/{jobDisplayId}/onhold/{onHoldId}/comment

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/onhold/{onHoldId}/comment"
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        path = path.replace("{onHoldId}", str(onHoldId))
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)

    def get_onhold_followupusers(self, jobDisplayId: str) -> Dict[str, Any]:
        """GET /api/job/{jobDisplayId}/onhold/followupusers

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/onhold/followupusers"
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        return self._make_request("GET", path, **kwargs)

    def get_onhold_followupuser(self, jobDisplayId: str, contactId: str) -> Dict[str, Any]:
        """GET /api/job/{jobDisplayId}/onhold/followupuser/{contactId}

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/onhold/followupuser/{contactId}"
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        path = path.replace("{contactId}", str(contactId))
        kwargs = {}
        return self._make_request("GET", path, **kwargs)

    def put_onhold_dates(self, jobDisplayId: str, onHoldId: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """PUT /api/job/{jobDisplayId}/onhold/{onHoldId}/dates

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/onhold/{onHoldId}/dates"
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        path = path.replace("{onHoldId}", str(onHoldId))
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("PUT", path, **kwargs)
