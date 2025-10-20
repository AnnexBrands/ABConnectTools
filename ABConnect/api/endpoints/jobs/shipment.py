"""Job Shipment API endpoints.

Auto-generated from swagger.json specification.
"""

from typing import List, Optional, Dict, Any, Union
from ABConnect.api.endpoints.base import BaseEndpoint
from ABConnect.api.models.jobshipment import BookShipmentRequest


class JobShipmentEndpoint(BaseEndpoint):
    """JobShipment API endpoint operations.

    Total endpoints: 11
    """

    api_path = "job"

    def post_shipment_book(
        self,
        jobDisplayId: str,
        data: Optional[Union[BookShipmentRequest, Dict[str, Any]]] = None
    ) -> Dict[str, Any]:
        """POST /api/job/{jobDisplayId}/shipment/book

        Args:
            jobDisplayId: The job display ID
            data: BookShipmentRequest as Pydantic model or dict

        Returns:
            Dict[str, Any]: API response data
        """
        path = f"/{jobDisplayId}/shipment/book"

        kwargs = {}
        if data is not None:
            # Validate incoming data and convert to API format
            validated_data = BookShipmentRequest.check(data)
            kwargs["json"] = validated_data

        return self._make_request("POST", path, **kwargs)

    def delete_shipment(self, jobDisplayId: str) -> Dict[str, Any]:
        """DELETE /api/job/{jobDisplayId}/shipment

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/shipment"
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        return self._make_request("DELETE", path, **kwargs)

    def get_shipment_ratequotes(self, jobDisplayId: str, ship_out_date: Optional[str] = None, rates_sources: Optional[str] = None, settings_key: Optional[str] = None) -> Dict[str, Any]:
        """GET /api/job/{jobDisplayId}/shipment/ratequotes

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/shipment/ratequotes"
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        params = {}
        if ship_out_date is not None:
            params["ShipOutDate"] = ship_out_date
        if rates_sources is not None:
            params["RatesSources"] = rates_sources
        if settings_key is not None:
            params["SettingsKey"] = settings_key
        if params:
            kwargs["params"] = params
        return self._make_request("GET", path, **kwargs)

    def post_shipment_ratequotes(self, jobDisplayId: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """POST /api/job/{jobDisplayId}/shipment/ratequotes

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/shipment/ratequotes"
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)

    def get_shipment_origindestination(self, jobDisplayId: str) -> Dict[str, Any]:
        """GET /api/job/{jobDisplayId}/shipment/origindestination

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/shipment/origindestination"
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        return self._make_request("GET", path, **kwargs)

    def get_shipment_accessorials(self, jobDisplayId: str) -> Dict[str, Any]:
        """GET /api/job/{jobDisplayId}/shipment/accessorials

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/shipment/accessorials"
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        return self._make_request("GET", path, **kwargs)

    def post_shipment_accessorial(self, jobDisplayId: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """POST /api/job/{jobDisplayId}/shipment/accessorial

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/shipment/accessorial"
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)

    def delete_shipment_accessorial(self, addOnId: str, jobDisplayId: str) -> Dict[str, Any]:
        """DELETE /api/job/{jobDisplayId}/shipment/accessorial/{addOnId}

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/shipment/accessorial/{addOnId}"
        path = path.replace("{addOnId}", str(addOnId))
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        return self._make_request("DELETE", path, **kwargs)

    def get_shipment_ratesstate(self, jobDisplayId: str) -> Dict[str, Any]:
        """GET /api/job/{jobDisplayId}/shipment/ratesstate

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/shipment/ratesstate"
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        return self._make_request("GET", path, **kwargs)

    def get_shipment_exportdata(self, jobDisplayId: str) -> Dict[str, Any]:
        """GET /api/job/{jobDisplayId}/shipment/exportdata

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/shipment/exportdata"
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        return self._make_request("GET", path, **kwargs)

    def post_shipment_exportdata(self, jobDisplayId: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """POST /api/job/{jobDisplayId}/shipment/exportdata

        
        

        Returns:
            Dict[str, Any]: API response data
        """
        path = "/{jobDisplayId}/shipment/exportdata"
        path = path.replace("{jobDisplayId}", str(jobDisplayId))
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request("POST", path, **kwargs)
