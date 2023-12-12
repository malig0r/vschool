from rest_framework import generics, status, views
from django.shortcuts import get_object_or_404
import datetime
from rest_framework.response import Response
from .models import Lesson, Schedule, StudentGrade, Homework
from users.permissions import IsTeacher, ReadOnly
from users.models import TeacherProfile, StudentProfile
from .serializers import LessonSerializer, StudentGradeSerializer, ScheduleSerializer, ClosestLessonSerializer

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
    permission_classes = [IsTeacher]
    serializer_class = ScheduleSerializer
    queryset = Schedule.objects.all()

class ClosestLessonRetrieveView(generics.RetrieveAPIView):
    permission_classes = [IsTeacher]
    serializer_class = ClosestLessonSerializer
    def get_object(self):
        weekday = datetime.datetime.now().weekday() + 1
        print(weekday)
        group = self.request.query_params.get('group')
        subject = self.request.query_params.get('subject')
        return get_object_or_404(Schedule, group=group, weekday=weekday, subject=subject)
    
    # def get(self, request, *args, **kwargs):
    #     lesson = ClosestLessonSerializer(self.get_object())
    #     message = 'Would you like to start this lesson?'
    #     data = { 
    #         'message': message,
    #         'lesson': lesson,
    #         }
    #     return Response(data, status=status.HTTP_200_OK)

