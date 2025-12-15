"""Reports models for ABConnect API."""

from typing import Optional
from datetime import datetime
from pydantic import Field
from .base import ABConnectBaseModel, CompanyRelatedModel, IdentifiedModel, JobRelatedModel
from .enums import RangeDateEnum
from .shared import SortBy

class InsuranceReport(ABConnectBaseModel):
    """InsuranceReport model"""

    job_number: Optional[str] = Field(None, alias="jobNumber")
    franchisee: Optional[str] = Field(None)
    insurance_type: Optional[str] = Field(None, alias="insuranceType")
    no_of_piece: Optional[int] = Field(None, alias="noOfPiece")
    total_cost: Optional[float] = Field(None, alias="totalCost")
    job_date: Optional[str] = Field(None, alias="jobDate")
    insurance_cost: Optional[float] = Field(None, alias="insuranceCost")
    carrier: Optional[str] = Field(None)
    intacct_date: Optional[str] = Field(None, alias="intacctDate")
    total_records: Optional[int] = Field(None, alias="totalRecords")


class InsuranceReportRequest(ABConnectBaseModel):
    """InsuranceReportRequest model"""

    page_size: int = Field(..., alias="pageSize")
    page_no: int = Field(..., alias="pageNo")
    total_count: Optional[int] = Field(None, alias="totalCount")
    sort_by: SortBy = Field(..., alias="sortBy")
    start_date: Optional[datetime] = Field(None, alias="startDate")
    end_date: Optional[datetime] = Field(None, alias="endDate")


class ReferredByReport(ABConnectBaseModel):
    """ReferredByReport model"""

    referred_by: Optional[str] = Field(None, alias="referredBy")
    referred_name: Optional[str] = Field(None, alias="referredName")
    referred_by_category: Optional[str] = Field(None, alias="referredByCategory")
    quote_date: Optional[str] = Field(None, alias="quoteDate")
    booked_date: Optional[str] = Field(None, alias="bookedDate")
    revenue: Optional[float] = Field(None)
    profit: Optional[float] = Field(None)
    customer: Optional[str] = Field(None)
    job_display_id: Optional[int] = Field(None, alias="jobDisplayId")
    industry: Optional[str] = Field(None)
    customer_zip_code: Optional[str] = Field(None, alias="customerZipCode")
    intacct_date: Optional[str] = Field(None, alias="intacctDate")
    total_records: Optional[int] = Field(None, alias="totalRecords")


class ReferredByReportRequest(ABConnectBaseModel):
    """ReferredByReportRequest model"""

    page_size: int = Field(..., alias="pageSize")
    page_no: int = Field(..., alias="pageNo")
    total_count: Optional[int] = Field(None, alias="totalCount")
    sort_by: SortBy = Field(..., alias="sortBy")
    include: Optional[str] = Field(None)
    referred_by: Optional[str] = Field(None, alias="referredBy")
    referred_name: Optional[str] = Field(None, alias="referredName")
    referred_by_category: Optional[str] = Field(None, alias="referredByCategory")
    franchisee: Optional[str] = Field(None)
    company_id: Optional[str] = Field(None, alias="companyId")
    user_id: Optional[str] = Field(None, alias="userId")
    start_date: str = Field(..., alias="startDate", min_length=1)
    end_date: str = Field(..., alias="endDate", min_length=1)


class RevenueCustomer(IdentifiedModel):
    """RevenueCustomer model"""

    name: Optional[str] = Field(None)


class SalesForecastReport(JobRelatedModel):
    """SalesForecastReport model"""

    franchisee: Optional[str] = Field(None)
    company: Optional[str] = Field(None)
    job_type: Optional[str] = Field(None, alias="jobType")
    quote_date: Optional[str] = Field(None, alias="quoteDate")
    booked_date: Optional[str] = Field(None, alias="bookedDate")
    revenue: Optional[float] = Field(None)
    profit: Optional[float] = Field(None)
    gross_margin: Optional[float] = Field(None, alias="grossMargin")
    status: Optional[str] = Field(None)
    industry: Optional[str] = Field(None)
    customer_zip_code: Optional[str] = Field(None, alias="customerZipCode")
    intacct_date: Optional[str] = Field(None, alias="intacctDate")
    total_records: Optional[int] = Field(None, alias="totalRecords")


class SalesForecastReportRequest(ABConnectBaseModel):
    """SalesForecastReportRequest model"""

    page_size: int = Field(..., alias="pageSize")
    page_no: int = Field(..., alias="pageNo")
    total_count: Optional[int] = Field(None, alias="totalCount")
    sort_by: SortBy = Field(..., alias="sortBy")
    start_date: str = Field(..., alias="startDate", min_length=1)
    end_date: str = Field(..., alias="endDate", min_length=1)
    franchisee: Optional[str] = Field(None)
    job_status: Optional[str] = Field(None, alias="jobStatus")
    user_id: Optional[str] = Field(None, alias="userId")


