"""Job Parcelitems API endpoints.

Auto-generated from swagger.json specification.
"""

from typing import List, Optional, Dict, Any
from ABConnect.api.endpoints.base import BaseEndpoint


class JobParcelItemsEndpoint(BaseEndpoint):
    """JobParcelItems API endpoint operations.

    Total endpoints: 4
    """

    api_path = "job"

    def get_parcelitems(self, jobDisplayId: str) -> Dict[str, Any]:
        """GET /api/job/{jobDisplayId}/parcelitems

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/parcelitems"
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        return self._make_request("GET", path, **kwargs)

    def post_parcelitems(self, jobDisplayId: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """POST /api/job/{jobDisplayId}/parcelitems

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/parcelitems"
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
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

    def delete_parcelitems(self, parcelItemId: str, jobDisplayId: str) -> Dict[str, Any]:
        """DELETE /api/job/{jobDisplayId}/parcelitems/{parcelItemId}

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/parcelitems/{parcelItemId}"
        path = path.replace("{parcelItemId}", str(parcelItemId))
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        return self._make_request("DELETE", path, **kwargs)
