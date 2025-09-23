"""ABConnect API endpoints package.

Auto-generated from swagger.json specification.
Contains endpoint classes for all API modules.
"""

from .base import BaseEndpoint

from .SmsTemplate import SmstemplateEndpoint
from .Values import ValuesEndpoint
from .account import AccountEndpoint
from .address import AddressEndpoint
from .admin import AdminEndpoint
from .companies import CompaniesEndpoint
from .company import CompanyEndpoint
from .contacts import ContactsEndpoint
from .dashboard import DashboardEndpoint
from .documents import DocumentsEndpoint
from .e_sign import ESignEndpoint
from .email import EmailEndpoint
from .jobintacct import JobintacctEndpoint
from .lookup import LookupEndpoint
from .note import NoteEndpoint
from .notifications import NotificationsEndpoint
from .reports import ReportsEndpoint
from .rfq import RfqEndpoint
from .shipment import ShipmentEndpoint
from .users import UsersEndpoint
from .v2 import V2Endpoint
from .v3 import V3Endpoint
from .views import ViewsEndpoint
from .webhooks import WebhooksEndpoint

# Export all endpoint classes
__all__ = [
    "BaseEndpoint",
    "SmstemplateEndpoint",
    "ValuesEndpoint",
    "AccountEndpoint",
    "AddressEndpoint",
    "AdminEndpoint",
    "CompaniesEndpoint",
    "CompanyEndpoint",
    "ContactsEndpoint",
    "DashboardEndpoint",
    "DocumentsEndpoint",
    "ESignEndpoint",
    "EmailEndpoint",
    "JobintacctEndpoint",
    "LookupEndpoint",
    "NoteEndpoint",
    "NotificationsEndpoint",
    "ReportsEndpoint",
    "RfqEndpoint",
    "ShipmentEndpoint",
    "UsersEndpoint",
    "V2Endpoint",
    "V3Endpoint",
    "ViewsEndpoint",
    "WebhooksEndpoint",
]
