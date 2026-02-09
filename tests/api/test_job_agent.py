"""Tests for Job Agent/Status endpoints."""

import pytest
import json
from pathlib import Path
from ABConnect.api import models

fixtures = Path(__file__).parent.parent / "fixtures"


# ==============================================================================
# Agent fixture validation
# ==============================================================================

@pytest.fixture
def ChangeAgentOAData():
    fixture_path = fixtures / "ChangeAgent_OA.json"
    if not fixture_path.exists():
        pytest.skip("ChangeAgent_OA fixture not found — run examples/api/agent.py first")
    return json.loads(fixture_path.read_text())


def test_change_agent_oa_fixture(ChangeAgentOAData):
    """ChangeAgent_OA fixture validates against ServiceBaseResponse"""
    models.ServiceBaseResponse.model_validate(ChangeAgentOAData)


# ==============================================================================
# Write operations — xfail
# ==============================================================================

@pytest.mark.integration
@pytest.mark.xfail(reason="Human: Write op. POST /job/{id}/status/quote changes job status.")
def test_post_status_quote(api):
    """post_status_quote changes job status to quote"""
    from tests.constants import JOB_DISPLAY_ID
    result = api.jobs.status.post_status_quote(JOB_DISPLAY_ID, data={})
    assert result is not None
