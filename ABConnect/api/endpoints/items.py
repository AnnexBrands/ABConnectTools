"""Items endpoint for managing freight and parcel items within jobs.

This module provides methods for creating, reading, updating, and deleting
both freight and parcel items associated with shipping jobs.
"""

from typing import List, Dict, Any, Union
from ABConnect.api.endpoints.base import BaseEndpoint


class ItemsEndpoint(BaseEndpoint):
    """Endpoint for item-related API operations.
    
    This endpoint manages two types of items within jobs:
    - Freight items: Larger shipments typically moved via freight carriers
    - Parcel items: Smaller packages typically shipped via parcel services
    
    Available Methods:
        - get_freight: Retrieve freight items for a job
        - set_freight: Create/update freight items
        - get_parcel: Retrieve parcel items for a job
        - set_parcel: Create parcel items
        - update_parcel: Update specific parcel item
        - delete_parcel: Remove parcel item
    """
    def get_freight(self, jobid: str) -> List[Dict[str, Any]]:
        """Retrieve all freight items for a job.
        
        Gets the list of freight items associated with a specific job.
        Freight items typically represent larger shipments that require
        freight carrier services.
        
        Args:
            jobid (str): The job identifier (e.g., 'JOB-2024-001').
            
        Returns:
            list: A list of freight item dictionaries::

                [
                    {
                        'id': 123,
                        'description': 'Pallet of electronics',
                        'quantity': 2,
                        'weight': 500,
                        'weightUnit': 'lbs',
                        'dimensions': {
                            'length': 48,
                            'width': 40,
                            'height': 60,
                            'unit': 'inches'
                        },
                        'class': '85',
                        'nmfc': '123456',
                        'value': 5000.00,
                        'hazmat': False,
                        'stackable': True
                    },
                    ...
                ]

        Raises:
            ABConnectError: If the job is not found or API error occurs.
            
        Example:
            >>> endpoint = ItemsEndpoint()
            >>> freight_items = endpoint.get_freight('JOB-2024-001')
            >>> total_weight = sum(item['weight'] for item in freight_items)
            >>> print(f"Total freight weight: {total_weight} lbs")
        """
        job_data = self._r.call("GET", f"job/{jobid}")
        return job_data["freightItems"]

    def set_freight(self, jobid: str, freighitems: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Create or replace freight items for a job.
        
        Sets the complete list of freight items for a job. This operation
        replaces any existing freight items.
        
        Args:
            jobid (str): The job identifier (e.g., 'JOB-2024-001').
            freighitems (list): List of freight item dictionaries::
            
                [
                    {
                        'description': 'Pallet of electronics',
                        'quantity': 2,
                        'weight': 500,
                        'weightUnit': 'lbs',
                        'dimensions': {
                            'length': 48,
                            'width': 40,
                            'height': 60,
                            'unit': 'inches'
                        },
                        'class': '85',
                        'nmfc': '123456',
                        'value': 5000.00,
                        'hazmat': False,
                        'stackable': True
                    }
                ]
                
        Returns:
            dict: Response confirming the operation::

                {
                    'success': True,
                    'itemsCreated': 2,
                    'items': [...],
                    'totalWeight': 1000,
                    'totalValue': 10000.00
                }

        Raises:
            ABConnectError: If validation fails or API error occurs.
            
        Example:
            >>> endpoint = ItemsEndpoint()
            >>> freight_items = [
            ...     {
            ...         'description': 'Office Furniture',
            ...         'quantity': 1,
            ...         'weight': 250,
            ...         'class': '125',
            ...         'value': 1500.00
            ...     }
            ... ]
            >>> result = endpoint.set_freight('JOB-2024-001', freight_items)
        """
        return self._r.call("POST", f"job/{jobid}/freightitems", json=freighitems)

    def get_parcel(self, jobid: str) -> List[Dict[str, Any]]:
        """Retrieve all parcel items for a job.
        
        Gets the list of parcel items associated with a specific job.
        Parcel items typically represent smaller packages suitable for
        parcel carrier services (UPS, FedEx, etc.).
        
        Args:
            jobid (str): The job identifier (e.g., 'JOB-2024-001').
            
        Returns:
            list: A list of parcel item dictionaries::

                [
                    {
                        'id': 456,
                        'trackingNumber': '1Z999AA10123456789',
                        'description': 'Electronics - Box 1',
                        'weight': 25,
                        'weightUnit': 'lbs',
                        'dimensions': {
                            'length': 18,
                            'width': 12,
                            'height': 10,
                            'unit': 'inches'
                        },
                        'declaredValue': 1000.00,
                        'carrier': 'UPS',
                        'service': 'Ground',
                        'status': 'In Transit',
                        'reference1': 'PO-12345',
                        'reference2': 'DEPT-ELECTRONICS'
                    },
                    ...
                ]

        Raises:
            ABConnectError: If the job is not found or API error occurs.
            
        Example:
            >>> endpoint = ItemsEndpoint()
            >>> parcels = endpoint.get_parcel('JOB-2024-001')
            >>> for parcel in parcels:
            ...     print(f"Tracking: {parcel['trackingNumber']} - {parcel['status']}")
        """
        return self._r.call("GET", f"job/{jobid}/parcelitems")

    def set_parcel(self, jobid: str, parcelitems: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Create new parcel items for a job.
        
        Adds one or more parcel items to a job. Unlike freight items,
        this operation adds to existing items rather than replacing them.
        
        Args:
            jobid (str): The job identifier (e.g., 'JOB-2024-001').
            parcelitems (list): List of parcel item dictionaries::
            
                [
                    {
                        'description': 'Electronics - Box 1',
                        'weight': 25,
                        'weightUnit': 'lbs',
                        'dimensions': {
                            'length': 18,
                            'width': 12,
                            'height': 10,
                            'unit': 'inches'
                        },
                        'declaredValue': 1000.00,
                        'reference1': 'PO-12345',
                        'reference2': 'DEPT-ELECTRONICS'
                    }
                ]
                
        Returns:
            dict: Response with created items::

                {
                    'success': True,
                    'itemsCreated': 1,
                    'items': [
                        {
                            'id': 789,
                            'trackingNumber': '1Z999AA10123456789',
                            ...  # Full item details
                        }
                    ]
                }

        Raises:
            ABConnectError: If validation fails or API error occurs.
            
        Example:
            >>> endpoint = ItemsEndpoint()
            >>> new_parcels = [
            ...     {
            ...         'description': 'Laptop Computer',
            ...         'weight': 10,
            ...         'declaredValue': 2000.00,
            ...         'dimensions': {'length': 15, 'width': 10, 'height': 3}
            ...     }
            ... ]
            >>> result = endpoint.set_parcel('JOB-2024-001', new_parcels)
            >>> print(f"Created {result['itemsCreated']} parcels")
        """
        return self._r.call("POST", f"job/{jobid}/parcelitems", json=parcelitems)

    def update_parcel(self, jobid: str, parcelItemId: int, parcelitems: Dict[str, Any]) -> Dict[str, Any]:
        """Update a specific parcel item.
        
        Modifies the details of an existing parcel item. Only the fields
        provided in the update dictionary will be changed.
        
        Args:
            jobid (str): The job identifier (e.g., 'JOB-2024-001').
            parcelItemId (int): The ID of the parcel item to update.
            parcelitems (dict): Dictionary of fields to update::
            
                {
                    'description': 'Updated description',
                    'weight': 30,
                    'declaredValue': 1500.00,
                    'status': 'Delivered',
                    'trackingNumber': '1Z999AA10123456790'
                }
                
        Returns:
            dict: The updated parcel item::

                {
                    'id': 456,
                    'description': 'Updated description',
                    'weight': 30,
                    ...  # All item fields
                }

        Raises:
            ABConnectError: If the item is not found or API error occurs.
            
        Example:
            >>> endpoint = ItemsEndpoint()
            >>> # Update weight and tracking number
            >>> updates = {
            ...     'weight': 28,
            ...     'trackingNumber': '1Z999AA10123456790',
            ...     'status': 'Out for Delivery'
            ... }
            >>> updated = endpoint.update_parcel('JOB-2024-001', 456, updates)
            >>> print(f"Updated parcel: {updated['trackingNumber']}")
        """
        return self._r.call(
            "PUT", f"job/{jobid}/parcelitems/{parcelItemId}", json=parcelitems
        )

    def delete_parcel(self, jobid: str, parcelItemId: int) -> Dict[str, Any]:
        """Delete a specific parcel item from a job.
        
        Permanently removes a parcel item from the job. This action
        cannot be undone.
        
        Args:
            jobid (str): The job identifier (e.g., 'JOB-2024-001').
            parcelItemId (int): The ID of the parcel item to delete.
            
        Returns:
            dict: Confirmation of deletion::

                {
                    'success': True,
                    'message': 'Parcel item 456 deleted successfully',
                    'deletedItemId': 456
                }

        Raises:
            ABConnectError: If the item is not found or cannot be deleted.
            
        Example:
            >>> endpoint = ItemsEndpoint()
            >>> # Delete a parcel item
            >>> result = endpoint.delete_parcel('JOB-2024-001', 456)
            >>> if result['success']:
            ...     print(f"Deleted item {result['deletedItemId']}")
            
        Warning:
            Deleting a parcel item may affect job pricing and routing.
            Items with tracking numbers in use cannot be deleted.
        """
        return self._r.call("DELETE", f"job/{jobid}/parcelitems/{parcelItemId}")

