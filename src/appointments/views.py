from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Appointment
from .forms import NewAppointmentForm

# Create your views here.


def appointments(request):

    appointments = []
    if not request.user.is_staff:
        appointments = Appointment.objects.all().filter(patient_id=request.user.id)
    else:
        appointments = Appointment.objects.all()

    for appointment in appointments:
        appointment.appointment_time = Appointment.choices_slots[appointment.appointment_time][1]

    return render(request, 'appointments.html', {"object_list": appointments})


def new_appointment(request):
    if request.POST:
        if not request.user.is_staff:
            updated_request = request.POST.copy()
            updated_request.update({'patient': request.user})
            form = NewAppointmentForm(updated_request)
        else:
            form = NewAppointmentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, f'New record has been added.')
            return redirect('appointments')
    else:
        form = NewAppointmentForm()
        form.fields['doctor'].queryset = User.objects.filter(groups__name='Doctor')
        form.fields['patient'].queryset = User.objects.filter(groups__name='Patient')
        if not request.user.is_staff:
            form.fields['patient'].widget = form.fields['patient'].hidden_widget()
    return render(request, 'new_appointment.html', {"form" : form})


def edit_appointment(request, pk):
    appointment = Appointment.objects.get(pk=pk)
    if request.POST.get("delete"):
        appointment.delete()
        messages.error(request, f'Appointment has been delete.')
        return redirect('appointments')
    elif request.POST.get("confirm"):
        appointment.delete()
        messages.error(request, f'Appointment has been confirmed.')
        return redirect('appointments')
    elif request.POST.get('edit'):
        form = NewAppointmentForm(request.POST, instance=appointment)
        if form.is_valid():  # For more security might wanna add valiation so you can't manually(through html) assign nondoctor users to doctor
            form.save()
            messages.success(request, f'Record has been edited.')
            return redirect('appointments')
    else:
        form = NewAppointmentForm(instance=appointment)
        form.fields['doctor'].queryset = User.objects.filter(groups__name='Doctor')
        form.fields['patient'].queryset = User.objects.filter(groups__name='Patient')
        if not request.user.is_staff:
            form.fields['patient'].widget = form.fields['patient'].hidden_widget()

    return render(request, "edit_appointment.html", {"form" : form})


