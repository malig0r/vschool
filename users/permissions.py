from rest_framework import permissions
from .models import GuardianProfile

class IsTeacher(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'tchr'
    
class IsTeacherOrParent(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.role == 'tchr':
            return True
        parent = GuardianProfile.objects.get(user=request.user)
        return bool(obj.user in parent.students.all()) 
        
