"""Calendar models for ABConnect API."""

from typing import List, Optional
from pydantic import Field
from .base import ABConnectBaseModel

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
