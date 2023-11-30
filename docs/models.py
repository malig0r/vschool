# from django.db import models
# from users.models import StudentClass, TeacherProfile, StudentProfile

# class Lesson(models.Model):
#     teacher = models.ForeignKey(TeacherProfile, on_delete=models.CASCADE, null=False)
#     subject = models.CharField(max_length=120)
#     description = models.TextField()
#     class_id = models.ForeignKey(StudentClass, on_delete=models.SET_NULL)
#     date_time = models.DateTimeField()

# class Homework(models.Model):
#     description = models.TextField()
#     lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
#     deadline = models.DateTimeField()

# GRADE_CHOICES = [
#     ('1', 1),
#     ('2', 2),
#     ('3', 3),
#     ('4', 4),
#     ('5', 5),
#     ('6', 6),
#     ('7', 7),
#     ('8', 8),
#     ('9', 9),
#     ('10', 10),
# ]
# class StudentGrade(models.Model):
#     grade = models.IntegerChoices(choices=GRADE_CHOICES, null=False)
#     student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
#     lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, null=True)
#     teacher = models.ForeignKey(TeacherProfile, on_delete=models.SET_NULL, null=True)




