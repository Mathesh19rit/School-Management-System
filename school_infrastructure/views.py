# school_infrastructure/views.py

from django.shortcuts import render
from .models import Building, Facility

def building_list(request):
    buildings = Building.objects.all()
    return render(request, 'building_list.html', {'buildings': buildings})

def facility_list(request):
    facilities = Facility.objects.all()
    return render(request, 'facility_list.html', {'facilities': facilities})
