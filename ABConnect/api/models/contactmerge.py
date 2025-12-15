"""Contactmerge models for ABConnect API."""

from __future__ import annotations
from typing import List, Optional, TYPE_CHECKING
from pydantic import Field
from .base import ABConnectBaseModel
from .shared import StringMergePreviewDataItem

if TYPE_CHECKING:
    from .contacts import BaseContactDetails
    from .address import AddressDetailsMergePreviewDataItem

class MergeContactsPreviewInfo(ABConnectBaseModel):
    """MergeContactsPreviewInfo model"""

    contact_id: Optional[int] = Field(None, alias="contactId")
    base_info: Optional[BaseContactDetails] = Field(None, alias="baseInfo")
    phone_numbers: Optional[List[StringMergePreviewDataItem]] = Field(None, alias="phoneNumbers")
    emails: Optional[List[StringMergePreviewDataItem]] = Field(None)
    addresses: Optional[List[AddressDetailsMergePreviewDataItem]] = Field(None)


class MergeContactsPreviewRequestModel(ABConnectBaseModel):
    """MergeContactsPreviewRequestModel model"""

    merge_from_contact_ids: Optional[List[int]] = Field(None, alias="mergeFromContactIds")


class MergeContactsRequestModel(ABConnectBaseModel):
    """MergeContactsRequestModel model"""

    merge_from_contact_id: int = Field(..., alias="mergeFromContactId")


__all__ = ['MergeContactsPreviewInfo', 'MergeContactsPreviewRequestModel', 'MergeContactsRequestModel']
