"""Job Form API endpoints.

Auto-generated from swagger.json specification.
"""

from typing import List, Optional, Dict, Any
from ABConnect.api.endpoints.base import BaseEndpoint


class JobFormEndpoint(BaseEndpoint):
    """JobForm API endpoint operations.

    Total endpoints: 2
    """

    api_path = "job"

    def get_form_shipments(self, jobDisplayId: str) -> Dict[str, Any]:
        """GET /api/job/{jobDisplayId}/form/shipments

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/form/shipments"
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        return self._make_request("GET", path, **kwargs)

    def get_form(self, formId: str, jobDisplayId: str, type: Optional[str] = None, shipment_plan_i_d: Optional[str] = None) -> Dict[str, Any]:
        """GET /api/job/{jobDisplayId}/form/{formid}

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/form/{formid}"
        path = path.replace("{formId}", str(formId))
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        params = {}
        if type is not None:
            params["type"] = type
        if shipment_plan_i_d is not None:
            params["shipmentPlanID"] = shipment_plan_i_d
        if params:
            kwargs["params"] = params
        return self._make_request("GET", path, **kwargs)
