import pytest

@pytest.mark.integration
def test_get_contact(api, models, schema):
    """server data validates against ContactDetails model"""
    ContactDetailsModelName = schema['CONTACTS']['GET'].response_model
    ContactDetailsClass = getattr(models, ContactDetailsModelName)
    contact = api.contacts.get(266841)
    assert isinstance(contact, ContactDetailsClass), "api.contacts.get should return a ContactDetails instance"
    assert isinstance(contact.addresses_list[0].address.coordinates, models.LatLng), "Address coordinates should be a LatLng instance"

def test_contact_model(models, ContactDetailsData):
    models.ContactDetails.model_validate(ContactDetailsData)


@pytest.mark.integration
def test_get_user(api):
    """server returns current user contact info"""
    user = api.contacts.get_user()
    assert isinstance(user, dict), "api.contacts.get_user should return user info"
    assert "fullName" in user or "companyId" in user, "User data should have fullName or companyId"


def test_contact_user_fixture(ContactUserData):
    """fixture has expected structure"""
    assert "fullName" in ContactUserData or "companyId" in ContactUserData