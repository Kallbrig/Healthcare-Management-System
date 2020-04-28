from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views as portals_views

urlpatterns = [
    path('patient_portal/', portals_views.patient_portal, name='patient-portal'),
    path('ceo_portal/', portals_views.ceo_portal, name='ceo-portal'),
    path('doctor_portal/', portals_views.doctor_portal, name='doctor-portal'),
    path('staff_portal/', portals_views.staff_portal, name='staff-portal'),
    path('nurse_portal/', portals_views.nurse_portal, name='nurse-portal'),
    path('profile/', portals_views.profile, name='profile'),
    path('nurse_salary/', portals_views.nurse_salary.as_view(), name='nurse-salary'),
    path('doctor_salary/', portals_views.doctor_salary.as_view(), name='doctor-salary'),
    path('edit_nurse_salary/<int:pk>/', portals_views.edit_nurse_salary.as_view(), name='edit-nurse-salary'),
    path('edit_doctor_salary/<int:pk>/', portals_views.edit_doctor_salary.as_view(), name='edit-nurse-salary'),

]