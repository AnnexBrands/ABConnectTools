import pytest


# Account tests
@pytest.mark.integration
def test_get_profile(api):
    """server returns account profile"""
    profile = api.account.get_profile()
    assert isinstance(profile, dict), "api.account.get_profile should return a dict"


def test_profile_fixture(AccountProfileData):
    """fixture has expected structure"""
    assert isinstance(AccountProfileData, dict), "AccountProfile fixture should be a dict"


# Dashboard tests
@pytest.mark.integration
def test_get_dashboard(api):
    """server returns dashboard data"""
    dashboard = api.dashboard.get()
    assert isinstance(dashboard, dict), "api.dashboard.get should return a dict"


def test_dashboard_fixture(DashboardData):
    """fixture has expected structure"""
    assert isinstance(DashboardData, dict), "Dashboard fixture should be a dict"


@pytest.mark.integration
def test_get_gridviews(api):
    """server returns gridviews"""
    gridviews = api.dashboard.get_gridviews()
    assert isinstance(gridviews, list), "api.dashboard.get_gridviews should return a list"


def test_gridviews_fixture(DashboardGridViewsData):
    """fixture has expected structure"""
    assert isinstance(DashboardGridViewsData, list), "DashboardGridViews fixture should be a list"


# Partner tests
@pytest.mark.integration
def test_get_partner_list(api):
    """server returns partner list"""
    partners = api.partner.get_list()
    assert isinstance(partners, list), "api.partner.get_list should return a list"


def test_partner_list_fixture(PartnerListData):
    """fixture has expected structure"""
    assert isinstance(PartnerListData, list), "PartnerList fixture should be a list"


# Shipment tests
@pytest.mark.integration
def test_get_accessorials(api):
    """server returns shipment accessorials"""
    accessorials = api.shipment.get_accessorials()
    assert isinstance(accessorials, list), "api.shipment.get_accessorials should return a list"


def test_accessorials_fixture(ShipmentAccessorialsData):
    """fixture has expected structure"""
    assert isinstance(ShipmentAccessorialsData, list), "ShipmentAccessorials fixture should be a list"


# Users tests
@pytest.mark.integration
def test_get_pocusers(api):
    """server returns POC users"""
    pocusers = api.users.get_pocusers()
    assert isinstance(pocusers, list), "api.users.get_pocusers should return a list"


def test_pocusers_fixture(UsersPocUsersData):
    """fixture has expected structure"""
    assert isinstance(UsersPocUsersData, list), "UsersPocUsers fixture should be a list"


@pytest.mark.integration
def test_get_roles(api):
    """server returns user roles"""
    roles = api.users.get_roles()
    assert isinstance(roles, list), "api.users.get_roles should return a list"


def test_roles_fixture(UsersRolesData):
    """fixture has expected structure"""
    assert isinstance(UsersRolesData, list), "UsersRoles fixture should be a list"


# Views tests
@pytest.mark.integration
def test_get_views_all(api):
    """server returns all views"""
    views = api.views.get_all()
    assert isinstance(views, list), "api.views.get_all should return a list"


def test_views_all_fixture(ViewsAllData):
    """fixture has expected structure"""
    assert isinstance(ViewsAllData, list), "ViewsAll fixture should be a list"


@pytest.mark.integration
def test_get_datasetsps(api):
    """server returns dataset stored procedures"""
    datasetsps = api.views.get_datasetsps()
    assert isinstance(datasetsps, list), "api.views.get_datasetsps should return a list"


def test_datasetsps_fixture(ViewsDatasetSpsData):
    """fixture has expected structure"""
    assert isinstance(ViewsDatasetSpsData, list), "ViewsDatasetSps fixture should be a list"


# Notifications tests
@pytest.mark.integration
def test_get_notifications(api):
    """server returns notifications"""
    notifications = api.notifications.get_get()
    assert isinstance(notifications, dict), "api.notifications.get_get should return a dict"


def test_notifications_fixture(NotificationsData):
    """fixture has expected structure"""
    assert isinstance(NotificationsData, dict), "Notifications fixture should be a dict"


# Values tests
@pytest.mark.integration
def test_get_values(api):
    """server returns values"""
    values = api.values.get_get()
    assert isinstance(values, dict), "api.values.get_get should return a dict"


def test_values_fixture(ValuesData):
    """fixture has expected structure"""
    assert isinstance(ValuesData, dict), "Values fixture should be a dict"
