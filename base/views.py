from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import *
from .forms import *

def home(request):
    if request.user.is_authenticated: 
        if request.method == 'POST':
            configuration = Configuration.objects.create(customer=request.user.customer, name=f'{request.user.customer}s {request.POST.get("radio-1", "")}')
            if 'add-to-cart' in request.POST:
                order_item = OrderItem.objects.create(customer=request.user.customer, configuration=configuration)
                order = Order.objects.filter(customer=request.user.customer, is_completed=False)
                if order.exists():
                    if order[0].configurations.filter(configuration__id=configuration.id, order__customer=request.user.customer).exists():
                        order_item.quantity += 1
                        order_item.save()
                        messages.info(request, "This items quantity was updated")
                    else:
                        order[0].configurations.add(order_item)
                        messages.info(request, "This item was added to your cart")
                else:
                    ordered_date = timezone.now()
                    order = Order.objects.create(customer=request.user.customer, date_ordered=ordered_date)
                    order.configurations.add(order_item)
                    messages.info(request, "This item was added to your cart")
            elif 'save-and-quit' in request.POST:
                pass

            for item in request.POST:
                if item != 'csrfmiddlewaretoken' and item != 'add-to-cart' and item != 'save-and-quit':
                    if 'add-to-cart' in request.POST:
                        chosen_item = get_object_or_404(Item, id=request.POST.get(item, ""))
                        configuration_item, created = ConfigurationItem.objects.get_or_create(item=chosen_item, customer=request.user.customer)
                        configuration.configuration_items.add(chosen_item)
                    elif 'save-and-quit' in request.POST:
                        chosen_item = get_object_or_404(Item, id=request.POST.get(item, ""))
                        configuration_item, created = ConfigurationItem.objects.get_or_create(item=chosen_item, customer=request.user.customer)
                        configuration.configuration_items.add(chosen_item)

    items = Item.objects.all()
    categories = Category.objects.all()
    max_steps = categories.count()
    configuration_items = [
        Item.objects.filter(category=1),
        Item.objects.filter(category=2),
        Item.objects.filter(category=3),
        Item.objects.filter(category=4),
        Item.objects.filter(category=5),
        Item.objects.filter(category=6),
        Item.objects.filter(category=7)
    ]

    order = []
    if request.user.is_authenticated:
        try:
            order = Order.objects.get(customer=request.user.customer, is_completed=False)
        except ObjectDoesNotExist:
            order = []
    
    staff_picks = Configuration.objects.filter(is_staff_pick=True)
    staff_picks_indexes = range(len(staff_picks))

    context = {
        'items': items,
        'order': order,
        'categories': categories,
        'max_steps': max_steps,
        'configuration_items': configuration_items,
        'staff_picks': staff_picks,
        'staff_picks_indexes': staff_picks_indexes
    }
    return render(request, 'base/home.html', context)

def configurator(request):
    guitar_models = Item.objects.filter(category=1)
    configuration_items = [
        Item.objects.filter(category=2),
        Item.objects.filter(category=3),
        Item.objects.filter(category=4),
        Item.objects.filter(category=5),
        Item.objects.filter(category=6),
        Item.objects.filter(category=7)
    ]

    context = {
        'guitar_models': guitar_models,
        'configuration_items': configuration_items
    }
    return render(request, 'base/configurator/configurator.html', context)

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
    configurations = Configuration.objects.filter(customer=request.user.customer)

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
        'configurations': configurations,
    }
    return render(request, 'base/account/account.html', context)

def logout_user(request):
    logout(request)
    return redirect('home')
    
def add_to_cart(request, item_id, *args, **kwargs):
    configuration = get_object_or_404(Configuration, id=item_id)
    order_item, created = OrderItem.objects.get_or_create(configuration=configuration, customer=request.user.customer)
    order = Order.objects.filter(customer=request.user.customer, is_completed=False)
    if order.exists():
        if order[0].configurations.filter(configuration__id=configuration.id, order__customer=request.user.customer).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This items quantity was updated")
        else:
            order[0].configurations.add(order_item)
            messages.info(request, "This item was added to your cart")
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(customer=request.user.customer, date_ordered=ordered_date)
        order.configurations.add(order_item)
        messages.info(request, "This item was added to your cart")
    return redirect('home')

def remove_from_cart(request, item_id, *args, **kwargs):
    configuration = get_object_or_404(Configuration, id=item_id)
    order = Order.objects.filter(customer=request.user.customer, is_completed=False)
    if order.exists():
        if order[0].configurations.filter(configuration__id=configuration.id).exists():
            order_item = OrderItem.objects.filter(configuration=configuration)[0]
            order_item.delete()
            messages.info(request, "This item was removed to your cart")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect('home')
    else:
        messages.info(request, "User does not have an order")
        return redirect('home')
    return redirect('home')