import factory

from users.models import User, StudentGroup

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


