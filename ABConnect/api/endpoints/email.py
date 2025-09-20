"""Email API endpoints.

Auto-generated from swagger.json specification.
Provides type-safe access to /api/email/* endpoints.
"""

from .base import BaseEndpoint


class EmailEndpoint(BaseEndpoint):
    """Email API endpoint operations.
    
    Handles all API operations for /api/email/* endpoints.
    Total endpoints: 1
    """
    
    api_path = "/api/email"

    def post_labelrequest(self, jobDisplayId: str) -> dict:
        """POST /api/email/{jobDisplayId}/labelrequest
        
        
        
        Returns:
            dict: API response data
        """
        path = "/{jobDisplayId}/labelrequest"
        path = path.replace("{jobDisplayId}", jobDisplayId)
        return self._make_request("POST", path, **kwargs)
