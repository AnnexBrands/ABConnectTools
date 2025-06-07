"""Contacts endpoint for managing contact information.

This module provides methods for retrieving contact details from the ABC API.
"""

from ABConnect.api.endpoints.base import BaseEndpoint


class ContactsEndpoint(BaseEndpoint):
    """Endpoint for contact-related API operations.
    
    This endpoint provides methods to retrieve contact information
    from the ABC API using contact IDs.
    """
    def get(self, id: int) -> dict:
        """Retrieve contact information by contact ID.
        
        Fetches detailed information about a specific contact using their
        unique identifier.

        Args:
            id (int): The unique contact identifier. This should be a positive
                integer representing the contact's ID in the system.

        Returns:
            dict: A dictionary containing contact information with structure::

                {
                    'id': 123,
                    'firstName': 'John',
                    'lastName': 'Doe',
                    'email': 'john.doe@example.com',
                    'phone': '+1-555-123-4567',
                    'mobile': '+1-555-987-6543',
                    'title': 'Operations Manager',
                    'companyId': 'uuid-string',
                    'companyName': 'ABC Company',
                    'addresses': [
                        {
                            'type': 'Business',
                            'line1': '123 Main St',
                            'line2': 'Suite 100',
                            'city': 'New York',
                            'state': 'NY',
                            'zip': '10001',
                            'country': 'US'
                        }
                    ],
                    'preferences': {
                        'emailNotifications': True,
                        'smsNotifications': False
                    },
                    'active': True,
                    'created': '2023-01-01T00:00:00Z',
                    'modified': '2023-12-01T00:00:00Z'
                }

        Raises:
            ABConnectError: If the contact ID is not found or if there's an API error.
            
        Example:
            >>> endpoint = ContactsEndpoint()
            >>> contact = endpoint.get(12345)
            >>> print(f"Contact: {contact['firstName']} {contact['lastName']}")
            >>> print(f"Email: {contact['email']}")
            >>> print(f"Company: {contact['companyName']}")
        """
        return self._r.call("GET", f"contacts/{id}")
