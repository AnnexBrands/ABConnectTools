"""
SmsTemplate API Examples - Notification Tokens and Job Statuses

This example demonstrates getting SMS template configuration data.
"""

from ABConnect.api import ABConnectAPI
from _helpers import save_fixture

api = ABConnectAPI(env='staging', username='instaquote')

# Get notification tokens
tokens = api.sms_template.get_notificationtokens()
print(f"Notification tokens type: {type(tokens)}")
save_fixture(tokens, "SmsTemplateNotificationTokens")

# Get job statuses for SMS templates
statuses = api.sms_template.get_jobstatuses()
print(f"Job statuses type: {type(statuses)}")
save_fixture(statuses, "SmsTemplateJobStatuses")

# Get SMS template list
templates = api.sms_template.get_list()
print(f"Templates type: {type(templates)}")
print(f"Templates count: {len(templates) if isinstance(templates, list) else 'N/A'}")
save_fixture(templates, "SmsTemplateList")
