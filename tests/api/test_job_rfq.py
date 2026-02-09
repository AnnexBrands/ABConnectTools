"""Tests for Job RFQ endpoints."""

import pytest
from tests.constants import JOB_DISPLAY_ID


@pytest.mark.integration
def test_get_rfq(api):
    """get_rfq returns RFQ data for job"""
    result = api.jobs.rfq.get_rfq(JOB_DISPLAY_ID)
    assert result is not None


@pytest.mark.integration
@pytest.mark.xfail(reason=(
    "Human: Needs valid companyId and rfqServiceType. "
    "Use COMPANY_ID from constants with a service type string."
))
def test_get_rfq_statusof_forcompany(api):
    """get_rfq_statusof_forcompany returns RFQ status for company"""
    from tests.constants import COMPANY_ID
    result = api.jobs.rfq.get_rfq_statusof_forcompany(COMPANY_ID, "NEED_SERVICE_TYPE", JOB_DISPLAY_ID)
    assert result is not None
