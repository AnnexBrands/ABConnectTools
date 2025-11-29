from typing import List, Optional, Any
from datetime import datetime
from pydantic import BaseModel, Field, validator


# Core model shared across various DTOs
class LotDataDto(BaseModel):
    qty: Optional[int] = Field(None, alias='Qty')
    l: Optional[float] = Field(None, alias='L')
    w: Optional[float] = Field(None, alias='W')
    h: Optional[float] = Field(None, alias='H')
    wgt: Optional[float] = Field(None, alias='Wgt')
    value: Optional[float] = Field(None, alias='Value')
    cpack: Optional[int] = Field(None, alias='Cpack')
    description: Optional[str] = Field(None, alias='Description')
    force_crate: Optional[bool] = Field(None, alias='ForceCrate')
    item_id: Optional[int] = Field(None, alias='ItemID')
    notes: Optional[str] = Field(None, alias='Notes')
    noted_conditions: Optional[str] = Field(None, alias='NotedConditions')
    do_not_tip: Optional[bool] = Field(None, alias='DoNotTip')
    commodity_id: Optional[int] = Field(None, alias='CommodityId')

    class Config:
        populate_by_name = True
        allow_population_by_field_name = True


class ImageLinkDto(BaseModel):
    id: int = Field(..., alias='Id')
    link: str


class LotCatalogDto(BaseModel):
    catalog_id: int = Field(..., alias='CatalogId')
    lot_number: str = Field(..., alias='LotNumber')


class LotCatalogInformationDto(BaseModel):
    id: int
    lot_number: str = Field(..., alias='LotNumber')


class SellerDto(BaseModel):
    id: int
    name: Optional[str] = None
    customer_display_id: int = Field(..., alias='CustomerDisplayId')
    is_active: bool = Field(..., alias='IsActive')


class CatalogDto(BaseModel):
    id: int
    customer_catalog_id: Optional[str] = Field(None, alias='CustomerCatalogId')
    agent: Optional[str] = None
    title: Optional[str] = None
    start_date: datetime = Field(..., alias='StartDate')
    end_date: datetime = Field(..., alias='EndDate')
    is_completed: bool = Field(..., alias='IsCompleted')


class CatalogWithSellersDto(CatalogDto):
    sellers: List[SellerDto]


class CatalogExpandedDto(CatalogDto):
    sellers: List[SellerDto]
    lots: List[LotCatalogInformationDto]


class SellerExpandedDto(SellerDto):
    catalogs: List[CatalogDto]


class PaginatedList(BaseModel):
    items: List[Any]
    page_number: int = Field(..., alias='PageNumber')
    total_pages: int = Field(..., alias='TotalPages')
    total_items: int = Field(..., alias='TotalItems')
    has_previous_page: bool = Field(..., alias='HasPreviousPage')
    has_next_page: bool = Field(..., alias='HasNextPage')


class CatalogExpandedDtoPaginatedList(PaginatedList):
    items: List[CatalogExpandedDto]


class LotDtoPaginatedList(PaginatedList):
    items: List['LotDto']


class SellerExpandedDtoPaginatedList(PaginatedList):
    items: List[SellerExpandedDto]


class LotDto(BaseModel):
    id: int
    customer_item_id: Optional[str] = Field(None, alias='CustomerItemId')
    initial_data: LotDataDto = Field(..., alias='InitialData')
    overriden_data: List[LotDataDto] = Field(default_factory=list, alias='OverridenData')
    catalogs: List[LotCatalogDto]
    image_links: List[ImageLinkDto] = Field(default_factory=list, alias='ImageLinks')


# Bulk models
class BulkInsertSellerRequest(BaseModel):
    name: Optional[str] = None
    customer_display_id: int = Field(..., alias='CustomerDisplayId')
    is_active: bool = Field(..., alias='IsActive')


