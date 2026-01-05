import pytest
from ABConnect.api import models


# Account tests
@pytest.mark.integration
def test_get_profile(api):
    """server returns account profile"""
    profile = api.account.get_profile()
    assert isinstance(profile, models.AccountProfile), "api.account.get_profile should return AccountProfile"


def test_profile_fixture(AccountProfileData):
    """fixture has expected structure"""
    models.AccountProfile.model_validate(AccountProfileData)


# Dashboard tests
@pytest.mark.integration
def test_get_dashboard(api):
    """server returns dashboard data"""
    dashboard = api.dashboard.get()
    models.DashboardResponse.model_validate(dashboard)


def test_dashboard_fixture(DashboardData):
    """fixture has expected structure"""
    models.DashboardResponse.model_validate(DashboardData)


@pytest.mark.integration
def test_get_gridviews(api):
    """server returns gridviews"""
    gridviews = api.dashboard.get_gridviews()
    [models.GridViewDetails.model_validate(item) for item in gridviews]


def test_gridviews_fixture(DashboardGridViewsData):
    """fixture has expected structure"""
    for item in DashboardGridViewsData:
        models.GridViewDetails.model_validate(item)


# Partner tests
@pytest.mark.integration
def test_get_partner_list(api, models):
    """server returns partner list"""
    partners = api.partner.get_list()
    [models.Partner.model_validate(partner) for partner in partners]


def test_partner_list_fixture(PartnerListData):
    """fixture has expected structure"""
    for item in PartnerListData:
        models.Partner.model_validate(item)


# Shipment tests
@pytest.mark.integration
def test_get_accessorials(api):
    """server returns shipment accessorials"""
    accessorials = api.shipment.get_accessorials()
    [models.ParcelAddOn.model_validate(item) for item in accessorials]


def test_accessorials_fixture(ShipmentAccessorialsData):
    """fixture has expected structure"""
    for item in ShipmentAccessorialsData:
        models.ParcelAddOn.model_validate(item)


# Users tests
@pytest.mark.integration
def test_get_pocusers(api):
    """server returns POC users"""
    pocusers = api.users.get_pocusers()
    [models.PocUser.model_validate(user) for user in pocusers]


def test_pocusers_fixture(UsersPocUsersData):
    """fixture has expected structure"""
    for item in UsersPocUsersData:
        models.PocUser.model_validate(item)


@pytest.mark.integration
def test_get_roles(api):
    """server returns user roles as list of strings"""
    roles = api.users.get_roles()
    assert isinstance(roles, list), "roles should be a list"
    assert all(isinstance(role, str) for role in roles), "all roles should be strings"


def test_roles_fixture(UsersRolesData):
    """fixture has expected structure - list of role name strings"""
    assert isinstance(UsersRolesData, list), "UsersRoles fixture should be a list"
    assert all(isinstance(role, str) for role in UsersRolesData), "all roles should be strings"


# Views tests
@pytest.mark.integration
def test_get_views_all(api):
    """server returns all views"""
    views = api.views.get_all()
    assert isinstance(views, list), "api.views.get_all should return a list"


def test_views_all_fixture(ViewsAllData):
    """fixture has expected structure"""
    for item in ViewsAllData:
        models.GridViewDetails.model_validate(item)


@pytest.mark.integration
def test_get_datasetsps(api):
    """server returns dataset stored procedures as list of strings"""
    datasetsps = api.views.get_datasetsps()
    assert isinstance(datasetsps, list), "datasetsps should be a list"
    assert all(isinstance(sp, str) for sp in datasetsps), "all stored procedures should be strings"


def test_datasetsps_fixture(ViewsDatasetSpsData):
    """fixture has expected structure - list of stored procedure name strings"""
    assert isinstance(ViewsDatasetSpsData, list), "ViewsDatasetSps fixture should be a list"
    assert all(isinstance(sp, str) for sp in ViewsDatasetSpsData), "all stored procedures should be strings"


# Notifications tests
@pytest.mark.integration
def test_get_notifications(api):
    """server returns notifications"""
    notifications = api.notifications.get_get()
    assert isinstance(notifications, models.NotificationsResponse), "should return NotificationsResponse"


def test_notifications_fixture(NotificationsData):
    """fixture has expected structure"""
    models.NotificationsResponse.model_validate(NotificationsData)


# Values tests
@pytest.mark.integration
def test_get_values(api):
    """server returns values"""
    values = api.values.get_get()
    assert isinstance(values, models.ValuesResponse), "should return ValuesResponse"


def test_values_fixture(ValuesData):
    """fixture has expected structure"""
    models.ValuesResponse.model_validate(ValuesData)
