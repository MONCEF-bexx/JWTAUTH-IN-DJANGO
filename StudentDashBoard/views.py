from django.shortcuts import render
from rest_framework.permissions import BasePermission
from rest_framework import viewsets
from .models import Student, Teacher
from .serializer import StudentSerializer, TeacherSerializer

class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return obj.owner.owner == request.user
    

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff


class IsTeacher(BasePermission):
    def has_permission(self,request,view):
        return request.method == "GET" 
    def has_object_permission(self, request, view, obj):
        return obj.owner.owner == request.user and request.method == "GET"


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    permission_classes = [IsOwnerOrAdmin]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Student.objects.all()
        teacher = Teacher.objects.get(owner=self.request.user)
        return Student.objects.filter(owner=teacher)

    def perform_create(self, serializer):
        teacher = Teacher.objects.get(owner=self.request.user)
        serializer.save(owner=teacher)


class TeacherViewSet(viewsets.ModelViewSet):
    serializer_class = TeacherSerializer
    permission_classes = [IsAdmin & IsTeacher]
