"""
Contacts API Examples - Getting Responses as Pydantic Objects

This example demonstrates how to work with contacts and get typed responses.
"""

from ABConnect.api import ABConnectAPI
from pprint import pprint

api = ABConnectAPI()

artemis = api.contacts.get_ah(1103)
# Now you have a typed Pydantic object
print(f"Contact type: {type(artemis.addresses_list)}")
pprint(artemis.addresses_list)