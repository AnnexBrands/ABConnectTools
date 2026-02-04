import pytest
from tests.constants import CONTACT_ID


@pytest.mark.integration
def test_get_contact(api, models, schema):
    """server data validates against ContactDetails model"""
    ContactDetailsModelName = schema['CONTACTS']['GET'].response_model
    ContactDetailsClass = getattr(models, ContactDetailsModelName)
    contact = api.contacts.get(CONTACT_ID)
    ContactDetailsClass.model_validate(contact)


def test_contact_model(models, ContactDetailsData):
    models.ContactDetails.model_validate(ContactDetailsData)


@pytest.mark.integration
def test_get_user(api, models):
    """server returns current user contact info"""
    user = api.contacts.get_user()
    models.ContactUser.model_validate(user)


def test_contact_user_fixture(ContactUserData, models):
    """fixture has expected structure"""
    models.ContactUser.model_validate(ContactUserData)


# ==============================================================================
# Parameterized GETs using CONTACT_ID from constants
# ==============================================================================

@pytest.mark.integration
def test_get_editdetails(api):
    """get_editdetails returns contact edit details"""
    result = api.contacts.get_editdetails(CONTACT_ID)
    assert result is not None


@pytest.mark.integration
def test_get_primarydetails(api):
    """get_primarydetails returns primary contact details"""
    result = api.contacts.get_primarydetails(CONTACT_ID)
    assert result is not None


@pytest.mark.integration
def test_get_history_aggregated(api):
    """get_history_aggregated returns aggregated cost history"""
    result = api.contacts.get_history_aggregated(CONTACT_ID)
    assert result is not None


@pytest.mark.integration
def test_get_history_graphdata(api):
    """get_history_graphdata returns history graph data"""
    result = api.contacts.get_history_graphdata(CONTACT_ID)
    assert result is not None


# ==============================================================================
# Write operations — xfail
# ==============================================================================

@pytest.mark.integration
@pytest.mark.xfail(reason="Human: Write op. POST /contacts/search requires WebApiDataSourceLoadOptions.")
def test_search_contacts(api):
    """search returns matching contacts"""
    result = api.contacts.post_search(data={})
    assert result is not None


@pytest.mark.integration
@pytest.mark.xfail(reason="Human: Write op. POST /contacts/editdetails creates contact data.")
def test_post_editdetails(api):
    """post_editdetails creates contact details"""
    result = api.contacts.post_editdetails(data={})
    assert result is not None
