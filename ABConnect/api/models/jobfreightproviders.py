"""Jobfreightproviders models for ABConnect API."""

from typing import Optional
from datetime import datetime
from pydantic import Field
from .base import ABConnectBaseModel, JobRelatedModel
from .enums import CarrierAPI
from .shared import CarrierAccountInfo, ServiceBaseResponse  # noqa: F401 - re-exported


class PricedFreightProvider(ABConnectBaseModel):
    """PricedFreightProvider model"""

    option_index: Optional[int] = Field(None, alias="optionIndex")
    shipment_type: Optional[str] = Field(None, alias="shipmentType")
    provider_api: Optional[CarrierAPI] = Field(None, alias="providerAPI")
    provider_id: Optional[str] = Field(None, alias="providerId")
    provider_code: Optional[str] = Field(None, alias="providerCode")
    provider_company_name: Optional[str] = Field(None, alias="providerCompanyName")
    total_sell: Optional[float] = Field(None, alias="totalSell")
    transit: Optional[int] = Field(None)
    quote_no: Optional[str] = Field(None, alias="quoteNo")
    pro_num: Optional[str] = Field(None, alias="proNum")
    option_active: Optional[bool] = Field(None, alias="optionActive")
    shipment_accepted: Optional[bool] = Field(None, alias="shipmentAccepted")
    shipment_accepted_date: Optional[datetime] = Field(None, alias="shipmentAcceptedDate")
    obtain_nfm_job_state: Optional[str] = Field(None, alias="obtainNFMJobState")
    used_carrier_account_info: Optional[CarrierAccountInfo] = Field(None, alias="usedCarrierAccountInfo")


class SetRateModel(ABConnectBaseModel):
    """SetRateModel model"""

    rates_key: str = Field(..., alias="ratesKey", min_length=1)
    carrier_code: str = Field(..., alias="carrierCode", min_length=1)
    carrier_account_id: Optional[int] = Field(None, alias="carrierAccountId")
    active: Optional[bool] = Field(None)


class ShipmentPlanProvider(JobRelatedModel):
    """ShipmentPlanProvider model"""

    freight_quote_options_id: Optional[str] = Field(None, alias="freightQuoteOptionsId")
    provider_id: Optional[str] = Field(None, alias="providerId")
    is_primary: Optional[bool] = Field(None, alias="isPrimary")
    provider_company_code: Optional[str] = Field(None, alias="providerCompanyCode")
    provider_company_name: Optional[str] = Field(None, alias="providerCompanyName")
    original_company_name: Optional[str] = Field(None, alias="originalCompanyName")
    freight_amount: Optional[float] = Field(None, alias="freightAmount")
    accessorial_amount: Optional[float] = Field(None, alias="accessorialAmount")
    caf_note: Optional[str] = Field(None, alias="cafNote")
    quote_no: Optional[str] = Field(None, alias="quoteNo")
    pro_num: Optional[str] = Field(None, alias="proNum")
    transit: Optional[int] = Field(None)
    shipment_type: Optional[str] = Field(None, alias="shipmentType")
    miles: Optional[float] = Field(None)
    logo: Optional[str] = Field(None)
    option_index: Optional[int] = Field(None, alias="optionIndex")
    option_active: Optional[bool] = Field(None, alias="optionActive")
    shipment_accepted: Optional[bool] = Field(None, alias="shipmentAccepted")
    shipment_accepted_date: Optional[datetime] = Field(None, alias="shipmentAcceptedDate")
    used_api: Optional[CarrierAPI] = Field(None, alias="usedApi")
    bill_to_franchisee_id: Optional[str] = Field(None, alias="billToFranchiseeId")
    bill_to_company_code: Optional[str] = Field(None, alias="billToCompanyCode")
    obtain_nfm_job_state: Optional[str] = Field(None, alias="obtainNfmJobState")
    used_carrier_account_info: Optional[CarrierAccountInfo] = Field(None, alias="usedCarrierAccountInfo")


__all__ = ['PricedFreightProvider', 'ServiceBaseResponse', 'SetRateModel', 'ShipmentPlanProvider']
