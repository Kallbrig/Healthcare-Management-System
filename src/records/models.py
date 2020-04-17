from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, Group
from django.urls import reverse

from django.template.defaultfilters import slugify
from django.utils import timezone


# Create your models here.


class Record(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Pat')
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Doc')
    # THESE DEFAULT TO NOW. THEY SHOULD DEFAULT TO APPOINTMENT TIME
    appointment_date = models.DateField(default=timezone.now().date())
    appointment_time = models.TimeField(default=timezone.now().date())

    def __str__(self):
        return self.patient.__str__() + " - " + self.appointment_date.__str__()

    def get_absolute_url(self):
        return reverse('', kwargs={'pk': self.pk})
