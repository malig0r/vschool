from rest_framework import generics, status, views
from rest_framework.response import Response
from .models import Lesson, Schedule, StudentGrade, Homework
from users.permissions import IsTeacher, ReadOnly
from users.models import TeacherProfile, StudentProfile
from .serializers import LessonSerializer, StudentGradeSerializer

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
