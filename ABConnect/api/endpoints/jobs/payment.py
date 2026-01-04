"""Job Payment API endpoints.

Provides access to job payment operations including ACH payments,
bank source management, and payment verification.
"""

from typing import Optional, Dict, Any
from ABConnect.api.endpoints.base import BaseEndpoint
from ABConnect.api.routes import SCHEMA


class JobPaymentEndpoint(BaseEndpoint):
    """Job Payment API endpoint operations.

    Handles payment creation, ACH operations, and bank source management.
    """

    api_path = "job"
    routes = SCHEMA["JOB"]

    def get_payment_create(self, jobDisplayId: str) -> Dict[str, Any]:
        """Get payment creation options for a job.

        Args:
            jobDisplayId: The job display ID

        Returns:
            Payment creation configuration
        """
        route = self.routes['GET_PAYMENT_CREATE']
        route.params = {"jobDisplayId": str(jobDisplayId)}
        return self._make_request(route)

    def post_payment_ACHPaymentSession(
        self,
        jobDisplayId: str,
        data: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Create an ACH payment session for a job.

        Args:
            jobDisplayId: The job display ID
            data: ACH payment session parameters

        Returns:
            ServiceBaseResponse with session info
        """
        route = self.routes['POST_PAYMENT_ACHPAYMENT_SESSION']
        route.params = {"jobDisplayId": str(jobDisplayId)}
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def post_payment_ACHCreditTransfer(
        self,
        jobDisplayId: str,
        data: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Initiate an ACH credit transfer for a job.

        Args:
            jobDisplayId: The job display ID
            data: ACH credit transfer parameters

        Returns:
            ServiceBaseResponse confirming transfer
        """
        route = self.routes['POST_PAYMENT_ACHCREDIT_TRANSFER']
        route.params = {"jobDisplayId": str(jobDisplayId)}
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def get_payment(
        self,
        jobDisplayId: str,
        job_sub_key: Optional[str] = None
    ) -> Dict[str, Any]:
        """Get payment information for a job.

        Args:
            jobDisplayId: The job display ID
            job_sub_key: Optional job sub key filter

        Returns:
            Payment details for the job
        """
        route = self.routes['GET_PAYMENT']
        route.params = {"jobDisplayId": str(jobDisplayId)}
        kwargs = {}
        if job_sub_key is not None:
            kwargs["params"] = {"jobSubKey": job_sub_key}
        return self._make_request(route, **kwargs)

    def post_payment_attachCustomerBank(
        self,
        jobDisplayId: str,
        data: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Attach a customer bank account to a job payment.

        Args:
            jobDisplayId: The job display ID
            data: AttachCustomerBankModel with bank details

        Returns:
            ServiceBaseResponse confirming attachment
        """
        route = self.routes['POST_PAYMENT_ATTACH_CUSTOMER_BANK']
        route.params = {"jobDisplayId": str(jobDisplayId)}
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def post_payment_verifyJobACHSource(
        self,
        jobDisplayId: str,
        data: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Verify an ACH source for a job payment.

        Args:
            jobDisplayId: The job display ID
            data: VerifyBankAccountRequest with verification data

        Returns:
            ServiceBaseResponse confirming verification
        """
        route = self.routes['POST_PAYMENT_VERIFY_JOB_ACHSOURCE']
        route.params = {"jobDisplayId": str(jobDisplayId)}
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def post_payment_cancelJobACHVerification(
        self,
        jobDisplayId: str,
        data: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Cancel an ACH verification for a job payment.

        Args:
            jobDisplayId: The job display ID
            data: Optional cancellation parameters

        Returns:
            ServiceBaseResponse confirming cancellation
        """
        route = self.routes['POST_PAYMENT_CANCEL_JOB_ACHVERIFICATION']
        route.params = {"jobDisplayId": str(jobDisplayId)}
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def get_payment_sources(self, jobDisplayId: str) -> Dict[str, Any]:
        """Get available payment sources for a job.

        Args:
            jobDisplayId: The job display ID

        Returns:
            List[PaymentSourceDetails] with available sources
        """
        route = self.routes['GET_PAYMENT_SOURCES']
        route.params = {"jobDisplayId": str(jobDisplayId)}
        return self._make_request(route)

    def post_payment_bysource(
        self,
        jobDisplayId: str,
        data: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Process a payment using a specific source.

        Args:
            jobDisplayId: The job display ID
            data: Payment source and amount details

        Returns:
            ServiceBaseResponse confirming payment
        """
        route = self.routes['POST_PAYMENT_BYSOURCE']
        route.params = {"jobDisplayId": str(jobDisplayId)}
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def post_payment_banksource(
        self,
        jobDisplayId: str,
        data: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Add a bank source for a job payment.

        Args:
            jobDisplayId: The job display ID
            data: PaymentSourceDetails with bank info

        Returns:
            ServiceBaseResponse confirming addition
        """
        route = self.routes['POST_PAYMENT_BANKSOURCE']
        route.params = {"jobDisplayId": str(jobDisplayId)}
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)
