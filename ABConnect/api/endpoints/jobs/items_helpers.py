"""Items helper functions for fetching and casting job items.

Provides convenience methods for accessing different types of items with
automatic Pydantic model casting for type safety.
"""

import logging
from typing import List, Union
from ABConnect.api.endpoints.base import BaseEndpoint
from ABConnect.api.models.jobparcelitems import ParcelItem
from ABConnect.api.models.job import FreightShimpment
from ABConnect.api.models.shared import CalendarItem

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

        self._parcel_endpoint = JobParcelItemsEndpoint()
        self._job_endpoint = JobEndpoint()

    def parcelitems(self, job_display_id: Union[int, str]) -> List[ParcelItem]:
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
            parcel_items = [ParcelItem(**item) for item in items_data]
            logger.debug(f"Successfully cast {len(parcel_items)} parcel items")
            return parcel_items
        except Exception as e:
            logger.error(f"Error casting parcel items to Pydantic models: {e}")
            raise

    def freightitems(self, job_display_id: Union[int, str]) -> List[FreightShimpment]:
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
            freight_items = [FreightShimpment(**item) for item in freight_items_data]
            logger.debug(f"Successfully cast {len(freight_items)} freight items")
            return freight_items
        except Exception as e:
            logger.error(f"Error casting freight items to Pydantic models: {e}")
            raise

    def jobitems(self, job_display_id: Union[int, str]) -> List[CalendarItem]:
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
            calendar_items = [CalendarItem(**item) for item in response]
            logger.debug(f"Successfully cast {len(calendar_items)} calendar items")
            return calendar_items
        except Exception as e:
            logger.error(f"Error casting calendar items to Pydantic models: {e}")
            raise


__all__ = ['ItemsHelper']
