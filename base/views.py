from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Category
from .models import Item
from .models import StaffPickItem
from .models import StaffPick
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
            return render(request, 'base/account/login.html', {'error': 'Invalid login credentials'})
    else:
        return render(request, 'base/account/login.html')

def register_view(request):
    return render(request, 'base/account/register.html')

def logout_user(request):
    logout(request)
    return redirect('home')
    
