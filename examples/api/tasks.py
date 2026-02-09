"""
Task Timeline Examples - Walk a job through statuses 2-10

Demonstrates the discriminated-union task models and timeline helpers
against the staging environment.

Usage:
    python tasks.py                     # Run all examples
    python tasks.py get_timeline        # Run a single example
    python tasks.py help                # List available examples
"""

from datetime import datetime, timedelta
from ABConnect.api.models import TaskCodes
from ABConnect.api.models.shared import PickupTask, PackagingTask, StorageTask, CarrierTaskModel
from ABConnect.api.models.jobtimeline import DeleteTaskResponse, TimelineResponse, SaveResponseModel
from _base import ExampleRunner
from _helpers import save_fixture
from _constants import TASK_JOB_DISPLAY_ID


class TaskExamples(ExampleRunner):
    def __init__(self):
        super().__init__("Tasks API", api_kwargs=dict(username="instaquote", env="staging"))
        self.add("delete_all", "Reset: delete all tasks (status 1)", self.delete_all)
        self.add("get_timeline", "GET timeline (status 1)", self.get_timeline)
        self.add("schedule", "Schedule pickup (status 2)", self.schedule)
        self.add("received", "Received (status 3)", self.received)
        self.add("pack_start", "Packaging started (status 4)", self.pack_start)
        self.add("pack_finish", "Packaging completed (status 5)", self.pack_finish)
        self.add("storage_begin", "Storage (status 6)", self.storage_begin)
        self.add("carrier_schedule", "Carrier scheduled (status 7)", self.carrier_schedule)
        self.add("carrier_pickup", "Carrier pickup (status 8)", self.carrier_pickup)
        self.add("carrier_delivery", "Delivered (status 10)", self.carrier_delivery)

    def _times(self):
        now = datetime.now().replace(minute=0, second=0, microsecond=0)
        return now.isoformat(), (now + timedelta(hours=1)).isoformat()

    def delete_all(self):
        deleted = self.api.tasks.delete_all(TASK_JOB_DISPLAY_ID)
        print(f"  Deleted {len(deleted)} task(s)")

    def get_timeline(self):
        r = self.api.tasks.get_timeline(TASK_JOB_DISPLAY_ID)
        assert isinstance(r, TimelineResponse), f"Expected TimelineResponse, got {type(r)}"
        print(f"  success={r.success}, tasks={len(r.tasks or [])}")
        save_fixture(r, "TimelineResponse")
        for t in r.tasks or []:
            tc = t.task_code
            if tc == "PU":
                assert isinstance(t, PickupTask)
            elif tc == "PK":
                assert isinstance(t, PackagingTask)
            elif tc == "ST":
                assert isinstance(t, StorageTask)
            elif tc == "CP":
                assert isinstance(t, CarrierTaskModel)
            print(f"  task {tc}: {type(t).__name__}")

    def schedule(self):
        start, _ = self._times()
        r = self.api.tasks.schedule(TASK_JOB_DISPLAY_ID, start)
        assert r is not None, "schedule() returned None - job already past status 1"
        assert isinstance(r, SaveResponseModel)
        assert isinstance(r.task, PickupTask)
        print(f"  success={r.success}, task_exists={r.task_exists}")
        print(f"  plannedStartDate={r.task.planned_start_date}")
        save_fixture(r, "SaveResponseModel_schedule")

    def received(self):
        start, end = self._times()
        r = self.api.tasks.received(TASK_JOB_DISPLAY_ID, start, end)
        assert r is not None, "received() returned None - job already past status 2"
        assert isinstance(r, SaveResponseModel)
        assert isinstance(r.task, PickupTask)
        print(f"  success={r.success}, completedDate={r.task.completed_date}")
        save_fixture(r, "SaveResponseModel_received")

    def pack_start(self):
        start, _ = self._times()
        r = self.api.tasks.pack_start(TASK_JOB_DISPLAY_ID, start)
        assert r is not None, "pack_start() returned None - job already past status 3"
        assert isinstance(r, SaveResponseModel)
        assert isinstance(r.task, PackagingTask)
        print(f"  success={r.success}, timeLog.start={r.task.time_log.start if r.task.time_log else None}")
        save_fixture(r, "SaveResponseModel_pack_start")

    def pack_finish(self):
        _, end = self._times()
        r = self.api.tasks.pack_finish(TASK_JOB_DISPLAY_ID, end)
        assert r is not None, "pack_finish() returned None - job already past status 4"
        assert isinstance(r, SaveResponseModel)
        assert isinstance(r.task, PackagingTask)
        print(f"  success={r.success}, timeLog.end={r.task.time_log.end if r.task.time_log else None}")
        save_fixture(r, "SaveResponseModel_pack_finish")

    def storage_begin(self):
        start, _ = self._times()
        r = self.api.tasks.storage_begin(TASK_JOB_DISPLAY_ID, start)
        assert isinstance(r, SaveResponseModel)
        assert isinstance(r.task, StorageTask)
        print(f"  success={r.success}, timeLog.start={r.task.time_log.start if r.task.time_log else None}")
        save_fixture(r, "SaveResponseModel_storage_begin")

    def carrier_schedule(self):
        start, _ = self._times()
        r = self.api.tasks.carrier_schedule(TASK_JOB_DISPLAY_ID, start)
        assert r is not None, "carrier_schedule() returned None - job already past status 6"
        assert isinstance(r, SaveResponseModel)
        assert isinstance(r.task, CarrierTaskModel)
        print(f"  success={r.success}, scheduledDate={r.task.scheduled_date}")
        save_fixture(r, "SaveResponseModel_carrier_schedule")

    def carrier_pickup(self):
        start, _ = self._times()
        r = self.api.tasks.carrier_pickup(TASK_JOB_DISPLAY_ID, start)
        assert r is not None, "carrier_pickup() returned None - job already past status 7"
        assert isinstance(r, SaveResponseModel)
        assert isinstance(r.task, CarrierTaskModel)
        print(f"  success={r.success}, pickupCompletedDate={r.task.pickup_completed_date}")
        save_fixture(r, "SaveResponseModel_carrier_pickup")

    def carrier_delivery(self):
        _, end = self._times()
        r = self.api.tasks.carrier_delivery(TASK_JOB_DISPLAY_ID, end)
        assert isinstance(r, SaveResponseModel)
        assert isinstance(r.task, CarrierTaskModel)
        print(f"  success={r.success}, deliveryCompletedDate={r.task.delivery_completed_date}")
        save_fixture(r, "SaveResponseModel_carrier_delivery")


if __name__ == "__main__":
    TaskExamples().run()
