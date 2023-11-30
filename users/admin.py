from django.contrib import admin
from .models import StudentGroup, User, StudentProfile, TeacherProfile, GuardianProfile

admin.site.register(User)
admin.site.register(StudentProfile)
admin.site.register(StudentGroup)
admin.site.register(TeacherProfile)
admin.site.register(GuardianProfile)

