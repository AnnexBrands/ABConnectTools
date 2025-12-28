"""Job helper functions for common operations.

Provides convenience methods for job operations including agent changes.
"""

import logging
from typing import Optional, Dict, Any
from ABConnect.api.endpoints.jobs.job import JobEndpoint

logger = logging.getLogger(__name__)

# ServiceType mapping based on API enum
# These values map to the ServiceType enum in the API
SERVICE_TYPE_PICKPACK = 0  # Origin Agent (OA) - PickPack operations
SERVICE_TYPE_DELIVERY = 1  # Delivery Agent (DA) - Delivery operations
SERVICE_TYPE_2 = 2  # Unknown - needs documentation
SERVICE_TYPE_3 = 3  # Unknown - needs documentation
SERVICE_TYPE_4 = 4  # Unknown - needs documentation


class AgentEndpoint(JobEndpoint):
    """Enhanced job endpoint with helper methods for common operations.

    Extends the base JobEndpoint with convenience methods that:
    - Accept agent codes or UUIDs
    - Provide clear method names for specific operations
    - Handle agent resolution automatically
    """

    def oa(
        self,
        jobid: int,
        agent: str,
        recalculate_price: bool = False,
        apply_rebate: bool = False,
    ) -> Dict[str, Any]:
        """Change Origin Agent (PickPack) for a job.

        Args:
            jobid: Job display ID
            agent: Agent code (e.g., 'JM') or agent UUID
            recalculate_price: Whether to recalculate the job price
            apply_rebate: Whether to apply rebate

        Returns:
            API response dictionary

        """
        agent_id = self.get_cache(agent)


        return self.post_changeAgent(
            jobDisplayId=str(jobid),
            data={
                "serviceType": "PickAndPack",
                "agentId": agent_id,
                "recalculatePrice": recalculate_price,
                "applyRebate": apply_rebate,
            },
        )

    def da(
        self,
        jobid: int,
        agent: str,
        recalculate_price: bool = False,
        apply_rebate: bool = False,
    ) -> Dict[str, Any]:
        """Change Delivery Agent for a job.

        Args:
            jobid: Job display ID
            agent: Agent code (e.g., 'ABC') or agent UUID
            recalculate_price: Whether to recalculate the job price
            apply_rebate: Whether to apply rebate

        Returns:
            API response dictionary

        Examples:
            # Change DA using agent code
            api.jobs.job.change_da(2000000, "ABC")

            # Change DA with rebate
            api.jobs.job.change_da(2000000, "ABC", apply_rebate=True)
        """
        agent_id = self._resolve_agent_identifier(agent)

        logger.info(
            f"Changing Delivery Agent for job {jobid} to {agent} (UUID: {agent_id})"
        )

        return self.post_changeAgent(
            jobDisplayId=str(jobid),
            data={
                "serviceType": SERVICE_TYPE_DELIVERY,
                "agentId": agent_id,
                "recalculatePrice": recalculate_price,
                "applyRebate": apply_rebate,
            },
        )

    def change(
        self,
        jobid: int,
        agent: str,
        service_type: int,
        recalculate_price: bool = False,
        apply_rebate: bool = False,
    ) -> Dict[str, Any]:
        """Change agent for any service type.

        Generic method for changing agents when you need to specify the service type.

        Args:
            jobid: Job display ID
            agent: Agent code or agent UUID
            service_type: Service type integer (0=PickPack, 1=Delivery, 2-4=TBD)
            recalculate_price: Whether to recalculate the job price
            apply_rebate: Whether to apply rebate

        Returns:
            API response dictionary

        Examples:
            # Change agent for service type 2
            api.jobs.job.change_agent(2000000, "XYZ", service_type=2)

            # Change with all options
            api.jobs.job.change_agent(2000000, "XYZ", 3, recalculate_price=True, apply_rebate=True)
        """
        agent_id = self._resolve_agent_identifier(agent)

        logger.info(
            f"Changing agent for job {jobid} to {agent} (UUID: {agent_id}) with service type {service_type}"
        )

        return self.post_changeAgent(
            jobDisplayId=str(jobid),
            data={
                "serviceType": service_type,
                "agentId": agent_id,
                "recalculatePrice": recalculate_price,
                "applyRebate": apply_rebate,
            },
        )
