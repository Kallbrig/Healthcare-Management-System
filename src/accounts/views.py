from django.shortcuts import render, redirect
from django.http import HttpResponse
# from .models import Record
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin, AccessMixin



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
