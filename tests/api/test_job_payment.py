"""Tests for Job Payment endpoints."""

import pytest
from tests.constants import JOB_DISPLAY_ID


@pytest.mark.integration
def test_get_payment(api):
    """get_payment returns payment data for job"""
    result = api.jobs.payment.get_payment(JOB_DISPLAY_ID)
    assert result is not None


@pytest.mark.integration
def test_get_payment_create(api):
    """get_payment_create returns payment creation data"""
    result = api.jobs.payment.get_payment_create(JOB_DISPLAY_ID)
    assert result is not None


@pytest.mark.integration
def test_get_payment_sources(api):
    """get_payment_sources returns payment sources"""
    result = api.jobs.payment.get_payment_sources(JOB_DISPLAY_ID)
    assert result is not None


# ==============================================================================
# Write operations — xfail
# ==============================================================================

@pytest.mark.integration
@pytest.mark.xfail(reason="Human: Financial write op. POST creates ACH payment session.")
def test_post_payment_ach(api):
    """post_payment_ACHPaymentSession creates ACH session"""
    result = api.jobs.payment.post_payment_ACHPaymentSession(JOB_DISPLAY_ID, data={})
    assert result is not None


@pytest.mark.integration
@pytest.mark.xfail(reason="Human: Financial write op. POST processes payment by source.")
def test_post_payment_bysource(api):
    """post_payment_bysource pays by source"""
    result = api.jobs.payment.post_payment_bysource(JOB_DISPLAY_ID, data={})
    assert result is not None
