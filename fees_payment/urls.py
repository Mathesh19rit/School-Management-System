# fees_payment/urls.py

from django.urls import path
from .views import fees_payment_list, fees_payment_create

urlpatterns = [
    path('fees-payment/', fees_payment_list, name='fees_payment_list'),
    path('fees-payment/create/', fees_payment_create, name='fees_payment_create'),
]