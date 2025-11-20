from django.shortcuts import render
from rest_framework.permissions import BasePermission
from rest_framework import viewsets,serializers
from .models import Student, Teacher , User
from .serializer import StudentSerializer, TeacherSerializer
from rest_framework.exceptions import ValidationError 

class IsStudent(BasePermission):
    def has_permission(self,request,view):
        if request.user.role.lower() == 'student':
            return True

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff :
            return True
        return request.user == getattr(getattr(obj,'teacher',None),'user',None) 
    

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role in ['admin','ADMIN']


class IsTeacher(BasePermission):
    def has_permission(self,request,view):
        return request.user.role in ['teacher','TEACHER']
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff  :
            return True
        else : 
            return request.user.role in ['teacher','TEACHER']


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    permission_classes = [IsOwner|IsTeacher]

    def get_queryset(self):
        if self.request.user.is_staff :
                return Student.objects.all()
        if self.request.user.role in ['teacher','TEACHER'] :
            teacher = Teacher.objects.get(user=self.request.user)
            return Student.objects.filter(teacher=teacher)
        return Student.objects.filter(user=self.request.user)
    def perform_create(self,serializer):
        if self.request.user.role in ['teacher','TEACHER'] : 
            teacher = Teacher.objects.get(user = self.request.user)
            try :
                user = User.objects.get(email = self.request.user).first()
            except user.DoesNotExist :
                raise ValidationError(f"No user found with email '{self.request.user.email}'")
            serializer.save(user=user , teacher=teacher)
    
class TeacherViewSet(viewsets.ModelViewSet):
    serializer_class = TeacherSerializer
    permission_classes = [IsAdmin|IsTeacher]
    def get_queryset(self):
        if self.request.user.is_staff : 
            return Teacher.objects.all()
        return Teacher.objects.all().filter(user = self.request.user)
    def perform_create(self,serializer):
        user = User.objects.all().filter(email = serializer.validated_data.get("email")).first()
        if  user and user.role.lower() =='teacher':
            serializer.save(user=user)
        else :
            raise ValidationError("this email does not exist")