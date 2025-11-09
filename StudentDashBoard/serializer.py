from rest_framework import serializers
from .models import Student,Teacher 
from .models import User
class StudentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='user.username')
    teacher = serializers.ReadOnlyField(source='teacher.name')
    class Meta:
        model = Student
        fields = ['id', 'name', 'email','owner','teacher']

class TeacherSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='user.username')
    students = StudentSerializer(many=True , read_only = True)
    class Meta:
        model = Teacher 
        fields = ['id','name','email','students','owner']

class UserSerializer(serializers.ModelSerializer):
    class Meta :
        model = User 
        fields = ['id','username','email','role']