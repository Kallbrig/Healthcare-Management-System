from django import forms
from .models import Appointment


class NewAppointmentForm(forms.ModelForm):
    class Meta:
        fields = ['doctor','patient',  'appointment_date', 'appointment_time']
        model = Appointment
from django import forms
from .models import Appointment


class NewAppointmentForm(forms.ModelForm):
    class Meta:
        fields = ['doctor','patient',  'appointment_date', 'appointment_time']
        model = Appointment