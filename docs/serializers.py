from rest_framework import serializers
from .models import Lesson, Schedule, Homework, StudentGrade
from users.serializers import TeacherProfileSerializer, StudentGroupSerializer, StudentProfileSerializer

# class Lesson(models.Model):
#     teacher = models.ForeignKey(TeacherProfile, on_delete=models.CASCADE, null=False)
#     subject = models.CharField(max_length=20, choices=SUBJECT_CHOICES, null=False)
#     description = models.TextField()
#     group = models.ForeignKey(StudentGroup, on_delete=models.SET_NULL, null=True)
#     time_slot = models.CharField(max_length=50, choices=TIMESLOT_OPTIONS, null=False)
#     date = models.DateField(auto_now_add=True)

class LessonSerializer(serializers.ModelSerializer):
    teacher = TeacherProfileSerializer(many=False, read_only=False)
    group = serializers.RelatedField(many=False, read_only=False)
    class Meta:
        fields = [
            'description',
            'subject',
            'time_slot',
            'date',
        ]

class ClosestLessonSerializer(serializers.Serializer):
    pass

class ScheduleSerializer(serializers.ModelSerializer):
    pass

class StudentGradeSerializer(serializers.ModelSerializer):
    pass

class HomeworkSerializer(serializers.ModelSerializer):
    pass