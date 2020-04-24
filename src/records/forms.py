from django import forms
from records.models import Record


class NewRecordForm(forms.ModelForm):
	class Meta:
		fields = ['doctor','appointment_date', 'appointment_time', 'weight_lbs', 'height_feet', 'height_inches', 'blood_pressure', 'pulse', 'reason_for_visit', 'prescription', 'treatment']
		model = Record