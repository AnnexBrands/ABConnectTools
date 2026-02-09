"""Tests for Job Email endpoints."""

import pytest
from tests.constants import JOB_DISPLAY_ID


# All email routes are POST operations that send emails.

@pytest.mark.integration
@pytest.mark.xfail(reason="Human: Write op. POST sends email — do NOT test without confirmation.")
def test_post_email(api):
    """post_email sends an email"""
    result = api.jobs.email.post_email(JOB_DISPLAY_ID, data={})
    assert result is not None


@pytest.mark.integration
@pytest.mark.xfail(reason="Human: Write op. POST sends document email — do NOT test without confirmation.")
def test_post_email_senddocument(api):
    """post_email_senddocument sends a document via email"""
    result = api.jobs.email.post_email_senddocument(JOB_DISPLAY_ID, data={})
    assert result is not None
