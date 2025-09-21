#!/usr/bin/env python3
"""
SMS Template API Examples

This example demonstrates how to work with SMS templates using:
1. ABConnect API client (Python)
2. CLI commands

SMS Template endpoints:
- GET /api/SmsTemplate/notificationTokens - Get notification tokens
- GET /api/SmsTemplate/jobStatuses - Get job statuses
- GET /api/SmsTemplate/list - List templates (requires companyId)
- GET /api/SmsTemplate/{templateId} - Get specific template
- POST /api/SmsTemplate/save - Save/create template
- DELETE /api/SmsTemplate/{templateId} - Delete template
"""

import os
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

def get_example_data():
    """Get example fixture data."""
    print("🔧 SMS Template API Examples")
    print("=" * 50)
    print("Using TRAINING company and template ID 1 for examples")
    print()

    return "ed282b80-54fe-4f42-bf1b-69103ce1f76c", 1

def python_api_examples(company_id: str, template_id: int):
    """Demonstrate Python API client usage."""
    print("\n" + "=" * 50)
    print("🐍 PYTHON API CLIENT EXAMPLES")
    print("=" * 50)

    try:
        from ABConnect import ABConnectAPI

        # Initialize API client
        print("# Initialize API client")
        print("from ABConnect import ABConnectAPI")
        print("api = ABConnectAPI()")
        print()

        # Note: Due to dependencies, we'll show the code structure
        print("# Example API calls (code structure):")
        print()

        # List templates
        print("# 1. List SMS templates for a company (convenience method)")
        print(f"templates = api.sms_template.list('TRAINING')  # By company code")
        print("print('Templates:', templates)")
        print()
        print("# Alternative: List by company UUID")
        print(f"templates = api.sms_template.list('{company_id}')")
        print("print('Templates:', templates)")
        print()

        # Get specific template
        print("# 2. Get specific SMS template")
        print(f"template = api.sms_template.get_get('{template_id}')")
        print("print('Template details:', template)")
        print()

        # Get notification tokens
        print("# 3. Get notification tokens")
        print("tokens = api.sms_template.get_notificationtokens()")
        print("print('Notification tokens:', tokens)")
        print()

        # Get job statuses
        print("# 4. Get job statuses")
        print("statuses = api.sms_template.get_jobstatuses()")
        print("print('Job statuses:', statuses)")
        print()

        # Create/save template
        print("# 5. Create/save SMS template")
        print("new_template = {")
        print("    'name': 'Example Template',")
        print("    'message': 'Hello [[CustomerFirstName]], your job [[JobID]] is ready!',")
        print("    'isActive': True")
        print("}")
        print("result = api.sms_template.post_save(new_template)")
        print("print('Save result:', result)")
        print()

        # Delete template
        print("# 6. Delete SMS template")
        print(f"result = api.sms_template.delete_delete('{template_id}')")
        print("print('Delete result:', result)")

    except ImportError as e:
        print(f"⚠️  Cannot import ABConnect API: {e}")
        print("Install dependencies first: pip install -e .[dev]")

def cli_examples(company_id: str, template_id: int):
    """Demonstrate CLI usage."""
    print("\n" + "=" * 50)
    print("🖥️  CLI EXAMPLES")
    print("=" * 50)

    print("# Show SmsTemplate endpoint info")
    print("ab smstemplate")
    print()

    print("# Get notification tokens")
    print("ab smstemplate get_notificationtokens")
    print()

    print("# Get job statuses")
    print("ab smstemplate get_jobstatuses")
    print()

    print("# List SMS templates by company code")
    print("ab smstemplate list TRAINING")
    print()

    print("# List SMS templates by company UUID")
    print(f"ab smstemplate list {company_id}")
    print()

    print("# List all accessible templates")
    print("ab smstemplate list")
    print()


def model_examples():
    """Show model structure and usage."""
    print("\n" + "=" * 50)
    print("📋 PYDANTIC MODEL EXAMPLES")
    print("=" * 50)

    print("# SmsTemplateModel structure (from swagger):")
    print("class SmsTemplateModel:")
    print("    id: Optional[int] = None")
    print("    name: Optional[str] = None  # max 500 chars")
    print("    message: Optional[str] = None  # max 1024 chars")
    print("    isActive: Optional[bool] = None")
    print()

    print("# Example model usage:")
    print("template_data = {")
    print("    'name': 'Order Confirmation',")
    print("    'message': 'Hi [[CustomerFirstName]]! Your order [[JobID]] is confirmed.',")
    print("    'isActive': True")
    print("}")
    print()

    print("# Available message tokens (use [[TokenName]] format):")
    print("# [[CustomerFirstName]] - Customer first name")
    print("# [[CustomerLastName]] - Customer last name")
    print("# [[JobID]] - Job display ID")
    print("# [[JobStatus]] - Job status")
    print("# [[CompanyName]] - Company name")
    print("# [[PickupScheduled]] - Pickup date")
    print("# [[DeliveryScheduled]] - Delivery date")
    print("# [[BookedDate]] - Booking date")
    print("# [[JobAmount]] - Job amount")
    print("# See ab smstemplate get_notificationtokens for full list")

def main():
    """Main example runner."""
    try:
        # Get example data
        company_id, template_id = get_example_data()

        # Run examples
        python_api_examples(company_id, template_id)
        cli_examples(company_id, template_id)
        model_examples()

        print("\n" + "=" * 50)
        print("✅ SMS Template Examples Complete!")
        print("=" * 50)

    except Exception as e:
        print(f"\n❌ Error running examples: {e}")

if __name__ == "__main__":
    main()