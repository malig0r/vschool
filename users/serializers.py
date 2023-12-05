from rest_framework import serializers
from cryptography.fernet import Fernet
from .models import User, StudentProfile, StudentGroup, GuardianProfile, TeacherProfile
from django.contrib.auth import authenticate
from cryptography.fernet import Fernet
from django.conf import settings


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(
        label='Username',
        write_only=True
    )

    password = serializers.CharField(
        label='Password',
        write_only=True
    )

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
            if not user:
                raise serializers.ValidationError('Wrong username or password')
            
        else:
            raise serializers.ValidationError('Please provide username and password')
        attrs['user'] = user
        return attrs

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        label='Password',
        write_only=True
    )

    class Meta:

        model = User
        fields = (
            "id",
            "email",
            "username",
            "password",
            "role"
        )
    
    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User.objects.create_user(
            username=validated_data["username"], 
            password=password, 
            role=validated_data["role"],
            email=validated_data["email"]
        )
        return user
    
    def get_invite_code(self, user):
        unique_string = f"{user.id}"
        fernet = Fernet(settings.CRYPTOGRAPHY_KEY)
        invite_code = fernet.encrypt(unique_string.encode())
        return str(invite_code, encoding='utf-8')

class GuardianSerializer(UserSerializer):
    invite_code = serializers.CharField(
        label='Invite code',
        write_only=True
    )
    class Meta:
        model = User

        fields = (
            "id",
            'username',
            "email",
            "password",
            'role',
            'invite_code'
        )

    def validate(self, attrs):
        code = attrs.get('invite_code')
        try:
            user_id = Fernet(settings.CRYPTOGRAPHY_KEY).decrypt(code).decode()
            inviter = User.objects.get(id=user_id)
        except:
            raise serializers.ValidationError('Wrong invite code')
        if inviter:
            return super().validate(attrs)
        else:
            raise serializers.ValidationError('Wrong invite code')

    
class TeacherProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model = TeacherProfile
        fields = [
            'name',
            'last_name',
            'primary_subject',
            'created',
            'updated',
            'invite_code',
            'user'
        ]
        read_only_fields = ['updated', 'invite_code']
        extra_kwargs = {
            'invite_code': {'read_only': True}
        }


class StudentProfileSerializer(serializers.ModelSerializer):
    group = serializers.StringRelatedField(many=False)
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model = StudentProfile
        fields = [
            'name',
            'last_name',
            'created',
            'updated',
            'group',
            'id',
            'user',
        ]
        read_only_fields = ['updated', 'group']

class GuardianProfileSerializer(serializers.ModelSerializer):
    students = UserSerializer(many=True, read_only=True)
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model = GuardianProfile
        fields = [
            'name',
            'last_name',
            'created',
            'updated',
            'students',
            'user'
        ]
        read_only_fields = ['updated']

class StudentGroupSerializer(serializers.ModelSerializer):
    students = StudentProfileSerializer(many=True, read_only=False)
    class Meta:
        model = StudentGroup
        fields = [
            'name',
            'creation_year',
            'specialisation',
            'students',
            'id'
        ]
    def create(self, validated_data):
        students_data = validated_data.pop('students')
        group = StudentGroup.objects.create(**validated_data)
        for student_data in students_data:
            student, created = StudentProfile.objects.get_or_create(**student_data)
            group.students.add(student)
        return group
    
    def update(self, instance, validated_data):
        students_data = validated_data.pop('students')
        instance = super(StudentGroupSerializer, self).update(instance, validated_data)
        for student_data in students_data:
            student, created = StudentProfile.objects.get_or_create(**student_data)
            instance.students.add(student)
        return instance
