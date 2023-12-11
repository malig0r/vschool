from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist
from .models import Lesson, Schedule, Homework, StudentGrade
from users.serializers import TeacherProfileSerializer, StudentGroupSerializer, StudentProfileSerializer
from users.models import TeacherProfile, StudentGroup #TBD



class LessonSerializer(serializers.ModelSerializer):
    # teacher = serializers.RelatedField(many=False, read_only=False, queryset=TeacherProfile.objects.all())
    # group = serializers.RelatedField(many=False, read_only=False, queryset=StudentGroup.objects.all())
    teacher = serializers.StringRelatedField(many=False)
    group = serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=StudentGroup.objects.all())
    ignore_warnings = serializers.BooleanField(required=False)
    class Meta:
        model = Lesson
        fields = [
            'description',
            'subject',
            'time_slot',
            'date',
            'teacher',
            'group',
            'ignore_warnings'
        ]
    def validate(self, attrs):
        ignore_warnings = attrs.pop('ignore_warnings')
        if ignore_warnings:
            return attrs
        
        try:
            lesson = Lesson.objects.get(**attrs)
        except ObjectDoesNotExist:
            return attrs

        raise serializers.ValidationError('There is an overlapping lesson, check input details')
    
   
        
    

class ClosestLessonSerializer(serializers.Serializer):
    pass

class ScheduleSerializer(serializers.ModelSerializer):
    pass

class StudentGradeSerializer(serializers.ModelSerializer):
    pass

class HomeworkSerializer(serializers.ModelSerializer):
    pass