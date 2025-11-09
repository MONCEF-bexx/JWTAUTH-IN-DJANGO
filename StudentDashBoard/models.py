from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    class Roles(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        TEACHER = 'TEACHER', 'Teacher'
        STUDENT = 'STUDENT', 'Student'
    
    role = models.CharField(
        max_length = 20 ,
        choices = Roles.choices,
        default = Roles.STUDENT
    )
    def __str__(self):
        return f"{self.username} ({self.role})"
    


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    teacher = models.ForeignKey('Teacher',on_delete=models.SET_NULL,null=True,related_name='students')
    user = models.OneToOneField(User,on_delete = models.CASCADE,null = True)
    def __str__(self):
        return self.name
    
class Teacher(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(unique=True)
    user = models.OneToOneField(User,on_delete = models.CASCADE)

    def __str__(self):
        return self.name