"""
Notes API Examples - Comprehensive note operations

This module demonstrates how to work with job notes using the Notes API
and appropriate Pydantic models for type-safe operations.

Key learnings:
- Create notes: Use TaskNoteModel and api.jobs.note.post_note()
- Retrieve notes: Use api.jobs.note.get_note() -> List[JobTaskNote]
- Filter by task: Use category or task_code parameters

Usage:
    python notes.py                 # Run all examples
    python notes.py get             # Run a single example
    python notes.py help            # List available examples
"""

from typing import List
from ABConnect.models import TaskNoteModel, JobTaskNote, TaskCodes
from _base import ExampleRunner


JOB_DISPLAY_ID = 4648545


class NotesExamples(ExampleRunner):
    def __init__(self):
        super().__init__("Notes API", api_kwargs=dict(env='staging', username='instaquote'))
        self.add("get", "Get notes for a job", self.get_notes)
        self.add("create", "Create a packaging note", self.create_packaging_note)
        self.add("filter", "Get notes filtered by task code", self.get_filtered)
        self.add("taskcodes", "Show available task codes", self.task_codes)
        self.add("cli", "CLI and curl usage examples", self.cli_and_curl_examples)

    def get_notes(self):
        response = self.api.jobs.note.get_note(jobDisplayId=str(JOB_DISPLAY_ID))
        if isinstance(response, list):
            notes: List[JobTaskNote] = [JobTaskNote(**note) for note in response]
            print(f"Found {len(notes)} note(s)\n")
            for idx, note in enumerate(notes, 1):
                print(f"Note #{idx}:")
                print(f"  ID: {note.id}")
                print(f"  Comment: {note.comment}")
                print(f"  Author: {note.author}")
                print(f"  Created: {note.created_date}")
                print(f"  Important: {note.is_important}")
                if idx == 1:
                    print(f"\n  Serialized: {note.model_dump(by_alias=True, exclude_none=True)}")
                print()
        else:
            print(f"Unexpected response format: {type(response)}")

    def create_packaging_note(self):
        note = TaskNoteModel(
            comments="test notes",
            task_code=TaskCodes.PACKAGING,
            is_important=False,
            is_completed=False,
            send_notification=False
        )
        print(f"Note details:")
        print(f"  Task Code: {note.task_code} (Packaging)")
        print(f"  Comments: {note.comments}")

        note_data = note.model_dump(by_alias=True, exclude_none=True)
        print(f"Sending to API: {note_data}\n")

        response = self.api.jobs.note.post_note(
            jobDisplayId=str(JOB_DISPLAY_ID),
            data=note_data
        )
        print(f"Response: {response}")

    def get_filtered(self):
        response = self.api.jobs.note.get_note(
            jobDisplayId=str(JOB_DISPLAY_ID),
            task_code=TaskCodes.PACKAGING
        )
        if isinstance(response, list):
            notes = [JobTaskNote(**note) for note in response]
            print(f"Found {len(notes)} packaging note(s)")
            for idx, note in enumerate(notes, 1):
                print(f"  #{idx}: {note.comment} (by {note.author})")

    def task_codes(self):
        print("Task codes align with job timeline tasks:")
        print(f"  {TaskCodes.PICKUP} - Pickup task notes")
        print(f"  {TaskCodes.PACKAGING} - Packaging task notes")
        print(f"  {TaskCodes.STORAGE} - Storage task notes")
        print(f"  {TaskCodes.CARRIER} - Carrier task notes")
        print(f"  {TaskCodes.DELIVERY} - Delivery task notes")

    def cli_and_curl_examples(self):
        print("CLI Usage:\n")
        print(f"  ab jobs note get_note --jobDisplayId {JOB_DISPLAY_ID}")
        print(f"  ab jobs note get_note --jobDisplayId {JOB_DISPLAY_ID} --task_code PK")

        print("\ncurl Usage:\n")
        print(f'  curl -H "Authorization: Bearer $TOKEN" "$API_BASE/api/job/{JOB_DISPLAY_ID}/note"')
        print(f'  curl -H "Authorization: Bearer $TOKEN" "$API_BASE/api/job/{JOB_DISPLAY_ID}/note?taskCode=PK"')

        print("\nPython API:\n")
        print(f"  response = api.jobs.note.get_note(jobDisplayId='{JOB_DISPLAY_ID}')")
        print("  notes = [JobTaskNote(**note) for note in response]")


if __name__ == "__main__":
    NotesExamples().run()
