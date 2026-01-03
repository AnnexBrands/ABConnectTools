"""
Miscellaneous API Examples - Various endpoints without path parameters

This example demonstrates getting data from various endpoints.
"""

from ABConnect.api import ABConnectAPI
from _helpers import save_fixture


def to_serializable(obj):
    """Convert Pydantic models or lists of models to dicts."""
    if isinstance(obj, list):
        return [to_serializable(item) for item in obj]
    if hasattr(obj, 'model_dump'):
        return obj.model_dump(by_alias=True)
    return obj


api = ABConnectAPI(env='staging', username='instaquote')

# Account - GET_PROFILE
try:
    profile = api.account.get_profile()
    print(f"Account profile type: {type(profile)}")
    save_fixture(to_serializable(profile), "AccountProfile")
except Exception as e:
    print(f"Account profile failed: {e}")

# Dashboard - GET
try:
    dashboard = api.dashboard.get()
    print(f"Dashboard type: {type(dashboard)}")
    save_fixture(to_serializable(dashboard), "Dashboard")
except Exception as e:
    print(f"Dashboard failed: {e}")

# Dashboard - GRIDVIEWS
try:
    gridviews = api.dashboard.get_gridviews()
    print(f"Dashboard gridviews type: {type(gridviews)}")
    save_fixture(to_serializable(gridviews), "DashboardGridViews")
except Exception as e:
    print(f"Dashboard gridviews failed: {e}")

# Partner - GET
try:
    partners = api.partner.get_list()
    print(f"Partners type: {type(partners)}")
    print(f"Partners count: {len(partners) if isinstance(partners, list) else 'N/A'}")
    save_fixture(to_serializable(partners), "PartnerList")
except Exception as e:
    print(f"Partner list failed: {e}")

# Shipment - ACCESSORIALS
try:
    accessorials = api.shipment.get_accessorials()
    print(f"Shipment accessorials type: {type(accessorials)}")
    save_fixture(to_serializable(accessorials), "ShipmentAccessorials")
except Exception as e:
    print(f"Shipment accessorials failed: {e}")

# Users - POCUSERS
try:
    pocusers = api.users.get_pocusers()
    print(f"POC users type: {type(pocusers)}")
    save_fixture(to_serializable(pocusers), "UsersPocUsers")
except Exception as e:
    print(f"POC users failed: {e}")

# Users - ROLES
try:
    roles = api.users.get_roles()
    print(f"User roles type: {type(roles)}")
    save_fixture(to_serializable(roles), "UsersRoles")
except Exception as e:
    print(f"User roles failed: {e}")

# Views - ALL
try:
    views = api.views.get_all()
    print(f"Views all type: {type(views)}")
    save_fixture(to_serializable(views), "ViewsAll")
except Exception as e:
    print(f"Views all failed: {e}")

# Views - DATASETSPS
try:
    datasetsps = api.views.get_datasetsps()
    print(f"Views datasetsps type: {type(datasetsps)}")
    save_fixture(to_serializable(datasetsps), "ViewsDatasetSps")
except Exception as e:
    print(f"Views datasetsps failed: {e}")

# Notifications - GET
try:
    notifications = api.notifications.get_get()
    print(f"Notifications type: {type(notifications)}")
    save_fixture(to_serializable(notifications), "Notifications")
except Exception as e:
    print(f"Notifications failed: {e}")

# Values - GET
try:
    values = api.values.get_get()
    print(f"Values type: {type(values)}")
    save_fixture(to_serializable(values), "Values")
except Exception as e:
    print(f"Values failed: {e}")

print("\nDone!")
