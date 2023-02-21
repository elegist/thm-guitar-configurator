from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages

def home(request):
    context = {}
    return render(request, 'base/home.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')
    
    context = {}
    return render(request, 'base/account/login.html', context)

def register_view(request):
    user_form = RegisterForm()

    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            user = user_form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')
    
    context = {
        'user_form': user_form,
    }
    return render(request, 'base/account/register.html', context)

@login_required(login_url='login')
def account_view(request):
    # update_user_form = UpdateUserForm(instance=request.user)
    # if request.method == 'POST':
    #     update_user_form = UpdateUserForm(request.POST, instance=request.user)
    #     if update_user_form.is_valid():
    #         update_user_form.save()
    #         user = update_user_form.cleaned_data.get('username')
    #         messages.success(request, 'Account informations changed for ' + user)
    #         return redirect('account')

    context = {}
    return render(request, 'base/account/account.html', context)

def logout_user(request):
    logout(request)
    return redirect('home')
    
