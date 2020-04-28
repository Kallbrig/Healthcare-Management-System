from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse




class Patient(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Patient')
    patientAddress = models.CharField(max_length=50)
    patientPhone = models.IntegerField()
    patientSSN = models.IntegerField()
    patientInsurance = models.CharField(max_length=50)

    def __str__(self):
        return self.patient.get_full_name()


class Doctor(models.Model):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Doctor')
    salary = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.doctor.get_full_name()

    def get_absolute_url(self):
        return reverse('doctor-salary')


class Nurse(models.Model):
    nurse = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Nurse')
    salary = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nurse.get_full_name()

    def get_absolute_url(self):
        return reverse('nurse-salary')