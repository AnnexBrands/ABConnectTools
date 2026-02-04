"""Tests for Views API endpoints."""

import pytest
from ABConnect.api import models
from tests.constants import VIEW_ID


# ==============================================================================
# Parameterless GETs (working)
# ==============================================================================

@pytest.mark.integration
def test_get_views_all(api):
    """server returns all views"""
    views = api.views.get_all()
    assert isinstance(views, list), "api.views.get_all should return a list"


def test_views_all_fixture(ViewsAllData):
    """fixture has expected structure"""
    for item in ViewsAllData:
        models.GridViewDetails.model_validate(item)


@pytest.mark.integration
def test_get_datasetsps(api):
    """server returns dataset stored procedures as list of strings"""
    datasetsps = api.views.get_datasetsps()
    assert isinstance(datasetsps, list), "datasetsps should be a list"
    assert all(isinstance(sp, str) for sp in datasetsps), "all stored procedures should be strings"


def test_datasetsps_fixture(ViewsDatasetSpsData):
    """fixture has expected structure - list of stored procedure name strings"""
    assert isinstance(ViewsDatasetSpsData, list), "ViewsDatasetSps fixture should be a list"
    assert all(isinstance(sp, str) for sp in ViewsDatasetSpsData), "all stored procedures should be strings"


# ==============================================================================
# DATASETSP - parameterized GET (can use SP name from fixture)
# ==============================================================================

@pytest.mark.integration
def test_get_datasetsp(api, ViewsDatasetSpsData):
    """server returns columns for a specific stored procedure"""
    if not ViewsDatasetSpsData:
        pytest.skip("No stored procedures available in fixture")
    sp_name = ViewsDatasetSpsData[0]
    columns = api.views.get_datasetsp(sp_name)
    assert isinstance(columns, list), "datasetsp should return a list"


# ==============================================================================
# Parameterized GETs using VIEW_ID from constants
# ==============================================================================

@pytest.mark.integration
def test_get_view(api):
    """get_get returns a specific view"""
    result = api.views.get_get(str(VIEW_ID))
    assert isinstance(result, models.GridViewDetails)


@pytest.mark.integration
def test_get_accessinfo(api):
    """get_accessinfo returns view access info"""
    result = api.views.get_accessinfo(str(VIEW_ID))
    assert result is not None


# ==============================================================================
# Write operations
# ==============================================================================

@pytest.mark.integration
@pytest.mark.xfail(reason=(
    "Human: Destructive operation. Only test if safe to delete a view in staging. "
    "Call api.views.delete_delete(viewId) with a test view."
))
def test_delete_view(api):
    """delete_delete removes a view"""
    result = api.views.delete_delete("NEED_VALID_VIEW_ID")
    assert result is not None


@pytest.mark.integration
@pytest.mark.xfail(reason=(
    "Human: Write operation. Call api.views.post_post(data) with valid "
    "GridViewDetails data. Inspect ViewsAll fixture for field structure."
))
def test_create_view(api):
    """post_post creates a new view"""
    result = api.views.post_post({"name": "test_view"})
    assert result is not None


@pytest.mark.integration
@pytest.mark.xfail(reason=(
    "Human: Write operation. Call api.views.put_access(viewId, data) "
    "with VIEW_ID and access data."
))
def test_put_access(api):
    """put_access updates view access permissions"""
    result = api.views.put_access(str(VIEW_ID), {})
    assert result is not None
