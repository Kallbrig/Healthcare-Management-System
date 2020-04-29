from django import forms
from accounts.models import Nurse, Doctor


class UpdateNurseForm(forms.ModelForm):
    new_salary = forms.DecimalField(max_digits=9, decimal_places=2)

    class Meta:
        fields = ['new_salary']
        model = Nurse

    def save(self, commit=True):
        Nurse.salary = self.new_salary
        Nurse.save()


class UpdateDoctorForm(forms.ModelForm):
    new_salary = forms.DecimalField(max_digits=9, decimal_places=2)

    class Meta:
        fields = ['new_salary']
        model = Doctor

    def save(self, commit=True):
        Doctor.salary = self.new_salary
        Doctor.save()
