"""
Documents API Examples - Upload, list, and thumbnail operations

This module demonstrates how to work with the Documents API using both
the convenient alias (client.docs) and the full endpoint path.

Usage:
    python documents.py             # Run all examples
    python documents.py upload      # Run a single example
    python documents.py help        # List available examples
"""

from ABConnect import models
from _base import ExampleRunner


class DocumentExamples(ExampleRunner):
    def __init__(self):
        super().__init__("Documents API", api_kwargs=dict(env='staging', username='instaquote'))
        self.add("upload", "Upload images to a job item", self.upload_imgs)
        self.add("list", "List documents for a job", self.list_docs)
        self.add("thumbnail", "Get a document thumbnail", self.get_thumbnail)

    def upload_imgs(self):
        filename = "ABConnect/tiny.jpg"
        with open(filename, "rb") as f:
            file_data = f.read()
        attachments = {
            "img1": (filename, file_data, "image/jpeg")
        }

        for key, value in attachments.items():
            response = self.api.docs.upload_item_photos(
                jobid=2000000,
                itemid="8FA87330-AF59-EF11-8393-16D570081145",
                files={key: value},
            )
            print(f"  Uploaded {key}: {response}")

    def list_docs(self):
        r = self.api.docs.list(2000000)
        for doc in r:
            print(doc)

    def get_thumbnail(self):
        path = 'job/2000000/tiny.jpg'
        thumb = self.api.docs.thumbnail(path)
        print(thumb[:10])


if __name__ == "__main__":
    DocumentExamples().run()
