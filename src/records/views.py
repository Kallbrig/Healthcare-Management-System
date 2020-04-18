from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView
from django.contrib.auth.models import User
from .models import Record


# Create your views here.


class RecordUserList(ListView):
    template_name = 'records_list.html'
    model = User
    ordering = ['-last_name']
    paginate_by = 25


class Records(DetailView):
    model = Record
    template_name = 'record.html'
    context_object_name = 'record'

def new_patient(request):
	return render(request, 'new_patient.html', {'title': 'New-patient'})


def new_record(request):
	return render(request, 'new_record.html', {'title': 'New-record'})