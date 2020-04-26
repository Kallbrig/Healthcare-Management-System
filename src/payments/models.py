from django.db import models
from django.contrib.auth.models import User
from django.contrib.admin.utils import timezone


# When records and payments are merged, we may want to integrate a record to an invoice so they're linked.


# Create your models here.
class Invoice(models.Model):
    # invoice number is it's primary key
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    amount_owed = models.DecimalField(decimal_places=2, max_digits=8)
    amount_billed = models.DecimalField(decimal_places=2, max_digits=8)
    date_billed = models.DateField(default=timezone.now)


    def amount_owed_as_string(self):
        return str(self.amount_owed)

    def __str__(self):
        return str(self.pk) + " - " + str(self.amount_billed)


class Payment(models.Model):
    payment_method = models.CharField(max_length=15)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    payment_amount = models.DecimalField(decimal_places=2, max_digits=8)

    def __str__(self):
        return str(self.invoice.pk) + " - " + str(self.payment_amount)
