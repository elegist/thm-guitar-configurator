from django.shortcuts import render

# Create your views here.

configurators = [
    {'id': 1, 'name': 'Choose a Type'},
    {'id': 2, 'name': 'Pick a color'},
    {'id': 3, 'name': 'Choose Pickups'},
]

def home(request):
    return render(request, 'base/home.html', {'configurators': configurators})

def configurator(request):
    return render(request, 'base/configurator.html')
