# school_app/forms.py

from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    role_choices = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    ]

    role = forms.ChoiceField(choices=role_choices, required=True)

