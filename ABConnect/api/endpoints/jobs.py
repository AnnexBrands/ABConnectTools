"""Jobs endpoint for managing shipping and logistics jobs.

This module provides methods for retrieving job details and modifying
job properties such as the assigned agent.
"""

from typing import Dict, Any, Optional
from ABConnect.common import load_json_resource
from ABConnect.api.endpoints.base import BaseEndpoint
from ABConnect.exceptions import ABConnectError


class JobsEndpoint(BaseEndpoint):
    """Endpoint for job-related API operations.
    
    This endpoint provides methods to manage shipping and logistics jobs,
    including retrieving job details and modifying job assignments.
    
    Available Methods:
        - get: Retrieve complete job details
        - change_agent: Change the assigned agent for a job
    """
    def get(self, jobid: str) -> Dict[str, Any]:
        """Retrieve complete details for a job.
        
        Fetches comprehensive information about a specific job including
        shipment details, items, timeline, pricing, and current status.
        
        Args:
            jobid (str): The job identifier (e.g., 'JOB-2024-001').
                This can be either the display ID or internal job ID.
                
        Returns:
            dict: Complete job information with structure::

                {
                    'id': 'internal-job-id',
                    'displayId': 'JOB-2024-001',
                    'status': 'In Transit',
                    'type': 'Regular|3PL|DirectShip',
                    'customer': {
                        'id': 'customer-uuid',
                        'code': 'CUST123',
                        'name': 'Customer Name'
                    },
                    'agent': {
                        'id': 'agent-uuid',
                        'code': 'AGT456',
                        'name': 'Agent Name'
                    },
                    'origin': {
                        'address': {...},
                        'contact': {...},
                        'scheduledDate': '2024-01-15T09:00:00Z'
                    },
                    'destination': {
                        'address': {...},
                        'contact': {...},
                        'scheduledDate': '2024-01-20T17:00:00Z'
                    },
                    'freightItems': [...],
                    'parcelItems': [...],
                    'pricing': {
                        'subtotal': 1000.00,
                        'tax': 80.00,
                        'total': 1080.00,
                        'currency': 'USD'
                    },
                    'timeline': [
                        {
                            'event': 'Created',
                            'timestamp': '2024-01-10T10:00:00Z',
                            'user': 'john.doe@example.com'
                        },
                        ...
                    ],
                    'documents': [...],
                    'notes': [...],
                    'created': '2024-01-10T10:00:00Z',
                    'modified': '2024-01-15T14:30:00Z'
                }

        Raises:
            ABConnectError: If the job is not found or API error occurs.
            
        Example:
            >>> endpoint = JobsEndpoint()
            >>> job = endpoint.get('JOB-2024-001')
            >>> print(f"Job Status: {job['status']}")
            >>> print(f"Customer: {job['customer']['name']}")
            >>> print(f"Total Price: ${job['pricing']['total']}")
        """
        return self._r.call("GET", f"job/{jobid}")

    def change_agent(
        self,
        jobid: str,
        CompanyCode: str,
        serviceType: str = "PickAndPack",
        recalculatePrice: bool = False,
        applyRebate: bool = False,
    ) -> Dict[str, Any]:
        """Change the assigned agent for a job.
        
        Updates the agent responsible for handling a job. This can trigger
        price recalculation and rebate application based on the parameters.
        
        Args:
            jobid (str): The job identifier (e.g., 'JOB-2024-001').
            CompanyCode (str): The company code of the new agent (e.g., 'AGT789').
                Must be a valid agent company code from the system.
            serviceType (str, optional): The type of service the agent will provide.
                Common values include:
                - 'PickAndPack' (default): Standard pick and pack service
                - 'WhiteGlove': Premium handling service
                - 'Storage': Storage and warehousing
                - 'CrossDock': Cross-docking service
            recalculatePrice (bool, optional): Whether to recalculate the job price
                based on the new agent's rates. Defaults to False.
            applyRebate (bool, optional): Whether to apply any applicable rebates
                for the new agent. Defaults to False.
                
        Returns:
            dict: Response containing the updated job information::

                {
                    'success': True,
                    'jobId': 'JOB-2024-001',
                    'previousAgent': {
                        'id': 'old-agent-uuid',
                        'code': 'AGT456',
                        'name': 'Previous Agent'
                    },
                    'newAgent': {
                        'id': 'new-agent-uuid',
                        'code': 'AGT789',
                        'name': 'New Agent'
                    },
                    'priceChange': {
                        'previous': 1000.00,
                        'new': 950.00,
                        'difference': -50.00
                    } if recalculatePrice else None,
                    'rebateApplied': 25.00 if applyRebate else None
                }

        Raises:
            ABConnectError: If the company code is not found, the job doesn't exist,
                or the agent change is not allowed for the job's current status.
            
        Example:
            >>> endpoint = JobsEndpoint()
            >>> # Change agent without price recalculation
            >>> result = endpoint.change_agent(
            ...     jobid='JOB-2024-001',
            ...     CompanyCode='AGT789',
            ...     serviceType='WhiteGlove'
            ... )
            >>> 
            >>> # Change agent with price recalculation and rebate
            >>> result = endpoint.change_agent(
            ...     jobid='JOB-2024-001',
            ...     CompanyCode='AGT789',
            ...     serviceType='PickAndPack',
            ...     recalculatePrice=True,
            ...     applyRebate=True
            ... )
            >>> if result['priceChange']:
            ...     print(f"Price changed by ${result['priceChange']['difference']}")
            
        Note:
            The company code must exist in the local companies.json cache.
            Agent changes may be restricted based on job status and type.
        """
        companies = load_json_resource("companies.json")
        companyid = companies.get(CompanyCode)
        
        if not companyid:
            raise ABConnectError(f"Company code {CompanyCode} not found.")
            
        return self._r.call(
            "POST",
            f"job/{jobid}/changeAgent",
            json={
                "serviceType": serviceType,
                "agentId": companyid,
                "recalculatePrice": recalculatePrice,
                "applyRebate": applyRebate,
            },
        )
