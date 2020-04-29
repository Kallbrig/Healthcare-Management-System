from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, DetailView, UpdateView, FormView
from django.contrib.auth.models import User, Group
from accounts.models import Doctor, Nurse
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin, AccessMixin


def user_belongs_to_ceo_group(user):
    if user in Group.objects.get(name='CEO').user_set.all():
        return True
    else:
        return False


@login_required
def portal(request):
    groups = []
    if request.user in Group.objects.get(name='CEO').user_set.all():
        groups.append('ceo')

    if request.user in Group.objects.get(name='Nurse').user_set.all():
        groups.append('nurse')

    if request.user in Group.objects.get(name='Doctor').user_set.all():
        groups.append('doctor')

    if request.user in Group.objects.get(name='Patient').user_set.all():
        groups.append('patient')

    if request.user in Group.objects.get(name='Staff').user_set.all():
        groups.append('staff')

    return render(request, 'portal.html', {'title': 'Portal', 'groups': groups})


def profile(request):
    return render(request, 'profile.html', {'title': 'Profile'})


#
class doctor_salary(UserPassesTestMixin, ListView):
    model = Doctor
    template_name = 'doctor_salary.html'
    redirect_field_name = '/portals/'

    def test_func(self):
        if self.request.user in Group.objects.get(name='CEO').user_set.all():
            return True
        else:
            return False

    permission_denied_message = 'You do not have the proper permissions to access this page.'


class nurse_salary(UserPassesTestMixin, ListView):
    model = Nurse
    template_name = 'nurse_salary.html'

    def test_func(self):
        if self.request.user in Group.objects.get(name='CEO').user_set.all():
            return True
        else:
            return False

    permission_denied_message = 'You do not have the proper permissions to access this page.'


class edit_nurse_salary(UserPassesTestMixin, UpdateView):
    model = Nurse
    fields = ['salary']
    template_name = 'edit_nurse_salary.html'
    success_url = reverse_lazy('nurse-salary')

    def test_func(self):
        if self.request.user in Group.objects.get(name='CEO').user_set.all():
            return True
        else:
            return False

    permission_denied_message = 'You do not have the proper permissions to access this page.'


class edit_doctor_salary(UserPassesTestMixin, UpdateView):
    model = Doctor
    fields = ['salary']
    template_name = 'edit_doctor_salary.html'
    success_url = reverse_lazy('doctor-salary')
    redirect_field_name = '/portal/'

    def test_func(self):
        if self.request.user in Group.objects.get(name='CEO').user_set.all():
            return True
        else:
            return False

    permission_denied_message = 'You do not have the proper permissions to access this page.'
