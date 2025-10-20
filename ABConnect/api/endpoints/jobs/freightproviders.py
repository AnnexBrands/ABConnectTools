
"""Job Freightproviders API endpoints.

Auto-generated from swagger.json specification.
"""

from typing import List, Optional, Dict, Any
from pydantic import TypeAdapter

from ABConnect.api.endpoints.base import BaseEndpoint
from ABConnect.api.models.jobfreightproviders import PricedFreightProvider, ServiceBaseResponse, ShipmentPlanProvider, SetRateModel

class JobFreightProvidersEndpoint(BaseEndpoint):
    """JobFreightProviders API endpoint operations.

    Total endpoints: 3
    """

    api_path = "job"

    def post_freightproviders(self, jobDisplayId: str, data: Optional[List[Dict[str, Any]]] = None) -> Dict[str, Any]:
        """POST /api/job/{jobDisplayId}/freightproviders

        Args:
            jobDisplayId: The job display ID
            data: List of ShipmentPlanProvider objects (as dicts or models)

        Returns:
            Dict[str, Any]: ServiceBaseResponse as dict (validated)
        """
        path = f"/{jobDisplayId}/freightproviders"

        kwargs = {}
        if data is not None:
            # Validate incoming data and convert to API format
            validated_data = ShipmentPlanProvider.check(data)
            kwargs["json"] = validated_data

        response = self._make_request("POST", path, **kwargs)
        validated_response = ServiceBaseResponse.model_validate(response)
        return validated_response.model_dump(by_alias=True)

    def get_freightproviders(self, jobDisplayId: str, provider_indexes: Optional[str] = None, shipment_types: Optional[str] = None, only_active: Optional[str] = None) -> Dict[str, Any]:
        """GET /api/job/{jobDisplayId}/freightproviders

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = f"/{jobDisplayId}/freightproviders"
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
        
        response = self._make_request("GET", path, **kwargs)
        providers = TypeAdapter(list[PricedFreightProvider]).validate_python(response)
        return [p.model_dump(by_alias=True) for p in providers]



    def post_freightproviders_ratequote(self, optionIndex: str, jobDisplayId: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """POST /api/job/{jobDisplayId}/freightproviders/{optionIndex}/ratequote

        Args:
            optionIndex: The freight provider option index
            jobDisplayId: The job display ID
            data: SetRateModel data (ratesKey, carrierCode, etc.)

        Returns:
            Dict[str, Any]: API response data (validated)
        """
        path = f"/{jobDisplayId}/freightproviders/{optionIndex}/ratequote"

        kwargs = {}
        if data is not None:
            # Validate incoming data and convert to API format
            validated_data = SetRateModel.check(data)
            kwargs["json"] = validated_data

        return self._make_request("POST", path, **kwargs)
