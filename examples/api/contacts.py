"""
Contacts API Examples - Getting Responses as Pydantic Objects

This example demonstrates how to work with contacts and get typed responses.
"""

from ABConnect.api import ABConnectAPI, models
from _helpers import save_fixture
from _constants import CONTACT_ID

api = ABConnectAPI(env='staging', username='instaquote')

# Get contact by ID using route-based endpoint
contact_obj = api.contacts.get(CONTACT_ID)

# Now you have a typed Pydantic object
print(f"type: {type(contact_obj)}")
print(f"coordinates: {contact_obj.addresses_list[0].address.coordinates}")
save_fixture(contact_obj, "ContactDetails")

# Get current user's contact info
user_contact = api.contacts.get_user()
print(f"User contact type: {type(user_contact)}")
save_fixture(user_contact, "ContactUser")