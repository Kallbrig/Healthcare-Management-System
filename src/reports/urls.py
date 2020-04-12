"""reports URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
"""


from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views as reports_views


urlpatterns = [
    # path('reports_list/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('', reports_views.ReportListView.as_view(), name='report-list'),
    path('<int:pk>/', reports_views.ReportDetailView.as_view(), name='report'),




]
