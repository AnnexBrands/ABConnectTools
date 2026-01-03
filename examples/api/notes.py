"""Examples for Notes API endpoints and models.

This module demonstrates how to work with job notes using the Notes API
and appropriate Pydantic models for type-safe operations.

Key learnings:
- Create notes: Use TaskNoteModel and api.jobs.note.post_note()
- Retrieve notes: Use api.jobs.note.get_note() → List[JobTaskNote]
- Filter by task: Use category or task_code parameters
"""

from typing import List
from datetime import datetime
from ABConnect import ABConnectAPI
from ABConnect.models import TaskNoteModel, JobTaskNote, TaskCodes


# Example job ID
JOB_DISPLAY_ID = 4648545


def create_packaging_note(job_display_id: int = JOB_DISPLAY_ID,
                          comment: str = "test notes",
                          send_notification: bool = False):
    """Create a new packaging (PK) note for a job.

    Args:
        job_display_id: The job display ID to add the note to
        comment: The note comment/text
        send_notification: Whether to send notification to users

    Returns:
        API response with created note details
    """
    print(f"=== Creating Packaging Note for Job {job_display_id} ===\n")

    # Initialize API
    api = ABConnectAPI(env='staging', username='instaquote')

    # Create the note model
    note = TaskNoteModel(
        comments=comment,
        task_code=TaskCodes.PACKAGING,  # PK = Packaging task
        is_important=False,
        is_completed=False,
        send_notification=send_notification
    )

    print(f"Note details:")
    print(f"  Task Code: {note.task_code} (Packaging)")
    print(f"  Comments: {note.comments}")
    print(f"  Important: {note.is_important}")
    print(f"  Completed: {note.is_completed}")
    print(f"  Send Notification: {note.send_notification}")
    print()

    try:
        # Post the note
        # Convert Pydantic model to dict with API field names
        note_data = note.model_dump(by_alias=True, exclude_none=True)

        print(f"Sending to API: {note_data}")
        print()

        response = api.jobs.note.post_note(
            jobDisplayId=str(job_display_id),
            data=note_data
        )

        print(f"✅ Note created successfully!")
        print(f"Response: {response}")
        print()

        return response

    except Exception as e:
        print(f"❌ Error creating note: {e}")
        print("\nThis is a demo - requires valid job ID and permissions")
        import traceback
        traceback.print_exc()
        return None


def get_job_notes(job_display_id: int = JOB_DISPLAY_ID,
                  task_code: str = None,
                  category: str = None):
    """Retrieve notes for a job with optional filtering.

    Args:
        job_display_id: The job display ID to get notes for
        task_code: Optional task code filter (PU, PK, ST, CP, DE)
        category: Optional category filter

    Returns:
        List of JobTaskNote Pydantic models
    """
    filter_desc = []
    if task_code:
        filter_desc.append(f"task_code={task_code}")
    if category:
        filter_desc.append(f"category={category}")

    filter_str = " with filters: " + ", ".join(filter_desc) if filter_desc else ""
    print(f"=== Getting Notes for Job {job_display_id}{filter_str} ===\n")

    # Initialize API
    api = ABConnectAPI()

    try:
        # Get notes from the API
        response = api.jobs.note.get_note(
            jobDisplayId=str(job_display_id),
            task_code=task_code,
            category=category
        )

        # Cast response to list of JobTaskNote models
        if isinstance(response, list):
            notes: List[JobTaskNote] = [
                JobTaskNote(**note) for note in response
            ]

            print(f"Found {len(notes)} note(s)\n")

            if notes:
                for idx, note in enumerate(notes, 1):
                    print(f"Note #{idx}:")
                    print(f"  ID: {note.id}")
                    print(f"  Comment: {note.comment}")
                    print(f"  Author: {note.author}")
                    print(f"  Created: {note.created_date}")
                    print(f"  Important: {note.is_important}")
                    print(f"  Completed: {note.is_completed}")

                    # Show model serialization for first note
                    if idx == 1:
                        print(f"\n  Serialized (API format):")
                        print(f"  {note.model_dump(by_alias=True, exclude_none=True)}")
                    print()
            else:
                print("No notes found for this job")

            return notes

        else:
            print(f"Unexpected response format: {type(response)}")
            print(f"Response: {response}")
            return []

    except Exception as e:
        print(f"Error fetching notes: {e}")
        print("\nThis is a demo - requires valid job ID")
        import traceback
        traceback.print_exc()
        return []


def demonstrate_task_codes():
    """Demonstrate different task codes for notes."""
    print("=== Available Task Codes for Notes ===\n")

    print("Task codes align with job timeline tasks:")
    print(f"  {TaskCodes.PICKUP} - Pickup task notes")
    print(f"  {TaskCodes.PACKAGING} - Packaging task notes")
    print(f"  {TaskCodes.STORAGE} - Storage task notes")
    print(f"  {TaskCodes.CARRIER} - Carrier task notes")
    print(f"  {TaskCodes.DELIVERY} - Delivery task notes")
    print()

    print("Example: Create notes for different tasks")
    print()

    # Examples for different task codes
    examples = [
        (TaskCodes.PICKUP, "Customer requested early pickup"),
        (TaskCodes.PACKAGING, "Extra padding required for fragile items"),
        (TaskCodes.STORAGE, "Store in climate-controlled area"),
        (TaskCodes.CARRIER, "Carrier pickup scheduled for 2pm"),
        (TaskCodes.DELIVERY, "Contact customer 1 hour before delivery"),
    ]

    for task_code, comment in examples:
        print(f"# {task_code} Note:")
        print(f"note = TaskNoteModel(")
        print(f"    comments='{comment}',")
        print(f"    task_code=TaskCodes.{task_code.name}")
        print(f")")
        print()


