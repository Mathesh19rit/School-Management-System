# school_management_system/urls.py

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('school/', include('school_app.urls')),
    path('fees/', include('fees_payment.urls')),
    path('school_infrastructure/',include('school_infrastructure.urls')), 
    path('sports/', include('sports.urls')),
    path('accounts/', include('django.contrib.auth.urls')), 
]
