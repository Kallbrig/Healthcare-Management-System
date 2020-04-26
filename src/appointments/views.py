from django.shortcuts import render

# Create your views here.

def appointments(request):
    return  render(request, 'appointments.html')