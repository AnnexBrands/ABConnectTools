"""Account models for ABConnect API."""

from typing import Optional
from pydantic import Field
from .base import ABConnectBaseModel
from .enums import ForgotType

class ChangePasswordModel(ABConnectBaseModel):
    """ChangePasswordModel model"""

    old_password: str = Field(..., alias="oldPassword", min_length=1)
    new_password: str = Field(..., alias="newPassword", min_length=1)
    confirm_password: str = Field(..., alias="confirmPassword", min_length=1)


class ConfirmEmailModel(ABConnectBaseModel):
    """ConfirmEmailModel model"""

    user_name: Optional[str] = Field(None, alias="userName")
    token: Optional[str] = Field(None)


class ForgotLoginModel(ABConnectBaseModel):
    """ForgotLoginModel model"""

    user_name: Optional[str] = Field(None, alias="userName")
    email: Optional[str] = Field(None)
    forgot_type: Optional[ForgotType] = Field(None, alias="forgotType")


class RegistrationModel(ABConnectBaseModel):
    """RegistrationModel model"""

    user_name: str = Field(..., alias="userName", min_length=1)
    password: str = Field(..., min_length=4, max_length=100)
    confirm_password: Optional[str] = Field(None, alias="confirmPassword")
    full_name: str = Field(..., alias="fullName", min_length=1)
    email: str = Field(..., min_length=1)
    key: Optional[str] = Field(None)
    source_job_display_id: Optional[str] = Field(None, alias="sourceJobDisplayId")


class ResetPasswordModel(ABConnectBaseModel):
    """ResetPasswordModel model"""

    user_name: str = Field(..., alias="userName", min_length=1)
    token: str = Field(..., min_length=1)
    password: str = Field(..., min_length=1)
    confirm_password: str = Field(..., alias="confirmPassword", min_length=1)


__all__ = ['ChangePasswordModel', 'ConfirmEmailModel', 'ForgotLoginModel', 'RegistrationModel', 'ResetPasswordModel']
