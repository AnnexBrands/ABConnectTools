"""Tests for Catalog API endpoints (catalog-api.abconnect.co).

Covers all 17 HTTP methods across Catalog, Lot, Seller, and Bulk endpoints.
"""

import pytest
from ABConnect.api.models.catalog import (
    CatalogExpandedDtoPaginatedList,
    CatalogExpandedDto,
    LotDtoPaginatedList,
    LotDto,
    SellerExpandedDtoPaginatedList,
    SellerExpandedDto,
    SellerDto,
    PaginatedList,
)


# ==============================================================================
# Catalog endpoint - GET /api/Catalog
# ==============================================================================

@pytest.mark.integration
def test_catalog_list(api):
    """api.catalog.catalogs.list() returns paginated catalog list"""
    result = api.catalog.catalogs.list()
    assert isinstance(result, CatalogExpandedDtoPaginatedList), "Should return CatalogExpandedDtoPaginatedList"
    assert hasattr(result, 'items'), "Result should have items"
    assert hasattr(result, 'page_number'), "Result should have page_number"
    assert hasattr(result, 'total_pages'), "Result should have total_pages"
    assert hasattr(result, 'total_items'), "Result should have total_items"
    assert isinstance(result.items, list), "items should be a list"


@pytest.mark.integration
def test_catalog_list_filter_customer_catalog_id(api):
    """api.catalog.catalogs.list(customer_catalog_id=...) filters by customer catalog ID"""
    all_result = api.catalog.catalogs.list()
    if not all_result.items:
        pytest.skip("No catalogs available to test filtering")
    target = all_result.items[0].customer_catalog_id
    result = api.catalog.catalogs.list(customer_catalog_id=target)
    assert isinstance(result, CatalogExpandedDtoPaginatedList)
    for item in result.items:
        assert item.customer_catalog_id == target


@pytest.mark.integration
def test_catalog_list_filter_is_completed(api):
    """api.catalog.catalogs.list(is_completed=...) filters by completion status"""
    result = api.catalog.catalogs.list(is_completed=False)
    assert isinstance(result, CatalogExpandedDtoPaginatedList)
    for item in result.items:
        assert item.is_completed is False


def test_catalog_list_fixture(CatalogListData):
    """CatalogList fixture has expected paginated structure"""
    assert isinstance(CatalogListData, dict), "CatalogList fixture should be a dict"
    assert "items" in CatalogListData, "Should have items key"
    assert "pageNumber" in CatalogListData, "Should have pageNumber key"
    assert "totalPages" in CatalogListData, "Should have totalPages key"
    assert "totalItems" in CatalogListData, "Should have totalItems key"


def test_catalog_list_fixture_validates(CatalogListData):
    """CatalogList fixture validates against CatalogExpandedDtoPaginatedList model"""
    result = CatalogExpandedDtoPaginatedList.model_validate(CatalogListData)
    assert isinstance(result, CatalogExpandedDtoPaginatedList)
    assert isinstance(result.items, list)
    if result.items:
        item = result.items[0]
        assert isinstance(item, CatalogExpandedDto)
        assert hasattr(item, 'id')
        assert hasattr(item, 'title')
        assert hasattr(item, 'start_date')
        assert hasattr(item, 'end_date')


# ==============================================================================
# Catalog endpoint - GET /api/Catalog/{id}
# ==============================================================================

@pytest.mark.integration
@pytest.mark.xfail(reason=(
    "Human: Call api.catalog.catalogs.get(catalog_id) with a valid catalog ID "
    "from the CatalogList fixture (pick first item's id field). "
    "Save fixture via save_fixture(result, 'CatalogDetail')."
))
def test_catalog_get(api):
    """api.catalog.catalogs.get() returns a specific catalog"""
    result = api.catalog.catalogs.get(catalog_id=0)
    assert isinstance(result, CatalogExpandedDto)


# ==============================================================================
# Catalog endpoint - POST /api/Catalog
# ==============================================================================

