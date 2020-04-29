from django.urls import path, include
from .views import *



urlpatterns = [
    path('', appointments, name="appointments"),
    path('new_appointment/', new_appointment, name='new_appointment'),
    path('appointment/<int:pk>', edit_appointment , name="editAppointment"),

]