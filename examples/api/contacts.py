"""
Contacts API Examples - Getting Responses as Pydantic Objects

This example demonstrates how to work with contacts and get typed responses.

Usage:
    python contacts.py              # Run all examples
    python contacts.py get          # Run a single example
    python contacts.py help         # List available examples
"""

from _base import ExampleRunner
from _helpers import save_fixture
from _constants import CONTACT_ID


class ContactExamples(ExampleRunner):
    def __init__(self):
        super().__init__("Contacts API", api_kwargs=dict(env='staging', username='instaquote'))
        self.add("get", "Get contact by ID", self.get_contact)
        self.add("user", "Get current user's contact info", self.get_user)

    def get_contact(self):
        contact_obj = self.api.contacts.get(CONTACT_ID)
        print(f"type: {type(contact_obj)}")
        print(f"coordinates: {contact_obj.addresses_list[0].address.coordinates}")
        save_fixture(contact_obj, "ContactDetails")

    def get_user(self):
        user_contact = self.api.contacts.get_user()
        print(f"User contact type: {type(user_contact)}")
        save_fixture(user_contact, "ContactUser")


if __name__ == "__main__":
    ContactExamples().run()
