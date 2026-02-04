"""Tests for Job OnHold endpoints."""

import pytest
from tests.constants import JOB_DISPLAY_ID


@pytest.mark.integration
def test_get_onhold_list(api):
    """get_onhold_list returns on-hold items for job"""
    result = api.jobs.onhold.get_onhold_list(JOB_DISPLAY_ID)
    assert result is not None


@pytest.mark.integration
def test_get_onhold_followupusers(api):
    """get_onhold_followupusers returns follow-up users"""
    result = api.jobs.onhold.get_onhold_followupusers(JOB_DISPLAY_ID)
    assert result is not None


# ==============================================================================
# Routes needing onHoldId (genuinely missing)
# ==============================================================================

@pytest.mark.integration
@pytest.mark.xfail(reason="Human: Needs a valid onHoldId from get_onhold_list response.")
def test_get_onhold(api):
    """get_onhold returns a specific on-hold item"""
    result = api.jobs.onhold.get_onhold(JOB_DISPLAY_ID, "NEED_ONHOLD_ID")
    assert result is not None


@pytest.mark.integration
@pytest.mark.xfail(reason="Human: Needs a valid onHoldId and contactId.")
def test_get_onhold_followupuser(api):
    """get_onhold_followupuser returns a specific follow-up user"""
    from tests.constants import CONTACT_ID
    result = api.jobs.onhold.get_onhold_followupuser(JOB_DISPLAY_ID, str(CONTACT_ID))
    assert result is not None


# ==============================================================================
# Write operations — xfail
# ==============================================================================

@pytest.mark.integration
@pytest.mark.xfail(reason="Human: Write op. POST creates on-hold, needs SaveOnHoldRequest data.")
def test_post_onhold(api):
    """post_onhold creates an on-hold item"""
    result = api.jobs.onhold.post_onhold(JOB_DISPLAY_ID, data={})
    assert result is not None


@pytest.mark.integration
@pytest.mark.xfail(reason="Human: Destructive. DELETE removes on-hold for job.")
def test_delete_onhold(api):
    """delete_onhold deletes on-hold items"""
    result = api.jobs.onhold.delete_onhold(JOB_DISPLAY_ID)
    assert result is not None