@pytest.mark.integration
@pytest.mark.xfail(reason=(
    "Human: Write operation. Call api.catalog.catalogs.create(data) with a valid "
    "AddCatalogRequest. Inspect CatalogList fixture for field structure."
))
def test_catalog_create(api):
    """api.catalog.catalogs.create() creates a new catalog"""
    from ABConnect.api.models.catalog import AddCatalogRequest
    from datetime import datetime
    data = AddCatalogRequest(
        customer_catalog_id="TEST-001",
        title="Test Catalog",
        start_date=datetime.now(),
        end_date=datetime.now(),
    )
    result = api.catalog.catalogs.create(data)
    assert result is not None


# ==============================================================================
# Catalog endpoint - PUT /api/Catalog/{id}
# ==============================================================================

@pytest.mark.integration
@pytest.mark.xfail(reason=(
    "Human: Write operation. Call api.catalog.catalogs.update(catalog_id, data) "
    "with a valid catalog ID and UpdateCatalogRequest."
))
def test_catalog_update(api):
    """api.catalog.catalogs.update() updates an existing catalog"""
    from ABConnect.api.models.catalog import UpdateCatalogRequest
    from datetime import datetime
    data = UpdateCatalogRequest(
        customer_catalog_id="TEST-001",
        title="Updated Catalog",
        start_date=datetime.now(),
        end_date=datetime.now(),
    )
    result = api.catalog.catalogs.update(catalog_id=0, data=data)
    assert result is not None


# ==============================================================================
# Catalog endpoint - DELETE /api/Catalog/{id}
# ==============================================================================

@pytest.mark.integration
@pytest.mark.xfail(reason=(
    "Human: Destructive operation. Only test if safe to delete a catalog in staging. "
    "Call api.catalog.catalogs.delete(catalog_id) with a test catalog."
))
def test_catalog_delete(api):
    """api.catalog.catalogs.delete() removes a catalog"""
    api.catalog.catalogs.delete(catalog_id=0)


# ==============================================================================
# Seller endpoint - GET /api/Seller
# ==============================================================================

@pytest.mark.integration
def test_seller_list(api):
    """api.catalog.sellers.list() returns paginated seller list"""
    result = api.catalog.sellers.list()
    assert isinstance(result, SellerExpandedDtoPaginatedList), "Should return SellerExpandedDtoPaginatedList"
    assert hasattr(result, 'items'), "Result should have items"
    assert hasattr(result, 'page_number'), "Result should have page_number"
    assert hasattr(result, 'total_items'), "Result should have total_items"
    assert isinstance(result.items, list), "items should be a list"


@pytest.mark.integration
def test_seller_list_filter_is_active(api):
    """api.catalog.sellers.list(is_active=...) filters by active status"""
    result = api.catalog.sellers.list(is_active=True)
    assert isinstance(result, SellerExpandedDtoPaginatedList)
    for item in result.items:
        assert item.is_active is True


@pytest.mark.integration
def test_seller_list_filter_name(api):
    """api.catalog.sellers.list(name=...) filters by seller name"""
    all_result = api.catalog.sellers.list()
    if not all_result.items:
        pytest.skip("No sellers available to test filtering")
    target = all_result.items[0].name
    result = api.catalog.sellers.list(name=target)
    assert isinstance(result, SellerExpandedDtoPaginatedList)
    for item in result.items:
        assert item.name == target


def test_seller_list_fixture(CatalogSellerListData):
    """CatalogSellerList fixture has expected paginated structure"""
    assert isinstance(CatalogSellerListData, dict), "CatalogSellerList fixture should be a dict"
    assert "items" in CatalogSellerListData, "Should have items key"
    assert "pageNumber" in CatalogSellerListData, "Should have pageNumber key"
    assert "totalItems" in CatalogSellerListData, "Should have totalItems key"


