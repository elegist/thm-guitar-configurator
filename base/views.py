from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from .models import Category
from .models import Item
from .models import StaffPickItem
from .models import StaffPick
from .models import RegisterForm, Cart, CartItem
from .serializers import CategorySerializer, ItemSerializer, CartSerializer, CartItemSerializer, StaffPickSerializer, StaffPickItemSerializer
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

def logout_user(request):
    logout(request)
    return redirect('home')
    

# Django rest_framework

def category_list(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return JsonResponse(serializer.data, safe=False)

def item_list(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return JsonResponse(serializer.data, safe=False)

def cart_list(request):
    carts = Cart.objects.all()
    serializer = CartSerializer(carts, many=True)
    return JsonResponse(serializer.data, safe=False)

def cartItem_list(request):
    cartItems = CartItem.objects.all()
    serializer = CartItemSerializer(cartItems, many=True)
    return JsonResponse(serializer.data, safe=False)

def staffPick_list(request):
    staffPicks = StaffPick.objects.all()
    serializer = StaffPickSerializer(staffPicks, many=True)
    return JsonResponse(serializer.data, safe=False)

def staffPickItem_list(request):
    staffPickItems = StaffPickItem.objects.all()
    serializer = StaffPickItemSerializer(staffPickItems, many=True)
    return JsonResponse(serializer.data, safe=False)