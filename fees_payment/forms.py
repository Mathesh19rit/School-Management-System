# fees_payment/forms.py

from django import forms
from .models import Fee

class FeePaymentForm(forms.ModelForm):
    class Meta:
        model = Fee
        fields = ['student', 'amount', 'description']
