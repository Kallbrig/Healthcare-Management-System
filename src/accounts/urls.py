from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views as account_views

from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html',), name='login'),
    path('register/', account_views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    # path('profile/', account_views.profile, name='profile'),

]
