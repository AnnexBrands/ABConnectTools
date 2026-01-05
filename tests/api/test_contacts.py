import pytest

@pytest.mark.integration
def test_get_contact(api, models, schema):
    """server data validates against ContactDetails model"""
    ContactDetailsModelName = schema['CONTACTS']['GET'].response_model
    ContactDetailsClass = getattr(models, ContactDetailsModelName)
    contact = api.contacts.get(266841)
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