# fees_payment/models.py

from django.db import models
from school_app.models import Student

class Fee(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField(auto_now_add=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.student} - {self.amount} - {self.payment_date}"
