"""Job Sms API endpoints.

Auto-generated from swagger.json specification.
"""

from typing import List, Optional, Dict, Any
from ABConnect.api.endpoints.base import BaseEndpoint


class JobSmsEndpoint(BaseEndpoint):
    """JobSms API endpoint operations.

    Total endpoints: 3
    """

    api_path = "job"

    def get_sms(self, jobDisplayId: str) -> Dict[str, Any]:
        """GET /api/job/{jobDisplayId}/sms

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/sms"
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        return self._make_request("GET", path, **kwargs)

    def post_sms(self, jobDisplayId: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """POST /api/job/{jobDisplayId}/sms

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/sms"
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)

    def get_sms_templatebased(self, templateId: str, jobDisplayId: str) -> Dict[str, Any]:
        """GET /api/job/{jobDisplayId}/sms/templatebased/{templateId}

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/sms/templatebased/{templateId}"
        path = path.replace("{templateId}", str(templateId))
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        return self._make_request("GET", path, **kwargs)
