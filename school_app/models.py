# school_app/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    # Add more fields as needed

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Add more fields as needed

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateField()
    # Add more fields as needed

class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # Add more fields as needed

class Grade(models.Model):
    enrollment = models.ForeignKey('Enrollment', on_delete=models.CASCADE)
    grade_value = models.FloatField()
    # Add more fields as needed

# class UserModel(AbstractUser):
#     role = models.ForeignKey('Roles', on_delete=models.CASCADE)