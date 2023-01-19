from django.shortcuts import render
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
    staffPicksTotals = []

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
        'staffPicksIndex': staffPicksIndex
    }
    return render(request, 'base/home.html', context)


