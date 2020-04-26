from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Appointment(models.Model):

    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="PatientAppointment")
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    appointment_date = models.DateField(default=timezone.now)
    appointment_time = models.TimeField(default=timezone.now)


    def __str__(self):
        return self.patient.__str__() + " - " + self.appointment_date.__str__()

    def get_absolute_url(self):
        return reverse('', kwargs={'pk': self.pk})