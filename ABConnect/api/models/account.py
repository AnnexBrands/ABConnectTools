"""Account models for ABConnect API."""

from typing import Any, Dict, List, Optional
from pydantic import Field
from .base import ABConnectBaseModel
from .enums import ForgotType


class AccountProfile(ABConnectBaseModel):
    """Account profile model for GET /account/profile response.

    Contains the user's account information including contact details,
    social logins, and payment sources.
    """

    user_name: Optional[str] = Field(None, alias="userName")
    email: Optional[str] = Field(None)
    contact_info: Optional[Dict[str, Any]] = Field(None, alias="contactInfo")
    social_logins: Optional[List[Dict[str, Any]]] = Field(default_factory=list, alias="socialLogins")
    payment_sources: Optional[List[Dict[str, Any]]] = Field(default_factory=list, alias="paymentSources")

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
    """ 
        Model for initiating a forgot-username or forgot-password request.    
    
        example:
        ---------
        >>> from ABConnect.api import models
        >>> request = models.ForgotLoginModel(
        ...     user_name="training",
        ...     email="abconnect@annexbrands.com",
        ...     forgot_type=models.ForgotType.USERNAME
        ... )
        >>> response = abapi.account.post_forgot(request)
        >>> print(response.success)   # True if the request was processed
        >>> print(response.message)   # e.g., "No account found with that email"
    
    """

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


__all__ = ['AccountProfile', 'ChangePasswordModel', 'ConfirmEmailModel', 'ForgotLoginModel', 'RegistrationModel', 'ResetPasswordModel']
