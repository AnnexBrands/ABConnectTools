"""Tests for Job Notes endpoints."""

import pytest
from tests.constants import JOB_DISPLAY_ID


@pytest.mark.integration
def test_get_note(api):
    """get_note returns notes for job"""
    result = api.jobs.note.get_note(JOB_DISPLAY_ID)
    assert result is not None


@pytest.mark.integration
def test_get_note_list(api):
    """get_note_list returns note list for job"""
    result = api.jobs.note.get_note_list(JOB_DISPLAY_ID)
    assert result is not None


# ==============================================================================
# Write operations — xfail
# ==============================================================================

@pytest.mark.integration
@pytest.mark.xfail(reason="Human: Write op. POST creates a note, needs TaskNoteModel data.")
def test_post_note(api):
    """post_note creates a note"""
    result = api.jobs.note.post_note(JOB_DISPLAY_ID, data={})
    assert result is not None
