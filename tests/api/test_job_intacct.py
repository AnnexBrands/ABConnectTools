"""Tests for Job Intacct endpoints."""

import pytest
from tests.constants import JOB_DISPLAY_ID


@pytest.mark.integration
def test_get_jobintacct(api):
    """get_jobintacct returns intacct data for job"""
    result = api.jobs.intacct.get_jobintacct(JOB_DISPLAY_ID)
    assert result is not None


# ==============================================================================
# Write operations — xfail
# ==============================================================================

@pytest.mark.integration
@pytest.mark.xfail(reason="Human: Write op. POST creates intacct entry.")
def test_post_jobintacct(api):
    """post_jobintacct creates intacct entry"""
    result = api.jobs.intacct.post_jobintacct(JOB_DISPLAY_ID, data={})
    assert result is not None


@pytest.mark.integration
@pytest.mark.xfail(reason="Human: Write op. POST creates intacct draft.")
def test_post_jobintacct_draft(api):
    """post_jobintacct_draft creates intacct draft"""
    result = api.jobs.intacct.post_jobintacct_draft(JOB_DISPLAY_ID, data={})
    assert result is not None
