from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist
from .models import Lesson, Schedule, Homework, StudentGrade, Attendance, TIMESLOT_OPTIONS, SUBJECT_CHOICES
from users.serializers import TeacherProfileSerializer, StudentGroupSerializer, StudentProfileSerializer
from users.models import StudentGroup, StudentProfile #TBD
from datetime import date, timedelta



class LessonSerializer(serializers.ModelSerializer):
    teacher = serializers.StringRelatedField(many=False)
    group = serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=StudentGroup.objects.all())
    ignore_warnings = serializers.BooleanField(required=False)
    schedule = serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=Schedule.objects.all())
    class Meta:
        model = Lesson
        fields = [
            'description',
            'subject',
            'time_slot',
            'date',
            'teacher',
            'group',
            'ignore_warnings',
            'schedule',
            'id'
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
    
   
        
    

class ClosestLessonSerializer(serializers.ModelSerializer):
    group = serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=StudentGroup.objects.all())
    class Meta:
        model = Schedule
        fields = [
            'name',
            'group',
            'time_slot',
            'weekday',
            'subject',
            'id'
        ]

class ScheduleSerializer(serializers.ModelSerializer):
    group = serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset= StudentGroup.objects.all())
    class Meta:
        model = Schedule
        fields = [
            'name',
            'group',
            'weekday',
            'start_date',
            'end_date',
            'subject',
            'time_slot',
            'id'
        ]

    

class StudentGradeSerializer(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=StudentProfile.objects.all())
    teacher = serializers.StringRelatedField(many=False, read_only=True)
    lesson = serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=Lesson.objects.all())
    class Meta:
        model = StudentGrade
        fields = [
            'student',
            'teacher',
            'grade',
            'lesson',
            'id',
        ]


# class LessonsListingField(serializers.RelatedField):
#     def to_representation(self, value):
#         return '%s %s' % (value.time_slot, value.subject)
    
    # def get_queryset(self):
    #     week_start = date.today()
    #     week_start -= timedelta(days=week_start.weekday())
    #     week_end = week_start + timedelta(days=7)
    #     return Lesson.objects.filter(
    #         date__gte=week_start,
    #         date__lt=week_end
    #     )


class WeeklyJournalSerializer(serializers.ModelSerializer):
    lessons = serializers.StringRelatedField(many=True, read_only=True)
    grade = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Schedule
        fields = [
            'weekday',
            'lessons',
            'grade'
        ]

class AttendanceSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(many=False, read_only=False)
    students = StudentProfileSerializer(many=True, read_only=False)

    class Meta:
        model = Attendance
        fields = ['lesson', 'students']

    def create(self, validated_data):
        lesson_data = validated_data.pop('lesson')
        students_data = validated_data.pop('students')
        lesson, created = Lesson.objects.get_or_create(**lesson_data)
        attendance = Attendance.objects.create(lesson=lesson)
        for student_data in students_data:
            student = StudentProfile.objects.get(**student_data)
            attendance.students.add(student)
        return attendance