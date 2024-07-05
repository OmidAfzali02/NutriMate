from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages # to show flash messages
from django.contrib.auth import authenticate, login, logout

from .forms import RegistrationForm
from .models import User, Meal, Ingredient

from datetime import datetime
from .calculator import nutritional_calc


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


@login_required(login_url="/login")
def userProfile(request, pk):
    user = User.objects.get(id=pk)
    context = {"user": user}
    return render(request, 'profile.html', context)

@login_required(login_url="/login") 
def food_calorie_view(request):
    ingredients = Ingredient.objects.all()
    user = request.user
    food_data = {}
    ings = {}
    if request.method == 'POST':
        food_names = request.POST.getlist('food_name[]')
        food_amounts = request.POST.getlist('food_amount[]')
        meal_type = request.POST.get('meal_type')

        for name, amount in zip(food_names, food_amounts):
            if name and amount:
                food_data[name.strip()] = amount.strip()
                ing = Ingredient.objects.filter(name=name).first()
                calorie = ing.calorie
                protein = ing.protein
                carbohydrates = ing.carbohydrates
                fat = ing.fat
                sugar = ing.sugar
                creatine = ing.creatine
                glutamine = ing.glutamine
                ourData = {name: {'calorie':calorie, 'protein':protein, 'carbohydrates': carbohydrates, 'fat':fat, 'sugar':sugar,'creatine':creatine, 'glutamine':glutamine}}
                ings.update(ourData)
        
        if food_data is not {}:
            totals = nutritional_calc(food_data, ings)
    
        new_meal = Meal.objects.create(
            person = user,
            ingredient_list = food_data,
            kind = meal_type,
            total_calorie = totals.get('total_calorie'),
            total_protein = totals.get('total_protein'),
            total_carbs = totals.get('total_carbohydrates'),
            total_fat = totals.get('total_fat'),
            total_sugar = totals.get('total_sugar'),
            total_creatine = totals.get('total_creatine'),
            total_glutamine = totals.get('total_glutamine')
        )
        new_meal.save()

    return render(request, 'calculate.html', {'ingredients': ingredients})
