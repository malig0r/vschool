from django.contrib import admin
from .models import Lesson, StudentGrade, Schedule, Homework, Attendance

admin.site.register(Lesson)
admin.site.register(StudentGrade)
admin.site.register(Schedule)
admin.site.register(Homework)
admin.site.register(Attendance)

