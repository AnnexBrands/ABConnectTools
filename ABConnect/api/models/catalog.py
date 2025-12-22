"""Catalog API models.

Models for the Catalog service API (catalog-api.abconnect.co).
API returns camelCase field names.
"""

from typing import Any, List, Optional
from datetime import datetime
from pydantic import AliasChoices, Field, field_validator

from .base import ABConnectBaseModel


__all__ = [
    # Core DTOs
    'LotDataDto',
    'ImageLinkDto',
    'LotCatalogDto',
    'LotCatalogInformationDto',
    'SellerDto',
    'CatalogDto',
    'CatalogWithSellersDto',
    'CatalogExpandedDto',
    'SellerExpandedDto',
    'LotDto',
    'LotOverrideDto',
    # Paginated lists
    'PaginatedList',
    'CatalogExpandedDtoPaginatedList',
    'LotDtoPaginatedList',
    'SellerExpandedDtoPaginatedList',
    # Request models
    'AddCatalogRequest',
    'UpdateCatalogRequest',
    'AddLotRequest',
    'UpdateLotRequest',
    'GetLotsOverridesQuery',
    'AddSellerRequest',
    'UpdateSellerRequest',
    # Bulk models
    'BulkInsertSellerRequest',
    'BulkInsertLotRequest',
    'BulkInsertCatalogRequest',
    'BulkInsertRequest',
]


# =============================================================================
# Core DTOs (API returns camelCase)
# =============================================================================

class LotDataDto(ABConnectBaseModel):
    """Core lot data shared across various DTOs.

    Note: API returns mixed casing but DB/writes expect PascalCase.
    Uses validation_alias for reading (camelCase) and serialization_alias for writing (PascalCase).
    """
    model_config = {"populate_by_name": True, "extra": "ignore"}

    # All fields use PascalCase for serialization (API writes)
    # validation_alias handles camelCase from API reads
    qty: Optional[int] = Field(None, validation_alias=AliasChoices('Qty', 'qty'), serialization_alias='Qty', description="Quantity")
    l: Optional[float] = Field(None, validation_alias=AliasChoices('L', 'l'), serialization_alias='L', description="Length")
    w: Optional[float] = Field(None, validation_alias=AliasChoices('W', 'w'), serialization_alias='W', description="Width")
    h: Optional[float] = Field(None, validation_alias=AliasChoices('H', 'h'), serialization_alias='H', description="Height")
    wgt: Optional[float] = Field(None, validation_alias=AliasChoices('Wgt', 'wgt'), serialization_alias='Wgt', description="Weight")
    value: Optional[float] = Field(None, validation_alias=AliasChoices('Value', 'value'), serialization_alias='Value', description="Value")
    cpack: Optional[str] = Field(None, validation_alias=AliasChoices('CPack', 'Cpack', 'cpack'), serialization_alias='CPack', description="Container pack ID")
    description: Optional[str] = Field(None, validation_alias=AliasChoices('Description', 'description'), serialization_alias='Description')
    notes: Optional[str] = Field(None, validation_alias=AliasChoices('Notes', 'notes'), serialization_alias='Notes')
    item_id: Optional[int] = Field(None, validation_alias=AliasChoices('ItemID', 'itemID'), serialization_alias='ItemID', description="Item ID")
    force_crate: Optional[bool] = Field(None, validation_alias=AliasChoices('ForceCrate', 'forceCrate'), serialization_alias='ForceCrate')
    noted_conditions: Optional[str] = Field(None, validation_alias=AliasChoices('NotedConditions', 'notedConditions'), serialization_alias='NotedConditions')
    do_not_tip: Optional[bool] = Field(None, validation_alias=AliasChoices('DoNotTip', 'doNotTip'), serialization_alias='DoNotTip')
    commodity_id: Optional[int] = Field(None, validation_alias=AliasChoices('CommodityId', 'commodityId'), serialization_alias='CommodityId', description="Commodity/HS code ID")

    @field_validator('commodity_id', 'item_id', 'qty', mode='before')
    @classmethod
    def empty_string_to_none(cls, v):
        """Convert empty strings to None for optional int fields."""
        if v == '':
            return None
        return v


