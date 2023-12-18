import factory

from docs.models import Lesson, Schedule, Attendance, StudentGrade
from users.models import User, StudentGroup
from datetime import date

class TeacherFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = 'igor.malachov1@gmail.com'
    password = '123'
    username = 'igorm'
    role = 'tchr'
    is_staff = True



class GroupFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = StudentGroup
    name = '1A'
    creation_year = '2023'
    specialisation = 'Mathematics'

class StudentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = 'abobo4ka.malachov1@gmail.com'
    password = '123'
    username = 'abobo4ka'
    role = 'std'
    is_staff = False

class GuardianFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = 'aboba.malachov1@gmail.com'
    password = '123'
    username = 'aboba'
    role = 'grd'
    is_staff = False



    
class ScheduleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Schedule
    name = '1A 2023 1st quarter'
    group = factory.SubFactory(GroupFactory)
    weekday = '1'
    start_date = '2023-12-12'
    end_date = '2024-12-12'
    subject = 'math'
    time_slot = '1'

class LessonFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Lesson

    subject = 'math'
    description = 'Just a regular math class'
    group = factory.SubFactory(GroupFactory)
    time_slot = '1'
    date = date.today()

class GradeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = StudentGrade
    lesson = factory.SubFactory(LessonFactory)
    grade = '9'
