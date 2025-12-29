"""Email API endpoints.

Auto-generated from swagger.json specification.
Provides type-safe access to email/* endpoints.
"""

from ABConnect.api.endpoints.base import BaseEndpoint


class EmailEndpoint(BaseEndpoint):
    """Email API endpoint operations.
    
    Handles all API operations for /api/email/* endpoints.
    Total endpoints: 1
    """
    
    api_path = "email"

    def post_labelrequest(self, jobDisplayId: str) -> dict:
        """POST /api/email/{jobDisplayId}/labelrequest
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/labelrequest"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        kwargs = {}
        return self._make_request("POST", path, **kwargs)
