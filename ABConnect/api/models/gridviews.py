"""Gridviews models for ABConnect API."""

from __future__ import annotations
from typing import List, Optional
from pydantic import Field
from .base import IdentifiedModel
from .shared import StoredProcedureColumn

class GridViewAccess(IdentifiedModel):
    """GridViewAccess model"""

    company_id: Optional[str] = Field(None, alias="companyId")
    role_id: Optional[int] = Field(None, alias="roleId")
    user_id: Optional[int] = Field(None, alias="userId")
    company_name: Optional[str] = Field(None, alias="companyName")
    role_name: Optional[str] = Field(None, alias="roleName")
    user_login: Optional[str] = Field(None, alias="userLogin")
    user_email: Optional[str] = Field(None, alias="userEmail")


class GridViewDetails(IdentifiedModel):
    """GridViewDetails model"""

    name: Optional[str] = Field(None)
    data_key: Optional[str] = Field(None, alias="dataKey")
    is_active: Optional[bool] = Field(None, alias="isActive")
    stored_procedure: Optional[str] = Field(None, alias="storedProcedure")
    columns_specification: Optional[str] = Field(None, alias="columnsSpecification")
    sp_columns: Optional[List[StoredProcedureColumn]] = Field(None, alias="spColumns")


__all__ = ['GridViewAccess', 'GridViewDetails']
