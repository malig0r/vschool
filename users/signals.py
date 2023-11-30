from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import TeacherProfile, GuardianProfile, StudentProfile
from django.contrib.auth import get_user_model
from .serializers import UserSerializer


User = get_user_model()


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        match instance.role: 
            case 'std':
                profile = StudentProfile(user=instance)
                profile.save()
            case 'tchr':
                serializer = UserSerializer(instance)
                invite_code = serializer.get_invite_code(instance)
                profile = TeacherProfile(user=instance, invite_code=invite_code)
                profile.save()
            case 'grd':
                profile = GuardianProfile(user=instance)
                profile.save()
