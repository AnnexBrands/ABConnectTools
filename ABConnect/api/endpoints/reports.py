"""Reports API endpoints.

Auto-generated from swagger.json specification.
Provides type-safe access to reports/* endpoints.
"""

from ABConnect.api.endpoints.base import BaseEndpoint


class ReportsEndpoint(BaseEndpoint):
    """Reports API endpoint operations.
    
    Handles all API operations for /api/reports/* endpoints.
    Total endpoints: 8
    """
    
    api_path = "reports"

    def post_insurance(self, data: dict = None) -> dict:
        """POST /api/reports/insurance
        
        
        
        Returns:
            dict: API response data
        """
        path = "/insurance"
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def post_sales(self, data: dict = None) -> dict:
        """POST /api/reports/sales
        
        
        
        Returns:
            dict: API response data
        """
        path = "/sales"
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def post_sales_summary(self, data: dict = None) -> dict:
        """POST /api/reports/sales/summary
        
        
        
        Returns:
            dict: API response data
        """
        path = "/sales/summary"
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def post_referredby(self, data: dict = None) -> dict:
        """POST /api/reports/referredBy
        
        
        
        Returns:
            dict: API response data
        """
        path = "/referredBy"
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def post_web2lead(self, data: dict = None) -> dict:
        """POST /api/reports/web2Lead
        
        
        
        Returns:
            dict: API response data
        """
        path = "/web2Lead"
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def post_toprevenuesalesreps(self, data: dict = None) -> dict:
        """POST /api/reports/topRevenueSalesReps
        
        
        
        Returns:
            dict: API response data
        """
        path = "/topRevenueSalesReps"
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def post_toprevenuecustomers(self, data: dict = None) -> dict:
        """POST /api/reports/topRevenueCustomers
        
        
        
        Returns:
            dict: API response data
        """
        path = "/topRevenueCustomers"
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
    def post_salesdrilldown(self, data: dict = None) -> dict:
        """POST /api/reports/salesDrilldown
        
        
        
        Returns:
            dict: API response data
        """
        path = "/salesDrilldown"
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
