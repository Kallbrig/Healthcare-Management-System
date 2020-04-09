from django.shortcuts import render, redirect
from django.http import HttpResponse
# from .models import Record
from django.contrib import messages
from .forms import UserRegisterForm


def login(request):
    form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'accounts/login.html', context=context)


def register(request):
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
    return render(request, 'accounts/login.html', context=context)
