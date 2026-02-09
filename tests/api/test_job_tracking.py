"""Tests for Job Tracking endpoints."""

import pytest
from tests.constants import JOB_DISPLAY_ID


@pytest.mark.integration
def test_get_tracking(api):
    """get_tracking returns tracking data for job"""
    result = api.jobs.tracking.get_tracking(JOB_DISPLAY_ID)
    assert result is not None


@pytest.mark.integration
@pytest.mark.xfail(reason="Human: Needs a valid proNumber from tracking response.")
def test_get_tracking_shipment(api):
    """get_tracking_shipment returns shipment tracking"""
    result = api.jobs.tracking.get_tracking_shipment("NEED_PRO_NUMBER", JOB_DISPLAY_ID)
    assert result is not None
