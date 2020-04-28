from django.db import models
from django.contrib.auth.models import User, Group
from django.urls import reverse


class Patient(models.Model):
    patient = models.ForeignKey(User, limit_choices_to={'groups': 3, }, on_delete=models.CASCADE,
                                related_name='Patient')
    patientAddress = models.CharField(max_length=50)
    patientPhone = models.IntegerField(max_length=11, )
    patientSSN = models.IntegerField(max_length=9)
    patientInsurance = models.PositiveIntegerField(max_length=12)

    def __str__(self):
        return self.patient.get_full_name()

    def get_absolute_url(self):
        return reverse('new_patient')


class Doctor(models.Model):
    doctor = models.ForeignKey(User, limit_choices_to={'groups': 1, }, on_delete=models.CASCADE, related_name='Doctor')
    salary = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.doctor.get_full_name()

    def get_absolute_url(self):
        return reverse('doctor-salary')


class Nurse(models.Model):
    nurse = models.ForeignKey(User, limit_choices_to={'groups': 2, }, on_delete=models.CASCADE, related_name='Nurse')
    salary = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nurse.get_full_name()

    def get_absolute_url(self):
        return reverse('nurse-salary')
