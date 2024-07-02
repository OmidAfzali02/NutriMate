from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages # to show flash messages
from django.contrib.auth import authenticate, login, logout

from .forms import RegistrationForm
from .models import User

from datetime import datetime

# Create your views here.

def home(request):
    context = {}
    return render(request, 'home.html', context)


def login_page(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        email = request.POST.get('email').lower()
        password = request.POST.get("password")
        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, "Username not found")

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.error(request, "Username or Password is incorrect")

    context = {'page': page}
    return render(request, 'login.html', context)

def userLogout(request):
    logout(request)
    return redirect("/")

def userRegister(request):
    page = 'register'
    form = RegistrationForm()

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = user.email.lower()
            user.save()
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'An error occured during registration! ')
        

    context = {'page': page, 'form': form}
    return render(request, 'login.html', context)