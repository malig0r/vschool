from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class User(AbstractUser):
    ROLE_OPTIONS = [
    ('std', 'Student'),
    ('tchr', 'Teacher'),
    ('grd', 'Guardian')             
]
    
    username = models.CharField(max_length=100, unique=True)
    role = models.CharField(max_length=10, choices=ROLE_OPTIONS, null=False, default='tchr', editable=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=500)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    extra_kwargs = {
        'password': {'write_only': True},
        'role': {'read_only': True}
    }
    def __str__(self):
        return f'{self.email}'
    
class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    primary_subject = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(null=True)
    invite_code = models.CharField(max_length=255, null=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=True)
    
    def __str__(self) -> str:
        if self.name:
            return f'{self.last_name} {self.name}'
        else:
            return self.user.email
    
    class Meta:
        ordering = ['created']

class StudentGroup(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=True)
    creation_year = models.IntegerField(null=False, blank=False)
    specialisation = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['name']

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(null=True)
    group = models.ForeignKey(StudentGroup, on_delete=models.SET_NULL, null=True, default=None, related_name='students')
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self) -> str:
        if self.name:
            return f'{self.last_name} {self.name}'
        else:
            return self.user.email
    
    class Meta:
        ordering = ['created']

class GuardianProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=True)
    students = models.ManyToManyField(User, blank=True, related_name='students')
    
    def __str__(self) -> str:
        if self.name:
            return f'{self.last_name} {self.name}'
        else:
            return self.user.email
    
    class Meta:
        ordering = ['created']