class ImageLinkDto(ABConnectBaseModel):
    """Image link reference."""

    id: int = Field(..., alias='id')
    link: str = Field(..., alias='link')


class LotCatalogDto(ABConnectBaseModel):
    """Lot-to-catalog association."""

    catalog_id: int = Field(..., alias='catalogId')
    lot_number: str = Field(..., alias='lotNumber')


class LotCatalogInformationDto(ABConnectBaseModel):
    """Basic lot information within a catalog."""

    id: int = Field(..., alias='id')
    lot_number: str = Field(..., alias='lotNumber')


class SellerDto(ABConnectBaseModel):
    """Seller information."""

    id: int = Field(..., alias='id')
    name: Optional[str] = Field(None, alias='name')
    customer_display_id: int = Field(..., alias='customerDisplayId')
    is_active: bool = Field(..., alias='isActive')


class CatalogDto(ABConnectBaseModel):
    """Catalog information."""

    id: int = Field(..., alias='id')
    customer_catalog_id: Optional[str] = Field(None, alias='customerCatalogId')
    agent: Optional[str] = Field(None, alias='agent')
    title: Optional[str] = Field(None, alias='title')
    start_date: datetime = Field(..., alias='startDate')
    end_date: datetime = Field(..., alias='endDate')
    is_completed: bool = Field(..., alias='isCompleted')


class CatalogWithSellersDto(CatalogDto):
    """Catalog with associated sellers."""

    sellers: List[SellerDto] = Field(default_factory=list, alias='sellers')


class CatalogExpandedDto(CatalogDto):
    """Catalog with sellers and lots."""

    sellers: List[SellerDto] = Field(default_factory=list, alias='sellers')
    lots: List[LotCatalogInformationDto] = Field(default_factory=list, alias='lots')


class SellerExpandedDto(SellerDto):
    """Seller with associated catalogs."""

    catalogs: List[CatalogDto] = Field(default_factory=list, alias='catalogs')


class LotDto(ABConnectBaseModel):
    """Full lot information."""

    id: int = Field(..., alias='id')
    customer_item_id: Optional[str] = Field(None, alias='customerItemId')
    initial_data: LotDataDto = Field(..., alias='initialData')
    overriden_data: List[LotDataDto] = Field(default_factory=list, alias='overridenData')
    catalogs: List[LotCatalogDto] = Field(default_factory=list, alias='catalogs')
    image_links: List[ImageLinkDto] = Field(default_factory=list, alias='imageLinks')


class LotOverrideDto(LotDataDto):
    """Lot override data with customer item ID."""

    customer_item_id: str = Field(..., alias='customerItemId')


# =============================================================================
# Paginated Lists
# =============================================================================

class PaginatedList(ABConnectBaseModel):
    """Base paginated list response."""

    items: List[Any] = Field(default_factory=list, alias='items')
    page_number: int = Field(..., alias='pageNumber')
    total_pages: int = Field(..., alias='totalPages')
    total_items: int = Field(..., alias='totalItems')
    has_previous_page: bool = Field(..., alias='hasPreviousPage')
    has_next_page: bool = Field(..., alias='hasNextPage')


class CatalogExpandedDtoPaginatedList(PaginatedList):
    """Paginated list of expanded catalogs."""

    items: List[CatalogExpandedDto] = Field(default_factory=list, alias='items')


class LotDtoPaginatedList(PaginatedList):
    """Paginated list of lots."""

    items: List[LotDto] = Field(default_factory=list, alias='items')


class SellerExpandedDtoPaginatedList(PaginatedList):
    """Paginated list of expanded sellers."""

    items: List[SellerExpandedDto] = Field(default_factory=list, alias='items')


