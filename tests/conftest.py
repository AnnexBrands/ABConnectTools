"""Pytest configuration and fixtures for ABConnect tests."""

import pytest
from ABConnect import ABConnectAPI, models as _models
from ABConnect.routes import SCHEMA
import json
from pathlib import Path
fixtures = Path(__file__).parent / "fixtures"

def pytest_configure(config):
    """Register custom pytest markers."""
    config.addinivalue_line("markers", "integration: marks tests as integration tests (require API access)")
    config.addinivalue_line("markers", "slow: marks tests as slow running")


@pytest.fixture(scope="session")
def api():
    """Session-scoped ABConnectAPI instance for staging environment."""
    return ABConnectAPI(env='staging', username='instaquote')


@pytest.fixture(scope="session")
def models():
    """Provide ABConnect models module for isinstance checks in tests."""
    return _models

@pytest.fixture(scope="session")
def schema():
    return SCHEMA

@pytest.fixture
def ContactDetailsData():
    return json.loads((fixtures / "ContactDetails.json").read_text())


@pytest.fixture
def CompanySimpleData():
    return json.loads((fixtures / "CompanySimple.json").read_text())


@pytest.fixture
def ContactUserData():
    return json.loads((fixtures / "ContactUser.json").read_text())


@pytest.fixture
def CompanyBrandsData():
    return json.loads((fixtures / "CompanyBrands.json").read_text())


@pytest.fixture
def CompanyBrandsTreeData():
    return json.loads((fixtures / "CompanyBrandsTree.json").read_text())


@pytest.fixture
def CompanyAvailableByCurrentUserData():
    return json.loads((fixtures / "CompanyAvailableByCurrentUser.json").read_text())


@pytest.fixture
def SmsTemplateNotificationTokensData():
    return json.loads((fixtures / "SmsTemplateNotificationTokens.json").read_text())


@pytest.fixture
def SmsTemplateJobStatusesData():
    return json.loads((fixtures / "SmsTemplateJobStatuses.json").read_text())


@pytest.fixture
def SmsTemplateListData():
    return json.loads((fixtures / "SmsTemplateList.json").read_text())


@pytest.fixture
def LookupCountriesData():
    return json.loads((fixtures / "LookupCountries.json").read_text())


@pytest.fixture
def LookupContactTypesData():
    return json.loads((fixtures / "LookupContactTypes.json").read_text())


@pytest.fixture
def LookupDocumentTypesData():
    return json.loads((fixtures / "LookupDocumentTypes.json").read_text())


@pytest.fixture
def LookupAccessKeysData():
    return json.loads((fixtures / "LookupAccessKeys.json").read_text())


@pytest.fixture
def LookupDensityClassMapData():
    return json.loads((fixtures / "LookupDensityClassMap.json").read_text())


@pytest.fixture
def LookupParcelPackageTypesData():
    return json.loads((fixtures / "LookupParcelPackageTypes.json").read_text())


@pytest.fixture
def AccountProfileData():
    return json.loads((fixtures / "AccountProfile.json").read_text())


@pytest.fixture
def DashboardData():
    return json.loads((fixtures / "Dashboard.json").read_text())


@pytest.fixture
def DashboardGridViewsData():
    return json.loads((fixtures / "DashboardGridViews.json").read_text())


@pytest.fixture
def PartnerListData():
    return json.loads((fixtures / "PartnerList.json").read_text())


@pytest.fixture
def ShipmentAccessorialsData():
    return json.loads((fixtures / "ShipmentAccessorials.json").read_text())


@pytest.fixture
def UsersPocUsersData():
    return json.loads((fixtures / "UsersPocUsers.json").read_text())


@pytest.fixture
def UsersRolesData():
    return json.loads((fixtures / "UsersRoles.json").read_text())


@pytest.fixture
def ViewsAllData():
    return json.loads((fixtures / "ViewsAll.json").read_text())


@pytest.fixture
def ViewsDatasetSpsData():
    return json.loads((fixtures / "ViewsDatasetSps.json").read_text())


@pytest.fixture
def NotificationsData():
    return json.loads((fixtures / "Notifications.json").read_text())


@pytest.fixture
def ValuesData():
    return json.loads((fixtures / "Values.json").read_text())