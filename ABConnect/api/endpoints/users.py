"""Users endpoint for managing user profiles and permissions.

This module provides methods for retrieving user information and
accessing user-specific resources like accessible companies.
"""

from typing import Dict, List, Any
from .base import BaseEndpoint


class UsersEndpoint(BaseEndpoint):
    """Endpoint for user-related API operations.
    
    This endpoint provides methods to retrieve information about the
    authenticated user and their permissions within the system.
    
    Available Methods:
        - me: Get current user's profile
        - access_companies: Get companies the user can access
    """
    def me(self) -> Dict[str, Any]:
        """Retrieve the current authenticated user's profile.
        
        Gets detailed information about the currently logged-in user,
        including their personal details, roles, and permissions.
        
        Returns:
            dict: User profile information with structure::

                {
                    'id': 123,
                    'username': 'john.doe',
                    'email': 'john.doe@example.com',
                    'firstName': 'John',
                    'lastName': 'Doe',
                    'fullName': 'John Doe',
                    'phoneNumber': '+1-555-123-4567',
                    'roles': ['Admin', 'Operations'],
                    'permissions': [
                        'jobs.create',
                        'jobs.edit',
                        'companies.view'
                    ],
                    'company': {
                        'id': 'company-uuid',
                        'code': 'COMP123',
                        'name': 'Example Company'
                    },
                    'preferences': {
                        'timezone': 'America/New_York',
                        'dateFormat': 'MM/DD/YYYY',
                        'language': 'en-US',
                        'emailNotifications': True
                    },
                    'active': True,
                    'lastLogin': '2024-01-15T10:30:00Z',
                    'created': '2023-01-01T00:00:00Z',
                    'modified': '2024-01-15T10:30:00Z'
                }

        Raises:
            ABConnectError: If not authenticated or API error occurs.
            
        Example:
            >>> endpoint = UsersEndpoint()
            >>> user = endpoint.me()
            >>> print(f"Logged in as: {user['fullName']} ({user['email']})")
            >>> print(f"Roles: {', '.join(user['roles'])}")
            >>> if 'Admin' in user['roles']:
            ...     print("User has admin privileges")
        """
        return self._r.call("GET", "/account/profile")

    def access_companies(self) -> List[Dict[str, Any]]:
        """Get list of companies accessible by the current user.
        
        Retrieves all companies that the authenticated user has permission
        to access. This includes companies where the user has any level of
        access rights.
        
        Returns:
            list: A list of company dictionaries the user can access::

                [
                    {
                        'id': 'company-uuid-1',
                        'code': 'COMP123',
                        'name': 'Primary Company',
                        'type': 'Customer',
                        'accessLevel': 'Full',
                        'permissions': [
                            'view',
                            'edit',
                            'create_jobs',
                            'manage_users'
                        ],
                        'isDefault': True,
                        'active': True
                    },
                    {
                        'id': 'company-uuid-2',
                        'code': 'PART456',
                        'name': 'Partner Company',
                        'type': 'Agent',
                        'accessLevel': 'Limited',
                        'permissions': [
                            'view',
                            'create_jobs'
                        ],
                        'isDefault': False,
                        'active': True
                    },
                    ...
                ]

        Raises:
            ABConnectError: If not authenticated or API error occurs.
            
        Example:
            >>> endpoint = UsersEndpoint()
            >>> companies = endpoint.access_companies()
            >>> print(f"User has access to {len(companies)} companies")
            >>> 
            >>> # Find primary company
            >>> primary = next((c for c in companies if c['isDefault']), None)
            >>> if primary:
            ...     print(f"Primary company: {primary['name']} ({primary['code']})")
            >>> 
            >>> # List all companies with full access
            >>> full_access = [c for c in companies if c['accessLevel'] == 'Full']
            >>> for company in full_access:
            ...     print(f"Full access to: {company['name']}")
            
        Note:
            The list of accessible companies determines which companies
            the user can perform operations on throughout the system.
        """
        return self._r.call("GET", "companies/availableByCurrentUser")
