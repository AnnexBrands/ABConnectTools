"""
Miscellaneous API Examples - Various endpoints without path parameters

This example demonstrates getting data from various endpoints.

Usage:
    python misc_endpoints.py            # Run all examples
    python misc_endpoints.py profile    # Run a single example
    python misc_endpoints.py help       # List available examples
"""

from _base import ExampleRunner
from _helpers import save_fixture


def to_serializable(obj):
    """Convert Pydantic models or lists of models to dicts."""
    if isinstance(obj, list):
        return [to_serializable(item) for item in obj]
    if hasattr(obj, 'model_dump'):
        return obj.model_dump(by_alias=True)
    return obj


class MiscExamples(ExampleRunner):
    def __init__(self):
        super().__init__("Miscellaneous API", api_kwargs=dict(env='staging', username='instaquote'))
        self.add("profile", "Account profile", self.account_profile)
        self.add("dashboard", "Dashboard data", self.dashboard)
        self.add("gridviews", "Dashboard grid views", self.gridviews)
        self.add("partners", "Partner list", self.partners)
        self.add("accessorials", "Shipment accessorials", self.accessorials)
        self.add("pocusers", "POC users", self.pocusers)
        self.add("roles", "User roles", self.roles)
        self.add("views_all", "All views", self.views_all)
        self.add("datasetsps", "Views dataset SPs", self.datasetsps)
        self.add("notifications", "Notifications", self.notifications)
        self.add("values", "Values", self.values)

    def _fetch(self, label, call, fixture_name):
        result = call()
        print(f"{label} type: {type(result)}")
        if isinstance(result, list):
            print(f"{label} count: {len(result)}")
        save_fixture(to_serializable(result), fixture_name)

    def account_profile(self):
        self._fetch("Account profile", self.api.account.get_profile, "AccountProfile")

    def dashboard(self):
        self._fetch("Dashboard", self.api.dashboard.get, "Dashboard")

    def gridviews(self):
        self._fetch("Dashboard gridviews", self.api.dashboard.get_gridviews, "DashboardGridViews")

    def partners(self):
        self._fetch("Partners", self.api.partner.get_list, "PartnerList")

    def accessorials(self):
        self._fetch("Shipment accessorials", self.api.shipment.get_accessorials, "ShipmentAccessorials")

    def pocusers(self):
        self._fetch("POC users", self.api.users.get_pocusers, "UsersPocUsers")

    def roles(self):
        self._fetch("User roles", self.api.users.get_roles, "UsersRoles")

    def views_all(self):
        self._fetch("Views all", self.api.views.get_all, "ViewsAll")

    def datasetsps(self):
        self._fetch("Views datasetsps", self.api.views.get_datasetsps, "ViewsDatasetSps")

    def notifications(self):
        self._fetch("Notifications", self.api.notifications.get_get, "Notifications")

    def values(self):
        self._fetch("Values", self.api.values.get_get, "Values")


if __name__ == "__main__":
    MiscExamples().run()
