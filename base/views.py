from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages

def home(request):
    context = {}
    return render(request, 'base/home.html', context)

def login_user(request):
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

def register(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            user_name = register_form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user_name)
            return redirect('login')
    else:
        register_form = RegisterForm()
    
    context = {
        'register_form': register_form,
    }
    return render(request, 'base/account/register.html', context)

@login_required(login_url='login')
def account(request):
    if request.method == 'POST':
        update_user_form = UpdateUserForm(request.POST, instance=request.user)
        update_customer_form = UpdateCustomerForm(request.POST, instance=request.user.customer)
        if update_user_form.is_valid() and update_customer_form.is_valid():
            update_user_form.save()
            update_customer_form.save()
            user = update_user_form.cleaned_data.get('username')
            messages.success(request, 'Account informations changed for ' + user)
            return redirect('account')
    else:
        update_user_form = UpdateUserForm(instance=request.user)
        update_customer_form = UpdateCustomerForm(instance=request.user.customer)

    context = {
        'update_user_form': update_user_form,
        'update_customer_form': update_customer_form,
    }
    return render(request, 'base/account/account.html', context)

def logout_user(request):
    logout(request)
    return redirect('home')
    
