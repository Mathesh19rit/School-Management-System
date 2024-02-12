# school_infrastructure/urls.py

from django.urls import path
from .views import building_list, facility_list

urlpatterns = [
    path('buildings/', building_list, name='building_list'),
    path('facilities/', facility_list, name='facility_list'),
]
