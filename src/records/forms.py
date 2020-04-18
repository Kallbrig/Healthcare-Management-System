from django import forms
from accounts.models import Patient 


class newRecordForm(forms.ModelForm):
	class Meta:
		fields = ['patientAddress', 'patientPhone', 'PatientSSN', 'PatientInsurance']