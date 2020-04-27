from django import forms
from .models import Appointment
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _



class NewAppointmentForm(forms.ModelForm):
    class Meta:
        fields = ['doctor', 'patient',  'appointment_date', 'appointment_time']
        model = Appointment

    def clean(self):
        cleaned_data = super().clean()
        doctor = self.cleaned_data.get("doctor")
        date = self.cleaned_data.get("appointment_date")
        time = self.cleaned_data.get('appointment_time')
        appointments = Appointment.objects.all().filter(appointment_time=time, appointment_date=date, doctor=doctor)
        if len(appointments) > 0:
            raise ValidationError(_('This time slot has been taken by another patient. Please choose another time.'))