def test_seller_list_fixture_validates(CatalogSellerListData):
    """CatalogSellerList fixture validates against SellerExpandedDtoPaginatedList model"""
    result = SellerExpandedDtoPaginatedList.model_validate(CatalogSellerListData)
    assert isinstance(result, SellerExpandedDtoPaginatedList)
    assert isinstance(result.items, list)
    if result.items:
        item = result.items[0]
        assert isinstance(item, SellerExpandedDto)
        assert hasattr(item, 'id')
        assert hasattr(item, 'name')
        assert hasattr(item, 'customer_display_id')
        assert hasattr(item, 'is_active')


# ==============================================================================
# Seller endpoint - GET /api/Seller/{id}
# ==============================================================================

@pytest.mark.integration
@pytest.mark.xfail(reason=(
    "Human: Call api.catalog.sellers.get(seller_id) with a valid seller ID "
    "from the CatalogSellerList fixture (pick first item's id field). "
    "Save fixture via save_fixture(result, 'CatalogSellerDetail')."
))
def test_seller_get(api):
    """api.catalog.sellers.get() returns a specific seller"""
    result = api.catalog.sellers.get(seller_id=0)
    assert isinstance(result, SellerExpandedDto)


# ==============================================================================
# Seller endpoint - POST /api/Seller
# ==============================================================================

@pytest.mark.integration
@pytest.mark.xfail(reason=(
    "Human: Write operation. Call api.catalog.sellers.create(data) with a valid "
    "AddSellerRequest. Inspect CatalogSellerList fixture for field structure."
))
def test_seller_create(api):
    """api.catalog.sellers.create() creates a new seller"""
    from ABConnect.api.models.catalog import AddSellerRequest
    data = AddSellerRequest(
        name="Test Seller",
        customer_display_id=99999,
        is_active=True,
    )
    result = api.catalog.sellers.create(data)
    assert result is not None


# ==============================================================================
# Seller endpoint - PUT /api/Seller/{id}
# ==============================================================================

@pytest.mark.integration
@pytest.mark.xfail(reason=(
    "Human: Write operation. Call api.catalog.sellers.update(seller_id, data) "
    "with a valid seller ID and UpdateSellerRequest."
))
def test_seller_update(api):
    """api.catalog.sellers.update() updates an existing seller"""
    from ABConnect.api.models.catalog import UpdateSellerRequest
    data = UpdateSellerRequest(
        name="Updated Seller",
        customer_display_id=99999,
        is_active=True,
    )
    result = api.catalog.sellers.update(seller_id=0, data=data)
    assert result is not None


# ==============================================================================
# Seller endpoint - DELETE /api/Seller/{id}
# ==============================================================================

@pytest.mark.integration
@pytest.mark.xfail(reason=(
    "Human: Destructive operation. Only test if safe to delete a seller in staging. "
    "Call api.catalog.sellers.delete(seller_id) with a test seller."
))
def test_seller_delete(api):
    """api.catalog.sellers.delete() removes a seller"""
    api.catalog.sellers.delete(seller_id=0)


# ==============================================================================
# Lot endpoint - GET /api/Lot
# ==============================================================================

@pytest.mark.integration
def test_lot_list(api):
    """api.catalog.lots.list() returns paginated lot list"""
    result = api.catalog.lots.list()
    assert isinstance(result, LotDtoPaginatedList), "Should return LotDtoPaginatedList"
    assert hasattr(result, 'items'), "Result should have items"
    assert hasattr(result, 'page_number'), "Result should have page_number"
    assert hasattr(result, 'total_items'), "Result should have total_items"
    assert isinstance(result.items, list), "items should be a list"


@pytest.mark.integration
def test_lot_list_filter_customer_item_id(api):
    """api.catalog.lots.list(customer_item_id=...) filters by customer item ID"""
    all_result = api.catalog.lots.list()
    if not all_result.items:
        pytest.skip("No lots available to test filtering")
    target = all_result.items[0].customer_item_id
    result = api.catalog.lots.list(customer_item_id=target)
    assert isinstance(result, LotDtoPaginatedList)
    for item in result.items:
        assert item.customer_item_id == target


