"""Items helper functions for fetching and casting job items.

Provides convenience methods for accessing different types of items with
automatic Pydantic model casting for type safety.
"""

import logging
from typing import List, Union
from ABConnect.api.endpoints.base import BaseEndpoint
from ABConnect.api import models
from ABConnect.config import get_config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ItemsHelper(BaseEndpoint):
    """Helper for fetching different types of job items with Pydantic models.

    This class provides convenience methods that:
    - Fetch items from the appropriate endpoint
    - Cast responses to proper Pydantic models
    - Handle different response formats
    - Provide type-safe item access

    Usage:
        api = ABConnectAPI()
        items = api.jobs.items

        # Get parcel items
        parcel_items = items.parcelitems(4675060)
        for item in parcel_items:
            print(f"{item.description}: {item.job_item_pkd_weight} lbs")

        # Get freight items
        freight_items = items.freightitems(4637814)
        for item in freight_items:
            print(f"Class {item.freight_item_class}: {item.cube} cu ft")

        # Get job/calendar items
        job_items = items.jobitems(4637814)
        for item in job_items:
            print(f"{item.name}: {item.weight} lbs")
    """

    def __init__(self):
        """Initialize the items helper."""
        super().__init__()
        # Import endpoint classes here to avoid circular imports
        from ABConnect.api.endpoints.jobs.parcelitems import JobParcelItemsEndpoint
        from ABConnect.api.endpoints.jobs.job import JobEndpoint
        from ABConnect.api.endpoints.jobs.note import JobNoteEndpoint

        self._parcel_endpoint = JobParcelItemsEndpoint()
        self._job_endpoint = JobEndpoint()
        self._note_endpoint = JobNoteEndpoint()

    def parcelitems(self, job_display_id: Union[int, str]) -> List[models.ParcelItem]:
        """Fetch parcel items for a job with Pydantic model casting.

        Parcel items are items configured for parcel shipping (UPS, FedEx, USPS)
        with specific packaging dimensions and weights.

        Args:
            job_display_id: The job display ID (int or string)

        Returns:
            List of ParcelItem Pydantic models

        Example:
            >>> items = api.jobs.items.parcelitems(4675060)
            >>> for item in items:
            ...     print(f"{item.description}: {item.job_item_pkd_weight} lbs")
        """
        logger.debug(f"Fetching parcel items for job {job_display_id}")

        # Get parcel items from the API
        response = self._parcel_endpoint.get_parcelitems(jobDisplayId=str(job_display_id))

        # Extract parcel items from response (API may return dict with 'parcelItems' key)
        items_data = None
        if isinstance(response, dict) and 'parcelItems' in response:
            items_data = response['parcelItems']
        elif isinstance(response, list):
            items_data = response
        else:
            logger.warning(f"Unexpected response format for parcel items: {type(response)}")
            return []

        if items_data is None:
            logger.warning("No parcel items data found in response")
            return []

        # Cast response to list of ParcelItem models
        try:
            parcel_items = [models.ParcelItem(**item) for item in items_data]
            logger.debug(f"Successfully cast {len(parcel_items)} parcel items")
            return parcel_items
        except Exception as e:
            logger.error(f"Error casting parcel items to Pydantic models: {e}")
            raise

    def freightitems(self, job_display_id: Union[int, str]) -> List[models.FreightShimpment]:
        """Fetch freight items for a job with Pydantic model casting.

        Freight items are items configured for freight shipping (LTL, FTL)
        with NMFC classifications and freight-specific details.

        Args:
            job_display_id: The job display ID (int or string)

        Returns:
            List of FreightShimpment Pydantic models

        Example:
            >>> items = api.jobs.items.freightitems(4637814)
            >>> for item in items:
            ...     print(f"Class {item.freight_item_class} (NMFC: {item.nmfc_item})")
        """
        logger.debug(f"Fetching freight items for job {job_display_id}")

        # Get the full job from the API
        job = self._job_endpoint.get(jobDisplayId=str(job_display_id))

        # Extract freight items from the job
        freight_items_data = job.get('freightItems', [])

        if not freight_items_data:
            logger.debug(f"No freight items found for job {job_display_id}")
            return []

        # Cast response to list of FreightShimpment models
        try:
            freight_items = [models.FreightShimpment(**item) for item in freight_items_data]
            logger.debug(f"Successfully cast {len(freight_items)} freight items")
            return freight_items
        except Exception as e:
            logger.error(f"Error casting freight items to Pydantic models: {e}")
            raise

    def jobitems(self, job_display_id: Union[int, str]) -> List[models.CalendarItem]:
        """Fetch job/calendar items for a job with Pydantic model casting.

        Job/calendar items are general items in the calendar view with basic
        dimensions and weight, used for scheduling and inventory tracking.

        Args:
            job_display_id: The job display ID (int or string)

        Returns:
            List of CalendarItem Pydantic models

        Example:
            >>> items = api.jobs.items.jobitems(4637814)
            >>> for item in items:
            ...     print(f"{item.name}: {item.weight} lbs (${item.value})")
        """
        logger.debug(f"Fetching calendar items for job {job_display_id}")

        # Get calendar items from the API
        response = self._job_endpoint.get_calendaritems(jobDisplayId=str(job_display_id))

        # Response should be a list
        if not isinstance(response, list):
            logger.warning(f"Unexpected response format for calendar items: {type(response)}")
            return []

        if not response:
            logger.debug(f"No calendar items found for job {job_display_id}")
            return []

        # Cast response to list of CalendarItem models
        try:
            calendar_items = [models.CalendarItem(**item) for item in response]
            logger.debug(f"Successfully cast {len(calendar_items)} calendar items")
            return calendar_items
        except Exception as e:
            logger.error(f"Error casting calendar items to Pydantic models: {e}")
            raise

    def logged_delete_parcel_items(self, job_display_id: Union[int, str]) -> bool:
        """Delete all parcel items for a job and log the action with a note.

        This method:
        1. Fetches all parcel items for the job
        2. Creates a compact note listing deleted items with their details
        3. Deletes each parcel item
        4. Returns success/failure status

        Args:
            job_display_id: The job display ID (int or string)

        Returns:
            bool: True if all operations succeeded, False if any errors occurred

        Example:
            >>> items_helper = api.jobs.items
            >>> success = items_helper.logged_delete_parcel_items(4675060)
            >>> if success:
            ...     print("All parcel items deleted and logged successfully")
        """
        logger.info(f"Starting logged deletion of parcel items for job {job_display_id}")

        try:
            # Get current user from authentication config
            try:
                user_name = get_config("ABCONNECT_USERNAME", "").strip()
            except Exception as e:
                logger.warning(f"Could not get username from config: {e}")
                user_name = ""

            # Get all parcel items
            parcel_items = self.parcelitems(job_display_id)

            if not parcel_items:
                logger.info(f"No parcel items found for job {job_display_id}")
                return True  # Nothing to delete, consider it success

            # Format compact note with parcel item details
            item_summaries = []
            for item in parcel_items:
                # Format: qty descr LxHxD Wlbs
                qty = item.quantity or 1
                desc = item.description or "Item"
                length = item.job_item_pkd_length or 0
                height = item.job_item_pkd_height or 0
                depth = item.job_item_pkd_width or 0  # Width is actually depth in our notation
                weight = item.job_item_pkd_weight or 0

                summary = f"{qty} {desc} {length}x{height}x{depth} {weight}lbs"
                item_summaries.append(summary)

            # Create compact note
            items_list = ", ".join(item_summaries)
            if user_name:
                note_text = f"{user_name} deleted parcel items [{items_list}]"
            else:
                note_text = f"Deleted parcel items [{items_list}]"

            # Truncate if note is too long (8000 char limit)
            if len(note_text) > 7900:
                note_text = note_text[:7900] + "...]"

            logger.debug(f"Creating note: {note_text}")

            # Create note using TaskNoteModel
            note = models.TaskNoteModel(
                comments=note_text,
                task_code=models.TaskCodes.PACKAGING,
                is_important=False,
                is_completed=False,
                send_notification=False
            )

            # Post the note
            note_data = note.model_dump(by_alias=True, exclude_none=True)
            note_response = self._note_endpoint.post_note(
                jobDisplayId=str(job_display_id),
                data=note_data
            )
            logger.info(f"Note created successfully: {note_response.get('id', 'N/A')}")

            # Delete each parcel item
            # Note: Use item.id (integer like 2443776), not item.job_item_id (UUID)
            deleted_count = 0
            failed_items = []

            for item in parcel_items:
                logger.info(f"Attempting to delete parcel item {item.id} (description: {item.description})")
                try:
                    self._parcel_endpoint.delete_parcelitems(
                        parcelItemId=str(item.id),
                        jobDisplayId=str(job_display_id)
                    )
                    deleted_count += 1
                    logger.info(f"Successfully deleted parcel item {item.id}")
                except Exception as e:
                    # DELETE endpoint returns 200 with non-JSON response, which raises an error
                    # Check if it's actually a successful deletion (HTTP 200)
                    error_msg = str(e)
                    logger.debug(f"Exception during delete of item {item.id}: {error_msg}")

                    if "HTTP 200" in error_msg and "not valid JSON" in error_msg:
                        # This is actually a successful deletion
                        deleted_count += 1
                        logger.info(f"Successfully deleted parcel item {item.id} (200 OK, non-JSON response)")
                    else:
                        # Real error - log it but continue with other items
                        logger.error(f"Failed to delete parcel item {item.id}: {error_msg}")
                        failed_items.append(item.id)

            # Report results
            if failed_items:
                logger.warning(f"Failed to delete {len(failed_items)} items: {failed_items}")
                return False

            logger.info(f"Successfully deleted {deleted_count} parcel items for job {job_display_id}")
            return True

        except Exception as e:
            logger.error(f"Error in logged_delete_parcel_items for job {job_display_id}: {e}")
            return False

    def replace_parcels(self, job_display_id: Union[int, str], parcel_items: List[Union[models.ParcelItem, dict]]) -> bool:
        """Replace all parcel items for a job with new items.

        This method:
        1. Deletes all existing parcel items with logging (using logged_delete_parcel_items)
        2. Posts the new parcel items to the job
        3. Returns success/failure status

        Args:
            job_display_id: The job display ID (int or string)
            parcel_items: List of parcel items (ParcelItem models or dictionaries)

        Returns:
            bool: True if all operations succeeded, False if any errors occurred

        Example:
            >>> from ABConnect.api.models.jobparcelitems import ParcelItem
            >>> items_helper = api.jobs.items
            >>> new_items = [
            ...     ParcelItem(
            ...         description="Box 1",
            ...         quantity=2,
            ...         job_item_pkd_length=10.0,
            ...         job_item_pkd_width=8.0,
            ...         job_item_pkd_height=6.0,
            ...         job_item_pkd_weight=25.0
            ...     )
            ... ]
            >>> success = items_helper.replace_parcels(4675060, new_items)
            >>> if success:
            ...     print("Parcel items replaced successfully")
        """
        logger.info(f"Starting parcel replacement for job {job_display_id}")

        try:
            # Step 1: Delete existing parcel items with logging
            delete_success = self.logged_delete_parcel_items(job_display_id)
            if not delete_success:
                logger.error(f"Failed to delete existing parcel items for job {job_display_id}")
                return False

            # Step 2: Prepare new parcel items data
            items_data = []
            for item in parcel_items:
                if isinstance(item, models.ParcelItem):
                    # Convert Pydantic model to dict with aliases
                    item_dict = item.model_dump(by_alias=True, exclude_none=True)
                elif isinstance(item, dict):
                    item_dict = item
                else:
                    logger.error(f"Invalid parcel item type: {type(item)}")
                    return False
                items_data.append(item_dict)

            # Step 3: Post new parcel items
            logger.info(f"Posting {len(items_data)} new parcel items to job {job_display_id}")
            try:
                response = self._parcel_endpoint.post_parcelitems(
                    jobDisplayId=str(job_display_id),
                    data=items_data
                )
                logger.info(f"Successfully posted new parcel items: {response}")
                return True
            except Exception as e:
                logger.error(f"Failed to post new parcel items: {e}")
                return False

        except Exception as e:
            logger.error(f"Error in replace_parcels for job {job_display_id}: {e}")
            return False


__all__ = ['ItemsHelper']
