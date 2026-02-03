"""Task timeline example: walk a job through statuses 2-10.

Demonstrates the discriminated-union task models and timeline helpers
against the staging environment.
"""

from ABConnect import ABConnectAPI
from ABConnect.api.models import TaskCodes
from ABConnect.api.models.shared import PickupTask, PackagingTask, StorageTask, CarrierTaskModel
from ABConnect.api.models.jobtimeline import (
    DeleteTaskResponse,
    TimelineResponse,
    SaveResponseModel,
)
from _constants import TASK_JOB_DISPLAY_ID
from _helpers import save_fixture
from datetime import datetime, timedelta

# --- Setup ---
api = ABConnectAPI(username="instaquote", env="staging")
job = TASK_JOB_DISPLAY_ID

now = datetime.now().replace(minute=0, second=0, microsecond=0)
start = now.isoformat()
end = (now + timedelta(hours=1)).isoformat()

# =====================================================================
# 0. Reset: delete all tasks so the job starts at status 1
# =====================================================================
print("=== 0. delete_all  (reset to status 1) ===")
deleted = api.tasks.delete_all(job)
print(f"  Deleted {len(deleted)} task(s)")

# =====================================================================
# 1. GET timeline  (status 1 - New Job)
# =====================================================================
print("\n=== 1. get_timeline  (status 1) ===")
r1 = api.tasks.get_timeline(job)
assert isinstance(r1, TimelineResponse), f"Expected TimelineResponse, got {type(r1)}"
print(f"  success={r1.success}, tasks={len(r1.tasks or [])}")
save_fixture(r1, "TimelineResponse")

# Verify each task is the correct subclass
for t in r1.tasks or []:
    tc = t.task_code
    if tc == "PU":
        assert isinstance(t, PickupTask), f"PU task should be PickupTask, got {type(t)}"
    elif tc == "PK":
        assert isinstance(t, PackagingTask), f"PK task should be PackagingTask, got {type(t)}"
    elif tc == "ST":
        assert isinstance(t, StorageTask), f"ST task should be StorageTask, got {type(t)}"
    elif tc == "CP":
        assert isinstance(t, CarrierTaskModel), f"CP task should be CarrierTaskModel, got {type(t)}"
    print(f"  task {tc}: {type(t).__name__}")

# =====================================================================
# 2. schedule  (status 2 - Scheduled)
# =====================================================================
print("\n=== 2. schedule  (status 2) ===")
r2 = api.tasks.schedule(job, start)
assert r2 is not None, "schedule() returned None - job already past status 1"
assert isinstance(r2, SaveResponseModel), f"Expected SaveResponseModel, got {type(r2)}"
assert isinstance(r2.task, PickupTask), f"Expected PickupTask, got {type(r2.task)}"
print(f"  success={r2.success}, task_exists={r2.task_exists}")
print(f"  plannedStartDate={r2.task.planned_start_date}")
save_fixture(r2, "SaveResponseModel_schedule")

# =====================================================================
# 3. received  (status 3 - Received)
# =====================================================================
print("\n=== 3. received  (status 3) ===")
r3 = api.tasks.received(job, start, end)
assert r3 is not None, "received() returned None - job already past status 2"
assert isinstance(r3, SaveResponseModel), f"Expected SaveResponseModel, got {type(r3)}"
assert isinstance(r3.task, PickupTask), f"Expected PickupTask, got {type(r3.task)}"
print(f"  success={r3.success}, completedDate={r3.task.completed_date}")
save_fixture(r3, "SaveResponseModel_received")

# =====================================================================
# 4. pack_start  (status 4 - Packaging Started)
# =====================================================================
print("\n=== 4. pack_start  (status 4) ===")
r4 = api.tasks.pack_start(job, start)
assert r4 is not None, "pack_start() returned None - job already past status 3"
assert isinstance(r4, SaveResponseModel), f"Expected SaveResponseModel, got {type(r4)}"
assert isinstance(r4.task, PackagingTask), f"Expected PackagingTask, got {type(r4.task)}"
print(f"  success={r4.success}, timeLog.start={r4.task.time_log.start if r4.task.time_log else None}")
save_fixture(r4, "SaveResponseModel_pack_start")

# =====================================================================
# 5. pack_finish  (status 5 - Packaging Completed)
# =====================================================================
print("\n=== 5. pack_finish  (status 5) ===")
r5 = api.tasks.pack_finish(job, end)
assert r5 is not None, "pack_finish() returned None - job already past status 4"
assert isinstance(r5, SaveResponseModel), f"Expected SaveResponseModel, got {type(r5)}"
assert isinstance(r5.task, PackagingTask), f"Expected PackagingTask, got {type(r5.task)}"
print(f"  success={r5.success}, timeLog.end={r5.task.time_log.end if r5.task.time_log else None}")
save_fixture(r5, "SaveResponseModel_pack_finish")

# =====================================================================
# 6. storage_begin  (status 6 - Storage)
# =====================================================================
print("\n=== 6. storage_begin  (status 6) ===")
r6 = api.tasks.storage_begin(job, start)
assert isinstance(r6, SaveResponseModel), f"Expected SaveResponseModel, got {type(r6)}"
assert isinstance(r6.task, StorageTask), f"Expected StorageTask, got {type(r6.task)}"
print(f"  success={r6.success}, timeLog.start={r6.task.time_log.start if r6.task.time_log else None}")
save_fixture(r6, "SaveResponseModel_storage_begin")

# =====================================================================
# 7. carrier_schedule  (status 7 - Carrier Scheduled)
# =====================================================================
print("\n=== 7. carrier_schedule  (status 7) ===")
r7 = api.tasks.carrier_schedule(job, start)
assert r7 is not None, "carrier_schedule() returned None - job already past status 6"
assert isinstance(r7, SaveResponseModel), f"Expected SaveResponseModel, got {type(r7)}"
assert isinstance(r7.task, CarrierTaskModel), f"Expected CarrierTaskModel, got {type(r7.task)}"
print(f"  success={r7.success}, scheduledDate={r7.task.scheduled_date}")
save_fixture(r7, "SaveResponseModel_carrier_schedule")

# =====================================================================
# 8. carrier_pickup  (status 8 - Carrier Pickup)
# =====================================================================
print("\n=== 8. carrier_pickup  (status 8) ===")
r8 = api.tasks.carrier_pickup(job, start)
assert r8 is not None, "carrier_pickup() returned None - job already past status 7"
assert isinstance(r8, SaveResponseModel), f"Expected SaveResponseModel, got {type(r8)}"
assert isinstance(r8.task, CarrierTaskModel), f"Expected CarrierTaskModel, got {type(r8.task)}"
print(f"  success={r8.success}, pickupCompletedDate={r8.task.pickup_completed_date}")
save_fixture(r8, "SaveResponseModel_carrier_pickup")

# =====================================================================
# 10. carrier_delivery  (status 10 - Delivered)
# =====================================================================
print("\n=== 10. carrier_delivery  (status 10) ===")
r10 = api.tasks.carrier_delivery(job, end)
assert isinstance(r10, SaveResponseModel), f"Expected SaveResponseModel, got {type(r10)}"
assert isinstance(r10.task, CarrierTaskModel), f"Expected CarrierTaskModel, got {type(r10.task)}"
print(f"  success={r10.success}, deliveryCompletedDate={r10.task.delivery_completed_date}")
save_fixture(r10, "SaveResponseModel_carrier_delivery")

print("\nDone - walked job through statuses 2-10.")
