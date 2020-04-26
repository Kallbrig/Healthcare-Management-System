from django.urls import path, include
from .views import appointments



urlpatterns = [
    path('', appointments, name="appointments"),

]