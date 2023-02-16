from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import Category, Item, StaffPickItem, StaffPick
from .forms import RegisterForm, UpdateUserForm
from django.contrib import messages
# Create your views here.

def home(request):
    steps = Category.objects.all()
    models = Item.objects.filter(category=1)
    frets = Item.objects.filter(category=2)
    woods = Item.objects.filter(category=3)
    colors = Item.objects.filter(category=4)
    electronics = Item.objects.filter(category=5)
    hardware = Item.objects.filter(category=6)

    StratocasterStaff = StaffPickItem.objects.filter(staffPick = 1)
    TelecasterStaff = StaffPickItem.objects.filter(staffPick = 2)
    LesPaulStaff = StaffPickItem.objects.filter(staffPick = 3)
    FlyingVStaff = StaffPickItem.objects.filter(staffPick = 4)
    staffPicks = [StaffPickItem.objects.filter(staffPick = 1), StaffPickItem.objects.filter(staffPick = 2), StaffPickItem.objects.filter(staffPick = 3), StaffPickItem.objects.filter(staffPick = 4)]
    staffPicksIndex = range(len(staffPicks))
    stratIndex = range(len(StratocasterStaff))

    stratocasterTotal = 0
    for index in stratIndex:
        stratocasterTotal += StratocasterStaff[index].item.price

    context = {
        'steps': steps,
        'models': models,
        'frets': frets,
        'woods': woods,
        'colors': colors,
        'electronics': electronics,
        'hardware': hardware,
        'StratocasterStaff': StratocasterStaff,
        'TelecasterStaff': TelecasterStaff,
        'LesPaulStaff': LesPaulStaff, 
        'FlyingVStaff': FlyingVStaff,
        'staffPicks': staffPicks,
        'staffPicksIndex': staffPicksIndex,
        'stratocasterTotal': stratocasterTotal
    }
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
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')
    
    context = {'form': form}
    return render(request, 'base/account/register.html', context)

@login_required(login_url='login')
def account_view(request):
    update_user_form = UpdateUserForm(instance=request.user)
    if request.method == 'POST':
        update_user_form = UpdateUserForm(request.POST, instance=request.user)
        if update_user_form.is_valid():
            update_user_form.save()
            user = update_user_form.cleaned_data.get('username')
            messages.success(request, 'Account informations changed for ' + user)
            return redirect('account')

    context = {
        'update_user_form': update_user_form,
    }
    return render(request, 'base/account/account.html', context)

def logout_user(request):
    logout(request)
    return redirect('home')
    
