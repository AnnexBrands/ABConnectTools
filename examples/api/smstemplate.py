"""
SmsTemplate API Examples - Notification tokens and job statuses

Usage:
    python smstemplate.py               # Run all examples
    python smstemplate.py tokens        # Run a single example
    python smstemplate.py help          # List available examples
"""

from _base import ExampleRunner
from _helpers import save_fixture


class SmsTemplateExamples(ExampleRunner):
    def __init__(self):
        super().__init__("SmsTemplate API", api_kwargs=dict(env='staging', username='instaquote'))
        self.add("tokens", "Get notification tokens", self.get_tokens)
        self.add("statuses", "Get job statuses", self.get_statuses)
        self.add("list", "Get SMS template list", self.get_list)

    def get_tokens(self):
        tokens = self.api.sms_template.get_notificationtokens()
        print(f"Notification tokens type: {type(tokens)}")
        save_fixture(tokens, "SmsTemplateNotificationTokens")

    def get_statuses(self):
        statuses = self.api.sms_template.get_jobstatuses()
        print(f"Job statuses type: {type(statuses)}")
        save_fixture(statuses, "SmsTemplateJobStatuses")

    def get_list(self):
        templates = self.api.sms_template.get_list()
        print(f"Templates type: {type(templates)}")
        print(f"Templates count: {len(templates) if isinstance(templates, list) else 'N/A'}")
        save_fixture(templates, "SmsTemplateList")


if __name__ == "__main__":
    SmsTemplateExamples().run()
