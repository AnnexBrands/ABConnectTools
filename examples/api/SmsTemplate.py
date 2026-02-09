"""
SMS Template API Examples - Comprehensive template operations

Demonstrates notification tokens, job statuses, template CRUD, CLI, and models.

Usage:
    python SmsTemplate.py               # Run all examples
    python SmsTemplate.py python_api    # Run a single example
    python SmsTemplate.py help          # List available examples
"""

from _base import ExampleRunner


COMPANY_ID = "ed282b80-54fe-4f42-bf1b-69103ce1f76c"
TEMPLATE_ID = 1


class SmsTemplateFullExamples(ExampleRunner):
    def __init__(self):
        super().__init__("SMS Template API (Comprehensive)")
        self.add("python_api", "Python API client usage examples", self.python_api_examples)
        self.add("cli", "CLI usage examples", self.cli_examples)
        self.add("models", "Pydantic model structure and tokens", self.model_examples)

    def python_api_examples(self):
        print("from ABConnect import ABConnectAPI")
        print("api = ABConnectAPI()\n")

        print(f"# List SMS templates for a company")
        print(f"templates = api.sms_template.list('TRAINING')")
        print(f"templates = api.sms_template.list('{COMPANY_ID}')\n")

        print(f"# Get specific SMS template")
        print(f"template = api.sms_template.get_get('{TEMPLATE_ID}')\n")

        print("# Get notification tokens")
        print("tokens = api.sms_template.get_notificationtokens()\n")

        print("# Get job statuses")
        print("statuses = api.sms_template.get_jobstatuses()\n")

        print("# Create/save SMS template")
        print("new_template = {")
        print("    'name': 'Example Template',")
        print("    'message': 'Hello [[CustomerFirstName]], your job [[JobID]] is ready!',")
        print("    'isActive': True")
        print("}")
        print("result = api.sms_template.post_save(new_template)\n")

        print(f"# Delete SMS template")
        print(f"result = api.sms_template.delete_delete('{TEMPLATE_ID}')")

    def cli_examples(self):
        print("# Show SmsTemplate endpoint info")
        print("ab smstemplate\n")
        print("# Get notification tokens")
        print("ab smstemplate get_notificationtokens\n")
        print("# Get job statuses")
        print("ab smstemplate get_jobstatuses\n")
        print("# List SMS templates by company code")
        print("ab smstemplate list TRAINING\n")
        print(f"# List SMS templates by company UUID")
        print(f"ab smstemplate list {COMPANY_ID}\n")
        print("# List all accessible templates")
        print("ab smstemplate list")

    def model_examples(self):
        print("SmsTemplateModel structure (from swagger):")
        print("  id: Optional[int]")
        print("  name: Optional[str]      # max 500 chars")
        print("  message: Optional[str]   # max 1024 chars")
        print("  isActive: Optional[bool]\n")

        print("Available message tokens (use [[TokenName]] format):")
        print("  [[CustomerFirstName]]  - Customer first name")
        print("  [[CustomerLastName]]   - Customer last name")
        print("  [[JobID]]              - Job display ID")
        print("  [[JobStatus]]          - Job status")
        print("  [[CompanyName]]        - Company name")
        print("  [[PickupScheduled]]    - Pickup date")
        print("  [[DeliveryScheduled]]  - Delivery date")
        print("  [[BookedDate]]         - Booking date")
        print("  [[JobAmount]]          - Job amount")
        print("  See: ab smstemplate get_notificationtokens for full list")


if __name__ == "__main__":
    SmsTemplateFullExamples().run()
