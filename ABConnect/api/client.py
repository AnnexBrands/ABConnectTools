from .http import RequestHandler
from .auth import FileTokenStorage
from ABConnect.api.endpoints import (
    BaseEndpoint,
    ContactsEndpoint,
    CompaniesEndpoint,
    DocsEndpoint,
    FormsEndpoint,
    ItemsEndpoint,
    JobsEndpoint,
    TasksEndpoint,
    UsersEndpoint,
)


class ABConnectAPI:
    def __init__(self, token_storage=FileTokenStorage()):
        BaseEndpoint.set_request_handler(RequestHandler(token_storage))

        self.users = UsersEndpoint()
        self.companies = CompaniesEndpoint()
        self.contacts = ContactsEndpoint()
        self.docs = DocsEndpoint()
        self.forms = FormsEndpoint()
        self.items = ItemsEndpoint()
        self.jobs = JobsEndpoint()
        self.tasks = TasksEndpoint()
