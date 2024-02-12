# school_app/views.py

from django.shortcuts import render
from django.http import HttpResponse
from .models import Student, Course, Enrollment, Teacher, Grade
from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm

class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'registration/login.html'

def student_list(request):
    # Retrieve and display a list of students
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})
   
def course_list(request):
    # Retrieve and display a list of courses
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})
    
def enrollment_list(request):
    # Retrieve and display a list of enrollments
    return HttpResponse("List of Enrollments")

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher_list.html', {'teachers': teachers})

def grade_list(request):
    grades = Grade.objects.all()
    return render(request, 'grade_list.html', {'grades': grades})

