"""Job Freight Providers API endpoints.

Provides access to job freight provider operations including
retrieval, updates, and rate quote selection.
"""

from typing import Optional, Dict, Any, List
from pydantic import TypeAdapter

from ABConnect.api.endpoints.base import BaseEndpoint
from ABConnect.api.models.jobfreightproviders import (
    PricedFreightProvider,
    ServiceBaseResponse,
    ShipmentPlanProvider,
    SetRateModel
)
from ABConnect.api.routes import SCHEMA


class JobFreightProvidersEndpoint(BaseEndpoint):
    """Job Freight Providers API endpoint operations.

    Handles freight provider management and rate quotes for jobs.
    """

    api_path = "job"
    routes = SCHEMA["JOB"]

    def get_freightproviders(
        self,
        jobDisplayId: str,
        provider_indexes: Optional[str] = None,
        shipment_types: Optional[str] = None,
        only_active: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """Get freight providers for a job.

        Args:
            jobDisplayId: The job display ID
            provider_indexes: Optional provider indexes filter
            shipment_types: Optional shipment types filter
            only_active: Optional flag to show only active providers

        Returns:
            List[PricedFreightProvider] with provider details
        """
        route = self.routes['GET_FREIGHTPROVIDERS']
        route.params = {"jobDisplayId": jobDisplayId}
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

        response = self._make_request(route, **kwargs)
        providers = TypeAdapter(list[PricedFreightProvider]).validate_python(response)
        return [p.model_dump(by_alias=True) for p in providers]

    def post_freightproviders(
        self,
        jobDisplayId: str,
        data: Optional[List[Dict[str, Any]]] = None
    ) -> Dict[str, Any]:
        """Save freight providers for a job.

        Args:
            jobDisplayId: The job display ID
            data: List of ShipmentPlanProvider objects

        Returns:
            ServiceBaseResponse confirming save
        """
        route = self.routes['POST_FREIGHTPROVIDERS']
        route.params = {"jobDisplayId": str(jobDisplayId)}
        kwargs = {}
        if data is not None:
            validated_data = ShipmentPlanProvider.json(data)
            kwargs["json"] = validated_data

        response = self._make_request(route, **kwargs)
        validated_response = ServiceBaseResponse.model_validate(response)
        return validated_response.model_dump(by_alias=True)

    def post_freightproviders_ratequote(
        self,
        optionIndex: str,
        jobDisplayId: str,
        data: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Set a rate quote for a freight provider option.

        Args:
            optionIndex: The freight provider option index
            jobDisplayId: The job display ID
            data: SetRateModel with rate details

        Returns:
            ServiceBaseResponse confirming selection
        """
        route = self.routes['POST_FREIGHTPROVIDERS_RATEQUOTE']
        route.params = {
            "jobDisplayId": str(jobDisplayId),
            "optionIndex": str(optionIndex)
        }
        kwargs = {}
        if data is not None:
            validated_data = SetRateModel.json(data)
            kwargs["json"] = validated_data
        return self._make_request(route, **kwargs)
