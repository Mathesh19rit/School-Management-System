# school_app/urls.py

from django.urls import path
from . import views
from .views import CustomLoginView


urlpatterns = [
    path('students/', views.student_list, name='student_list'),
    path('courses/', views.course_list, name='course_list'),
    path('enrollments/', views.enrollment_list, name='enrollment_list'),
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('grades/', views.grade_list, name='grade_list'),
    path('login/', CustomLoginView.as_view(), name='login'),
]