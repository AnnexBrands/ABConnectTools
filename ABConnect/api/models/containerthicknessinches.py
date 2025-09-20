"""Containerthicknessinches models for ABConnect API."""

from typing import Optional
from pydantic import Field
from .base import ABConnectBaseModel

class ContainerThickness(ABConnectBaseModel):
    """ContainerThickness model"""

    container_id: Optional[int] = Field(None, alias="containerId")
    thickness_inches: Optional[float] = Field(None, alias="thicknessInches")


__all__ = ['ContainerThickness']
