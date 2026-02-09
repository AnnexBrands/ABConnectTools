"""Tests for Job Shipment endpoints."""

import pytest
from tests.constants import JOB_DISPLAY_ID


@pytest.mark.integration
def test_get_shipment_origindestination(api):
    """get_shipment_origindestination returns origin/destination"""
    result = api.jobs.shipment.get_shipment_origindestination(JOB_DISPLAY_ID)
    assert result is not None


@pytest.mark.integration
def test_get_shipment_accessorials(api):
    """get_shipment_accessorials returns accessorials for job"""
    result = api.jobs.shipment.get_shipment_accessorials(JOB_DISPLAY_ID)
    assert result is not None


@pytest.mark.integration
def test_get_shipment_ratesstate(api):
    """get_shipment_ratesstate returns rates state"""
    result = api.jobs.shipment.get_shipment_ratesstate(JOB_DISPLAY_ID)
    assert result is not None


@pytest.mark.integration
def test_get_shipment_exportdata(api):
    """get_shipment_exportdata returns export data"""
    result = api.jobs.shipment.get_shipment_exportdata(JOB_DISPLAY_ID)
    assert result is not None


@pytest.mark.integration
def test_get_shipment_ratequotes(api):
    """get_shipment_ratequotes returns rate quotes"""
    result = api.jobs.shipment.get_shipment_ratequotes(JOB_DISPLAY_ID)
    assert result is not None


# ==============================================================================
# Write operations — xfail
# ==============================================================================

@pytest.mark.integration
@pytest.mark.xfail(reason="Human: Write op. POST books a shipment.")
def test_post_shipment_book(api):
    """post_shipment_book books a shipment"""
    result = api.jobs.shipment.post_shipment_book(JOB_DISPLAY_ID, data={})
    assert result is not None


@pytest.mark.integration
@pytest.mark.xfail(reason="Human: Destructive. DELETE removes shipment.")
def test_delete_shipment(api):
    """delete_shipment deletes a shipment"""
    result = api.jobs.shipment.delete_shipment(JOB_DISPLAY_ID)
    assert result is not None
