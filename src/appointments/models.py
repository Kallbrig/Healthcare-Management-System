from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Appointment(models.Model):

    choices_slots = (
        (0, '08 AM'),
        (1, '09 AM'),
        (2, '10 AM'),
        (3, '11 AM'),
        (4, '12 PM'),
        (5, '01 PM'),
        (6, '02 PM'),
        (7, '03 PM'),
        (8, '04 PM'),
    )


    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="PatientAppointment")
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    appointment_date = models.DateField(default=timezone.now)
    appointment_time = models.SmallIntegerField(choices=choices_slots, blank=False)


    def __str__(self):
        return self.patient.__str__() + " - " + self.appointment_date.__str__()

    def get_absolute_url(self):
        return reverse('', kwargs={'pk': self.pk})
