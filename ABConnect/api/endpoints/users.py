from .base import BaseEndpoint


class UsersEndpoint(BaseEndpoint):
    def me(self):
        return self._r.call("GET", "/account/profile")

    def access_companies(self):
        return self._r.call("GET", "companies/availableByCurrentUser")
