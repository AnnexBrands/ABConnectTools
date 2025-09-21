"""Examples for Documents API endpoints and models.

This module demonstrates how to work with the Documents API using both
the convenient alias (client.docs) and the full endpoint path.
Includes examples of uploading files and working with Pydantic models.
"""

import requests
import io
import tempfile
import os
from pathlib import Path
from PIL import Image
from ABConnect.api import ABConnectAPI
from ABConnect.api.models.documents import DocumentUpdateModel
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
                jobid=2000000,
                itemid=1,
                files={key: value},
            )
            print(f"   Uploaded {key}: {response}")
        except Exception as e:
            print(f"   Upload demo for {key}: {e}")


def main():
    """Main examples runner."""
    print("=== ABConnect Documents API Examples ===\n")

    # Initialize API client (uses docs alias)
    api = ABConnectAPI()

    print("1. API Endpoint Access:")
    print(f"   - Full path: api.documents")
    print(f"   - Alias: api.docs (same object: {api.docs is api.documents})")
    print()

    # Example 1: Backward compatibility with existing code
    backward_compatibility_example(api)

    # Example 2: Modern API usage
    modern_api_example(api)

    # Example 3: Working with Pydantic models
    pydantic_models_example()

    # Example 4: CLI and curl examples
    cli_and_curl_examples()


def backward_compatibility_example(api):
    """Example showing backward compatibility with existing code."""
    print("2. Backward Compatibility Example:")
    print("   Using existing fetch_imgs() and upload_imgs() functions...")

    # Fetch images (this would work with real URLs)
    images = fetch_imgs()
    print(f"   Fetched {len(images)} demo images")

    # Upload using legacy method signature
    if images:
        upload_imgs(api, images)
    print()


def modern_api_example(api):
    """Example of modern API usage with new convenience methods."""
    print("3. Modern API Usage:")

    # Create a temporary image for demonstration
    with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as tmp_file:
        tmp_file.write(b'\xff\xd8\xff\xe0\x00\x10JFIF')  # Minimal JPEG header
        tmp_file_path = tmp_file.name

    try:
        # Modern upload_item_photo method
        print("   Using upload_item_photo() with Pydantic model:")
        response = api.docs.upload_item_photo(
            file_path=tmp_file_path,
            item_id="item-uuid-456",
            job_display_id="JOB-67890",
            shared=True
        )
        print(f"   Response: {response}")

    except Exception as e:
        print(f"   Demo upload: {e}")

    try:
        # List documents (using alias)
        print("   Listing documents for job:")
        docs = api.docs.get_list(job_display_id="JOB-67890")
        print(f"   Found: {docs}")

    except Exception as e:
        print(f"   Demo list: {e}")

    finally:
        os.unlink(tmp_file_path)

    print()


def pydantic_models_example():
    """Example of working with Pydantic models."""
    print("4. Working with Pydantic Models:")

    # ItemPhotoUploadRequest example
    upload_model = ItemPhotoUploadRequest(
        job_display_id=2000000,
        document_type=6,  # 6 for Item_Photo
        document_type_description="Item Photo",
        shared=28,  # Default shared value
        job_items=["550e8400-e29b-41d4-a716-446655440001"]  # UUID item IDs (using test standard)
    )

    print(f"   Upload Model: {upload_model}")
    print(f"   Serialized: {upload_model.model_dump(by_alias=True)}")
    print()

    # DocumentUpdateModel example
    update_model = DocumentUpdateModel(
        file_name="updated_drawing.pdf",
        type_id=3,
        shared=0,
        tags=["updated", "final"]
    )

    print(f"   Update Model: {update_model}")
    print()


def cli_and_curl_examples():
    """CLI and curl usage examples."""
    print("5. CLI Usage Examples:")
    print("   # List documents for a job")
    print("   ab documents get_list --job_display_id JOB-12345")
    print()
    print("   # Get a document")
    print("   ab documents get_get documents/path/to/file.pdf")
    print()

    print("6. curl Examples:")
    print("   # List documents")
    print("   curl -H \"Authorization: Bearer $TOKEN\" \\")
    print("        \"$API_BASE/api/documents/list?jobDisplayId=JOB-12345\"")
    print()
    print("   # Upload document")
    print("   curl -X POST \\")
    print("        -H \"Authorization: Bearer $TOKEN\" \\")
    print("        -F \"file=@photo.jpg\" \\")
    print("        -F \"JobDisplayId=JOB-12345\" \\")
    print("        -F \"DocumentType=1\" \\")
    print("        -F \"DocumentTypeDescription=Item Photo\" \\")
    print("        -F \"Shared=1\" \\")
    print("        -F \"JobItems=item-uuid-123\" \\")
    print("        \"$API_BASE/api/documents\"")
    print()


if __name__ == "__main__":
    main()