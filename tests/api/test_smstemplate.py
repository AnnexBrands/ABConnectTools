import pytest
from ABConnect.api import models


@pytest.mark.integration
def test_get_notificationtokens(api):
    """server returns notification tokens"""
    tokens = api.sms_template.get_notificationtokens()
    assert isinstance(tokens, list), "api.sms_template.get_notificationtokens should return a list"
    assert len(tokens) > 0, "Should have at least one token group"
    assert isinstance(tokens[0], models.NotificationTokenGroup), "Token group should be NotificationTokenGroup model"
    assert hasattr(tokens[0], 'group_name'), "Token group should have group_name attribute"
    assert hasattr(tokens[0], 'tokens'), "Token group should have tokens attribute"


def test_notificationtokens_fixture(SmsTemplateNotificationTokensData):
    """fixture has expected structure"""
    assert isinstance(SmsTemplateNotificationTokensData, list), "SmsTemplateNotificationTokens fixture should be a list"
    assert len(SmsTemplateNotificationTokensData) > 0, "Should have at least one token group"
    assert "groupName" in SmsTemplateNotificationTokensData[0], "Token group should have groupName"


@pytest.mark.integration
def test_get_jobstatuses(api):
    """server returns job statuses"""
    statuses = api.sms_template.get_jobstatuses()
    assert isinstance(statuses, list), "api.sms_template.get_jobstatuses should return a list"
    assert len(statuses) > 0, "Should have at least one status"
    assert isinstance(statuses[0], models.SmsJobStatus), "Status should be SmsJobStatus model"
    assert hasattr(statuses[0], 'key'), "Status should have key attribute"
    assert hasattr(statuses[0], 'name'), "Status should have name attribute"
    assert hasattr(statuses[0], 'value'), "Status should have value attribute"


def test_jobstatuses_fixture(SmsTemplateJobStatusesData):
    """fixture has expected structure"""
    assert isinstance(SmsTemplateJobStatusesData, list), "SmsTemplateJobStatuses fixture should be a list"
    assert len(SmsTemplateJobStatusesData) > 0, "Should have at least one status"
    assert "key" in SmsTemplateJobStatusesData[0], "Status should have key"


@pytest.mark.integration
def test_get_list(api):
    """server returns template list"""
    templates = api.sms_template.get_list()
    assert isinstance(templates, list), "api.sms_template.get_list should return a list"


def test_list_fixture(SmsTemplateListData):
    """fixture has expected structure"""
    assert isinstance(SmsTemplateListData, list), "SmsTemplateList fixture should be a list"


# ==============================================================================
# Routes needing parameters or write operations
# ==============================================================================

@pytest.mark.integration
@pytest.mark.xfail(reason=(
    "Human: Call api.sms_template.get_get(templateId) with a valid templateId "
    "from the SmsTemplateList fixture (pick first item's id field). "
    "Save fixture via save_fixture(result, 'SmsTemplateDetail')."
))
def test_get_template(api):
    """get_get returns a specific SMS template"""
    result = api.sms_template.get_get("NEED_VALID_TEMPLATE_ID")
    assert result is not None


@pytest.mark.integration
@pytest.mark.xfail(reason=(
    "Human: Destructive operation. Only test if safe to delete a template in staging. "
    "Call api.sms_template.delete_delete(templateId) with a test template."
))
def test_delete_template(api):
    """delete_delete removes an SMS template"""
    result = api.sms_template.delete_delete("NEED_VALID_TEMPLATE_ID")
    assert result is not None


@pytest.mark.integration
@pytest.mark.xfail(reason=(
    "Human: Write operation. Call api.sms_template.post_save(data) with valid "
    "SmsTemplateModel data. Inspect SmsTemplateList fixture for field structure."
))
def test_save_template(api):
    """post_save creates or updates an SMS template"""
    result = api.sms_template.post_save({"name": "test_template"})
    assert result is not None
