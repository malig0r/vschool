from rest_framework import generics, status, views
from django.shortcuts import get_object_or_404
import datetime
from rest_framework.response import Response
from .models import Lesson, Schedule, StudentGrade, Homework, Attendance
from users.permissions import IsTeacher, ReadOnly
from users.models import TeacherProfile, StudentProfile
from django.db.models import Prefetch
from .serializers import LessonSerializer, StudentGradeSerializer, ScheduleSerializer, ClosestLessonSerializer, WeeklyJournalSerializer, AttendanceSerializer

from datetime import date, timedelta

class LessonListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsTeacher|ReadOnly]
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    def perform_create(self, serializer):
        teacher = TeacherProfile.objects.get(user=self.request.user)
        serializer.save(teacher=teacher)


class StudentGradeListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsTeacher|ReadOnly]
    serializer_class = StudentGradeSerializer
    queryset = StudentGrade.objects.all()
    def get_queryset(self):
        if self.request.user.is_staff:
            return StudentGrade.objects.all()
        else:
            student = StudentProfile.objects.get(user=self.request.user)
            return StudentGrade.objects.filter(student=student)
    def perform_create(self, serializer):
        teacher = TeacherProfile.objects.get(user=self.request.user)
        serializer.save(teacher=teacher)

class ScheduleListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsTeacher|ReadOnly]
    serializer_class = ScheduleSerializer
    queryset = Schedule.objects.all()
    def get_queryset(self):
        if self.request.user.role == 'tchr':
            return Schedule.objects.all()
        else:
            return Schedule.objects.filter(group=self.request.user.profile.group)

class ClosestLessonRetrieveView(generics.RetrieveAPIView):
    permission_classes = [IsTeacher]
    serializer_class = ClosestLessonSerializer
    def get_object(self):
        weekday = datetime.datetime.now().weekday() + 1
        print(weekday)
        group = self.request.query_params.get('group')
        subject = self.request.query_params.get('subject')
        return get_object_or_404(Schedule, group=group, weekday=weekday, subject=subject)

class JournalRetrieveView(generics.ListAPIView):
    serializer_class = WeeklyJournalSerializer
    def get_queryset(self):
        profile = self.request.user.profile
        week_start = date.today()
        week_start -= timedelta(days=week_start.weekday())
        week_end = week_start + timedelta(days=7)
        return Lesson.objects.\
            prefetch_related(
                Prefetch('grades', queryset=StudentGrade.objects.filter(student=profile), to_attr='filtered_grades')
            ).\
            filter(group=self.request.user.profile.group, date__gte=week_start, date__lt=week_end)


class AttendanceListCreateView(generics.ListCreateAPIView):
    serializer_class = AttendanceSerializer
    permission_classes = [IsTeacher,]
    queryset = Attendance.objects.all()