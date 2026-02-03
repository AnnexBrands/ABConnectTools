"""Agent helper functions for job operations.

Provides convenience methods for changing job agents using friendly
company codes (resolved via cache) or direct UUIDs.
"""

import logging
from typing import Dict, Any
from ABConnect.api.endpoints.jobs.job import JobEndpoint
from ABConnect.api.models.enums import ServiceType

logger = logging.getLogger(__name__)


class AgentEndpoint(JobEndpoint):
    """Enhanced job endpoint with helper methods for agent changes.

    Extends the base JobEndpoint with convenience methods that:
    - Accept agent codes (e.g. "9999AZ") or UUIDs
    - Resolve codes to UUIDs via get_cache()
    - Provide clear method names for OA/DA operations
    """

    def oa(
        self,
        jobid: int,
        agent: str,
        recalculate_price: bool = False,
        apply_rebate: bool = False,
    ) -> Dict[str, Any]:
        """Change Origin Agent (PickAndPack) for a job.

        Args:
            jobid: Job display ID
            agent: Agent code (e.g., '9999AZ') or agent UUID
            recalculate_price: Whether to recalculate the job price
            apply_rebate: Whether to apply rebate

        Returns:
            ServiceBaseResponse confirming agent change
        """
        return self.change(jobid, agent, ServiceType.PICKANDPACK, recalculate_price, apply_rebate)

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
            agent: Agent code (e.g., '9999AZ') or agent UUID
            recalculate_price: Whether to recalculate the job price
            apply_rebate: Whether to apply rebate

        Returns:
            ServiceBaseResponse confirming agent change
        """
        return self.change(jobid, agent, ServiceType.DELIVERY, recalculate_price, apply_rebate)

    def change(
        self,
        jobid: int,
        agent: str,
        service_type: ServiceType,
        recalculate_price: bool = False,
        apply_rebate: bool = False,
    ) -> Dict[str, Any]:
        """Change agent for any service type.

        Resolves agent codes to UUIDs via get_cache() before calling the API.

        Args:
            jobid: Job display ID
            agent: Agent code (e.g., '9999AZ') or agent UUID
            service_type: ServiceType enum value
            recalculate_price: Whether to recalculate the job price
            apply_rebate: Whether to apply rebate

        Returns:
            ServiceBaseResponse confirming agent change
        """
        agent_id = self.get_cache(agent)
        logger.info(
            f"Changing agent for job {jobid} to {agent} (UUID: {agent_id}) "
            f"with service type {service_type.name}"
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
