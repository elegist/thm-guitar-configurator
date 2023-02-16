from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs) -> None:
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name', 'required': True})
        self.fields['last_name'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name', 'required': True})
        self.fields['email'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'required': True})
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'User Name', 'required': True})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Choose a password', 'required': True})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Repeat the password', 'required': True})