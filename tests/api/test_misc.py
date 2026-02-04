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


# ==============================================================================
# Dashboard parameterized tests (Commit 6)
# ==============================================================================

@pytest.mark.integration
def test_get_gridviewstate(api):
    """get_gridviewstate returns a specific grid view state"""
    from tests.constants import VIEW_ID
    result = api.dashboard.get_gridviewstate(str(VIEW_ID))
    assert result is not None


# ==============================================================================
# Account xfail tests (Commit 7)
# ==============================================================================

@pytest.mark.integration
@pytest.mark.xfail(reason=(
    "Human: Auth-modifying operation. POST /account/confirm requires "
    "ConfirmEmailModel data. Do NOT test against staging without confirmation."
))
def test_account_confirm(api):
    """post_confirm confirms an email"""
    result = api.account.post_confirm(data={})
    assert result is not None


@pytest.mark.integration
@pytest.mark.xfail(reason=(
    "Human: Auth-modifying operation. POST /account/forgot requires "
    "ForgotLoginModel data. Do NOT test against staging."
))
def test_account_forgot(api):
    """post_forgot sends a forgot password/username request"""
    result = api.account.post_forgot(data={})
    assert result is not None


# ==============================================================================
# Users xfail tests (Commit 8)
# ==============================================================================

@pytest.mark.integration
@pytest.mark.xfail(reason=(
    "Human: POST /users/list requires WebApiDataSourceLoadOptions data. "
    "Inspect the swagger schema for required fields."
))
def test_users_list(api):
    """users list returns filtered users"""
    result = api.users.post_list(data={})
    assert result is not None


@pytest.mark.integration
@pytest.mark.xfail(reason=(
    "Human: POST /users/user requires CreateUserModel data. "
    "This creates a user — do NOT test against staging without confirmation."
))
def test_users_create(api):
    """post_user creates a new user"""
    result = api.users.post_user(data={})
    assert result is not None


# ==============================================================================
# Partner xfail tests (Commit 35)
# ==============================================================================

@pytest.mark.integration
@pytest.mark.xfail(reason=(
    "Human: POST /partner/search requires search parameters. "
    "Inspect swagger for PartnerSearchRequest schema."
))
def test_partner_search(api):
    """partner search returns matching partners"""
    result = api.partner.post_search(data={})
    assert result is not None


# ==============================================================================
# Shipment standalone tests (Commit 35)
# ==============================================================================

@pytest.mark.integration
@pytest.mark.xfail(reason=(
    "Human: GET /shipment takes optional query params (franchisee_id, provider_id, pro_number). "
    "Try calling with known values to get a valid response."
))
def test_shipment_get(api):
    """get returns shipment details"""
    result = api.shipment.get_get()
    assert result is not None


@pytest.mark.integration
@pytest.mark.xfail(reason="Human: GET /shipment/document/{docId} needs a valid document ID.")
def test_shipment_document(api):
    """get_document returns a shipping document"""
    result = api.shipment.get_document("NEED_VALID_DOC_ID")
    assert result is not None
