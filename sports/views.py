# sports/views.py

from django.shortcuts import render
from .models import Sport

def sport_list(request):
    sports = Sport.objects.all()
    return render(request, 'sport_list.html', {'sports': sports})