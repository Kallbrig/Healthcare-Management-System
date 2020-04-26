from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import NewAppointmentForm


# Create your views here.

def appointments(request):
    return render(request, 'appointments.html')


def new_appointment(request):
    if request.POST:
        form = NewAppointmentForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = NewAppointmentForm()
        if not request.user.is_staff:
            del form.fields['patient']
        form.fields['doctor'].queryset = User.objects.filter(groups__name='Doctor')
    return render(request, 'new_appointment.html', {"form": form})
