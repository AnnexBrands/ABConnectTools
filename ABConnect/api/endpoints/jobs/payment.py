"""Job Payment API endpoints.

Auto-generated from swagger.json specification.
"""

from typing import List, Optional, Dict, Any
from ABConnect.api.endpoints.base import BaseEndpoint


class JobPaymentEndpoint(BaseEndpoint):
    """JobPayment API endpoint operations.

    Total endpoints: 10
    """

    api_path = "job"

    def get_payment_create(self, jobDisplayId: str) -> Dict[str, Any]:
        """GET /api/job/{jobDisplayId}/payment/create

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/payment/create"
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        return self._make_request("GET", path, **kwargs)

    def post_payment_ACHPaymentSession(self, jobDisplayId: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """POST /api/job/{jobDisplayId}/payment/ACHPaymentSession

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/payment/ACHPaymentSession"
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)

    def post_payment_ACHCreditTransfer(self, jobDisplayId: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """POST /api/job/{jobDisplayId}/payment/ACHCreditTransfer

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/payment/ACHCreditTransfer"
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)

    def get_payment(self, jobDisplayId: str, job_sub_key: Optional[str] = None) -> Dict[str, Any]:
        """GET /api/job/{jobDisplayId}/payment

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/payment"
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        params = {}
        if job_sub_key is not None:
            params["jobSubKey"] = job_sub_key
        if params:
            kwargs["params"] = params
        return self._make_request("GET", path, **kwargs)

    def post_payment_attachCustomerBank(self, jobDisplayId: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """POST /api/job/{jobDisplayId}/payment/attachCustomerBank

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/payment/attachCustomerBank"
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)

    def post_payment_verifyJobACHSource(self, jobDisplayId: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """POST /api/job/{jobDisplayId}/payment/verifyJobACHSource

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/payment/verifyJobACHSource"
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)

    def post_payment_cancelJobACHVerification(self, jobDisplayId: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """POST /api/job/{jobDisplayId}/payment/cancelJobACHVerification

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/payment/cancelJobACHVerification"
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)

    def get_payment_sources(self, jobDisplayId: str) -> Dict[str, Any]:
        """GET /api/job/{jobDisplayId}/payment/sources

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/payment/sources"
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        return self._make_request("GET", path, **kwargs)

    def post_payment_bysource(self, jobDisplayId: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """POST /api/job/{jobDisplayId}/payment/bysource

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/payment/bysource"
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)

    def post_payment_banksource(self, jobDisplayId: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """POST /api/job/{jobDisplayId}/payment/banksource

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/payment/banksource"
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
