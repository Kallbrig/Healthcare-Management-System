from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.contrib.auth.models import User, Group
from accounts.models import Patient
from records.models import Record
from records.forms import NewRecordForm, NewPatientForm
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin, AccessMixin


class RecordUserList(UserPassesTestMixin, ListView):
    template_name = 'records_list.html'
    model = Record

    def test_func(self):
        if self.request.user in Group.objects.get(

                name='Staff').user_set.all() or self.request.user in Group.objects.get(
            name='Nurse').user_set.all() or self.request.user in Group.objects.get(
            name='CEO').user_set.all() or self.request.user in Group.objects.get(name='Doctor').user_set.all():
            return True
        else:
            return False


class Records(UserPassesTestMixin, ListView):
    template_name = 'record.html'
    model = Record

    def test_func(self):
        if self.request.user in Group.objects.get(
                name='Staff').user_set.all() or self.request.user in Group.objects.get(
            name='Nurse').user_set.all() or self.request.user in Group.objects.get(
            name='CEO').user_set.all() or self.request.user in Group.objects.get(name='Doctor').user_set.all():

            return True
        else:
            return False

    def get_queryset(self):
        id = self.kwargs["pk"]
        records = Record.objects.all()
        record_list = records.filter(patient_id=id)
        return record_list


class new_record(UserPassesTestMixin,CreateView):
    model = Record
    template_name = 'new_record.html'
    form_class = NewRecordForm

    def test_func(self):
        if self.request.user in Group.objects.get(name='Staff').user_set.all():
            return True
        else:
            return False


class new_patient(CreateView):
    model = Patient
    template_name = 'new_patient.html'
    form_class = NewPatientForm

    def test_func(self):
        if self.request.user in Group.objects.get(name='Staff').user_set.all():
            return True
        else:
            return False


class edit_record(UpdateView):
    model = Record
    template_name = 'edit_record.html'
    form_class = NewRecordForm

    def test_func(self):
        if self.request.user in Group.objects.get(name='Nurse').user_set.all() or self.request.user in Group.objects.get(name='Doctor').user_set.all() or self.request.user in Group.objects.get(name='Staff').user_set.all():
            return True
        else:
            return False

    # def get_queryset(self):
    #     patients = Patient.objects.all()
    #     patient_list = []
    #     for patient in patients:
    #         if patient not in patient_list:
    #             patient_list.extend(User.objects.filter(id=patient.patient.id))
    #     return patient_list

# def new_patient(request):
#     if request.POST:
#         form = NewPatientForm(request.POST)
#         if form.is_valid():
#             form = form.clean()
#             user = form.get('patient')
#             patient_address = form.get('patientAddress')
#             patient_phone = form.get('patientPhone')
#             patient_ssn = form.get('patientSSN')
#             patient_insurance = form.get('patientInsurance')
#             Patient(patient=user, patientAddress=patient_address, patientPhone=patient_phone,
#                     patientSSN=patient_ssn, patientInsurance=patient_insurance, ).save()
#
#             messages.success(request, f'New patient has been added.')
#             return redirect('Record-User-List')
#     else:
#         form = NewPatientForm()
#         form.fields['patient'].queryset = User.objects.filter(groups__name='Patient')
#     return render(request, 'new_patient.html', {'title': 'New-patient', "new_patient_form": form})


# def new_record(request, pk):
#     if request.POST:
#         form = NewRecordForm(request.POST)
#         if form.is_valid():  # For more security might wanna add valiation so you can't manually(through html) assign nondoctor users to doctor
#             instance = form.save(commit=False)
#             instance.patient_id = pk
#             instance.save()
#             messages.success(request, f'New record has been added.')
#             return redirect('Record', pk=pk)
#     else:
#         form = NewRecordForm()
#         form.fields['doctor'].queryset = User.objects.filter(groups__name='Doctor')
#     return render(request, 'new_record.html', {'title': 'New-record', "new_record_form": form})


#
# def edit_record(request, id):
#     record = Record.objects.all().get(id=id)
#     if request.POST:
#         form = NewRecordForm(request.POST, instance=record)
#         if form.is_valid():  # For more security might wanna add valiation so you can't manually(through html) assign nondoctor users to doctor
#             form.save()
#             messages.success(request, f'Record has been edited.')
#             return redirect('Record', pk=record.patient_id)
#     else:
#         form = NewRecordForm(instance=record)
#         form.fields['doctor'].queryset = User.objects.filter(
#             groups__name='Doctor')
#
#     return render(request, 'edit_record.html',
#                   {"form": form})  # can reuse the 'new_record.html' if you think it's going to be cleaner


# Create your views here.


# class RecordUserList(ListView):
#     template_name = 'records_list.html'
#     model = User
#     ordering = ['-last_name']
#     paginate_by = 25
#
#     def get_queryset(self):
#         patients = Patient.objects.all()
#         patient_list = []
#         for patient in patients:
#             if patient not in patient_list:
#                 patient_list.extend(User.objects.filter(id=patient.patient.id))
#         return patient_list
