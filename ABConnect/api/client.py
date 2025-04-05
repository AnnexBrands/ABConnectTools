from ABConnect.api.endpoints import (
    BaseEndpoint,
    CompaniesEndpoint,
    ContactsEndpoint,
    DocsEndpoint,
    FormsEndpoint,
    ItemsEndpoint,
    JobsEndpoint,
    TasksEndpoint,
    UsersEndpoint,
)

from .auth import FileTokenStorage, SessionTokenStorage
from .http import RequestHandler


class ABConnectAPI:
    def __init__(self, request=None):
        token_storage = (
            SessionTokenStorage(request) if request is None else FileTokenStorage()
        )

        BaseEndpoint.set_request_handler(RequestHandler(token_storage))

        self.users = UsersEndpoint()
        self.companies = CompaniesEndpoint()
        self.contacts = ContactsEndpoint()
        self.docs = DocsEndpoint()
        self.forms = FormsEndpoint()
        self.items = ItemsEndpoint()
        self.jobs = JobsEndpoint()
        self.tasks = TasksEndpoint()
