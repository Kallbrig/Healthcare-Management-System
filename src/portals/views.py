from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, DetailView, UpdateView, FormView
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from accounts.models import Doctor, Nurse
from .forms import UpdateNurseForm, UpdateDoctorForm


# Create your views here.
def patient_portal(request):
    return render(request, 'patient_portal.html', {'title': 'Patient-portal'})


def ceo_portal(request):
    return render(request, 'CEO_portal.html', {'title': 'Ceo-portal'})


def doctor_portal(request):
    return render(request, 'doctor_portal.html', {'title': 'Doctor-portal'})


def staff_portal(request):
    return render(request, 'staff_portal.html', {'title': 'Staff-portal'})


def nurse_portal(request):
    return render(request, 'nurse_portal.html', {'title': 'Nurse-portal'})


def profile(request):
    return render(request, 'profile.html', {'title': 'Profile'})


class doctor_salary(ListView):
    model = Doctor
    template_name = 'doctor_salary.html'

class nurse_salary(ListView):
    model = Nurse
    template_name = 'nurse_salary.html'




class edit_nurse_salary(UpdateView):
    model = Nurse
    fields = ['salary']
    template_name = 'edit_nurse_salary.html'
    success_url = reverse_lazy('nurse-salary')

class edit_doctor_salary(UpdateView):
    model = Doctor
    fields = ['salary']
    template_name = 'edit_doctor_salary.html'
    success_url = reverse_lazy('doctor-salary')


# class edit_doctor_salary(FormView):
# 	model = Doctor
# 	form_class =
#
# 	def form_valid(self, form):
# 		form.save()
#
# 		return super().form_valid(form)


# class ContactView(FormView):
#     template_name = 'nurse_salary.html'
#     form_class = UpdateNurseForm
#     success_url = ''
#
#     def form_valid(self, form):
#         # This method is called when valid form data has been POSTed.
#         # It should return an HttpResponse.
#         form.send_email()
#         return super().form_valid(form)
