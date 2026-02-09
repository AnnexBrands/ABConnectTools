"""Tests for Documents API endpoints."""

import pytest
from tests.constants import JOB_DISPLAY_ID


@pytest.mark.integration
def test_list_documents(api):
    """list returns documents for a job"""
    result = api.docs.list(job_display_id=JOB_DISPLAY_ID)
    assert isinstance(result, list)


# ==============================================================================
# Routes needing document path/ID (get from list)
# ==============================================================================

@pytest.mark.integration
@pytest.mark.xfail(reason="Human: Needs a valid docPath from list() response.")
def test_get_document(api):
    """get returns a specific document"""
    result = api.docs.get("NEED_VALID_DOC_PATH")
    assert result is not None


@pytest.mark.integration
@pytest.mark.xfail(reason="Human: Needs a valid docPath from list() response.")
def test_get_thumbnail(api):
    """thumbnail returns document thumbnail"""
    result = api.docs.thumbnail("NEED_VALID_DOC_PATH")
    assert result is not None


# ==============================================================================
# Write operations — xfail
# ==============================================================================

@pytest.mark.integration
@pytest.mark.xfail(reason="Human: Write op. POST uploads a document.")
def test_post_document(api):
    """post uploads a document"""
    result = api.docs.post(data={})
    assert result is not None


@pytest.mark.integration
@pytest.mark.xfail(reason="Human: Destructive. PUT hides a document.")
def test_hide_document(api):
    """put_hide hides a document"""
    result = api.docs.put_hide("NEED_VALID_DOC_ID")
    assert result is not None
