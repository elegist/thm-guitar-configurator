from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Customer

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs) -> None:
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget = forms.TextInput(attrs={'id': 'usernameInput', 'class': 'form-control', 'placeholder': 'User Name'})
        self.fields['email'].widget = forms.TextInput(attrs={'id': 'emailInput', 'class': 'form-control', 'placeholder': 'Email'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'id': 'password1Input', 'class': 'form-control', 'placeholder': 'Choose a password'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'id': 'password2Input', 'class': 'form-control', 'placeholder': 'Repeat the password'})

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
    
    def __init__(self, *args, **kwargs) -> None:
        super(UpdateUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget = forms.TextInput(attrs={'id': 'usernameInput', 'class': 'form-control', 'placeholder': 'User Name'})
        self.fields['email'].widget = forms.TextInput(attrs={'id': 'emailInput', 'class': 'form-control', 'placeholder': 'Email'})

class UpdateCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'street', 'city', 'state', 'zip_code']
    
    def __init__(self, *args, **kwargs) -> None:
        super(UpdateCustomerForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].widget = forms.TextInput(attrs={'id': 'first_nameInput', 'class': 'form-control', 'placeholder': 'First Name'})
        self.fields['last_name'].widget = forms.TextInput(attrs={'id': 'last_nameInput', 'class': 'form-control', 'placeholder': 'Last Name'})
        self.fields['street'].widget = forms.TextInput(attrs={'id': 'streetInput', 'class': 'form-control', 'placeholder': 'Street'})
        self.fields['city'].widget = forms.TextInput(attrs={'id': 'cityInput', 'class': 'form-control', 'placeholder': 'City'})
        self.fields['state'].widget = forms.TextInput(attrs={'id': 'stateInput', 'class': 'form-control', 'placeholder': 'State'})
        self.fields['zip_code'].widget = forms.TextInput(attrs={'id': 'zip_codeInput', 'class': 'form-control', 'placeholder': 'Zip Code'})
