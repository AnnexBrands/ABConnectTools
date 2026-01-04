"""Job Shipment API endpoints.

Provides access to job shipment operations including booking, rate quotes,
accessorials, and export data management.
"""

from typing import Optional, Dict, Any, Union
from ABConnect.api.endpoints.base import BaseEndpoint
from ABConnect.api.models.jobshipment import BookShipmentRequest, DeleteShipRequestModel
from ABConnect.api.routes import SCHEMA


class JobShipmentEndpoint(BaseEndpoint):
    """Job Shipment API endpoint operations.

    Handles shipment booking, rate quotes, accessorials, and export data.
    """

    api_path = "job"
    routes = SCHEMA["JOB"]

    def post_shipment_book(
        self,
        jobDisplayId: str,
        data: Optional[Union[BookShipmentRequest, Dict[str, Any]]] = None,
    ) -> Dict[str, Any]:
        """Book a shipment for a job.

        Args:
            jobDisplayId: The job display ID
            data: BookShipmentRequest with booking details

        Returns:
            ServiceBaseResponse confirming booking
        """
        route = self.routes['POST_SHIPMENT_BOOK']
        route.params = {"jobDisplayId": str(jobDisplayId)}
        kwargs = {}
        if data is not None:
            validated_data = BookShipmentRequest.json(data)
            kwargs["json"] = validated_data
        return self._make_request(route, **kwargs)

    def delete_shipment(
        self,
        jobDisplayId: str,
        option_index: int = 3,
        force_delete: bool = True,
        data: Optional[Union[DeleteShipRequestModel, Dict[str, Any]]] = None,
    ) -> Dict[str, Any]:
        """Delete a shipment from a job.

        Args:
            jobDisplayId: The job display ID
            option_index: Option index for deletion (default: 3)
            force_delete: Force delete flag (default: True)
            data: DeleteShipRequestModel (overrides option_index/force_delete)

        Returns:
            ServiceBaseResponse confirming deletion
        """
        route = self.routes['DELETE_SHIPMENT']
        route.params = {"jobDisplayId": str(jobDisplayId)}
        kwargs = {}
        if data is None:
            data = DeleteShipRequestModel(
                option_index=option_index, force_delete=force_delete
            )
        validated_data = DeleteShipRequestModel.json(data)
        kwargs["json"] = validated_data
        return self._make_request(route, **kwargs)

    def get_shipment_ratequotes(
        self,
        jobDisplayId: str,
        ship_out_date: Optional[str] = None,
        rates_sources: Optional[str] = None,
        settings_key: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Get rate quotes for a job shipment.

        Args:
            jobDisplayId: The job display ID
            ship_out_date: Optional ship out date filter
            rates_sources: Optional rates sources filter
            settings_key: Optional settings key

        Returns:
            JobCarrierRatesModel with available rates
        """
        route = self.routes['GET_SHIPMENT_RATEQUOTES']
        route.params = {"jobDisplayId": str(jobDisplayId)}
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
        return self._make_request(route, **kwargs)

    def post_shipment_ratequotes(
        self,
        jobDisplayId: str,
        data: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Request rate quotes for a job shipment.

        Args:
            jobDisplayId: The job display ID
            data: TransportationRatesRequestModel with request params

        Returns:
            JobCarrierRatesModel with quoted rates
        """
        route = self.routes['POST_SHIPMENT_RATEQUOTES']
        route.params = {"jobDisplayId": str(jobDisplayId)}
        kwargs = {}
        if data is not None:
            validated_data = BookShipmentRequest.json(data)
            kwargs["json"] = validated_data
        return self._make_request(route, **kwargs)

    def get_shipment_origindestination(self, jobDisplayId: str) -> Dict[str, Any]:
        """Get origin and destination info for a job shipment.

        Args:
            jobDisplayId: The job display ID

        Returns:
            ShipmentOriginDestination with address details
        """
        route = self.routes['GET_SHIPMENT_ORIGINDESTINATION']
        route.params = {"jobDisplayId": str(jobDisplayId)}
        return self._make_request(route)

    def get_shipment_accessorials(self, jobDisplayId: str) -> Dict[str, Any]:
        """Get accessorials for a job shipment.

        Args:
            jobDisplayId: The job display ID

        Returns:
            List[JobParcelAddOn] with accessorial details
        """
        route = self.routes['GET_SHIPMENT_ACCESSORIALS']
        route.params = {"jobDisplayId": str(jobDisplayId)}
        return self._make_request(route)

    def post_shipment_accessorial(
        self,
        jobDisplayId: str,
        data: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Add an accessorial to a job shipment.

        Args:
            jobDisplayId: The job display ID
            data: JobParcelAddOn with accessorial details

        Returns:
            ServiceBaseResponse confirming addition
        """
        route = self.routes['POST_SHIPMENT_ACCESSORIAL']
        route.params = {"jobDisplayId": str(jobDisplayId)}
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def delete_shipment_accessorial(
        self,
        addOnId: str,
        jobDisplayId: str
    ) -> Dict[str, Any]:
        """Delete an accessorial from a job shipment.

        Args:
            addOnId: The accessorial add-on ID to delete
            jobDisplayId: The job display ID

        Returns:
            ServiceBaseResponse confirming deletion
        """
        route = self.routes['DELETE_SHIPMENT_ACCESSORIAL']
        route.params = {
            "jobDisplayId": str(jobDisplayId),
            "addOnId": str(addOnId)
        }
        return self._make_request(route)

    def get_shipment_ratesstate(self, jobDisplayId: str) -> Dict[str, Any]:
        """Get the current rates state for a job shipment.

        Args:
            jobDisplayId: The job display ID

        Returns:
            Rates state information
        """
        route = self.routes['GET_SHIPMENT_RATESSTATE']
        route.params = {"jobDisplayId": str(jobDisplayId)}
        return self._make_request(route)

    def get_shipment_exportdata(self, jobDisplayId: str) -> Dict[str, Any]:
        """Get export data for a job shipment.

        Args:
            jobDisplayId: The job display ID

        Returns:
            JobExportData with export information
        """
        route = self.routes['GET_SHIPMENT_EXPORTDATA']
        route.params = {"jobDisplayId": str(jobDisplayId)}
        return self._make_request(route)

    def post_shipment_exportdata(
        self,
        jobDisplayId: str,
        data: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Save export data for a job shipment.

        Args:
            jobDisplayId: The job display ID
            data: InternationalParams with export details

        Returns:
            ServiceBaseResponse confirming save
        """
        route = self.routes['POST_SHIPMENT_EXPORTDATA']
        route.params = {"jobDisplayId": str(jobDisplayId)}
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)
