"""Tests for Job SMS endpoints."""

import pytest
from tests.constants import JOB_DISPLAY_ID


@pytest.mark.integration
def test_get_sms(api):
    """get_sms returns SMS data for job"""
    result = api.jobs.sms.get_sms(JOB_DISPLAY_ID)
    assert result is not None


@pytest.mark.integration
@pytest.mark.xfail(reason="Human: Needs a valid templateId from SmsTemplateList fixture.")
def test_get_sms_templatebased(api):
    """get_sms_templatebased returns template-based SMS"""
    result = api.jobs.sms.get_sms_templatebased("NEED_TEMPLATE_ID", JOB_DISPLAY_ID)
    assert result is not None


# ==============================================================================
# Write operations — xfail
# ==============================================================================

@pytest.mark.integration
@pytest.mark.xfail(reason="Human: Write op. POST sends an SMS — do NOT test without confirmation.")
def test_post_sms(api):
    """post_sms sends an SMS"""
    result = api.jobs.sms.post_sms(JOB_DISPLAY_ID, data={})
    assert result is not None
