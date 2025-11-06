from rest_framework import serializers
from .models import Student,Teacher 
from django.contrib.auth.models import User
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'email', 'owner']

class TeacherSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True)
    owner = serializers.ReadOnlyField(source = 'owner.username')
    class Meta:
        model = Teacher 
        fields = ['id','name','email','students','owner']

class UserSerializer(serializers.ModelSerializer):
    class Meta :
        model = User 
        fields = ['id','email']