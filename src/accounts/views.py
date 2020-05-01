from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import Patient
from django.contrib.auth.models import User, Group
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin, AccessMixin
from django.views.generic import ListView, DetailView, UpdateView, FormView
from django.urls import reverse_lazy

def login(request):
    if request.user.is_authenticated:
        return redirect('portal')
    else:
        return redirect('login')


def register(request):
    if request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created! You Can Now Logn!')
            return redirect('login')
    else:
        form = UserRegisterForm()

    context = {'form': form}
    return render(request, 'accounts/register.html', context=context)


class ViewProfile(UserPassesTestMixin, DetailView):
    template_name = 'accounts/user_profile.html'
    model = Patient

    def test_func(self):
        if self.request.user in Group.objects.get(name='Patient').user_set.all():
            return True
        else:
            return False


class EditProfile(UserPassesTestMixin, UpdateView):
    template_name = 'accounts/edit_user_profile.html'
    model = Patient

    fields = [
        'patientAddress',
        'patientPhone',
        'patientInsurance',


    ]
    success_url = '/portals/'
    def test_func(self):
        if self.request.user in Group.objects.get(name='Patient').user_set.all():
            return True
        else:
            return False