@pytest.mark.integration
def test_lot_list_filter_lot_number(api):
    """api.catalog.lots.list(lot_number=...) filters by lot number"""
    all_result = api.catalog.lots.list()
    if not all_result.items:
        pytest.skip("No lots available to test filtering")
    # Find a lot that has catalogs with a lot_number
    target = None
    for lot in all_result.items:
        if lot.catalogs:
            target = lot.catalogs[0].lot_number
            break
    if target is None:
        pytest.skip("No lots with lot_number available to test filtering")
    result = api.catalog.lots.list(lot_number=target)
    assert isinstance(result, LotDtoPaginatedList)


def test_lot_list_fixture(CatalogLotListData):
    """CatalogLotList fixture has expected paginated structure"""
    assert isinstance(CatalogLotListData, dict), "CatalogLotList fixture should be a dict"
    assert "items" in CatalogLotListData, "Should have items key"
    assert "pageNumber" in CatalogLotListData, "Should have pageNumber key"
    assert "totalItems" in CatalogLotListData, "Should have totalItems key"


def test_lot_list_fixture_validates(CatalogLotListData):
    """CatalogLotList fixture validates against LotDtoPaginatedList model"""
    result = LotDtoPaginatedList.model_validate(CatalogLotListData)
    assert isinstance(result, LotDtoPaginatedList)
    assert isinstance(result.items, list)
    if result.items:
        item = result.items[0]
        assert isinstance(item, LotDto)
        assert hasattr(item, 'id')
        assert hasattr(item, 'initial_data')
        assert hasattr(item, 'catalogs')


# ==============================================================================
# Lot endpoint - GET /api/Lot/{id}
# ==============================================================================

@pytest.mark.integration
@pytest.mark.xfail(reason=(
    "Human: Call api.catalog.lots.get(lot_id) with a valid lot ID "
    "from the CatalogLotList fixture (pick first item's id field). "
    "Save fixture via save_fixture(result, 'CatalogLotDetail')."
))
def test_lot_get(api):
    """api.catalog.lots.get() returns a specific lot"""
    result = api.catalog.lots.get(lot_id=0)
    assert isinstance(result, LotDto)


# ==============================================================================
# Lot endpoint - POST /api/Lot
# ==============================================================================

@pytest.mark.integration
@pytest.mark.xfail(reason=(
    "Human: Write operation. Call api.catalog.lots.create(data) with a valid "
    "AddLotRequest. Inspect CatalogLotList fixture for field structure."
))
def test_lot_create(api):
    """api.catalog.lots.create() creates a new lot"""
    from ABConnect.api.models.catalog import AddLotRequest, LotDataDto
    data = AddLotRequest(
        customer_item_id="TEST-LOT-001",
        initial_data=LotDataDto(description="Test lot"),
    )
    result = api.catalog.lots.create(data)
    assert result is not None


# ==============================================================================
# Lot endpoint - PUT /api/Lot/{id}
# ==============================================================================

@pytest.mark.integration
@pytest.mark.xfail(reason=(
    "Human: Write operation. Call api.catalog.lots.update(lot_id, data) "
    "with a valid lot ID and UpdateLotRequest."
))
def test_lot_update(api):
    """api.catalog.lots.update() updates an existing lot"""
    from ABConnect.api.models.catalog import UpdateLotRequest
    data = UpdateLotRequest(
        customer_item_id="TEST-LOT-001-UPDATED",
    )
    result = api.catalog.lots.update(lot_id=0, data=data)
    assert result is not None


# ==============================================================================
# Lot endpoint - DELETE /api/Lot/{id}
# ==============================================================================

@pytest.mark.integration
@pytest.mark.xfail(reason=(
    "Human: Destructive operation. Only test if safe to delete a lot in staging. "
    "Call api.catalog.lots.delete(lot_id) with a test lot."
))
def test_lot_delete(api):
    """api.catalog.lots.delete() removes a lot"""
    api.catalog.lots.delete(lot_id=0)


# ==============================================================================
# Lot endpoint - POST /api/Lot/get-overrides
# ==============================================================================

