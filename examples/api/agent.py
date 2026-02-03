"""Agent change example: change OA and DA for a job.

Demonstrates resolving agent codes to UUIDs via get_cache()
and calling the changeAgent endpoint.
"""

from ABConnect import ABConnectAPI
from ABConnect.api.models.shared import ServiceBaseResponse
from _constants import TASK_JOB_DISPLAY_ID
from _helpers import save_fixture

# --- Setup ---
api = ABConnectAPI(username="instaquote")
job = TASK_JOB_DISPLAY_ID
agent_code = "9999AZ"

# =====================================================================
# 1. Change Origin Agent (OA / PickAndPack)
# =====================================================================
print("=== 1. oa  (change origin agent) ===")
r1 = api.jobs.agent.oa(job, agent_code)
assert isinstance(r1, ServiceBaseResponse), (
    f"Expected ServiceBaseResponse, got {type(r1)}"
)
print(f"  success={r1.success}")
save_fixture(r1, "ChangeAgent_OA")

# =====================================================================
# 2. Change Delivery Agent (DA)
# =====================================================================
print("\n=== 2. da  (change delivery agent) ===")
r2 = api.jobs.agent.da(job, agent_code)
assert isinstance(r2, ServiceBaseResponse), (
    f"Expected ServiceBaseResponse, got {type(r2)}"
)
print(f"  success={r2.success}")
save_fixture(r2, "ChangeAgent_DA")

print("\nDone.")
