import pytest
from users.models import TeacherProfile, StudentProfile
from datetime import date
pytestmark = pytest.mark.django_db

class TestScheduleModel:
    def test_str_method(self, schedule_factory):
        schedule = schedule_factory()
        assert schedule.__str__() == '1A 1A 2023 1st quarter'

class TestLessonModel:
    def test_str_method(self, lesson_factory, teacher_factory, schedule_factory):
        profile = TeacherProfile.objects.get(user=teacher_factory())
        schedule = schedule_factory()
        lesson = lesson_factory(teacher=profile, schedule=schedule)
        assert lesson.teacher.__str__() == 'igor.malachov1@gmail.com'
        assert lesson.__str__() == f'math 1A {date.today()}'
        assert lesson.schedule.__str__() == '1A 1A 2023 1st quarter'

class TestGradeFactory:
    def test_str_method(self, grade_factory, teacher_factory, student_factory):
        teacher = TeacherProfile.objects.get(user=teacher_factory())
        student = StudentProfile.objects.get(user=student_factory())
        grade = grade_factory(teacher=teacher, student=student)
        assert grade.teacher.__str__() == 'igor.malachov1@gmail.com'
        assert grade.lesson.__str__() == f'math 1A {date.today()}'
        assert grade.student.__str__() == 'abobo4ka.malachov1@gmail.com'
        assert grade.__str__() == '9 igor.malachov1@gmail.com'