"""Advancedsettings models for ABConnect API."""

from typing import Optional
from pydantic import Field
from .base import IdentifiedModel

class AdvancedSettingsEntitySaveModel(IdentifiedModel):
    """AdvancedSettingsEntitySaveModel model"""

    api_key: Optional[str] = Field(None, alias="apiKey")
    value: str = Field(..., min_length=1)
    name: Optional[str] = Field(None)


__all__ = ['AdvancedSettingsEntitySaveModel']
