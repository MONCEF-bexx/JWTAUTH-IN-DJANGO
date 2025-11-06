from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    owner = models.ForeignKey('Teacher',on_delete=models.CASCADE,related_name='students')

    def __str__(self):
        return self.name
    
class Teacher(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(unique=True)
    owner = models.OneToOneField(User,on_delete=models.CASCADE,related_name ='teacher')

    def __str__(self):
        return self.name