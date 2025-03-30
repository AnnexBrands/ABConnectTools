from ABConnect.api.endpoints.base import BaseEndpoint


class ContactsEndpoint(BaseEndpoint):
    def get(self, id) -> dict:
        return self._r.call("GET", f"contacts/{id}")
