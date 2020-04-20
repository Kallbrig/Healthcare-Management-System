from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView, DetailView, UpdateView
from django.contrib.auth.models import User
from accounts.models import Patient
from records.models import Record
from records.forms import NewRecordForm


# Create your views here.


class RecordUserList(ListView):
    template_name = 'records_list.html'
    model = User
    ordering = ['-last_name']
    paginate_by = 25

    def get_queryset(self):
        patients = Patient.objects.all()
        patient_list = []
        for patient in patients:
            patient_list.extend(User.objects.filter(id=patient.patient.id))
        return patient_list





class Records(ListView):
    template_name = 'record.html'
    model = Record
    paginate_by = 25

    def get_queryset(self):
        id = self.kwargs["pk"]
        records = Record.objects.all()
        record_list = records.filter(patient_id = id)
        return record_list





def new_patient(request):
	return render(request, 'new_patient.html', {'title': 'New-patient'})


def new_record(request,pk):
    if request.POST:
        form = NewRecordForm(request.POST)
        if form.is_valid(): #For more security might wanna add validation so you can't manually(through html) assign nondoctor users to doctor
            instance = form.save(commit=False)
            instance.patient_id = pk
            instance.save()
            messages.success(request, f'New record has been added.')
            return redirect('Record',pk=pk)
    else:
        form = NewRecordForm()
        form.fields['doctor'].queryset = User.objects.filter(
            groups__name='Doctor')
    return render(request, 'new_record.html', {'title': 'New-record', "new_record_form":form})