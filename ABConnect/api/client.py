from typing import Optional, Dict, Type, Any, List
import logging
import os

from ABConnect.config import Config
from ABConnect.api.endpoints import (
    BaseEndpoint,
    AccountEndpoint,
    AddressEndpoint,
    AdminEndpoint,
    CompaniesEndpoint,
    CompanyEndpoint,
    ContactsEndpoint,
    DashboardEndpoint,
    DocumentsEndpoint,
    ESignEndpoint,
    EmailEndpoint,
    JobintacctEndpoint,
    LookupEndpoint,
    NoteEndpoint,
    NotificationsEndpoint,
    ReportsEndpoint,
    RfqEndpoint,
    ShipmentEndpoint,
    SmstemplateEndpoint,
    UsersEndpoint,
    V2Endpoint,
    V3Endpoint,
    ValuesEndpoint,
    ViewsEndpoint,
    WebhooksEndpoint,
)
from ABConnect.api.endpoints.jobs import JobsPackage
from ABConnect.api.catalog import CatalogAPI

from .auth import FileTokenStorage, SessionTokenStorage
from .http_client import RequestHandler
# from .swagger import SwaggerParser
# from .builder import EndpointBuilder
# from .generic import GenericEndpoint
# from .raw import RawEndpoint
# from .tagged import TaggedResourceBuilder
# Friendly modules removed - using new schema-first approach

logger = logging.getLogger(__name__)


class ABConnectAPI:
    """ API client for ABConnect

    example usage:
    >>> from ABConnect import ABConnectAPI
    >>> abapi = ABConnectAPI(env='staging')
    >>> companies = abapi.companies.list()
    >>> print(companies)

    """

    def __init__(self, *args, **kwargs):
        """Initialize the API client."""
        
        env = kwargs.pop('env', 'prod')
        # if env:
        #     # If already loaded from a staging env file, don't reload from default
        #     if not (Config._loaded and ".staging" in Config._env_file):
        #         Config._loaded = False  # Force config reload
        #         Config.load()  # Reload with new environment

        if 'request' in kwargs:
            token_storage = SessionTokenStorage(**kwargs)
        else:
            token_storage = FileTokenStorage(**kwargs)

        self._token_storage = token_storage

        self._request_handler = RequestHandler(token_storage)
        BaseEndpoint.set_request_handler(self._request_handler)

        self._init_endpoints_()
        


    def _init_endpoints_(self):
        self.account = AccountEndpoint()
        self.address = AddressEndpoint()
        self.admin = AdminEndpoint()
        self.companies = CompaniesEndpoint()
        self.company = CompanyEndpoint()
        self.contacts = ContactsEndpoint()
        self.dashboard = DashboardEndpoint()
        self.documents = DocumentsEndpoint()
        self.e_sign = ESignEndpoint()
        self.email = EmailEndpoint()
        self.jobs = JobsPackage(self._request_handler)
        self.jobintacct = JobintacctEndpoint()
        self.lookup = LookupEndpoint()
        self.note = NoteEndpoint()
        self.notifications = NotificationsEndpoint()
        self.reports = ReportsEndpoint()
        self.rfq = RfqEndpoint()
        self.shipment = ShipmentEndpoint()
        self.sms_template = SmstemplateEndpoint()
        self.users = UsersEndpoint()
        self.v2 = V2Endpoint()
        self.v3 = V3Endpoint()
        self.values = ValuesEndpoint()
        self.views = ViewsEndpoint()
        self.webhooks = WebhooksEndpoint()
        # ALIASES
        self.docs = self.documents
        self.tasks = self.jobs.timeline
        self.forms = self.jobs.form

        self.catalog = CatalogAPI(self._token_storage)