class SalesForecastSummary(ABConnectBaseModel):
    """SalesForecastSummary model"""

    revenue: Optional[float] = Field(None)
    profit: Optional[float] = Field(None)
    gross_margin: Optional[float] = Field(None, alias="grossMargin")
    close_ratio: Optional[float] = Field(None, alias="closeRatio")


class SalesForecastSummaryRequest(ABConnectBaseModel):
    """SalesForecastSummaryRequest model"""

    start_date: datetime = Field(..., alias="startDate")
    end_date: datetime = Field(..., alias="endDate")
    franchisee: Optional[str] = Field(None)
    job_status: Optional[str] = Field(None, alias="jobStatus")
    user_id: Optional[str] = Field(None, alias="userId")


class Web2LeadReport(CompanyRelatedModel):
    """Web2LeadReport model"""

    franchisee_id: Optional[str] = Field(None, alias="franchiseeId")
    type: Optional[str] = Field(None)
    job_display_id: Optional[str] = Field(None, alias="jobDisplayId")
    intacct_status: Optional[str] = Field(None, alias="intacctStatus")
    lead_date: Optional[str] = Field(None, alias="leadDate")
    refer_page: Optional[str] = Field(None, alias="referPage")
    entry_url: Optional[str] = Field(None, alias="entryUrl")
    submission_page: Optional[str] = Field(None, alias="submissionPage")
    how_heard: Optional[str] = Field(None, alias="howHeard")
    email: Optional[str] = Field(None)
    phone: Optional[str] = Field(None)
    ship_from: Optional[str] = Field(None, alias="shipFrom")
    ship_to: Optional[str] = Field(None, alias="shipTo")
    referred_name: Optional[str] = Field(None, alias="referredName")
    customer_comments: Optional[str] = Field(None, alias="customerComments")
    current_book_price: Optional[float] = Field(None, alias="currentBookPrice")
    current_book_profit: Optional[float] = Field(None, alias="currentBookProfit")
    referred_by_category: Optional[str] = Field(None, alias="referredByCategory")
    total_records: Optional[int] = Field(None, alias="totalRecords")


class Web2LeadRevenueFilter(ABConnectBaseModel):
    """Web2LeadRevenueFilter model"""

    user_id: Optional[str] = Field(None, alias="userId")
    start_date: Optional[datetime] = Field(None, alias="startDate")
    end_date: Optional[datetime] = Field(None, alias="endDate")
    reffered_by: Optional[str] = Field(None, alias="refferedBy")
    reffered_categories: Optional[str] = Field(None, alias="refferedCategories")
    franchisees: Optional[str] = Field(None)
    industry_types: Optional[str] = Field(None, alias="industryTypes")
    customers: Optional[str] = Field(None)
    sales_reps: Optional[str] = Field(None, alias="salesReps")
    job_statuses: Optional[str] = Field(None, alias="jobStatuses")
    paid_statuses: Optional[str] = Field(None, alias="paidStatuses")
    ppc_campaigns: Optional[str] = Field(None, alias="ppcCampaigns")
    commodity_categories: Optional[str] = Field(None, alias="commodityCategories")
    split_by: Optional[str] = Field(None, alias="splitBy")
    count_customers: Optional[int] = Field(None, alias="countCustomers")
    top_count_sales_reps: Optional[int] = Field(None, alias="topCountSalesReps")
    groupby_date: Optional[RangeDateEnum] = Field(None, alias="groupbyDate")


class Web2LeadV2RequestModel(CompanyRelatedModel):
    """Web2LeadV2RequestModel model"""

    page_size: int = Field(..., alias="pageSize")
    page_no: int = Field(..., alias="pageNo")
    total_count: Optional[int] = Field(None, alias="totalCount")
    sort_by: SortBy = Field(..., alias="sortBy")
    start_date: datetime = Field(..., alias="startDate")
    end_date: datetime = Field(..., alias="endDate")
    franchisee_id: Optional[str] = Field(None, alias="franchiseeId")
    referred_by_category_id: Optional[str] = Field(None, alias="referredByCategoryId")
    referred_by_id: Optional[str] = Field(None, alias="referredById")
    search_terms: Optional[str] = Field(None, alias="searchTerms")
    user_id: Optional[str] = Field(None, alias="userId")


__all__ = ['InsuranceReport', 'InsuranceReportRequest', 'ReferredByReport', 'ReferredByReportRequest', 'RevenueCustomer', 'SalesForecastReport', 'SalesForecastReportRequest', 'SalesForecastSummary', 'SalesForecastSummaryRequest', 'Web2LeadReport', 'Web2LeadRevenueFilter', 'Web2LeadV2RequestModel']
