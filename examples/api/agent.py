"""
Agent API Examples - Change OA and DA for a job

Demonstrates resolving agent codes to UUIDs via get_cache()
and calling the changeAgent endpoint.

Usage:
    python agent.py                 # Run all examples
    python agent.py oa              # Run a single example
    python agent.py help            # List available examples
"""

from ABConnect.api.models.shared import ServiceBaseResponse
from _base import ExampleRunner
from _helpers import save_fixture
from _constants import TASK_JOB_DISPLAY_ID


class AgentExamples(ExampleRunner):
    def __init__(self):
        super().__init__("Agent API", api_kwargs=dict(username="instaquote"))
        self.add("oa", "Change origin agent (PickAndPack)", self.change_oa)
        self.add("da", "Change delivery agent", self.change_da)

    def change_oa(self):
        job = TASK_JOB_DISPLAY_ID
        agent_code = "9999AZ"
        r = self.api.jobs.agent.oa(job, agent_code)
        assert isinstance(r, ServiceBaseResponse), f"Expected ServiceBaseResponse, got {type(r)}"
        print(f"  success={r.success}")
        save_fixture(r, "ChangeAgent_OA")

    def change_da(self):
        job = TASK_JOB_DISPLAY_ID
        agent_code = "9999AZ"
        r = self.api.jobs.agent.da(job, agent_code)
        assert isinstance(r, ServiceBaseResponse), f"Expected ServiceBaseResponse, got {type(r)}"
        print(f"  success={r.success}")
        save_fixture(r, "ChangeAgent_DA")


if __name__ == "__main__":
    AgentExamples().run()
