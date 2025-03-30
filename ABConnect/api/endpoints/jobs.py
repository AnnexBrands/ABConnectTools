from ABConnect.common import load_json_resource
from ABConnect.api.endpoints.base import BaseEndpoint


class JobsEndpoint(BaseEndpoint):
    def get(self, jobid):
        """Get job details."""
        return self._r.call("GET", f"job/{jobid}")

    def change_agent(
        self,
        jobid,
        CompanyCode,
        serviceType="PickAndPack",
        recalculatePrice=False,
        applyRebate=False,
    ) -> dict:
        """Change the agent for a job."""
        companies = load_json_resource("companies.json")
        companyid = companies.get(CompanyCode)
        return (
            self._r.call(
                "POST",
                f"job/{jobid}/changeAgent",
                json={
                    "serviceType": serviceType,
                    "agentId": companyid,
                    "recalculatePrice": recalculatePrice,
                    "applyRebate": applyRebate,
                },
            ),
        )
