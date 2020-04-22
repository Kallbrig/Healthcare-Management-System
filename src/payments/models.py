from django.db import models
from django.contrib.auth.models import User


# When records and payments are merged, we may want to integrate a record to an invoice so they're linked.


# Create your models here.
class Invoice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    invoice_number = models.IntegerField()
    amount_owed = models.IntegerField()
    amount_billed = models.IntegerField()

    def __str__(self):
        return str(self.invoice_number) + " - " + str(self.amount_billed)


class Payment(models.Model):
    payment_method = models.CharField(max_length=15)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    payment_amount = models.IntegerField()

    def __str__(self):
        return str(self.invoice.invoice_number) + " - " + str(self.payment_amount)
