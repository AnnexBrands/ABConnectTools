"""Lookup models for ABConnect API."""

from typing import Optional
from pydantic import Field
from .base import IdentifiedModel

class ContactTypeEntity(IdentifiedModel):
    """ContactTypeEntity model"""

    value: Optional[str] = Field(None)


class CountryCodeDto(IdentifiedModel):
    """CountryCodeDto model"""

    name: Optional[str] = Field(None)
    iata_code: Optional[str] = Field(None, alias="iataCode")


__all__ = ['ContactTypeEntity', 'CountryCodeDto']