@pytest.mark.integration
@pytest.mark.xfail(reason=(
    "Human: Call api.catalog.lots.get_overrides(query) with a valid "
    "GetLotsOverridesQuery containing real customer_item_ids from the "
    "CatalogLotList fixture. Save fixture via save_fixture(result, 'CatalogLotOverrides')."
))
def test_lot_get_overrides(api):
    """api.catalog.lots.get_overrides() returns lot overrides"""
    from ABConnect.api.models.catalog import GetLotsOverridesQuery
    query = GetLotsOverridesQuery(customer_item_ids=["NEED_VALID_IDS"])
    result = api.catalog.lots.get_overrides(query)
    assert isinstance(result, list)


# ==============================================================================
# Bulk endpoint - POST /api/Bulk/insert
# ==============================================================================

@pytest.mark.integration
@pytest.mark.xfail(reason=(
    "Human: Write operation. Call api.catalog.bulk.insert(data) with a valid "
    "BulkInsertRequest. This creates catalogs, lots, and sellers in bulk."
))
def test_bulk_insert(api):
    """api.catalog.bulk.insert() performs bulk insert"""
    from ABConnect.api.models.catalog import BulkInsertRequest
    data = BulkInsertRequest(catalogs=[])
    api.catalog.bulk.insert(data)


# ==============================================================================
# Model validation tests
# ==============================================================================

def test_paginated_list_model():
    """PaginatedList model validates correctly"""
    data = {
        "items": [],
        "pageNumber": 1,
        "totalPages": 0,
        "totalItems": 0,
        "hasPreviousPage": False,
        "hasNextPage": False,
    }
    result = PaginatedList.model_validate(data)
    assert result.page_number == 1
    assert result.total_items == 0
    assert result.items == []


def test_catalog_expanded_dto_model():
    """CatalogExpandedDto validates with nested sellers and lots"""
    data = {
        "id": 1,
        "customerCatalogId": "CAT-001",
        "agent": "TestAgent",
        "title": "Test Catalog",
        "startDate": "2025-01-01T00:00:00",
        "endDate": "2025-12-31T00:00:00",
        "isCompleted": False,
        "sellers": [
            {"id": 1, "name": "Seller A", "customerDisplayId": 100, "isActive": True}
        ],
        "lots": [
            {"id": 10, "lotNumber": "LOT-001"}
        ],
    }
    result = CatalogExpandedDto.model_validate(data)
    assert result.id == 1
    assert result.title == "Test Catalog"
    assert len(result.sellers) == 1
    assert result.sellers[0].name == "Seller A"
    assert len(result.lots) == 1
    assert result.lots[0].lot_number == "LOT-001"


def test_seller_expanded_dto_model():
    """SellerExpandedDto validates with nested catalogs"""
    data = {
        "id": 1,
        "name": "Test Seller",
        "customerDisplayId": 100,
        "isActive": True,
        "catalogs": [
            {
                "id": 1,
                "customerCatalogId": "CAT-001",
                "title": "Catalog A",
                "startDate": "2025-01-01T00:00:00",
                "endDate": "2025-12-31T00:00:00",
                "isCompleted": False,
            }
        ],
    }
    result = SellerExpandedDto.model_validate(data)
    assert result.id == 1
    assert result.name == "Test Seller"
    assert len(result.catalogs) == 1
    assert result.catalogs[0].title == "Catalog A"


def test_lot_dto_model():
    """LotDto validates with nested initial_data and catalogs"""
    data = {
        "id": 1,
        "customerItemId": "ITEM-001",
        "initialData": {
            "Qty": 2,
            "L": 10.0,
            "W": 5.0,
            "H": 3.0,
            "Wgt": 15.0,
            "Description": "Test item",
        },
        "overridenData": [],
        "catalogs": [
            {"catalogId": 1, "lotNumber": "LOT-001"}
        ],
        "imageLinks": [],
    }
    result = LotDto.model_validate(data)
    assert result.id == 1
    assert result.customer_item_id == "ITEM-001"
    assert result.initial_data.qty == 2
    assert result.initial_data.l == 10.0
    assert result.initial_data.description == "Test item"
    assert len(result.catalogs) == 1
