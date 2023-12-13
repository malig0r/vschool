from django.db import models
from users.models import StudentGroup, TeacherProfile, StudentProfile

SUBJECT_CHOICES = [
    ('math', 'Mathematics'),
    ('phys', 'Physics'),
    ('eng', 'English language'),
    ('geo', 'Geography'),
    ('hist', 'History'),
]

TIMESLOT_OPTIONS = [
    ('1', '8:00 - 8:45'),
    ('2', '9:00 - 9:45'),
    ('3', '10:00 - 10:45'),
    ('4', '11:00 - 11:45'),
    ('5', '12:00 - 12:45'),
    ('6', '13:00 - 13:45'),
    ('7', '14:00 - 14:45'),
]

WEEKDAY_OPTIONS = [
    ('1', 'Monday'),
    ('2', 'Tuesday'),
    ('3', 'Wednesday'),
    ('4', 'Thursday'),
    ('5', 'Friday'),
    ('6', 'Saturday'),
]

GRADE_CHOICES = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
]


class Schedule(models.Model):
    name = models.CharField(max_length=200, null=False)
    group = models.ForeignKey(StudentGroup, on_delete=models.CASCADE)
    weekday = models.CharField(max_length=50,choices=WEEKDAY_OPTIONS, null=False, default='1')
    start_date = models.DateField()
    end_date = models.DateField()
    subject = models.CharField(max_length=20, choices=SUBJECT_CHOICES, null=False)
    time_slot = models.CharField(max_length=20, choices=TIMESLOT_OPTIONS, null=False, default='1')

    def __str__(self) -> str:
        if self.group:
            return f'{self.group.name} {self.name}'
        else:
            return self.name
    
    class Meta:
        ordering = ["weekday", "time_slot"]


class Lesson(models.Model):
    teacher = models.ForeignKey(TeacherProfile, on_delete=models.CASCADE, null=True)
    subject = models.CharField(max_length=20, choices=SUBJECT_CHOICES, null=False)
    description = models.TextField()
    group = models.ForeignKey(StudentGroup, on_delete=models.SET_NULL, null=True, related_name='lesson')
    time_slot = models.CharField(max_length=50, choices=TIMESLOT_OPTIONS, null=False)
    date = models.DateField(auto_now_add=True)
    schedule = models.ForeignKey(Schedule, on_delete=models.SET_NULL, null=True, default=None, related_name='lessons')
    
    
    def __str__(self) -> str:
        return f'{self.subject} {self.group} {self.date}'
    
    class Meta:
        ordering = ["time_slot"]

    

class Homework(models.Model):
    description = models.TextField()
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    deadline = models.DateField()
    def __str__(self) -> str:
        return f'{self.deadline} {self.lesson}'
    class Meta:
        ordering = ["deadline"]

class StudentGrade(models.Model):
    grade = models.CharField(max_length=10, choices=GRADE_CHOICES, null=False)
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, null=True)
    teacher = models.ForeignKey(TeacherProfile, on_delete=models.SET_NULL, null=True)
    def __str__(self) -> str:
        return f'{self.grade} {self.teacher}'
    
class Attendance(models.Model):
    lesson = models.OneToOneField(Lesson, on_delete=models.CASCADE, null=False, related_name='attendance')
    students = models.ManyToManyField(StudentProfile)
    



