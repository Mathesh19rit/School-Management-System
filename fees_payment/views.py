# fees_payment/views.py

from django.shortcuts import render, redirect
from .models import Fee
from .forms import FeePaymentForm

def fees_payment_list(request):
    fees = Fee.objects.all()
    return render(request, 'fees_payment_list.html', {'fees': fees})

def fees_payment_create(request):
    if request.method == 'POST':
        form = FeePaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fees_payment_list')
    else:
        form = FeePaymentForm()
    return render(request, 'fees_payment_form.html', {'form': form})
