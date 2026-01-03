import pytest


@pytest.mark.integration
def test_get_notificationtokens(api):
    """server returns notification tokens"""
    tokens = api.sms_template.get_notificationtokens()
    assert isinstance(tokens, list), "api.sms_template.get_notificationtokens should return a list"
    assert len(tokens) > 0, "Should have at least one token group"
    assert "groupName" in tokens[0], "Token group should have groupName"
    assert "tokens" in tokens[0], "Token group should have tokens"


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
    assert "key" in statuses[0], "Status should have key"
    assert "name" in statuses[0], "Status should have name"
    assert "value" in statuses[0], "Status should have value"


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
