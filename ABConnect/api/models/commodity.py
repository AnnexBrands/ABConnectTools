"""Commodity models for API version 709.

New models for commodity (HS code) management.
"""

from typing import List, Optional
from pydantic import Field

from .base import ABConnectBaseModel


__all__ = [
    'Commodity',
    'CommodityDetails',
    'CommodityWithParents',
    'CommodityMap',
    'CommodityMapDetails',
    'CommodityForMapInfo',
]


class Commodity(ABConnectBaseModel):
    """Commodity model representing an HS code or tariff classification.

    .. versionadded:: 709
    """

    id: int = Field(..., description="Commodity ID")
    code: Optional[str] = Field(None, description="HS code")
    name: Optional[str] = Field(None, description="Commodity name")
    description: Optional[str] = Field(None, description="Commodity description")
    parent_id: Optional[int] = Field(None, alias="parentId", description="Parent commodity ID")
    is_active: bool = Field(True, alias="isActive", description="Whether commodity is active")


class CommodityDetails(ABConnectBaseModel):
    """Detailed commodity model with parent information.

    .. versionadded:: 709
    """

    id: int = Field(..., description="Commodity ID")
    code: Optional[str] = Field(None, description="HS code")
    name: Optional[str] = Field(None, description="Commodity name")
    description: Optional[str] = Field(None, description="Commodity description")
    is_active: bool = Field(True, alias="isActive", description="Whether commodity is active")
    parent_id: Optional[int] = Field(None, alias="parentId", description="Parent commodity ID")
    parent_name: Optional[str] = Field(None, alias="parentName", description="Parent commodity name")
    parent_code: Optional[str] = Field(None, alias="parentCode", description="Parent HS code")
    parent_is_active: Optional[bool] = Field(None, alias="parentIsActive", description="Whether parent is active")


class CommodityWithParents(ABConnectBaseModel):
    """Commodity model with full parent hierarchy.

    .. versionadded:: 709
    """

    id: int = Field(..., description="Commodity ID")
    code: Optional[str] = Field(None, description="HS code")
    name: Optional[str] = Field(None, description="Commodity name")
    description: Optional[str] = Field(None, description="Commodity description")
    parent_id: Optional[int] = Field(None, alias="parentId", description="Parent commodity ID")
    is_active: bool = Field(True, alias="isActive", description="Whether commodity is active")
    parent_commodities: Optional[List["Commodity"]] = Field(
        None, alias="parentCommodities", description="List of parent commodities"
    )


class CommodityForMapInfo(ABConnectBaseModel):
    """Simplified commodity info for mapping.

    .. versionadded:: 709
    """

    id: int = Field(..., description="Commodity ID")
    code: Optional[str] = Field(None, description="HS code")
    name: Optional[str] = Field(None, description="Commodity name")


class CommodityMap(ABConnectBaseModel):
    """Commodity mapping model linking items to HS codes.

    .. versionadded:: 709
    """

    id: int = Field(..., description="Mapping ID")
    commodity_id: int = Field(..., alias="commodityId", description="Commodity ID")
    partner_id: Optional[int] = Field(None, alias="partnerId", description="Partner ID")
    outer_id: Optional[str] = Field(None, alias="outerId", description="External ID")


class CommodityMapDetails(ABConnectBaseModel):
    """Detailed commodity mapping with related entities.

    .. versionadded:: 709
    """

    id: int = Field(..., description="Mapping ID")
    outer_id: Optional[str] = Field(None, alias="outerId", description="External ID")
    commodity: Optional[CommodityForMapInfo] = Field(None, description="Associated commodity")
    partner: Optional["Partner"] = Field(None, description="Associated partner")


# Forward reference for Partner - will be resolved when partner.py is loaded
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .partner import Partner
