from django.urls import path
from . import views

urlpatterns = [
    path('lessons/', views.LessonListCreateView.as_view()),
    path('grades/', views.StudentGradeListCreateView.as_view()),
]