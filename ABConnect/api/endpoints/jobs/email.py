"""Job Email API endpoints.

Auto-generated from swagger.json specification.
"""

from typing import List, Optional, Dict, Any
from ABConnect.api.endpoints.base import BaseEndpoint


class JobEmailEndpoint(BaseEndpoint):
    """JobEmail API endpoint operations.

    Total endpoints: 4
    """

    api_path = "job"

    def post_email_senddocument(self, jobDisplayId: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """POST /api/job/{jobDisplayId}/email/senddocument

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/email/senddocument"
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)

    def post_email(self, jobDisplayId: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """POST /api/job/{jobDisplayId}/email

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/email"
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)

    def post_email_createtransactionalemail(self, jobDisplayId: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """POST /api/job/{jobDisplayId}/email/createtransactionalemail

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/email/createtransactionalemail"
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)

    def post_email_send(self, jobDisplayId: str, emailTemplateGuid: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """POST /api/job/{jobDisplayId}/email/{emailTemplateGuid}/send

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = f"/{jobDisplayId}/email/{emailTemplateGuid}/send"
        path = path.replace("{emailTemplateGuid}", str(emailTemplateGuid))
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
