from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, Group
from django.urls import reverse
import django


from django.template.defaultfilters import slugify
from django.utils import timezone


# Create your models here.


class Record(models.Model):
    choices_feet = (
        (0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
    )
    choices_inches = (
        (0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
        (11, '11'),
    )
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Pat')
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Doc')
    # THESE DEFAULT TO NOW. THEY SHOULD DEFAULT TO APPOINTMENT TIME
    appointment_date = models.DateField(default=timezone.now)
    appointment_time = models.TimeField(default=timezone.now)
    weight_lbs = models.PositiveIntegerField(blank=True, default=0)
    height_feet = models.PositiveSmallIntegerField(choices=choices_feet, default=0, blank=True)
    height_inches = models.PositiveSmallIntegerField(choices=choices_inches, default=0, blank=True)
    blood_pressure = models.CharField(blank=True, default='0/0', max_length=7)
    pulse = models.PositiveIntegerField(blank=True, default=0, )
    reason_for_visit = models.CharField(max_length=100, blank=True, null=True, )
    prescription = models.CharField(max_length=50, blank=True, null=True)
    treatment = models.TextField(max_length=500, blank=True, null=False, )

    def __str__(self):
        return self.patient.__str__() + " - " + self.appointment_date.__str__()

    def get_absolute_url(self):
        return reverse('', kwargs={'pk': self.pk})
