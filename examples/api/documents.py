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
from ABConnect.api import ABConnectAPI
from ABConnect.api.models.document_upload import ItemPhotoUploadRequest, ItemPhotoUploadResponse


def fetch_imgs():
    attachments = {}
    url = "https://s3.amazonaws.com/static2.liveauctioneers.com/176/387998/214867371_%d_m.jpg"
    for i in range(1, 3):
        with requests.Session() as session:
            response = session.get(url % i)
            response.raise_for_status()
            file_data = response.content

            with Image.open(io.BytesIO(file_data)) as img:
                img.load()
                output = io.BytesIO()
                img.save(output, format='JPEG', quality=1, optimize=True)

                form_field_name = f"img{i}"
                filename = f"{214867371}_{i}.jpg"
                content_type = response.headers.get("Content-Type")
                attachments[form_field_name] = (
                    filename,
                    file_data,
                    content_type,
                )
    return attachments


def upload_imgs(api, attachments):
    """Upload images using backward compatibility method."""
    for key, value in attachments.items():
        try:
            response = api.docs.upload_item_photos(
                jobid=2_000_000,
                itemid='8FA87330-AF59-EF11-8393-16D570081145',
                files={key: value},
            )
            print(f"   Uploaded {key}: {response}")
        except Exception as e:
            print(f"   Upload demo for {key}: {e}")


api = ABConnectAPI()
atts = fetch_imgs()
upload_imgs(api, atts)