"""Timeline helper functions with collision prevention.

Provides convenience methods for timeline operations that handle the get-update
pattern to avoid collisions when updating job timeline tasks.
"""

from typing import Optional, Dict, Any, Tuple
from ABConnect.api.endpoints.jobs.timeline import JobTimelineEndpoint
from ABConnect.common import load_json_resource
from ABConnect.api import models
from datetime import datetime, timedelta
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load status definitions
statuses = load_json_resource("statuses.json")


class TimelineHelpers(JobTimelineEndpoint):
    """Enhanced timeline endpoint with helper methods for common operations.

    This class provides convenience methods that:
    - Always fetch current task state before updating (prevents collisions)
    - Check current status to prevent invalid transitions
    - Provide intuitive method names for common timeline operations
    - Support optional email notifications
    """

    # Task templates for creating new tasks
    new_field_task_sch = {
        "taskCode": "PU",
        "completedDate": None,
    }  # Status 2

    new_field_task = {
        "taskCode": "PU",
        "onSiteTimeLog": {},
        "completedDate": None,
    }  # Status 3

    new_pack_task = {
        "taskCode": "PK",
        "timeLog": {},
        "workTimeLogs": [],
    }  # Status 4/5: Packaging

    new_store_task = {
        "taskCode": "ST",
        "timeLog": {},
        "workTimeLogs": [],
    }  # Status 6: Storage

    new_carrier_task = {
        "taskCode": "CP",
        "scheduledDate": None,
        "pickupCompletedDate": None,
        "deliveryCompletedDate": None,
    }  # Status 7/8/10: Carrier operations

    def get_task(
        self, jobid: int, taskcode: str
    ) -> Tuple[Dict[str, Any], Optional[Dict[str, Any]]]:
        """Get a specific task from the timeline with status information.

        Args:
            jobid: Job display ID
            taskcode: Task code (PU, PK, ST, CP, etc.)

        Returns:
            Tuple of (status_info, task_data or None)
        """
        timeline = self.get_timeline(str(jobid))
        status = timeline.get("jobSubManagementStatus", {})

        # Enrich status with code and description
        status_id = status.get("id")
        if status_id and status_id in statuses:
            statusinfo = statuses[status_id]
            status["code"] = statusinfo["code"]
            status["descr"] = statusinfo["descr"]
        else:
            status["code"] = 0
            status["descr"] = "Unknown"

        # Find the specific task
        for task in timeline.get("tasks", []):
            if task.get("taskCode") == taskcode:
                return status, task

        return status, None

    def set_task(
        self, jobid: int, taskcode: str, task: Dict[str, Any], createEmail: bool = False
    ) -> Dict[str, Any]:
        """Update or create a timeline task.

        This method handles both creating new tasks and updating existing ones.
        It uses POST to the timeline endpoint which intelligently merges updates.

        Args:
            jobid: Job display ID
            taskcode: Task code (not currently used but kept for compatibility)
            task: Task data dictionary
            createEmail: Whether to send email notification

        Returns:
            API response dictionary
        """
        return self.post_timeline(
            jobDisplayId=str(jobid),
            create_email="true" if createEmail else "false",
            data=task,
        )

    # ========== Pickup/Field Operations (Status 2-3) ==========

    def schedule(
        self,
        jobid: int,
        start: str,
        end: Optional[str] = None,
        createEmail: bool = False,
    ) -> Optional[Dict[str, Any]]:
        """Set the pickup scheduled date for a job (Status 2).

        Args:
            jobid: Job display ID
            start: Planned start date (ISO format)
            end: Optional planned end date (ISO format)
            createEmail: Whether to send email notification

        Returns:
            API response or None if already at/past this status
        """
        logger.info(f"Setting job {jobid} as scheduled with start={start}, end={end}")
        statusinfo, task = self.get_task(jobid, models.TaskCodes.PICKUP)
        curr = statusinfo.get("code", 0)

        if curr >= 2:
            logger.warning(
                f"Job {jobid} already at status {curr} ({statusinfo.get('descr', 'Unknown')})"
            )
            return None

        if not task:
            task = self.new_field_task_sch.copy()

        task["plannedStartDate"] = start
        if end:
            task["plannedEndDate"] = end

        return self.set_task(jobid, models.TaskCodes.PICKUP, task, createEmail)

    def _2(self, *args, **kwargs) -> Optional[Dict[str, Any]]:
        """Alias for schedule() - Set status 2."""
        return self.schedule(*args, **kwargs)

    def received(
        self,
        jobid: int,
        start: Optional[str] = None,
        end: Optional[str] = None,
        createEmail: bool = False
    ) -> Optional[Dict[str, Any]]:
        """Set the job as received (Status 3: Pickup completed).
        
        Handles onsite time logging according to the following rules:
        - If neither start nor end provided: end = now (current hour), no onSiteTimeLog
        - If only end provided: use end, do NOT include onSiteTimeLog
        - If only start provided: end = start + 1 hour, include onSiteTimeLog
        - If both provided: use both, include onSiteTimeLog
        
        Args:
            jobid: Job display ID
            start: Onsite start time in ISO format (e.g., "2025-12-20T14:30:00")
            end: Onsite end time/completion in ISO format
            createEmail: Whether to send email notification
        
        Returns:
            API response dict or None if job is already at/past status 3
        """
        logger.info(f"Setting job {jobid} as received with start={start}, end={end}")

        statusinfo, task = self.get_task(jobid, models.TaskCodes.PICKUP)
        curr = statusinfo.get("code", 0)
        if curr >= 3:
            logger.warning(
                f"Job {jobid} already at status {curr} ({statusinfo.get('descr', 'Unknown')})"
            )
            return None

        if not task:
            task = self.new_field_task.copy()

        # Determine final end time
        final_end: str
        include_onsite_log: bool = False
        onsite_start: Optional[str] = None
        onsite_end: Optional[str] = None

        if start and end:
            final_end = end
            include_onsite_log = True
            onsite_start = start
            onsite_end = end

        elif start and not end:
            try:
                start_dt = datetime.fromisoformat(start.replace("Z", "+00:00"))
                end_dt = start_dt + timedelta(hours=1)
                final_end = end_dt.isoformat(timespec='seconds')
                include_onsite_log = True
                onsite_start = start
                onsite_end = final_end
            except ValueError as e:
                logger.error(f"Invalid start datetime format for job {jobid}: {start}")
                raise ValueError(f"Invalid ISO format for start: {start}") from e

        elif end and not start:
            final_end = end
            include_onsite_log = False

        else:
            now = datetime.now()
            current_hour = now.replace(minute=0, second=0, microsecond=0)
            final_end = current_hour.isoformat(timespec='seconds') + "Z"
            include_onsite_log = False

        task["completedDate"] = final_end

        if include_onsite_log:
            task["onSiteTimeLog"] = {
                "start": onsite_start,
                "end": onsite_end
            }
        else:
            task.pop("onSiteTimeLog", None)

        return self.set_task(jobid, models.TaskCodes.PICKUP, task, createEmail)

    def _3(self, *args, **kwargs) -> Optional[Dict[str, Any]]:
        """Alias for received() - Set status 3."""
        return self.received(*args, **kwargs)

    # ========== Packaging Operations (Status 4-5) ==========

    def pack_start(
        self, jobid: int, start: str, createEmail: bool = False
    ) -> Optional[Dict[str, Any]]:
        """Set the packing start date for a job (Status 4).

        Args:
            jobid: Job display ID
            start: Packing start time (ISO format)
            createEmail: Whether to send email notification

        Returns:
            API response or None if already at/past this status
        """
        statusinfo, task = self.get_task(jobid, models.TaskCodes.PACKAGING)
        curr = statusinfo.get("code", 0)

        if curr >= 4:
            logger.warning(
                f"Job {jobid} already at status {curr} ({statusinfo.get('descr', 'Unknown')})"
            )
            return None

        if not task:
            task = self.new_pack_task.copy()

        task["timeLog"] = {"start": start}
        return self.set_task(jobid, models.TaskCodes.PACKAGING, task, createEmail)

    def _4(self, *args, **kwargs) -> Optional[Dict[str, Any]]:
        """Alias for pack_start() - Set status 4."""
        return self.pack_start(*args, **kwargs)

    def pack_finish(
        self, jobid: int, end: str, createEmail: bool = False
    ) -> Optional[Dict[str, Any]]:
        """Set the packing finish date for a job (Status 5).

        Args:
            jobid: Job display ID
            end: Packing end time (ISO format)
            createEmail: Whether to send email notification

        Returns:
            API response or None if already at/past this status
        """
        statusinfo, task = self.get_task(jobid, models.TaskCodes.PACKAGING)
        curr = statusinfo.get("code", 0)

        if curr >= 5:
            logger.warning(
                f"Job {jobid} already at status {curr} ({statusinfo.get('descr', 'Unknown')})"
            )
            return None

        if not task:
            task = self.new_pack_task.copy()
            task["timeLog"] = {}

        task["timeLog"]["end"] = end
        return self.set_task(jobid, models.TaskCodes.PACKAGING, task, createEmail)

    def _5(self, *args, **kwargs) -> Optional[Dict[str, Any]]:
        """Alias for pack_finish() - Set status 5."""
        return self.pack_finish(*args, **kwargs)

    # ========== Storage Operations (Status 6) ==========

    def storage_begin(
        self, jobid: int, start: str, createEmail: bool = False
    ) -> Dict[str, Any]:
        """Set the storage start date for a job (Status 6).

        Args:
            jobid: Job display ID
            start: Storage start time (ISO format)
            createEmail: Whether to send email notification

        Returns:
            API response
        """
        statusinfo, task = self.get_task(jobid, models.TaskCodes.STORAGE)

        if not task:
            task = self.new_store_task.copy()

        if "timeLog" not in task:
            task["timeLog"] = {}

        task["timeLog"]["start"] = start
        return self.set_task(jobid, models.TaskCodes.STORAGE, task, createEmail)

    def _6(self, *args, **kwargs) -> Dict[str, Any]:
        """Alias for storage_begin() - Set status 6."""
        return self.storage_begin(*args, **kwargs)

    def storage_end(
        self, jobid: int, end: str, createEmail: bool = False
    ) -> Dict[str, Any]:
        """Set the storage end date for a job.

        Args:
            jobid: Job display ID
            end: Storage end time (ISO format)
            createEmail: Whether to send email notification

        Returns:
            API response
        """
        statusinfo, task = self.get_task(jobid, models.TaskCodes.STORAGE)

        if not task:
            task = self.new_store_task.copy()

        if "timeLog" not in task:
            task["timeLog"] = {}

        task["timeLog"]["end"] = end
        return self.set_task(jobid, models.TaskCodes.STORAGE, task, createEmail)

    # ========== Carrier Operations (Status 7-8, 10) ==========

    def carrier_schedule(
        self, jobid: int, start: str, createEmail: bool = False
    ) -> Optional[Dict[str, Any]]:
        """Set the carrier scheduled date for a job (Status 7).

        Args:
            jobid: Job display ID
            start: Scheduled pickup date (ISO format)
            createEmail: Whether to send email notification

        Returns:
            API response or None if already at/past this status
        """
        statusinfo, task = self.get_task(jobid, models.TaskCodes.CARRIER)
        curr = statusinfo.get("code", 0)

        if curr >= 7:
            logger.warning(
                f"Job {jobid} already at status {curr} ({statusinfo.get('descr', 'Unknown')})"
            )
            return None

        if not task:
            task = self.new_carrier_task.copy()

        task["scheduledDate"] = start
        return self.set_task(jobid, models.TaskCodes.CARRIER, task, createEmail)

    def _7(self, *args, **kwargs) -> Optional[Dict[str, Any]]:
        """Alias for carrier_schedule() - Set status 7."""
        return self.carrier_schedule(*args, **kwargs)

    def carrier_pickup(
        self, jobid: int, start: str, createEmail: bool = False
    ) -> Optional[Dict[str, Any]]:
        """Set the carrier pickup date for a job (Status 8).

        Args:
            jobid: Job display ID
            start: Pickup completion date (ISO format)
            createEmail: Whether to send email notification

        Returns:
            API response or None if already at/past this status
        """
        statusinfo, task = self.get_task(jobid, models.TaskCodes.CARRIER)
        curr = statusinfo.get("code", 0)

        if curr >= 8:
            logger.warning(
                f"Job {jobid} already at status {curr} ({statusinfo.get('descr', 'Unknown')})"
            )
            return None

        if not task:
            task = self.new_carrier_task.copy()

        task["pickupCompletedDate"] = start
        return self.set_task(jobid, models.TaskCodes.CARRIER, task, createEmail)

    def _8(self, *args, **kwargs) -> Optional[Dict[str, Any]]:
        """Alias for carrier_pickup() - Set status 8."""
        return self.carrier_pickup(*args, **kwargs)

    def carrier_delivery(
        self, jobid: int, end: str, createEmail: bool = False
    ) -> Dict[str, Any]:
        """Set the carrier delivery date for a job (Status 10).

        Args:
            jobid: Job display ID
            end: Delivery completion date (ISO format)
            createEmail: Whether to send email notification

        Returns:
            API response
        """
        statusinfo, task = self.get_task(jobid, models.TaskCodes.CARRIER)

        if not task:
            task = self.new_carrier_task.copy()

        task["deliveryCompletedDate"] = end
        return self.set_task(jobid, models.TaskCodes.CARRIER, task, createEmail)

    def _10(self, *args, **kwargs) -> Dict[str, Any]:
        """Alias for carrier_delivery() - Set status 10."""
        return self.carrier_delivery(*args, **kwargs)

    # ========== Utility Methods ==========

    def delete(self, jobid: int, taskcode: str) -> Optional[Dict[str, Any]]:
        """Delete a timeline task.

        Args:
            jobid: Job display ID
            taskcode: Task code to delete (PU, PK, ST, CP, etc.)

        Returns:
            API response or None if task not found
        """
        status, task = self.get_task(jobid, taskcode)
        if task and "id" in task:
            return self.delete_timeline(
                timelineTaskId=str(task["id"]), jobDisplayId=str(jobid)
            )

        logger.warning(f"Task {taskcode} not found for job {jobid}")
        return None