# =============================================================================
# Request Models (send camelCase to API)
# =============================================================================

class AddCatalogRequest(ABConnectBaseModel):
    """Request to create a new catalog."""

    customer_catalog_id: Optional[str] = Field(None, alias='customerCatalogId')
    agent: Optional[str] = Field(None, alias='agent')
    title: Optional[str] = Field(None, alias='title')
    start_date: datetime = Field(..., alias='startDate')
    end_date: datetime = Field(..., alias='endDate')
    seller_ids: List[int] = Field(default_factory=list, alias='sellerIds')


class UpdateCatalogRequest(AddCatalogRequest):
    """Request to update an existing catalog."""
    pass


class AddLotRequest(ABConnectBaseModel):
    """Request to create a new lot."""

    customer_item_id: Optional[str] = Field(None, alias='customerItemId')
    image_links: List[str] = Field(default_factory=list, alias='imageLinks')
    overriden_data: List[LotDataDto] = Field(default_factory=list, alias='overridenData')
    catalogs: List[LotCatalogDto] = Field(default_factory=list, alias='catalogs')
    initial_data: LotDataDto = Field(..., alias='initialData')


class UpdateLotRequest(ABConnectBaseModel):
    """Request to update an existing lot."""

    customer_item_id: Optional[str] = Field(None, alias='customerItemId')
    image_links: List[str] = Field(default_factory=list, alias='imageLinks')
    overriden_data: List[LotDataDto] = Field(default_factory=list, alias='overridenData')
    catalogs: List[LotCatalogDto] = Field(default_factory=list, alias='catalogs')


class GetLotsOverridesQuery(ABConnectBaseModel):
    """Query parameters for getting lot overrides."""

    customer_comments: Optional[str] = Field(None, alias='customerComments')
    other_ref_no: Optional[str] = Field(None, alias='otherRefNo')
    customer_item_ids: List[str] = Field(default_factory=list, alias='customerItemIds')


class AddSellerRequest(ABConnectBaseModel):
    """Request to create a new seller."""

    name: Optional[str] = Field(None, alias='name')
    customer_display_id: int = Field(..., alias='customerDisplayId')
    is_active: bool = Field(..., alias='isActive')


class UpdateSellerRequest(AddSellerRequest):
    """Request to update an existing seller."""
    pass


# =============================================================================
# Bulk Request Models
# =============================================================================

class BulkInsertSellerRequest(ABConnectBaseModel):
    """Seller data for bulk insert."""

    name: Optional[str] = Field(None, alias='name')
    customer_display_id: int = Field(..., alias='customerDisplayId')
    is_active: bool = Field(..., alias='isActive')


class BulkInsertLotRequest(ABConnectBaseModel):
    """Lot data for bulk insert."""

    customer_item_id: str = Field(..., alias='customerItemId')
    lot_number: str = Field(..., alias='lotNumber')
    image_links: List[str] = Field(default_factory=list, alias='imageLinks')
    initial_data: LotDataDto = Field(..., alias='initialData')
    overriden_data: List[LotDataDto] = Field(default_factory=list, alias='overridenData')


class BulkInsertCatalogRequest(ABConnectBaseModel):
    """Catalog data for bulk insert."""

    customer_catalog_id: str = Field(..., alias='customerCatalogId')
    agent: str = Field(..., alias='agent')
    title: str = Field(..., alias='title')
    start_date: datetime = Field(..., alias='startDate')
    end_date: datetime = Field(..., alias='endDate')
    lots: List[BulkInsertLotRequest] = Field(default_factory=list, alias='lots')
    sellers: List[BulkInsertSellerRequest] = Field(default_factory=list, alias='sellers')


class BulkInsertRequest(ABConnectBaseModel):
    """Request for bulk insert of catalogs, lots, and sellers."""

    catalogs: List[BulkInsertCatalogRequest] = Field(default_factory=list, alias='catalogs')
