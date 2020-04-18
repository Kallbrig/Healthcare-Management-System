"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views as records_views

urlpatterns = [
    path('', records_views.RecordUserList.as_view(), name='Record-User-List'),
    path('<int:pk>/', records_views.Records.as_view(),name='Record'),
    path('new_patient/', records_views.new_patient, name='new_patient'),
     path('new_record/', records_views.new_record, name='new_record'),

]