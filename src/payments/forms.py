from django import forms
from django.contrib.auth.models import User
from . import models


class PaymentForm(forms.Form):
    payment_amount = forms.DecimalField(max_digits=8, decimal_places=2, min_value=0)
    invoice_number = forms.IntegerField(min_value=0)
    class Meta:
        model = models.Payment

        fields = [
            'payment_amount',
            'invoice_number',

        ]
