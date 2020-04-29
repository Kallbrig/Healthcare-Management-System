from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views as portals_views

urlpatterns = [

    path('', portals_views.portal, name='portal'),
    path('profile/', portals_views.profile, name='profile'),
    path('nurse_salary/', portals_views.nurse_salary.as_view(), name='nurse-salary'),
    path('doctor_salary/', portals_views.doctor_salary.as_view(), name='doctor-salary'),
    path('edit_nurse_salary/<int:pk>/', portals_views.edit_nurse_salary.as_view(), name='edit-nurse-salary'),
    path('edit_doctor_salary/<int:pk>/', portals_views.edit_doctor_salary.as_view(), name='edit-doctor-salary'),

]
