from pytest_factoryboy import register
from .factories import TeacherFactory, StudentFactory, GuardianFactory, GroupFactory


register(TeacherFactory)
register(StudentFactory)
register(GuardianFactory)
register(GroupFactory)
