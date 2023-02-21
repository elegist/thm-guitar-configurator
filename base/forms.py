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

        self.fields['username'].widget = forms.TextInput(attrs={'id': 'usernameInput', 'class': 'form-control', 'placeholder': 'User Name', 'required': True})
        self.fields['email'].widget = forms.TextInput(attrs={'id': 'emailInput', 'class': 'form-control', 'placeholder': 'Email', 'required': True})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'id': 'password1Input', 'class': 'form-control', 'placeholder': 'Choose a password', 'required': True})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'id': 'password2Input', 'class': 'form-control', 'placeholder': 'Repeat the password', 'required': True})

# class UpdateUserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'email', 'username']
    
#     def __init__(self, *args, **kwargs) -> None:
#         super(UpdateUserForm, self).__init__(*args, **kwargs)

#         self.fields['first_name'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'})
#         self.fields['last_name'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'})
#         self.fields['email'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
#         self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'User Name'})