# sports/urls.py

from django.urls import path
from .views import sport_list

urlpatterns = [
    path('sports/', sport_list, name='sport_list'),
]

