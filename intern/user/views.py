
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import  CreateUserForm,LoginForm
from django.contrib import messages
# Create your views here.
from datetime import datetime



@login_required(login_url="login")
def homepage(request):
    return render(request, 'user/dashboard.html')

def register(request):
    if request.user.is_authenticated:
        return redirect( 'home')
    form =CreateUserForm()
    if request.method == 'POST':
        form =CreateUserForm (request.POST)
        if form.is_valid():
            user= form.save()
            name=form.cleaned_data.get('username')
            messages.success(request, 'Account was created for'+ name)
            login(request, user)
            return redirect('home')
        else:
            for msg in form.error_messages:
                messages.error(request,"{msg}: {form.error_messages[msg]}")
            
    context ={'form':form}
    return render(request,'user/signup.html',context=context)

def my_login(request):
    if request.user.is_authenticated:
        return redirect( 'home')
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request,data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                messages.success(request, 'you have succesfully login in acccount'+ username)
                login(request, user)    
                return redirect('home')
    context= {"form":form}
    return render(request, 'user/login.html', context=context)


def userlogout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def dashboard(request):
    return render(request, 'user/dashboard.html', {'username': request.user.username})

@login_required(login_url='login')
def profile(request):
    user = request.user
    context = {
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        
    }
    return render(request, 'user/profile.html', context)