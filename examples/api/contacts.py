"""
Contacts API Examples - Getting Responses as Pydantic Objects

This example demonstrates how to work with contacts and get typed responses.
"""

from ABConnect.api import ABConnectAPI, models
from pprint import pprint

api = ABConnectAPI()
TRAINING_ID = 266841

training_obj = api.contacts.get(TRAINING_ID)
# Now you have a typed Pydantic object
print(f"type: {type(training_obj)}")
# pprint(training_obj.json())