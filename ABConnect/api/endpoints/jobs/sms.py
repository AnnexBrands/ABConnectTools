"""Job SMS API endpoints.

Provides access to job SMS operations including sending messages,
template-based messaging, and marking messages as read.
"""

from typing import Optional, Dict, Any
from ABConnect.api.endpoints.base import BaseEndpoint
from ABConnect.api.routes import SCHEMA


class JobSmsEndpoint(BaseEndpoint):
    """Job SMS API endpoint operations.

    Handles SMS message sending, retrieval, and status updates.
    """

    api_path = "job"
    routes = SCHEMA["JOB"]

    def get_sms(self, jobDisplayId: str) -> Dict[str, Any]:
        """Get SMS messages for a job.

        Args:
            jobDisplayId: The job display ID

        Returns:
            SMS message data for the job
        """
        route = self.routes['GET_SMS']
        route.params = {"jobDisplayId": str(jobDisplayId)}
        return self._make_request(route)

    def post_sms(
        self,
        jobDisplayId: str,
        data: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Send an SMS message for a job.

        Args:
            jobDisplayId: The job display ID
            data: SendSMSModel with message content

        Returns:
            ServiceBaseResponse confirming send
        """
        route = self.routes['POST_SMS']
        route.params = {"jobDisplayId": str(jobDisplayId)}
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def get_sms_templatebased(
        self,
        templateId: str,
        jobDisplayId: str
    ) -> Dict[str, Any]:
        """Get an SMS message based on a template.

        Args:
            templateId: The SMS template ID
            jobDisplayId: The job display ID

        Returns:
            SmsTemplateModel with populated template
        """
        route = self.routes['GET_SMS_TEMPLATEBASED']
        route.params = {
            "jobDisplayId": str(jobDisplayId),
            "templateId": str(templateId)
        }
        return self._make_request(route)

    def post_sms_read(
        self,
        jobDisplayId: str,
        data: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Mark SMS messages as read.

        Args:
            jobDisplayId: The job display ID
            data: MarkSmsAsReadModel with message IDs

        Returns:
            ServiceBaseResponse confirming update
        """
        route = self.routes['POST_SMS_READ']
        route.params = {"jobDisplayId": str(jobDisplayId)}
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)
