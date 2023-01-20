from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
# Create your models here.

class RegisterForm(UserCreationForm):
    address = forms.CharField(label="Address", max_length=50)
    city = forms.CharField(label="City", max_length=60)
    state = forms.CharField(label="State", max_length=30)
    zip = forms.CharField(label="Zip Code", max_length=6)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'address', 'city', 'state', 'zip', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs) -> None:
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'})
        self.fields['last_name'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'})
        self.fields['email'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'User Name'})
        self.fields['address'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'})
        self.fields['city'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'})
        self.fields['state'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'State'})
        self.fields['zip'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Zip'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Choose a password'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Repeat the password'})

## color, wood, frets, pickup, hardware##
class Category(models.Model):
    name = models.CharField(max_length = 150)
    categoryDesc = models.CharField(max_length = 150)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length = 150)
    category = models.ForeignKey(Category, verbose_name="fk_category", on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    description = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, verbose_name="fk_user", on_delete=models.CASCADE, null=True)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, verbose_name="fk_cart", on_delete=models.CASCADE, null=True)
    item = models.ForeignKey(Item, verbose_name="fk_item", on_delete=models.CASCADE, null=True)


class StaffPick(models.Model):
    name = models.CharField(max_length = 150)
    
    def __str__(self):
        return self.name

class StaffPickItem(models.Model):
    staffPick = models.ForeignKey(StaffPick, verbose_name="fk_StaffPick", on_delete=models.CASCADE, null=True)
    item = models.ForeignKey(Item, verbose_name="fk_item", on_delete=models.CASCADE, null=True)    

    def __str__(self):
        item = str(self.item)
        staffPick = str(self.staffPick)
        name = staffPick + " " + item
        return name