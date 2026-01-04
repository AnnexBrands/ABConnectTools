"""Job Email API endpoints.

Provides access to job email operations including sending documents,
transactional emails, and template-based emails.
"""

from typing import Optional, Dict, Any
from ABConnect.api.endpoints.base import BaseEndpoint
from ABConnect.api.routes import SCHEMA


class JobEmailEndpoint(BaseEndpoint):
    """Job Email API endpoint operations.

    Handles email sending for documents and transactional emails.
    """

    api_path = "job"
    routes = SCHEMA["JOB"]

    def post_email(
        self,
        jobDisplayId: str,
        data: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Send an email for a job.

        Args:
            jobDisplayId: The job display ID
            data: SendDocumentEmailModel with email content

        Returns:
            ServiceBaseResponse confirming send
        """
        route = self.routes['POST_EMAIL']
        route.params = {"jobDisplayId": str(jobDisplayId)}
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def post_email_senddocument(
        self,
        jobDisplayId: str,
        data: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Send a document via email for a job.

        Args:
            jobDisplayId: The job display ID
            data: SendDocumentEmailModel with document and recipients

        Returns:
            ServiceBaseResponse confirming send
        """
        route = self.routes['POST_EMAIL_SENDDOCUMENT']
        route.params = {"jobDisplayId": str(jobDisplayId)}
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def post_email_createtransactionalemail(
        self,
        jobDisplayId: str,
        data: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Create a transactional email for a job.

        Args:
            jobDisplayId: The job display ID
            data: Optional transactional email parameters

        Returns:
            ServiceBaseResponse confirming creation
        """
        route = self.routes['POST_EMAIL_CREATETRANSACTIONALEMAIL']
        route.params = {"jobDisplayId": str(jobDisplayId)}
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def post_email_send(
        self,
        jobDisplayId: str,
        emailTemplateGuid: str,
        data: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Send an email using a template.

        Args:
            jobDisplayId: The job display ID
            emailTemplateGuid: The email template GUID
            data: Optional template variables

        Returns:
            ServiceBaseResponse confirming send
        """
        route = self.routes['POST_EMAIL_SEND']
        route.params = {
            "jobDisplayId": str(jobDisplayId),
            "emailTemplateGuid": str(emailTemplateGuid)
        }
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)
