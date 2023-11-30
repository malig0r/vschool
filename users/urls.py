from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view()),
    path('logout/', views.LogoutView.as_view()),
    path('profile/', views.ProfileView.as_view()),
    path('register/', views.GuardianRegisterView.as_view()),
    path('add-student/', views.StudentRegisterView.as_view()),
    path('user/', views.UserUpdateView.as_view()),
    path('groups/', views.StudentGroupListCreateView.as_view()),
    path('groups/<str:pk>/', views.StudentGroupUpdateView.as_view()),
    path('student/<str:pk>/', views.StudentProfileView.as_view()),
    
]