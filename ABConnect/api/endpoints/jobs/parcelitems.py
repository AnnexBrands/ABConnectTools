"""Job Parcel Items API endpoints.

Provides access to job parcel item operations including creation,
retrieval, updates, and deletion.
"""

from typing import Optional, Dict, Any, Union, List
from ABConnect.api.endpoints.base import BaseEndpoint
from ABConnect.api.models.jobparcelitems import ParcelItem, SaveAllParcelItemsRequest
from ABConnect.api.routes import SCHEMA


class JobParcelItemsEndpoint(BaseEndpoint):
    """Job Parcel Items API endpoint operations.

    Handles parcel item management for jobs.
    """

    api_path = "job"
    routes = SCHEMA["JOB"]

    def get_parcelitems(
        self,
        jobDisplayId: str
    ) -> Union[List[ParcelItem], List[Dict[str, Any]]]:
        """Get all parcel items for a job.

        Args:
            jobDisplayId: The job display ID

        Returns:
            List[ParcelItemWithPackage] with parcel item details
        """
        route = self.routes['GET_PARCELITEMS']
        route.params = {"jobDisplayId": str(jobDisplayId)}
        return self._make_request(route)

    def post_parcelitems(
        self,
        jobDisplayId: str,
        data: Optional[Union[SaveAllParcelItemsRequest, Dict[str, Any]]] = None,
        parcel_items: Optional[List[Union[ParcelItem, Dict[str, Any]]]] = None,
        force_update: bool = False,
        job_modified_date: Optional[str] = None,
    ) -> Union[List[ParcelItem], List[Dict[str, Any]]]:
        """Save parcel items for a job.

        Args:
            jobDisplayId: The job display ID
            data: SaveAllParcelItemsRequest (overrides other params)
            parcel_items: List of parcel items
            force_update: Force update flag
            job_modified_date: Job modified date

        Returns:
            List[ParcelItemWithPackage] with saved items
        """
        route = self.routes['POST_PARCELITEMS']
        route.params = {"jobDisplayId": str(jobDisplayId)}
        kwargs = {}

        if data is None:
            data = SaveAllParcelItemsRequest(
                parcel_items=parcel_items,
                force_update=force_update,
                job_modified_date=job_modified_date,
            )

        validated_data = data.json() if hasattr(data, 'json') else data
        kwargs["json"] = validated_data
        return self._make_request(route, **kwargs)

    def get_parcel_items_with_materials(self, jobDisplayId: str) -> Dict[str, Any]:
        """Get parcel items with materials for a job.

        Args:
            jobDisplayId: The job display ID

        Returns:
            List[ParcelItemWithMaterials] with material details
        """
        route = self.routes['GET_PARCEL_ITEMS_WITH_MATERIALS']
        route.params = {"jobDisplayId": str(jobDisplayId)}
        return self._make_request(route)

    def delete_parcelitems(
        self,
        parcelItemId: str,
        jobDisplayId: str
    ) -> Dict[str, Any]:
        """Delete a parcel item from a job.

        Args:
            parcelItemId: The parcel item ID to delete
            jobDisplayId: The job display ID

        Returns:
            ServiceBaseResponse confirming deletion
        """
        route = self.routes['DELETE_PARCELITEMS']
        route.params = {
            "jobDisplayId": str(jobDisplayId),
            "parcelItemId": str(parcelItemId)
        }
        return self._make_request(route)
