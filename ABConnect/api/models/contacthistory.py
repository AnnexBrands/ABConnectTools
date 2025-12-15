"""Contacthistory models for ABConnect API."""

from __future__ import annotations
from typing import Any, Dict, List, Optional, TYPE_CHECKING
from pydantic import Field
from .base import ABConnectBaseModel, TimestampedModel
from .enums import StatusEnum
from .shared import SortingInfo, GroupingInfo, SummaryInfo

if TYPE_CHECKING:
    from .contacts import ContactHistoryRevenueSum, ContactHistoryPricePerPound

class ContactHistoryAggregatedCost(ABConnectBaseModel):
    """ContactHistoryAggregatedCost model"""

    sum_job_total_amount: Optional[float] = Field(None, alias="sumJobTotalAmount")
    sum_job_total_value: Optional[float] = Field(None, alias="sumJobTotalValue")
    sum_job_total_weight: Optional[float] = Field(None, alias="sumJobTotalWeight")
    avg_job_total_amount: Optional[float] = Field(None, alias="avgJobTotalAmount")
    avg_job_total_value: Optional[float] = Field(None, alias="avgJobTotalValue")
    avg_job_total_weight: Optional[float] = Field(None, alias="avgJobTotalWeight")


class ContactHistoryDataSourceLoadOptions(ABConnectBaseModel):
    """ContactHistoryDataSourceLoadOptions model"""

    require_total_count: Optional[bool] = Field(None, alias="requireTotalCount")
    require_group_count: Optional[bool] = Field(None, alias="requireGroupCount")
    is_count_query: Optional[bool] = Field(None, alias="isCountQuery")
    is_summary_query: Optional[bool] = Field(None, alias="isSummaryQuery")
    skip: Optional[int] = Field(None)
    take: Optional[int] = Field(None)
    sort: Optional[List[SortingInfo]] = Field(None)
    group: Optional[List[GroupingInfo]] = Field(None)
    filter: Optional[List[Dict[str, Any]]] = Field(None)
    total_summary: Optional[List[SummaryInfo]] = Field(None, alias="totalSummary")
    group_summary: Optional[List[SummaryInfo]] = Field(None, alias="groupSummary")
    select: Optional[List[str]] = Field(None)
    pre_select: Optional[List[str]] = Field(None, alias="preSelect")
    remote_select: Optional[bool] = Field(None, alias="remoteSelect")
    remote_grouping: Optional[bool] = Field(None, alias="remoteGrouping")
    expand_linq_sum_type: Optional[bool] = Field(None, alias="expandLinqSumType")
    primary_key: Optional[List[str]] = Field(None, alias="primaryKey")
    default_sort: Optional[str] = Field(None, alias="defaultSort")
    string_to_lower: Optional[bool] = Field(None, alias="stringToLower")
    paginate_via_primary_key: Optional[bool] = Field(None, alias="paginateViaPrimaryKey")
    sort_by_primary_key: Optional[bool] = Field(None, alias="sortByPrimaryKey")
    allow_async_over_sync: Optional[bool] = Field(None, alias="allowAsyncOverSync")
    statuses: Optional[List[StatusEnum]] = Field(None)


class ContactHistoryGraphData(ABConnectBaseModel):
    """ContactHistoryGraphData model"""

    revenue_sum: Optional[List[ContactHistoryRevenueSum]] = Field(None, alias="revenueSum")
    price_per_pound: Optional[List[ContactHistoryPricePerPound]] = Field(None, alias="pricePerPound")


class ContactHistoryInfo(TimestampedModel):
    """ContactHistoryInfo model"""

    job_id: Optional[str] = Field(None, alias="jobId")
    job_display_id: Optional[int] = Field(None, alias="jobDisplayId")
    company_id: Optional[str] = Field(None, alias="companyId")
    company_code: Optional[str] = Field(None, alias="companyCode")
    job_status: Optional[str] = Field(None, alias="jobStatus")
    job_total_amount: Optional[float] = Field(None, alias="jobTotalAmount")
    job_total_value: Optional[float] = Field(None, alias="jobTotalValue")
    job_total_weight: Optional[float] = Field(None, alias="jobTotalWeight")


__all__ = ['ContactHistoryAggregatedCost', 'ContactHistoryDataSourceLoadOptions', 'ContactHistoryGraphData', 'ContactHistoryInfo']
