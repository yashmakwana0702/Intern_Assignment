from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput,TextInput

class CreateUserForm(UserCreationForm) :
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    
    class Meta :
        model= User
        fields = ['username', 'first_name', 'last_name', 'email',  'password1', 'password2']

class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())