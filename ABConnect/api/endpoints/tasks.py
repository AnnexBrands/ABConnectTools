import logging
from typing import Optional
from ABConnect.api.endpoints.base import BaseEndpoint
from ABConnect.common import load_json_resource

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

statuses = load_json_resource("statuses.json")


class TasksEndpoint(BaseEndpoint):
    new_field_task = {
        "taskCode": "PU",
        "onSiteTimeLog": {},
        "completedDate": None,
    }  # 2/3 PU and 9 DE
    new_simple_task = {"taskCode": "PK", "timeLog": {}, "workTimeLogs": []}  # 4/5 PK
    new_carrier_task = {
        "taskCode": "CP",
        "scheduledDate": None,
        "pickupCompletedDate": None,
        "deliveryCompletedDate": None,
    }  # 7/8 TR

    def get(self, jobid: int) -> dict:
        """Get task details."""
        return self._r.call("GET", f"api/job/{jobid}/timeline")

    def set(self, jobid, taskcode: str, task: dict, createEmail: bool = False):
        url = "api/job/%(jobid)s/timeline?createEmail=%(createEmail)s" % {
            "jobid": jobid,
            "createEmail": createEmail,
        }
        return self._r.call("POST", url, json=task)

    def get_task(self, jobid: int, taskcode: str) -> tuple:
        """Get task details."""
        timeline = self.get(jobid)
        status = timeline.get("jobSubManagementStatus", {})
        statusinfo = statuses.get(status["id"], {})
        if statusinfo:
            status["code"] = statusinfo["code"]
            status["descr"] = statusinfo["descr"]

        for task in timeline["tasks"]:
            if task["taskCode"] == taskcode:
                return status, task

        return status, None

    def schedule(
        self, jobid: int, start: str, end: Optional[str] = None, createEmail=False
    ) -> dict:
        """Set the pickup scheduled date for a job."""
        statusinfo, task = self.get_task(jobid, "PU")
        curr = statusinfo.get("code", 0)

        if curr >= 2:
            logger.warning("{jobid} already status {curr}")
            return

        if not task:
            task = self.new_field_task

        task.update({"plannedStartDate": start})
        if end:
            task.update({"plannedEndDate": end})

        return self.set(jobid, "PU", task, createEmail=createEmail)

    def _2(self, *args, **kwargs) -> dict:
        """Alias to Set the pickup scheduled date for a job."""
        return self.schedule(*args, **kwargs)

    def received(
        self, jobid: int, start: str, end: str, createEmail: bool = False
    ) -> dict:
        """Set the received date for a job."""
        statusinfo, task = self.get_task(jobid, "PU")
        curr = statusinfo.get("code", 0)

        if curr >= 3:
            logger.warning(f"{jobid} already status {curr}")
            return

        if not task:
            task = self.new_field_task

        task["onSiteTimeLog"] = {"start": start, "end": end}
        task["completedDate"] = end
        return self.set(jobid, "PU", task)

    def _3(self, *args, **kwargs) -> dict:
        """Alias to Set the received date for a job."""
        return self.received(*args, **kwargs)

    def pack_start(self, jobid: int, start: str, createEmail: bool = False) -> dict:
        """Set the packing start date for a job."""
        statusinfo, task = self.get_task(jobid, "PK")
        curr = statusinfo.get("code", 0)

        if curr >= 4:
            logger.warning(f"{jobid} already status {curr}")
            return

        if not task:
            task = self.new_simple_task

        task["timeLog"] = {"start": start}
        return self.set(jobid, "PK", task, createEmail=createEmail)

    def _4(self, *args, **kwargs) -> dict:
        """Alias to Set the packing start date for a job."""
        return self.pack_start(*args, **kwargs)

    def pack_finish(self, jobid: int, end: str, createEmail: bool = False) -> dict:
        """Set the packing finish date for a job."""
        statusinfo, task = self.get_task(jobid, "PK")
        curr = statusinfo.get("code", 0)

        if curr >= 5:
            logger.warning(f"{jobid} already status {curr}")
            return

        if not task:
            task = self.new_simple_task

        task["timeLog"]["end"] = end
        return self.set(jobid, "PK", task, createEmail=createEmail)

    def _5(self, *args, **kwargs) -> dict:
        """Alias to Set the packing finish date for a job."""
        return self.pack_finish(*args, **kwargs)

    def storage_begin(self, jobid: int, start: str, createEmail: bool = False) -> dict:
        """Set the storage start date for a job."""
        statusinfo, task = self.get_task(jobid, "ST")
        curr = statusinfo.get("code", 0)

        if not task:
            task = self.new_simple_task

        task["timeLog"].update({"start": start})
        return self.set(jobid, "ST", task, createEmail=createEmail)

    def _6(self, *args, **kwargs) -> dict:
        """Alias to Set the storage start date for a job."""
        return self.storage_begin(*args, **kwargs)

    def storage_end(
        self,
        jobid: int,
        end: str,
        createEmailL: bool = False,
        createEmail: bool = False,
    ) -> dict:
        """Set the storage end date for a job."""
        statusinfo, task = self.get_task(jobid, "ST")
        curr = statusinfo.get("code", 0)

        if not task:
            task = self.new_simple_task

        task["timeLog"].update({"end": end})
        return self.set(jobid, "ST", task, createEmail=createEmail)

    def carrier_schedule(
        self, jobid: int, start: str, createEmail: bool = False
    ) -> dict:
        """Set the carrier scheduled date for a job."""
        statusinfo, task = self.get_task(jobid, "CP")
        curr = statusinfo.get("code", 0)

        if curr >= 7:
            logger.warning(f"{jobid} already status {curr}")
            return

        if not task:
            task = self.new_carrier_task

        task["scheduledDate"] = start
        return self.set(jobid, "CP", task, createEmail=createEmail)

    def _7(self, *args, **kwargs) -> dict:
        """Alias to Set the carrier scheduled date for a job."""
        return self.carrier_schedule(*args, **kwargs)

    def carrier_pickup(self, jobid: int, start: str, createEmail: bool = False) -> dict:
        """Set the carrier pickup date for a job."""
        statusinfo, task = self.get_task(jobid, "CP")
        curr = statusinfo.get("code", 0)

        if curr >= 8:
            logger.warning(f"{jobid} already status {curr}")
            return

        if not task:
            task = self.new_carrier_task

        task["pickupCompletedDate"] = start
        return self.set(jobid, "CP", task, createEmail=createEmail)

    def _8(self, *args, **kwargs) -> dict:
        """Alias to Set the carrier pickup date for a job."""
        return self.carrier_pickup(*args, **kwargs)

    def carrier_delivery(self, jobid: int, end: str, createEmail=False) -> dict:
        """Set the carrier delivery date for a job."""
        statusinfo, task = self.get_task(jobid, "CP")
        curr = statusinfo.get("code", 0)

        if not task:
            task = self.new_carrier_task

        task["deliveryCompletedDate"] = end
        return self.set(jobid, "CP", task, createEmail=createEmail)

    def _10(self, *args, **kwargs) -> dict:
        """Alias to Set the carrier delivery date for a job."""
        return self.carrier_delivery(*args, **kwargs)

    def delete(self, jobid: int, taskcode: str) -> dict:
        """Delete a task."""
        status, task = self.get_task(jobid, taskcode)
        if task:
            url_params = {"jobid": jobid, "timelineTaskId": task["id"]}
            url = "api/job/%(jobid)s/timeline/%(timelineTaskId)s" % url_params
            return self._r.call("DELETE", url)
