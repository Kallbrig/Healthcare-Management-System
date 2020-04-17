from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView
from django.contrib.auth.models import User


# Create your views here.


class ReportUserList(ListView):
    template_name = 'records_list.html'
    model = User
    ordering = ['-last_name']
    paginate_by = 25


class Record(DetailView):
    model = User
    template_name = 'record.html'
    context_object_name = 'record'
