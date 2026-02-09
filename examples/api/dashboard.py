"""
Dashboard API Examples - Retrieving dashboard data

Usage:
    python dashboard.py             # Run all examples
    python dashboard.py get         # Run a single example
    python dashboard.py help        # List available examples
"""

from _base import ExampleRunner
from _helpers import save_fixture
from _constants import VIEW_ID, COMPANY_ID


class DashboardExamples(ExampleRunner):
    def __init__(self):
        super().__init__("Dashboard API", api_kwargs=dict(username='instaquote'))
        self.add("get", "Get dashboard data by view and company", self.get_dashboard)

    def get_dashboard(self):
        dashboard_data = self.api.dashboard.get(view_id=VIEW_ID, company_id=COMPANY_ID)
        print(f"Dashboard data type: {type(dashboard_data)}")
        save_fixture(dashboard_data, "DashboardData")


if __name__ == "__main__":
    DashboardExamples().run()
