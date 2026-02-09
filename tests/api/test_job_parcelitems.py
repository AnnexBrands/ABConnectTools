"""Tests for Job ParcelItems endpoints."""

import pytest
from tests.constants import JOB_DISPLAY_ID


@pytest.mark.integration
def test_get_parcelitems(api):
    """get_parcelitems returns parcel items for job"""
    result = api.jobs.parcelitems.get_parcelitems(JOB_DISPLAY_ID)
    assert result is not None


@pytest.mark.integration
def test_get_parcel_items_with_materials(api):
    """get_parcel_items_with_materials returns parcel items with materials"""
    result = api.jobs.parcelitems.get_parcel_items_with_materials(JOB_DISPLAY_ID)
    assert result is not None


# ==============================================================================
# Write operations — xfail
# ==============================================================================

@pytest.mark.integration
@pytest.mark.xfail(reason="Human: Write op. POST saves parcel items.")
def test_post_parcelitems(api):
    """post_parcelitems saves parcel items"""
    result = api.jobs.parcelitems.post_parcelitems(JOB_DISPLAY_ID, data={})
    assert result is not None
