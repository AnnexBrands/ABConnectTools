"""Contacts API endpoints.

Auto-generated from swagger.json specification.
Provides type-safe access to contacts/* endpoints.
"""

from typing import List, Optional

from ABConnect.api.endpoints.base import BaseEndpoint
from ABConnect.api import models
from ABConnect.api.routes import SCHEMA


class ContactsEndpoint(BaseEndpoint):
    """Contacts API endpoint operations.

    Handles all API operations for /api/contacts/* endpoints.
    Total endpoints: 14
    """

    api_path = "contacts"
    routes = SCHEMA["CONTACTS"]

    def post_history(self, contactId: str, data: dict = None) -> dict:
        """POST /api/contacts/{contactId}/history

        Returns:
            dict: API response data
        """
        route = self.routes["HISTORY"]
        route.params = {"contactId": contactId}
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def get_history_aggregated(
        self, contactId: str, statuses: Optional[str] = None
    ) -> dict:
        """GET /api/contacts/{contactId}/history/aggregated

        Returns:
            dict: API response data
        """
        route = self.routes["HISTORY_AGGREGATED"]
        route.params = {"contactId": contactId}
        if statuses is not None:
            route.params["statuses"] = statuses
        return self._make_request(route)

    def get_history_graphdata(
        self, contactId: str, statuses: Optional[str] = None
    ) -> dict:
        """GET /api/contacts/{contactId}/history/graphdata

        Returns:
            dict: API response data
        """
        route = self.routes["HISTORY_GRAPHDATA"]
        route.params = {"contactId": contactId}
        if statuses is not None:
            route.params["statuses"] = statuses
        return self._make_request(route)

    def post_merge_preview(self, mergeToId: str, data: dict = None) -> dict:
        """POST /api/contacts/{mergeToId}/merge/preview

        Returns:
            dict: API response data
        """
        route = self.routes["MERGE_PREVIEW"]
        route.params = {"mergeToId": mergeToId}
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def put_merge(self, mergeToId: str, data: dict = None) -> dict:
        """PUT /api/contacts/{mergeToId}/merge

        Returns:
            dict: API response data
        """
        route = self.routes["MERGE"]
        route.params = {"mergeToId": mergeToId}
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def get(self, id: str) -> models.ContactDetails:
        """GET /api/contacts/{id}

        Retrieves contact details by ID.

        Args:
            id: Contact ID (GUID string)

        Returns:
            ContactDetails: Typed contact details model
        """
        route = self.routes['GET']
        route.params = {"id": id}
        return self._make_request(route)

    def get_ah(self, houseid, *args, **kwargs) -> dict:
        id = self.get_cache(houseid)
        return self.get(id)

    def get_user(self) -> dict:
        """GET /api/contacts/user

        Returns the current logged-in user's contact info.

        Returns:
            dict: Contact info for current user
        """
        route = self.routes['USER']
        return self._make_request(route)

    def get_editdetails(self, contactId: str) -> dict:
        """GET /api/contacts/{contactId}/editdetails

        Returns:
            dict: API response data
        """
        route = self.routes["GET_EDITDETAILS"]
        route.params = {"contactId": contactId}
        return self._make_request(route)

    def put_editdetails(
        self, contactId: str, franchisee_id: Optional[str] = None, data: dict = None
    ) -> dict:
        """PUT /api/contacts/{contactId}/editdetails

        Returns:
            dict: API response data
        """
        route = self.routes["PUT_EDITDETAILS"]
        route.params = {"contactId": contactId}
        if franchisee_id is not None:
            route.params["franchiseeId"] = franchisee_id
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def post_editdetails(
        self, franchisee_id: Optional[str] = None, data: dict = None
    ) -> dict:
        """POST /api/contacts/editdetails

        Returns:
            dict: API response data
        """
        route = self.routes["POST_EDITDETAILS"]
        if franchisee_id is not None:
            route.params = {"franchiseeId": franchisee_id}
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def post_search(self, company_id: Optional[str] = None, data: dict = None) -> dict:
        """POST /api/contacts/search

        Returns:
            dict: API response data
        """
        route = self.routes["SEARCH"]
        if company_id is not None:
            route.params = {"companyId": company_id}
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def post_v2_search(self, data: dict = None) -> List[dict]:
        """POST /api/contacts/v2/search

        Returns:
            dict: API response data
        """
        route = self.routes["V2_SEARCH"]
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def post_customers(self, data: dict = None) -> dict:
        """POST /api/contacts/customers

        Returns:
            dict: API response data
        """
        route = self.routes["CUSTOMERS"]
        kwargs = {}
        if data is not None:
            kwargs["json"] = data
        return self._make_request(route, **kwargs)

    def get_primarydetails(self, contactId: str) -> dict:
        """GET /api/contacts/{contactId}/primarydetails

        Returns:
            dict: API response data
        """
        route = self.routes["PRIMARYDETAILS"]
        route.params = {"contactId": contactId}
        return self._make_request(route)

    def get_did(self, displayId):
        id = self.get_cache(displayId)
        return self.get_get(id)
