from django.db import models
from django.contrib.auth.models import User


# Create your models here.
#
# class Record(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f'{self.user.email} {self.user.first_name}'


class Patient(models.Model):
	patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Patient')
	patientAddress = models.CharField(max_length=50)
	patientPhone = models.IntegerField()
	patientSSN = models.IntegerField()
	patientInsurance = models.CharField(max_length =50)
    #doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Doc')

def __str__ (self):
	return self.patient.get_full_name