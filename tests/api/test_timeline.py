"""Tests for job timeline endpoints with proper type validation.

All List responses must validate each element is the expected type.
"""
import pytest
from tests.constants import JOB_DISPLAY_ID


# =============================================================================
# GET /job/{jobDisplayId}/timeline -> TimelineResponse
# =============================================================================

@pytest.mark.integration
def test_get_timeline(api, models, schema):
    """server returns TimelineResponse with tasks list"""
    response_model = schema['JOB']['GET_TIMELINE_LIST'].response_model
    assert response_model == "TimelineResponse", f"Expected TimelineResponse, schema says {response_model}"

    timeline = api.jobs.timeline.get_timeline(JOB_DISPLAY_ID)
    assert isinstance(timeline, models.TimelineResponse), f"Expected TimelineResponse, got {type(timeline)}"

    # TimelineResponse.tasks is List[BaseTask]
    if timeline.tasks:
        for i, task in enumerate(timeline.tasks):
            assert isinstance(task, models.BaseTask), \
                f"Element {i} is {type(task)}, expected BaseTask"


# =============================================================================
# Model validation tests (fixture-based, no API call)
# =============================================================================

def test_carrier_task_model(models):
    """CarrierTask model validates sample data"""
    sample = {
        "id": 123,
        "jobId": "550e8400-e29b-41d4-a716-446655440000",
        "taskCode": "PICKUP",
        "plannedStartDate": "2024-01-15T10:00:00Z",
        "scheduledDate": "2024-01-15T10:00:00Z",
    }
    result = models.CarrierTask.model_validate(sample)
    assert isinstance(result, models.CarrierTask)
    assert result.task_code == "PICKUP"


def test_company_list_item_model(models):
    """CompanyListItem model validates sample data"""
    sample = {
        "id": "ed282b80-54fe-4f42-bf1b-69103ce1f76c",
        "code": "TRAINING",
        "name": "Training Company",
        "typeId": "8e809044-8d69-4618-9533-265d7e71db13"
    }
    result = models.CompanyListItem.model_validate(sample)
    assert isinstance(result, models.CompanyListItem)
    assert result.code == "TRAINING"


def test_delete_task_response_model(models):
    """DeleteTaskResponse model validates sample data"""
    sample = {
        "success": True,
        "errorMessage": None,
        "jobSubManagementStatus": None
    }
    result = models.DeleteTaskResponse.model_validate(sample)
    assert isinstance(result, models.DeleteTaskResponse)
    assert result.success is True


def test_save_response_model(models):
    """SaveResponseModel model validates sample data"""
    sample = {
        "success": True,
        "errorMessage": None,
        "taskExists": False,
        "task": None,
        "emailLogId": None,
        "jobSubManagementStatus": None
    }
    result = models.SaveResponseModel.model_validate(sample)
    assert isinstance(result, models.SaveResponseModel)
    assert result.success is True


def test_increment_job_status_response_model(models):
    """IncrementJobStatusResponseModel model validates sample data"""
    sample = {
        "message": "Job status incremented",
        "canUndo": True,
        "intactSendRequired": False
    }
    result = models.IncrementJobStatusResponseModel.model_validate(sample)
    assert isinstance(result, models.IncrementJobStatusResponseModel)
    assert result.can_undo is True


def test_service_base_response_model(models):
    """ServiceBaseResponse model validates sample data"""
    sample = {
        "success": True,
        "errorMessage": None
    }
    result = models.ServiceBaseResponse.model_validate(sample)
    assert isinstance(result, models.ServiceBaseResponse)
    assert result.success is True


# =============================================================================
# Schema validation tests
# =============================================================================

def test_timeline_routes_have_response_models(schema):
    """All timeline routes should have response_model defined"""
    timeline_routes = [
        'DELETE_TIMELINE',
        'GET_TIMELINE',
        'GET_TIMELINE_AGENT',
        'GET_TIMELINE_LIST',
        'PATCH_TIMELINE',
        'POST_TIMELINE',
        'POST_TIMELINE_INCREMENTJOBSTATUS',
        'POST_TIMELINE_UNDOINCREMENTJOBSTATUS',
    ]

    expected_models = {
        'DELETE_TIMELINE': 'DeleteTaskResponse',
        'GET_TIMELINE': 'CarrierTask',
        'GET_TIMELINE_AGENT': 'CompanyListItem',
        'GET_TIMELINE_LIST': 'TimelineResponse',
        'PATCH_TIMELINE': 'ServiceBaseResponse',
        'POST_TIMELINE': 'SaveResponseModel',
        'POST_TIMELINE_INCREMENTJOBSTATUS': 'IncrementJobStatusResponseModel',
        'POST_TIMELINE_UNDOINCREMENTJOBSTATUS': 'ServiceBaseResponse',
    }

    for route_name in timeline_routes:
        route = schema['JOB'].get(route_name)
        assert route is not None, f"Route {route_name} not found in JOB schema"
        assert route.response_model is not None, f"Route {route_name} has no response_model"
        assert route.response_model == expected_models[route_name], \
            f"Route {route_name} expected {expected_models[route_name]}, got {route.response_model}"
