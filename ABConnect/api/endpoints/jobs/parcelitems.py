"""Job Parcelitems API endpoints.

Auto-generated from swagger.json specification.
"""

from typing import List, Optional, Dict, Any, Union
from ABConnect.api.endpoints.base import BaseEndpoint
from ABConnect.api.models.jobparcelitems import ParcelItem, SaveAllParcelItemsRequest
from ABConnect.api.routes import SCHEMA


class JobParcelItemsEndpoint(BaseEndpoint):
    """JobParcelItems API endpoint operations.

    Total endpoints: 4
    """

    api_path = "job"

    def get_parcelitems(
        self, jobDisplayId: str
    ) -> Union[List[ParcelItem], List[Dict[str, Any]]]:
        """GET /api/job/{jobDisplayId}/parcelitems

        Args:
            jobDisplayId: The job display ID

        Returns:
            Union[List[ParcelItem], List[Dict[str, Any]]]: List of ParcelItem models or list of dicts
        """
        route = SCHEMA["GET_PARCELITEMS"]
        route.params = {"jobDisplayId": jobDisplayId}

        return self._make_request(route.method, route)

    def post_parcelitems(
        self,
        jobDisplayId: str,
        data: Optional[Union[SaveAllParcelItemsRequest, Dict[str, Any]]] = None,
        parcel_items: Optional[List[Union[ParcelItem, Dict[str, Any]]]] = None,
        force_update: bool = False,
        job_modified_date: Optional[str] = None,
    ) -> Union[List[ParcelItem], List[Dict[str, Any]]]:
        """POST /api/job/{jobDisplayId}/parcelitems

        Args:
            jobDisplayId: The job display ID
            data: SaveAllParcelItemsRequest as Pydantic model or dict (optional, overrides other params)
            parcel_items: List of ParcelItem models or dicts (used if data not provided)
            force_update: Force update flag (default: False)
            job_modified_date: Job modified date (optional)

        Returns:
            Union[List[ParcelItem], List[Dict[str, Any]]]: List of ParcelItem models or list of dicts
        """
        path = f"/{jobDisplayId}/parcelitems"
        kwargs = {"cast_response": True}

        # Use provided data or construct from parameters
        if data is None:
            data = SaveAllParcelItemsRequest(
                parcel_items=parcel_items,
                force_update=force_update,
                job_modified_date=job_modified_date,
            )

        # Validate incoming data and convert to API format
        validated_data = SaveAllParcelItemsRequestdata.json()
        kwargs["json"] = validated_data

        return self._make_request("POST", path, **kwargs)

    def get_parcel_items_with_materials(self, jobDisplayId: str) -> Dict[str, Any]:
        """GET /api/job/{jobDisplayId}/parcel-items-with-materials




        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/parcel-items-with-materials"
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        return self._make_request("GET", path, **kwargs)

    def delete_parcelitems(
        self, parcelItemId: str, jobDisplayId: str
    ) -> Dict[str, Any]:
        """DELETE /api/job/{jobDisplayId}/parcelitems/{parcelItemId}




        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/parcelitems/{parcelItemId}"
        path = path.replace("{parcelItemId}", str(parcelItemId))
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        return self._make_request("DELETE", path, **kwargs)
