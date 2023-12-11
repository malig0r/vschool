from rest_framework import generics, status, views
from rest_framework.response import Response
from .models import Lesson, Schedule, StudentGrade, Homework
from users.permissions import IsTeacher, ReadOnly
from users.models import TeacherProfile
from .serializers import LessonSerializer

class LessonListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsTeacher|ReadOnly]
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    def perform_create(self, serializer):
        teacher = TeacherProfile.objects.get(user=self.request.user)
        serializer.save(teacher=teacher)