"""
Note API Examples - Simple notes retrieval

Usage:
    python note.py                  # Run all examples
    python note.py get              # Run a single example
    python note.py help             # List available examples
"""

from _base import ExampleRunner


JOB_ID = 4637814


class NoteExamples(ExampleRunner):
    def __init__(self):
        super().__init__("Note API", api_kwargs=dict(env='staging', username='instaquote'))
        self.add("get", "Get notes for a job", self.get_notes)

    def get_notes(self):
        notes_response = self.api.jobs.note.get_note(jobDisplayId=JOB_ID)
        print(notes_response)


if __name__ == "__main__":
    NoteExamples().run()
