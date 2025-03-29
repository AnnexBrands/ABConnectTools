from .http import RequestHandler
from .auth import FileTokenStorage
from .endpoints.users import UsersEndpoint

class ABConnectAPI:
    def __init__(self, token_storage=None):
        if token_storage is None:
            token_storage = FileTokenStorage()
        self.token_storage = token_storage

        self.request_handler = RequestHandler(token_storage)

        self.users = UsersEndpoint(self.request_handler)