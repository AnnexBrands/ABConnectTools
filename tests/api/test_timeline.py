"""Tests for Job Timeline endpoints."""

import pytest
from ABConnect.api import models
from tests.constants import JOB_DISPLAY_ID


@pytest.mark.integration
def test_get_timeline(api):
    """get_timeline returns timeline data for job"""
    result = api.jobs.timeline.get_timeline(JOB_DISPLAY_ID)
    assert isinstance(result, models.TimelineResponse)


@pytest.mark.integration
def test_get_timeline_list(api):
    """get_timeline_list returns timeline task list"""
    result = api.jobs.timeline.get_timeline_list(JOB_DISPLAY_ID)
    assert result is not None


@pytest.mark.integration
def test_get_timeline_agent(api):
    """get_timeline_agent returns agent info for timeline"""
    result = api.jobs.timeline.get_timeline_agent(JOB_DISPLAY_ID)
    assert result is not None


# ==============================================================================
# Write operations — xfail
# ==============================================================================

@pytest.mark.integration
@pytest.mark.xfail(reason="Human: Write op. POST creates a timeline task.")
def test_post_timeline(api):
    """post_timeline creates a timeline task"""
    result = api.jobs.timeline.post_timeline(JOB_DISPLAY_ID, data={})
    assert result is not None


@pytest.mark.integration
@pytest.mark.xfail(reason="Human: Write op. POST increments job status.")
def test_post_incrementjobstatus(api):
    """post_incrementjobstatus increments status"""
    result = api.jobs.timeline.post_timeline_incrementjobstatus(JOB_DISPLAY_ID, data={})
    assert result is not None


@pytest.mark.integration
@pytest.mark.xfail(reason="Human: Destructive. DELETE removes a timeline task.")
def test_delete_timeline(api):
    """delete_timeline deletes a timeline task"""
    result = api.jobs.timeline.delete_timeline(JOB_DISPLAY_ID)
    assert result is not None
