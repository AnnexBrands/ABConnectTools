"""Documents endpoint for managing job-related documents.

This module provides methods for uploading, downloading, and listing documents
associated with jobs in the ABC API. It supports various document types including
labels, photos, and general attachments.
"""

from typing import List, Dict, Any, Optional, Tuple, BinaryIO
from ABConnect.api.endpoints.base import BaseEndpoint
from ABConnect.common import DocType, to_file_dict


class DocsEndpoint(BaseEndpoint):
    """Endpoint for document-related API operations.
    
    This endpoint provides comprehensive document management capabilities
    including uploading, downloading, and listing documents associated
    with jobs. It supports various document types such as labels, photos,
    and general attachments.
    
    Available Methods:
        - parcel_label: Download parcel shipping label
        - get: List all documents for a job
        - download: Download a specific document
        - upload: Upload documents to a job
        - upload_item_photos: Upload photos for specific items
    """
    def parcel_label(self, pro: str) -> Dict[str, Any]:
        """Download a parcel shipping label PDF.
        
        Retrieves the shipping label for a parcel shipment identified by its PRO
        (Progressive Rotating Order) number. The label is returned as a PDF file.

        Args:
            pro (str): The PRO number of the shipment (e.g., 'PRO123456').
                This is the unique tracking number assigned to the parcel.

        Returns:
            dict: A dictionary containing the PDF file data with structure::

                {
                    'filename': 'PRO123456_Label.pdf',
                    'content': b'<pdf binary data>',
                    'content_type': 'application/pdf',
                    'size': 12345
                }

        Raises:
            ABConnectError: If the PRO number is not found or if there's an API error.
            
        Example:
            >>> endpoint = DocsEndpoint()
            >>> label = endpoint.parcel_label('PRO123456')
            >>> # Save the label to disk
            >>> with open(label['filename'], 'wb') as f:
            ...     f.write(label['content'])
        """
        docpath = f"shipment/{pro}/{pro}_Label.pdf"
        uri = "documents/get/%s" % docpath
        response = self._r.call("GET", uri, raw=True)
        return to_file_dict(
            response,
            pro,
            "Label",
        )

    def get(self, jobid: str) -> List[Dict[str, Any]]:
        """List all documents associated with a job.
        
        Retrieves a list of all documents that have been uploaded or generated
        for a specific job. This includes various document types such as invoices,
        BOLs, photos, and other attachments.

        Args:
            jobid (str): The job display ID (e.g., 'JOB-2024-001').
                This is the human-readable job identifier.

        Returns:
            list: A list of dictionaries, each containing document information::

                [
                    {
                        'id': 123,
                        'documentType': 'Invoice',
                        'documentTypeId': 1,
                        'fileName': 'invoice_12345.pdf',
                        'filePath': 'jobs/JOB-2024-001/invoice_12345.pdf',
                        'fileSize': 245632,
                        'mimeType': 'application/pdf',
                        'uploadedBy': 'john.doe@example.com',
                        'uploadedDate': '2024-01-15T10:30:00Z',
                        'description': 'Customer Invoice',
                        'shared': True,
                        'itemIds': [],
                        'tags': ['billing', 'customer']
                    },
                    ...
                ]

        Raises:
            ABConnectError: If the job ID is not found or if there's an API error.
            
        Example:
            >>> endpoint = DocsEndpoint()
            >>> documents = endpoint.get('JOB-2024-001')
            >>> for doc in documents:
            ...     print(f"{doc['documentType']}: {doc['fileName']}")
            >>> # Filter for specific document types
            >>> invoices = [d for d in documents if d['documentType'] == 'Invoice']
        """
        url_params = {"jobDisplayId": jobid}
        return self._r.call("GET", "documents/list", params=url_params)

    def download(self, docpath: str) -> bytes:
        """Download a specific document by its path.
        
        Retrieves the binary content of a document using its storage path.
        This is typically used after getting the document path from the
        get() method.

        Args:
            docpath (str): The document's storage path (e.g., 'jobs/JOB-2024-001/invoice.pdf').
                This path is typically obtained from the 'filePath' field in the
                document list.

        Returns:
            bytes: The raw binary content of the document. The format depends
                on the document type (PDF, image, etc.).
                
        Raises:
            ABConnectError: If the document path is not found or if there's an API error.
            
        Example:
            >>> endpoint = DocsEndpoint()
            >>> # First, get the document list
            >>> docs = endpoint.get('JOB-2024-001')
            >>> # Download the first document
            >>> if docs:
            ...     content = endpoint.download(docs[0]['filePath'])
            ...     # Save to disk
            ...     with open(docs[0]['fileName'], 'wb') as f:
            ...         f.write(content)
            
        See Also:
            - get: List documents to obtain file paths
        """
        return self._r.call("GET", f"documents/get/{docpath}")

    def upload(self, jobid: str, files: List[Tuple[str, BinaryIO]], data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Upload one or more documents to a job.
        
        Uploads documents to be associated with a specific job. Supports
        uploading multiple files in a single request.

        Args:
            jobid (str): The job display ID (e.g., 'JOB-2024-001').
            files (list): A list of tuples containing file information.
                Each tuple should be ('field_name', file_object) where:
                
                - field_name: Usually 'file' or 'files[]'
                - file_object: An open file object in binary mode
                
            data (dict, optional): Additional metadata for the upload::
            
                {
                    'documentType': 'Invoice',
                    'description': 'Q1 2024 Invoice',
                    'shared': True,
                    'tags': ['billing', 'q1-2024']
                }

        Returns:
            dict: Upload response containing information about uploaded files::

                {
                    'success': True,
                    'uploadedFiles': [
                        {
                            'id': 456,
                            'fileName': 'invoice.pdf',
                            'fileSize': 123456,
                            'documentType': 'Invoice'
                        }
                    ],
                    'message': 'Files uploaded successfully'
                }

        Raises:
            ABConnectError: If the upload fails or if there's an API error.
            
        Example:
            >>> endpoint = DocsEndpoint()
            >>> # Upload a single file
            >>> with open('invoice.pdf', 'rb') as f:
            ...     result = endpoint.upload(
            ...         'JOB-2024-001',
            ...         [('file', f)],
            ...         {'documentType': 'Invoice', 'description': 'January Invoice'}
            ...     )
            >>> 
            >>> # Upload multiple files
            >>> files = []
            >>> for filename in ['doc1.pdf', 'doc2.pdf']:
            ...     f = open(filename, 'rb')
            ...     files.append(('files[]', f))
            >>> try:
            ...     result = endpoint.upload('JOB-2024-001', files)
            ... finally:
            ...     for _, f in files:
            ...         f.close()
        """
        url = f"documents/upload/{jobid}"
        return self._r.upload_file(url, files)

    def upload_item_photos(self, jobid: str, itemid: int, files: List[Tuple[str, BinaryIO]], rfqid: Optional[int] = None) -> Dict[str, Any]:
        """Upload photos for a specific item in a job.
        
        Uploads one or more photos associated with a particular item within a job.
        This is commonly used for documenting item condition, damage, or for
        inventory purposes.

        Args:
            jobid (str): The job display ID (e.g., 'JOB-2024-001').
            itemid (int): The ID of the item within the job.
            files (list): A list of tuples containing photo files.
                Each tuple should be ('field_name', file_object) where:
                - field_name: Usually 'file' or 'files[]'
                - file_object: An open image file in binary mode
            rfqid (int, optional): The RFQ (Request for Quote) ID if applicable.
                Used when photos are part of a quote request process.

        Returns:
            dict: Upload response containing information about uploaded photos::

                {
                    'success': True,
                    'uploadedFiles': [
                        {
                            'id': 789,
                            'fileName': 'item_photo_1.jpg',
                            'fileSize': 2048576,
                            'documentType': 'Item Photo',
                            'itemId': 123,
                            'thumbnailUrl': '/api/documents/thumbnail/789'
                        }
                    ],
                    'message': 'Photos uploaded successfully'
                }

        Raises:
            ABConnectError: If the upload fails or if there's an API error.
            
        Example:
            >>> endpoint = DocsEndpoint()
            >>> # Upload photos for an item
            >>> photo_files = []
            >>> for photo_path in ['front.jpg', 'back.jpg', 'damage.jpg']:
            ...     f = open(photo_path, 'rb')
            ...     photo_files.append(('files[]', f))
            >>> 
            >>> try:
            ...     result = endpoint.upload_item_photos(
            ...         jobid='JOB-2024-001',
            ...         itemid=12345,
            ...         files=photo_files,
            ...         rfqid=67890  # Optional
            ...     )
            ...     print(f"Uploaded {len(result['uploadedFiles'])} photos")
            ... finally:
            ...     for _, f in photo_files:
            ...         f.close()
            
        Note:
            - Accepted image formats typically include JPEG, PNG, and GIF
            - Maximum file size limits may apply (check API documentation)
            - Photos are automatically associated with the specified item
        """
        data = {
            "JobDisplayId": jobid,
            "DocumentType": DocType.Item_Photo.value,
            "DocumentTypeDescription": DocType.Item_Photo.fmt,
            "Shared": 28,
            "JobItems": [itemid],
            "RfqId": rfqid,
        }
        return self._r.upload_file("documents", files=files, data=data)
