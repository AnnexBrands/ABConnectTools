"""Calendar models for ABConnect API."""

from __future__ import annotations
from typing import List, Optional, TYPE_CHECKING
from pydantic import Field
from .base import ABConnectBaseModel

if TYPE_CHECKING:
    from .address import CalendarAddress
    from .contacts import CalendarContact
    from .job import BaseInfoCalendarJob, CalendarJob

class BaseInfoCalendar(ABConnectBaseModel):
    """BaseInfoCalendar model"""

    addresses: Optional[List[CalendarAddress]] = Field(None)
    jobs: Optional[List[BaseInfoCalendarJob]] = Field(None)


class Calendar(ABConnectBaseModel):
    """Calendar model"""

    addresses: Optional[List[CalendarAddress]] = Field(None)
    contacts: Optional[List[CalendarContact]] = Field(None)
    jobs: Optional[List[CalendarJob]] = Field(None)


__all__ = ['BaseInfoCalendar', 'Calendar']
