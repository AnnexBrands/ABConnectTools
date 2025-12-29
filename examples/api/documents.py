"""Examples for Documents API endpoints and models.

This module demonstrates how to work with the Documents API using both
the convenient alias (client.docs) and the full endpoint path.
Includes examples of uploading files and working with Pydantic models.
"""

import requests
import io
import os
from pathlib import Path
from PIL import Image
from ABConnect import ABConnectAPI
from ABConnect import models


def upload_imgs(api):
    """Upload images using backward compatibility method."""
    
    filename = "ABConnect/tiny.jpg"
    with open(filename, "rb") as f:
        file_data = f.read()
    attachments = {
        "img1": (
            filename,
            file_data,
            "image/jpeg",
        )
    }

    data = models.DocumentUploadRequest(
        job_display_id=2000000,
        document_type=models.DocumentType.ITEM_PHOTO,
        shared=28,
        job_items=["8FA87330-AF59-EF11-8393-16D570081145"],
    )

    for key, value in attachments.items():
        try:
            response = api.docs.upload_item_photos(
                jobid=2000000,
                itemid="8FA87330-AF59-EF11-8393-16D570081145",
                files={key: value},
            )
            print(f"   Uploaded {key}: {response}")
        except Exception as e:
            print(f"   Upload demo for {key}: {e}")


api = ABConnectAPI(env='staging', username='instaquote')

# upload_imgs(api)

# r = api.docs.list(2000000)
# for doc in r:
#     print(doc)

# path='job/2000000/tiny.jpg'
# thumb = api.docs.thumbnail(path)
# print (thumb[:10])

