from django.contrib.auth import login, logout
from django.shortcuts import get_object_or_404
from django.utils.timezone import now
from drf_spectacular.utils import extend_schema
from rest_framework import generics, permissions, status, views
from rest_framework.response import Response

from . import serializers
from .models import GuardianProfile, StudentGroup, StudentProfile
from .permissions import IsTeacher, IsTeacherOrParent


class LoginView(views.APIView):
    permission_classes = [permissions.AllowAny,]
    serializer_class = serializers.UserSerializer
    def post(self, request):
        serializer = serializers.LoginSerializer(data=self.request.data,
                                                 context={'request': self.request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        data = {
            'message': f'Welcome {user}'
        }
        return Response(data, status=status.HTTP_202_ACCEPTED)

class LogoutView(views.APIView):

    serializer_class = serializers.UserSerializer
    def post(self, request):
        logout(request)
        data = {
            'message': 'You have logged out'
        }
        return Response(data, status=status.HTTP_200_OK)

class GuardianRegisterView(views.APIView):
    
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data
        print(data)
        data['role'] = 'grd'
        print(data)
        serializer = serializers.GuardianSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class StudentRegisterView(views.APIView):
    serializer_class = serializers.UserSerializer
    def post(self, request):
        data = request.data
        data['role'] = 'std'
        serializer = serializers.UserSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            student = serializer.save()
            guardian = GuardianProfile.objects.get(user=request.user)
            guardian.students.add(student)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  
class ProfileView(generics.RetrieveUpdateAPIView):
    serializers = {
        'tchr': serializers.TeacherProfileSerializer,
        'std': serializers.StudentProfileSerializer,
        'grd': serializers.GuardianProfileSerializer
    }
    def get_serializer_class(self):
        return self.serializers.get(self.request.user.role)
    
    def get_object(self):
        profile_model = self.get_serializer_class().Meta.model
        profile = profile_model.objects.get(user=self.request.user)
        return profile
    def perform_update(self, serializer):
        serializer.save(updated=now())

class UserUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = serializers.UserSerializer
    def get_object(self):
        user = self.request.user
        return user
    def perform_update(self, serializer):
        serializer.save()

class StudentGroupListCreateView(generics.ListCreateAPIView):
    serializer_class = serializers.StudentGroupSerializer
    permission_classes = [IsTeacher,]
    queryset = StudentGroup.objects.all()

class StudentGroupUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = serializers.StudentGroupSerializer
    permission_classes = [IsTeacher,]
    def get_object(self):
        group = get_object_or_404(StudentGroup, pk=self.kwargs['pk'])
        return group

class StudentProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = serializers.StudentProfileSerializer
    permission_classes = [IsTeacherOrParent]
    def get_object(self):
        student = get_object_or_404(StudentProfile, pk=self.kwargs['pk'])
        self.check_object_permissions(self.request, student)
        return student
    def perform_update(self, serializer):
        serializer.save(updated=now())

