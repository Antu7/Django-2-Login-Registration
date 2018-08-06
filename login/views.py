from django.shortcuts import render
from .models import AuthUser
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def loginView(request):
    return render(request, "login.html")

@login_required(login_url='loginView')
def home(request):
    return render(request, "home.html")


def loginCheck(request):
    if request.method == 'POST' and 'username' in request.POST and 'password' in request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('loginView')
    return redirect('loginView')


def registration(request):
    checkData = AuthUser.objects.filter(email=request.POST.get('email'))
    if not checkData:
        User.objects.create_user(
            username=request.POST.get('username'),
            email=request.POST.get('email'),
            password=(request.POST.get('password')),
        )
        messages.add_message(request, messages.INFO, 'User Saved Successfully')
        return redirect('loginView')
    else:
        messages.add_message(request, messages.INFO, 'Email Already Exists')
        return redirect('loginView')


def logout_view(request):
    logout(request)
    return redirect('loginView')