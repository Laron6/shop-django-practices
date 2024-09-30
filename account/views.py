from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.http import HttpRequest

from account.forms import RegisterForm, LoginForm, ProfileForm
from account.models import Profile


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт {username} был успешно создан!')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'account/register.html', {'form': form})


def login_user(request: HttpRequest):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', context={
        'title': 'Авторизация',
        'form': form,
    })


@login_required(login_url='login')
def profile_view(request: HttpRequest):
    user = Profile.objects.select_related('user').get(user=request.user)
    return render(request, 'account/profile.html', context={
        'user': user
    })


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'account/edit_profile.html', {'form': form})