class BulkInsertLotRequest(BaseModel):
    customer_item_id: str = Field(..., alias='CustomerItemId')
    lot_number: str = Field(..., alias='LotNumber')
    image_links: List[str] = Field(default_factory=list, alias='ImageLinks')
    initial_data: LotDataDto = Field(..., alias='InitialData')
    overriden_data: List[LotDataDto] = Field(default_factory=list, alias='OverridenData')


class BulkInsertCatalogRequest(BaseModel):
    customer_catalog_id: str = Field(..., alias='CustomerCatalogId')
    agent: str
    title: str
    start_date: datetime = Field(..., alias='StartDate')
    end_date: datetime = Field(..., alias='EndDate')
    lots: List[BulkInsertLotRequest] = Field(default_factory=list)
    sellers: List[BulkInsertSellerRequest] = Field(default_factory=list)


class BulkInsertRequest(BaseModel):
    catalogs: List[BulkInsertCatalogRequest]


# Request models
class AddCatalogRequest(BaseModel):
    customer_catalog_id: Optional[str] = Field(None, alias='CustomerCatalogId')
    agent: Optional[str] = None
    title: Optional[str] = None
    start_date: datetime = Field(..., alias='StartDate')
    end_date: datetime = Field(..., alias='EndDate')
    seller_ids: Optional[List[int]] = Field(default_factory=list, alias='SellerIds')


class UpdateCatalogRequest(AddCatalogRequest):
    pass


class AddLotRequest(BaseModel):
    customer_item_id: Optional[str] = Field(None, alias='CustomerItemId')
    image_links: Optional[List[str]] = Field(default_factory=list, alias='ImageLinks')
    overriden_data: Optional[List[LotDataDto]] = Field(default_factory=list, alias='OverridenData')
    catalogs: Optional[List[LotCatalogDto]] = Field(default_factory=list)
    initial_data: LotDataDto = Field(..., alias='InitialData')


class UpdateLotRequest(BaseModel):
    customer_item_id: Optional[str] = Field(None, alias='CustomerItemId')
    image_links: Optional[List[str]] = Field(default_factory=list, alias='ImageLinks')
    overriden_data: Optional[List[LotDataDto]] = Field(default_factory=list, alias='OverridenData')
    catalogs: Optional[List[LotCatalogDto]] = Field(default_factory=list)


class GetLotsOverridesQuery(BaseModel):
    customer_comments: Optional[str] = Field(None, alias='CustomerComments')
    other_ref_no: Optional[str] = Field(None, alias='OtherRefNo')
    customer_item_ids: Optional[List[str]] = Field(default_factory=list, alias='CustomerItemIds')


class LotOverrideDto(LotDataDto):
    customer_item_id: str = Field(..., alias='CustomerItemId')


class AddSellerRequest(BaseModel):
    name: Optional[str] = None
    customer_display_id: int = Field(..., alias='CustomerDisplayId')
    is_active: bool = Field(..., alias='IsActive')


class UpdateSellerRequest(AddSellerRequest):
    pass


# Validator example for required fields (can be extended)
@validator('*', pre=True, always=True)
def check_required_fields(cls, v, field, **kwargs):
    # Example: Ensure dates are not in the past/future if needed; customize per model
    return v