def main():
    """Main examples runner."""
    print("=== ABConnect Notes API Examples ===\n")

    print("This module demonstrates working with job notes:\n")
    print("1. Creating Notes - Use TaskNoteModel to create task-specific notes")
    print("   Model: TaskNoteModel from jobnote.py")
    print("   Endpoint: api.jobs.note.post_note()")
    print()
    print("2. Retrieving Notes - Get and filter notes for a job")
    print("   Model: JobTaskNote from jobnote.py")
    print("   Endpoint: api.jobs.note.get_note()")
    print()

    # Example 1: Get existing notes (if any)
    print("Step 1: Check existing notes for the job")
    print("-" * 60)
    existing_notes = get_job_notes(job_display_id=JOB_DISPLAY_ID)

    # Example 2: Create a new packaging note
    print("\nStep 2: Create a new packaging (PK) note")
    print("-" * 60)
    created_note = create_packaging_note(
        job_display_id=JOB_DISPLAY_ID,
        comment="test notes"
    )

    # Example 3: Get notes filtered by task code
    if created_note:
        print("\nStep 3: Retrieve notes filtered by packaging task")
        print("-" * 60)
        pk_notes = get_job_notes(
            job_display_id=JOB_DISPLAY_ID,
            task_code=TaskCodes.PACKAGING
        )

    # Example 4: Show task codes
    print("\n" + "=" * 60)
    demonstrate_task_codes()

    # Show CLI and curl examples
    cli_and_curl_examples()


def cli_and_curl_examples():
    """CLI and curl usage examples."""
    print("=" * 60)
    print("CLI Usage Examples")
    print("=" * 60)
    print()

    print("# Get all notes for a job")
    print(f"ab jobs note get_note --jobDisplayId {JOB_DISPLAY_ID}")
    print()

    print("# Get notes filtered by task code")
    print(f"ab jobs note get_note --jobDisplayId {JOB_DISPLAY_ID} --task_code PK")
    print()

    print("# Create a note (requires JSON data)")
    print(f"ab jobs note post_note --jobDisplayId {JOB_DISPLAY_ID} --data '{{")
    print('  "comments": "test notes",')
    print('  "taskCode": "PK",')
    print('  "isImportant": false,')
    print('  "sendNotification": false')
    print("}}'")
    print()

    print("=" * 60)
    print("curl Examples")
    print("=" * 60)
    print()

    print("# Get notes for a job")
    print("curl -H \"Authorization: Bearer $TOKEN\" \\")
    print(f"     \"$API_BASE/api/job/{JOB_DISPLAY_ID}/note\"")
    print()

    print("# Get notes filtered by task code")
    print("curl -H \"Authorization: Bearer $TOKEN\" \\")
    print(f"     \"$API_BASE/api/job/{JOB_DISPLAY_ID}/note?taskCode=PK\"")
    print()

    print("# Create a note")
    print("curl -X POST \\")
    print("     -H \"Authorization: Bearer $TOKEN\" \\")
    print("     -H \"Content-Type: application/json\" \\")
    print(f"     -d '{{")
    print('       "comments": "test notes",')
    print('       "taskCode": "PK",')
    print('       "isImportant": false,')
    print('       "sendNotification": false')
    print(f"     }}' \\")
    print(f"     \"$API_BASE/api/job/{JOB_DISPLAY_ID}/note\"")
    print()

    print("=" * 60)
    print("Python API Examples")
    print("=" * 60)
    print()

    print("from ABConnect.api import ABConnectAPI")
    print("from ABConnect.api.models.jobnote import TaskNoteModel, JobTaskNote")
    print("from ABConnect.common import TaskCodes")
    print()
    print("api = ABConnectAPI()")
    print()

    print("# Create a packaging note")
    print("note = TaskNoteModel(")
    print("    comments='test notes',")
    print("    task_code=TaskCodes.PACKAGING,")
    print("    is_important=False,")
    print("    send_notification=False")
    print(")")
    print()
    print("response = api.jobs.note.post_note(")
    print(f"    jobDisplayId='{JOB_DISPLAY_ID}',")
    print("    data=note.model_dump(by_alias=True, exclude_none=True)")
    print(")")
    print()

    print("# Get notes and cast to Pydantic models")
    print(f"response = api.jobs.note.get_note(jobDisplayId='{JOB_DISPLAY_ID}')")
    print("notes = [JobTaskNote(**note) for note in response]")
    print("for note in notes:")
    print("    print(f'{note.author}: {note.comment}')")
    print()

    print("# Filter notes by task code")
    print(f"response = api.jobs.note.get_note(")
    print(f"    jobDisplayId='{JOB_DISPLAY_ID}',")
    print("    task_code=TaskCodes.PACKAGING")
    print(")")
    print()


if __name__ == "__main__":
    main()
