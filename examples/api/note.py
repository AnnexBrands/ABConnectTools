from ABConnect import ABConnectAPI

api = ABConnectAPI(env='staging', username='instaquote')
from ABConnect import models

JOB_ID = 4637814

def print_note_details():
    """Print details of notes for a specific entity."""
    api = ABConnectAPI(env='staging', username='instaquote')

    # Fetch notes for the given JOB_ID
    notes_response = api.jobs.note.get_note(jobDisplayId=JOB_ID)
    print(notes_response)
    # notes_data = notes_response['notes'] if 'notes' in notes_response else notes_response

    # # Cast notes to Note model instances
    # from ABConnect.api.models.note import Note
    # notes = [Note(**note) for note in notes_data]

    # # Print note details
    # for note in notes:
    #     print(f"Note ID: {note.note_id}")
    #     print(f"Created By: {note.created_by}")
    #     print(f"Created At: {note.created_at}")
    #     print(f"Content: {note.content}")
    #     print("-" * 40)

print_note_details()