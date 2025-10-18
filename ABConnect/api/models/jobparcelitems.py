"""Jobparcelitems models for ABConnect API."""

from typing import Optional
from pydantic import Field
from .base import IdentifiedModel

class ParcelItem(IdentifiedModel):
    """ParcelItem model"""

    job_item_id: Optional[str] = Field(None, alias="jobItemId")
    description: Optional[str] = Field(None)
    quantity: Optional[int] = Field(None)
    job_item_pkd_length: Optional[float] = Field(None, alias="jobItemPkdLength")
    job_item_pkd_width: Optional[float] = Field(None, alias="jobItemPkdWidth")
    job_item_pkd_height: Optional[float] = Field(None, alias="jobItemPkdHeight")
    job_item_pkd_weight: Optional[float] = Field(None, alias="jobItemPkdWeight")
    job_item_parcel_value: Optional[float] = Field(None, alias="jobItemParcelValue")
    parcel_package_type_id: Optional[int] = Field(None, alias="parcelPackageTypeId")
    package_type_code: Optional[str] = Field(None, alias="packageTypeCode")
    insure_key: Optional[str] = Field(None, alias="insureKey")


class ParcelItemWithPackage(IdentifiedModel):
    """ParcelItemWithPackage model"""

    job_item_id: Optional[str] = Field(None, alias="jobItemId")
    description: Optional[str] = Field(None)
    quantity: Optional[int] = Field(None)
    job_item_pkd_length: Optional[float] = Field(None, alias="jobItemPkdLength")
    job_item_pkd_width: Optional[float] = Field(None, alias="jobItemPkdWidth")
    job_item_pkd_height: Optional[float] = Field(None, alias="jobItemPkdHeight")
    job_item_pkd_weight: Optional[float] = Field(None, alias="jobItemPkdWeight")
    job_item_parcel_value: Optional[float] = Field(None, alias="jobItemParcelValue")
    parcel_package_type_id: Optional[int] = Field(None, alias="parcelPackageTypeId")
    insure_key: Optional[str] = Field(None, alias="insureKey")
    package_type_code: Optional[str] = Field(None, alias="packageTypeCode")


__all__ = ['ParcelItem', 'ParcelItemWithPackage']
