"""Contactmerge models for ABConnect API."""

from typing import List, Optional
from pydantic import Field
from .base import ABConnectBaseModel

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
