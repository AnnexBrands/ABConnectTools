from ABConnect import ABConnectAPI
from ABConnect.api.models import TaskCodes
from ABConnect.api.models.jobtimeline import (
    DeleteTaskResponse,
    TimelineResponse,
    SaveResponseModel,
)
from datetime import datetime

start = datetime(2026, 1, 26, 12, 14)
end = datetime(2026, 1, 26, 12, 15)

api = ABConnectAPI(username="instaquote")

job = 5649470

# r1: TimelineResponse - get all timeline tasks
r1 = api.tasks.get_timeline(job)
print(r1)
print(f"  r1.success={r1.success}, tasks={len(r1.tasks or [])}")

# r2: DeleteTaskResponse - delete pickup task
r2 = api.tasks.delete(job, TaskCodes.PICKUP)
print(r2)
if r2 is not None:
    assert isinstance(r2, DeleteTaskResponse), (
        f"Expected DeleteTaskResponse, got {type(r2)}"
    )
    print(f"  r2 is DeleteTaskResponse: True, r2.success={r2.success}")
else:
    print("  r2: task not found (None)")

# r3: SaveResponseModel - mark job as received (pass ISO strings, not datetime)
r3 = api.tasks.received(job, start.isoformat(), end.isoformat())
print(r3)
if r3 is not None:
    print(f"  r3.success={r3.success}, r3.task_exists={r3.task_exists}")
else:
    print("  r3: already at or past status 3 (None)")
