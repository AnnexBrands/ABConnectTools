
def test_get_contact(api, models):
    contact = api.contacts.get(266841)
    assert isinstance(contact, models.ContactDetails)
    print(contact)