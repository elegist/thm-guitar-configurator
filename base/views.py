from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import *
from .forms import *

def home(request):
    if request.method == 'POST':
        try:
            customer = request.user.customer
        except:
            device = request.COOKIES['device']
            customer, created = Customer.objects.get_or_create(device=device)

        configuration = Configuration.objects.create(customer=customer, name=f'Configuration {request.POST.get("radio-1", "")}')
        if 'add-to-cart' in request.POST:
            for item in request.POST:
                if item != 'csrfmiddlewaretoken' and item != 'add-to-cart' and item != 'save-and-quit':
                    chosen_item = get_object_or_404(Item, id=request.POST.get(item, ""))
                    configuration.configuration_items.add(chosen_item)
            return redirect('add-to-cart', item_id=configuration.id)
        elif 'save-and-quit' in request.POST:
            for item in request.POST:
                if item != 'csrfmiddlewaretoken' and item != 'add-to-cart' and item != 'save-and-quit':
                    chosen_item = get_object_or_404(Item, id=request.POST.get(item, ""))
                    configuration.configuration_items.add(chosen_item)
            return redirect('account')
        
        order = Order.objects.get(customer=customer, is_completed=False)
    else:
        try:
            if request.user.is_authenticated:
                customer = request.user.customer
            else:
                customer = Customer.objects.get(device=request.COOKIES['device'])
            order = Order.objects.get(customer=customer, is_completed=False)
        except:
            order = []

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

def login_user(request):
    if request.user.is_authenticated:
        return redirect('account')
    else:
        try:
            customer = Customer.objects.get(device=request.COOKIES['device'])
            order = Order.objects.get(customer=customer, is_completed=False)
        except:
            order = []
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')
    
    context = {
        'order': order
    }
    return render(request, 'base/account/login.html', context)

def register(request):
    if request.user.is_authenticated:
        return redirect('account')
    else:
        try:
            customer = Customer.objects.get(device=request.COOKIES['device'])
            order = Order.objects.get(customer=customer, is_completed=False)
        except:
            order = []
        if request.method == 'POST':
            register_form = RegisterForm(request.POST)
            if register_form.is_valid():
                user = register_form.save()
                # guest_customer = Customer.objects.filter(device=request.COOKIES['device'])
                # if guest_customer.exists():
                #     guest_customer.update(user=user)
                # else:
                Customer.objects.create(user=user)
                user_name = register_form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user_name)
                return redirect('login')
        else:
            register_form = RegisterForm()

    context = {
        'register_form': register_form,
        'order': order
    }
    return render(request, 'base/account/register.html', context)

@login_required(login_url='login')
def account(request):
    try:
        order = Order.objects.get(customer=request.user.customer, is_completed=False)
    except:
        order = []

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
        'order': order
    }
    return render(request, 'base/account/account.html', context)

def logout_user(request):
    logout(request)
    return redirect('home')
    
def add_to_cart(request, item_id, *args, **kwargs):
    try:
        customer = request.user.customer
    except:
        device = request.COOKIES['device']
        customer, created = Customer.objects.get_or_create(device=device)

    configuration = get_object_or_404(Configuration, id=item_id)
    order_item, created = OrderItem.objects.get_or_create(configuration=configuration, customer=customer)
    order = Order.objects.filter(customer=customer, is_completed=False)
    if order.exists():
        if order[0].configurations.filter(configuration__id=configuration.id, order__customer=customer).exists():
            order_item.quantity += 1
            order_item.save()
        else:
            order[0].configurations.add(order_item)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(customer=customer, date_ordered=ordered_date)
        order.configurations.add(order_item)
    return redirect('home')

def remove_from_cart(request, item_id, *args, **kwargs):
    try:
        customer = request.user.customer
    except:
        device = request.COOKIES['device']
        customer, created = Customer.objects.get_or_create(device=device)

    configuration = get_object_or_404(Configuration, id=item_id)
    order = Order.objects.filter(customer=customer, is_completed=False)
    if order.exists():
        if order[0].configurations.filter(configuration__id=configuration.id).exists():
            order_item = OrderItem.objects.filter(configuration=configuration)[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order_item.delete()
        else:
            return redirect('home')
    else:
        return redirect('home')
    return redirect('home')

@login_required(login_url='register')
def order_summary(request):
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, is_completed=False)
    order_items = order.configurations.all()
    context = {
        'order': order,
        'order_items': order_items
    }
    return render(request, 'base/cart/order-summary.html', context)
