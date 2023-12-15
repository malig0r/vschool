import pytest
from users.models import TeacherProfile, StudentProfile, GuardianProfile
pytestmark = pytest.mark.django_db

class TestTeacherProfileModel:
    def test_str_method(self, teacher_factory):
        user = teacher_factory()
        assert user.__str__() == 'igor.malachov1@gmail.com'

    def test_profile_signal(self, teacher_factory):
        profile = TeacherProfile.objects.get(user=teacher_factory())
        assert profile.__str__() == 'igor.malachov1@gmail.com'
        profile.name = 'Igor'
        profile.last_name = 'Malachov'
        assert profile.__str__() == 'Malachov Igor'

class TestGroupModel:
    def test_str_method(self, group_factory):
        group = group_factory()
        assert group.__str__() == '1A'

class TestStudentProfileModel:
    def test_str_method(self, student_factory):
        user = student_factory()
        assert user.__str__() == 'abobo4ka.malachov1@gmail.com'

    def test_profile_signal(self, student_factory, group_factory):
        profile = StudentProfile.objects.get(user=student_factory())
        assert profile.__str__() == 'abobo4ka.malachov1@gmail.com'
        profile.name = 'Abobo4ka'
        profile.last_name = 'Malachov'
        profile.group = group_factory()
        assert profile.__str__() == 'Malachov Abobo4ka'
        assert profile.group.__str__() == '1A'

class TestGuardianProfileModel:
    def test_str_method(self, guardian_factory):
        user = guardian_factory()
        assert user.__str__() == 'aboba.malachov1@gmail.com'

    def test_profile_signal(self, guardian_factory, student_factory):
        profile = GuardianProfile.objects.get(user=guardian_factory())
        assert profile.__str__() == 'aboba.malachov1@gmail.com'
        profile.name = 'Aboba'
        profile.last_name = 'Malachov'
        student = student_factory()
        profile.students.add(student)
        assert profile.__str__() == 'Malachov Aboba'
        assert student in profile.students.all()