from ABConnect.api import ABConnectAPI
from _helpers import save_fixture
from _constants import VIEW_ID, COMPANY_ID

api = ABConnectAPI(username='instaquote')
# Get dashboard data
dashboard_data = api.dashboard.get(view_id=VIEW_ID, company_id=COMPANY_ID)
print(f"Dashboard data type: {type(dashboard_data)}")
save_fixture(dashboard_data, "DashboardData")