from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView, DetailView, UpdateView
from django.contrib.auth.models import User
from accounts.models import Doctor, Nurse


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

def doctor_salary(request):
	doctors = Doctor.objects.all()
	context = {'doctors': doctors}
	return render(request, 'doctor_salary.html', context)


def nurse_salary(request):
	nurses = Nurse.objects.all()
	context = {'nurses': nurses}
	return render(request, 'nurse_salary.html', context)