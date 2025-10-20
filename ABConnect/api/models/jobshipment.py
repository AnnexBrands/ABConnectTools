"""Jobshipment models for ABConnect API."""

from __future__ import annotations

from typing import List, Optional, TYPE_CHECKING
from datetime import datetime
from pydantic import Field
from .base import ABConnectBaseModel
from .enums import CarrierAPI

if TYPE_CHECKING:
    from .job import JobExportData
    from .contacts import ShipmentContactDetails, ShipmentContactAddressDetails
    from .shared import (
        BookShipmentSpecificParams,
        Commodity,
        ExportPackingInfo,
        ExportTotalCosts,
        USPSSpecific,
        FedExSpecific,
        UPSSpecific,
        CarrierRateModel,
        LastObtainNFM,
        CarrierProviderMessage,
        HandlingUnitModel,
    )

class BookShipmentRequest(ABConnectBaseModel):
    """BookShipmentRequest model"""

    quote_option_index: Optional[int] = Field(None, alias="quoteOptionIndex")
    ship_out_date: Optional[datetime] = Field(None, alias="shipOutDate")
    international_params: Optional[JobExportData] = Field(None, alias="internationalParams")
    carrier_specific_params: Optional[BookShipmentSpecificParams] = Field(None, alias="carrierSpecificParams")
    document_byte_code_required: Optional[bool] = Field(None, alias="documentByteCodeRequired")


class DeleteShipRequestModel(ABConnectBaseModel):
    """DeleteShipRequestModel model"""

    option_index: Optional[int] = Field(None, alias="optionIndex")
    force_delete: Optional[bool] = Field(None, alias="forceDelete")


class InternationalParams(ABConnectBaseModel):
    """InternationalParams model"""

    commodities: Optional[List[Commodity]] = Field(None)
    packing_info: Optional[List[ExportPackingInfo]] = Field(None, alias="packingInfo")
    customs_value: float = Field(..., alias="customsValue")
    invoice_number: Optional[str] = Field(None, alias="invoiceNumber")
    purchase_order_number: Optional[str] = Field(None, alias="purchaseOrderNumber")
    terms_of_sale: Optional[str] = Field(None, alias="termsOfSale")
    exporter_tax_id: Optional[str] = Field(None, alias="exporterTaxId")
    consignee_tax_id: Optional[str] = Field(None, alias="consigneeTaxId")
    total_costs: Optional[ExportTotalCosts] = Field(None, alias="totalCosts")
    sold_to: Optional[ShipmentContactDetails] = Field(None, alias="soldTo")
    usps_specific: Optional[USPSSpecific] = Field(None, alias="uspsSpecific")
    fed_ex_specific: Optional[FedExSpecific] = Field(None, alias="fedExSpecific")
    ups_specific: Optional[UPSSpecific] = Field(None, alias="upsSpecific")
    values_specified: Optional[bool] = Field(None, alias="valuesSpecified")


class JobCarrierRatesModel(ABConnectBaseModel):
    """JobCarrierRatesModel model"""

    rates_key: Optional[str] = Field(None, alias="ratesKey")
    rates: Optional[List[CarrierRateModel]] = Field(None)
    request_snapshot: Optional[LastObtainNFM] = Field(None, alias="requestSnapshot")
    errors: Optional[List[CarrierProviderMessage]] = Field(None)


class JobParcelAddOn(ABConnectBaseModel):
    """JobParcelAddOn model"""

    job_add_on_id: Optional[int] = Field(None, alias="jobAddOnId")
    parcel_add_on_id: Optional[int] = Field(None, alias="parcelAddOnId")
    parcel_add_on_unique_id: Optional[str] = Field(None, alias="parcelAddOnUniqueId")
    job_add_on_params: Optional[str] = Field(None, alias="jobAddOnParams")
    add_on_api: Optional[CarrierAPI] = Field(None, alias="addOnApi")


class ShipmentOriginDestination(ABConnectBaseModel):
    """ShipmentOriginDestination model"""

    origin: Optional[ShipmentContactAddressDetails] = Field(None)
    destination: Optional[ShipmentContactAddressDetails] = Field(None)


class TransportationRatesRequestModel(ABConnectBaseModel):
    """TransportationRatesRequestModel model"""

    handling_units: Optional[List[HandlingUnitModel]] = Field(None, alias="handlingUnits")
    ship_out_date: Optional[datetime] = Field(None, alias="shipOutDate")
    rates_sources: Optional[List[CarrierAPI]] = Field(None, alias="ratesSources")


__all__ = ['BookShipmentRequest', 'DeleteShipRequestModel', 'InternationalParams', 'JobCarrierRatesModel', 'JobParcelAddOn', 'ShipmentOriginDestination', 'TransportationRatesRequestModel']

# Rebuild models to resolve forward references
# This is done after all models are defined to avoid circular import issues
def _rebuild_models():
    """Rebuild all models in this module to resolve forward references."""
    try:
        # Import the modules containing the forward-referenced classes
        from . import job, contacts, shared, address

        # Create a namespace with all the classes that might be referenced
        namespace = {}
        for module in [job, contacts, shared, address]:
            for attr_name in dir(module):
                attr = getattr(module, attr_name)
                if isinstance(attr, type):  # Only include classes
                    namespace[attr_name] = attr

        # Now rebuild all models with the complete namespace
        BookShipmentRequest.model_rebuild(_types_namespace=namespace)
        DeleteShipRequestModel.model_rebuild(_types_namespace=namespace)
        InternationalParams.model_rebuild(_types_namespace=namespace)
        JobCarrierRatesModel.model_rebuild(_types_namespace=namespace)
        JobParcelAddOn.model_rebuild(_types_namespace=namespace)
        ShipmentOriginDestination.model_rebuild(_types_namespace=namespace)
        TransportationRatesRequestModel.model_rebuild(_types_namespace=namespace)
    except Exception:
        # If rebuild fails, models will be rebuilt lazily by Pydantic
        pass

# Call rebuild when module is imported
_rebuild_models()
