"""Users models for ABConnect API."""

from typing import List, Optional
from datetime import datetime
from pydantic import Field
from .base import ABConnectBaseModel, ActiveModel, IdentifiedModel, TimestampedModel


class PocUser(ABConnectBaseModel):
    """POC User model for GET /users/pocusers response.

    Simple model containing just id and name.
    """

    id: Optional[int] = Field(None)
    name: Optional[str] = Field(None)

class CreateUserModel(ActiveModel):
    """CreateUserModel model"""

    login: str = Field(..., min_length=1)
    contact_id: int = Field(..., alias="contactId")
    full_name: str = Field(..., alias="fullName", min_length=1)
    email: str = Field(..., min_length=1)
    email_confirmed: Optional[bool] = Field(None, alias="emailConfirmed")
    password: str = Field(..., min_length=1)
    lockout_date_utc: Optional[datetime] = Field(None, alias="lockoutDateUtc")
    lockout_enabled: Optional[bool] = Field(None, alias="lockoutEnabled")
    company_id: Optional[str] = Field(None, alias="companyId")
    role: str = Field(..., min_length=1)


class UserInfo(IdentifiedModel):
    """UserInfo model"""

    login: Optional[str] = Field(None)
    full_name: Optional[str] = Field(None, alias="fullName")
    contact_id: Optional[int] = Field(None, alias="contactId")
    contact_display_id: Optional[str] = Field(None, alias="contactDisplayId")
    contact_company_name: Optional[str] = Field(None, alias="contactCompanyName")
    contact_company_id: Optional[str] = Field(None, alias="contactCompanyId")
    contact_company_display_id: Optional[str] = Field(None, alias="contactCompanyDisplayId")
    email: Optional[str] = Field(None)
    email_confirmed: Optional[bool] = Field(None, alias="emailConfirmed")
    contact_phone: Optional[str] = Field(None, alias="contactPhone")
    contact_email: Optional[str] = Field(None, alias="contactEmail")
    password: Optional[str] = Field(None)
    lockout_date_utc: Optional[datetime] = Field(None, alias="lockoutDateUtc")
    lockout_enabled: Optional[bool] = Field(None, alias="lockoutEnabled")
    role: Optional[str] = Field(None)
    is_active: Optional[bool] = Field(None, alias="isActive")
    legacy_id: Optional[str] = Field(None, alias="legacyId")
    additional_user_companies: Optional[List[str]] = Field(None, alias="additionalUserCompanies")
    additional_user_companies_names: Optional[List[str]] = Field(None, alias="additionalUserCompaniesNames")
    crm_contact_id: Optional[int] = Field(None, alias="crmContactId")


class Users(TimestampedModel):
    """Users model"""

    row_id: Optional[int] = Field(None, alias="rowId")
    total_rows: Optional[int] = Field(None, alias="totalRows")
    user_name: Optional[str] = Field(None, alias="userName")
    password: Optional[str] = Field(None)
    user_expiration_date: Optional[datetime] = Field(None, alias="userExpirationDate")
    dashboard_user_id: Optional[str] = Field(None, alias="dashboardUserId")
    company_id: Optional[str] = Field(None, alias="companyId")
    has_access: Optional[bool] = Field(None, alias="hasAccess")
    is_active: Optional[bool] = Field(None, alias="isActive")
    dashboard_id: Optional[str] = Field(None, alias="dashboardId")
    results: Optional[str] = Field(None)
    role_id: Optional[str] = Field(None, alias="roleId")
    user_company_id: Optional[str] = Field(None, alias="userCompanyId")
    company_type: Optional[str] = Field(None, alias="companyType")
    corporate_company_id: Optional[str] = Field(None, alias="corporateCompanyId")
    usersystem_log_id: Optional[int] = Field(None, alias="usersystemLogId")
    ip_address: Optional[str] = Field(None, alias="ipAddress")
    user_id: Optional[str] = Field(None, alias="userId")
    login_time: Optional[datetime] = Field(None, alias="loginTime")
    logout_time: Optional[datetime] = Field(None, alias="logoutTime")
    create_by: Optional[str] = Field(None, alias="createBy")
    company_name: Optional[str] = Field(None, alias="companyName")
    company_code: Optional[str] = Field(None, alias="companyCode")
    name: Optional[str] = Field(None)
    from_date: Optional[datetime] = Field(None, alias="fromDate")
    to_date: Optional[datetime] = Field(None, alias="toDate")
    sorting_direction: Optional[str] = Field(None, alias="sortingDirection")
    sorting_by: Optional[str] = Field(None, alias="sortingBy")
    page_size: Optional[int] = Field(None, alias="pageSize")
    page_number: Optional[int] = Field(None, alias="pageNumber")
    country_name: Optional[str] = Field(None, alias="countryName")
    pricing_to_use: Optional[str] = Field(None, alias="pricingToUse")
    parent_company_id: Optional[str] = Field(None, alias="parentCompanyId")
    crm_contact_id: Optional[int] = Field(None, alias="crmContactId")


__all__ = ['CreateUserModel', 'PocUser', 'UserInfo', 'Users']
