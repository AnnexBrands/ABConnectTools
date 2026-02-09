"""Tests for Job FreightProviders endpoints."""

import pytest
from tests.constants import JOB_DISPLAY_ID


@pytest.mark.integration
def test_get_freightproviders(api):
    """get_freightproviders returns freight providers for job"""
    result = api.jobs.freightproviders.get_freightproviders(JOB_DISPLAY_ID)
    assert result is not None


# ==============================================================================
# Write operations — xfail
# ==============================================================================

@pytest.mark.integration
@pytest.mark.xfail(reason="Human: Write op. POST updates freight providers.")
def test_post_freightproviders(api):
    """post_freightproviders saves freight providers"""
    result = api.jobs.freightproviders.post_freightproviders(JOB_DISPLAY_ID, data=[])
    assert result is not None