class SchemaValidator:
    """
    A utility class to validate requests and responses against the schema models.
    Usage:
        validator = SchemaValidator()
        is_valid, errors = validator.validate_request('POST', '/api/Catalog', data=request_data)
        is_valid, errors = validator.validate_response('POST', '/api/Catalog', status_code=200, data=response_data)
    """

    def __init__(self):
        self.request_models = {
            'POST_/api/Bulk/insert': BulkInsertRequest,
            'POST_/api/Catalog': AddCatalogRequest,
            'GET_/api/Catalog': None,  # No request body
            'PUT_/api/Catalog/{id}': UpdateCatalogRequest,
            'DELETE_/api/Catalog/{id}': None,
            'GET_/api/Catalog/{id}': None,
            'POST_/api/Lot': AddLotRequest,
            'GET_/api/Lot': None,
            'PUT_/api/Lot/{id}': UpdateLotRequest,
            'DELETE_/api/Lot/{id}': None,
            'GET_/api/Lot/{id}': None,
            'POST_/api/Lot/get-overrides': GetLotsOverridesQuery,
            'POST_/api/Seller': AddSellerRequest,
            'GET_/api/Seller': None,
            'PUT_/api/Seller/{id}': UpdateSellerRequest,
            'DELETE_/api/Seller/{id}': None,
            'GET_/api/Seller/{id}': None,
        }
        self.response_models = {
            'POST_/api/Bulk/insert': None,  # No body
            'POST_/api/Catalog': CatalogWithSellersDto,
            'GET_/api/Catalog': CatalogExpandedDtoPaginatedList,
            'PUT_/api/Catalog/{id}': CatalogWithSellersDto,
            'DELETE_/api/Catalog/{id}': None,  # 204
            'GET_/api/Catalog/{id}': CatalogExpandedDto,
            'POST_/api/Lot': LotDto,
            'GET_/api/Lot': LotDtoPaginatedList,
            'PUT_/api/Lot/{id}': LotDto,
            'DELETE_/api/Lot/{id}': None,
            'GET_/api/Lot/{id}': LotDto,
            'POST_/api/Lot/get-overrides': List[LotOverrideDto],
            'POST_/api/Seller': SellerDto,
            'GET_/api/Seller': SellerExpandedDtoPaginatedList,
            'PUT_/api/Seller/{id}': SellerDto,
            'DELETE_/api/Seller/{id}': None,
            'GET_/api/Seller/{id}': SellerExpandedDto,
        }

    def _get_key(self, method: str, path: str) -> str:
        # Normalize path (ignore path params for simplicity; extend if needed)
        path = path.replace('/{id}', '/{id}').replace('/{lotId}', '/{id}')  # Assuming {id} for lots too
        return f'{method}_{path}'

    def validate_request(self, method: str, path: str, data: dict, query_params: dict = None) -> tuple[bool, Optional[str]]:
        """
        Validates the request body and optionally query params against the schema.
        Returns (is_valid: bool, error_msg: str or None)
        """
        key = self._get_key(method, path)
        model = self.request_models.get(key)
        if model is None:
            return True, None  # No body expected
        try:
            validated = model(**data)
            # For query params, you can add validation logic here if models are extended
            if query_params:
                # Placeholder: extend with query param models if needed
                pass
            return True, None
        except ValueError as e:
            return False, str(e)

    def validate_response(self, method: str, path: str, status_code: int, data: dict) -> tuple[bool, Optional[str]]:
        """
        Validates the response body against the schema for the given status_code.
        Assumes 200/201 for success; extend for errors (e.g., ProblemDetails).
        Returns (is_valid: bool, error_msg: str or None)
        """
        if status_code not in (200, 201, 204):
            # For errors, validate against ProblemDetails if provided
            try:
                from pydantic import create_model  # Dynamic if not defined
                ProblemDetails = create_model('ProblemDetails', type=(str, ...), title=(str, ...), status=(int, ...), detail=(str, ...))
                ProblemDetails(**data)
                return True, None
            except ValueError:
                return False, "Invalid error response format"
            return True, None  # Skip for non-2xx if not implemented

        if status_code == 204:
            return data is None, "204 should have no body" if data else None

        key = self._get_key(method, path)
        model = self.response_models.get(key)
        if model is None:
            return True, None
        try:
            validated = model(**data)
            return True, None
        except ValueError as e:
            return False, str(e)


# Example usage (commented out)
# validator = SchemaValidator()
# is_valid, err = validator.validate_request('POST', '/api/Catalog', {'startDate': '2025-01-01T00:00:00', 'endDate': '2025-01-02T00:00:00'})
# print(is_valid, err)