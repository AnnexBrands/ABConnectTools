"""Tests for Job Core endpoints."""

import pytest
from tests.constants import JOB_DISPLAY_ID


# ==============================================================================
# GET routes using JOB_DISPLAY_ID
# ==============================================================================

@pytest.mark.integration
def test_get_job(api):
    """get returns job data"""
    result = api.jobs.get(JOB_DISPLAY_ID)
    assert result is not None


@pytest.mark.integration
def test_get_search(api):
    """get_search returns search results"""
    result = api.jobs.get_search()
    assert result is not None


@pytest.mark.integration
def test_get_document_config(api):
    """get_documentConfig returns document configuration"""
    result = api.jobs.get_documentConfig()
    assert result is not None


@pytest.mark.integration
def test_get_job_access_level(api):
    """get_jobAccessLevel returns access level"""
    result = api.jobs.get_jobAccessLevel(job_display_id=JOB_DISPLAY_ID)
    assert result is not None


@pytest.mark.integration
def test_get_calendar_items(api):
    """get_calendaritems returns calendar items"""
    result = api.jobs.get_calendaritems(JOB_DISPLAY_ID)
    assert result is not None


@pytest.mark.integration
def test_get_feedback(api):
    """get_feedback returns feedback data"""
    result = api.jobs.get_feedback(JOB_DISPLAY_ID)
    assert result is not None


@pytest.mark.integration
def test_get_update_page_config(api):
    """get_updatePageConfig returns update page config"""
    result = api.jobs.get_updatePageConfig(JOB_DISPLAY_ID)
    assert result is not None


@pytest.mark.integration
def test_get_price(api):
    """get_price returns price data"""
    result = api.jobs.get_price(JOB_DISPLAY_ID)
    assert result is not None


# ==============================================================================
# Write operations — xfail
# ==============================================================================

@pytest.mark.integration
@pytest.mark.xfail(reason="Human: Write op. POST /job creates a new job.")
def test_post_job(api):
    """post creates a new job"""
    result = api.jobs.post(data={})
    assert result is not None


@pytest.mark.integration
@pytest.mark.xfail(reason="Human: Write op. POST /job/{id}/book books a job.")
def test_post_book(api):
    """post_book books a job"""
    result = api.jobs.post_book(JOB_DISPLAY_ID, data={})
    assert result is not None


@pytest.mark.integration
@pytest.mark.xfail(reason="Human: Write op. PUT /job/save updates job data.")
def test_put_save(api):
    """put_save saves job data"""
    result = api.jobs.put_save(data={})
    assert result is not None


@pytest.mark.integration
@pytest.mark.xfail(reason="Human: Write op. POST /job/transfer transfers a job.")
def test_post_transfer(api):
    """post_transfer transfers a job"""
    result = api.jobs.post_transfer(JOB_DISPLAY_ID, data={})
    assert result is not None
