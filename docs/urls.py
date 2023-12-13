from django.urls import path
from . import views

urlpatterns = [
    path('lessons/', views.LessonListCreateView.as_view()),
    path('grades/', views.StudentGradeListCreateView.as_view()),
    path('closest-lesson/', views.ClosestLessonRetrieveView.as_view()),
    path('schedules/', views.ScheduleListCreateView.as_view()),
    path('journal/', views.JournalRetrieveView.as_view()),
    path('attendance/', views.AttendanceListCreateView.as_view())

]