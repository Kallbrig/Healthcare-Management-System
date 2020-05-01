from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User, Group
from django.urls import reverse



class Patient(models.Model):
    patient = models.OneToOneField(User, limit_choices_to={'groups': 3, }, on_delete=models.CASCADE,
                                related_name='Patient')
    patientAddress = models.CharField(max_length=50)
    patientPhone = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    patientSSN = models.CharField(max_length=9, validators=[RegexValidator(r'^\d{1,10}$')])
    patientInsurance = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])

    def __str__(self):
        return self.patient.get_full_name()

    def get_absolute_url(self):
        return reverse('new_patient')


class Doctor(models.Model):
    doctor = models.OneToOneField(User, limit_choices_to={'groups': 1, }, on_delete=models.CASCADE, related_name='Doctor')
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    health_service_income = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.doctor.get_full_name()

    def get_absolute_url(self):
        return reverse('doctor-salary')


class Nurse(models.Model):
    nurse = models.OneToOneField(User, limit_choices_to={'groups': 2, }, on_delete=models.CASCADE, related_name='Nurse')
    salary = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nurse.get_full_name()

    def get_absolute_url(self):
        return reverse('nurse-salary')




# from django.db import models
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver
#
#
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     phone_number = models.IntegerField(max_length=10, blank=True)
#     location_as_zip = models.PositiveIntegerField(max_length=5,blank=False)
#     recieve_alerts = models.BooleanField(default=False,blank=False)
#
#
#
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()