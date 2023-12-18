import pytest
from pytest_factoryboy import register
from . import factories
from rest_framework.test import APIClient

register(factories.TeacherFactory)
register(factories.StudentFactory)
register(factories.GuardianFactory)
register(factories.GroupFactory)
register(factories.LessonFactory)
register(factories.ScheduleFactory)
register(factories.GradeFactory)

@pytest.fixture
def api_client():
    return APIClient
