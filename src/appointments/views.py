from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib import messages
from .models import Appointment
from .forms import NewAppointmentForm
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin, AccessMixin



def user_belongs_to_patient_or_doctor_group(user):
    if (user in Group.objects.get(name='Patient').user_set.all() and user.is_authenticated) or (user in Group.objects.get(name='Doctor').user_set.all() and user.is_authenticated):
        return True
    else:
        return False


@login_required()
@user_passes_test(user_belongs_to_patient_or_doctor_group)
def appointments(request):
    appointments = []
    if request.user.groups.filter(name="Patient").exists():
        appointments = Appointment.objects.all().filter(patient_id=request.user.id)
    elif request.user.groups.filter(name="Doctor").exists():
        appointments = Appointment.objects.all().filter(doctor_id=request.user.id)
    else:
        appointments = Appointment.objects.all()

    appointments = appointments.order_by("appointment_date", "appointment_time")

    for appointment in appointments:
        appointment.appointment_time = Appointment.choices_slots[appointment.appointment_time][1]

    return render(request, 'appointments.html', {"object_list": appointments})


@login_required()
def new_appointment(request):
    if request.POST:
        if request.user.groups.filter(name="Patient").exists():
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
        if request.user.groups.filter(name="Patient").exists():
            form.fields['patient'].widget = form.fields['patient'].hidden_widget()

    return render(request, 'new_appointment.html', {"form": form})


@login_required()
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
        if form.is_valid():
            form.save()
            messages.success(request, f'Record has been edited.')
            return redirect('appointments')
    else:
        form = NewAppointmentForm(instance=appointment)
        form.fields['doctor'].queryset = User.objects.filter(groups__name='Doctor')
        form.fields['patient'].queryset = User.objects.filter(groups__name='Patient')
        if request.user.groups.filter(name="Patient").exists():
            form.fields['patient'].widget = form.fields['patient'].hidden_widget()

    return render(request, "edit_appointment.html", {"form": form})
