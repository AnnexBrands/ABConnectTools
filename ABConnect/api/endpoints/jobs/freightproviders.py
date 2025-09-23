"""Job Freightproviders API endpoints.

Auto-generated from swagger.json specification.
"""

from typing import List, Optional, Dict, Any
from ABConnect.api.endpoints.base import BaseEndpoint


class JobFreightProvidersEndpoint(BaseEndpoint):
    """JobFreightProviders API endpoint operations.

    Total endpoints: 3
    """

    api_path = "job"

    def post_freightproviders(self, jobDisplayId: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """POST /api/job/{jobDisplayId}/freightproviders

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/freightproviders"
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)

    def get_freightproviders(self, jobDisplayId: str, provider_indexes: Optional[str] = None, shipment_types: Optional[str] = None, only_active: Optional[str] = None) -> Dict[str, Any]:
        """GET /api/job/{jobDisplayId}/freightproviders

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/freightproviders"
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        params = {}
        if provider_indexes is not None:
            params["ProviderIndexes"] = provider_indexes
        if shipment_types is not None:
            params["ShipmentTypes"] = shipment_types
        if only_active is not None:
            params["OnlyActive"] = only_active
        if params:
            kwargs["params"] = params
        return self._make_request("GET", path, **kwargs)

    def post_freightproviders_ratequote(self, optionIndex: str, jobDisplayId: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """POST /api/job/{jobDisplayId}/freightproviders/{optionIndex}/ratequote

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/freightproviders/{optionIndex}/ratequote"
        path = path.replace("{optionIndex}", str(optionIndex))
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
