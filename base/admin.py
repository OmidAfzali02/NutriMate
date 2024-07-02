from django.contrib import admin
from .models import User, Ingredient, Meal

# Register your models here.
admin.site.register(User)
admin.site.register(Ingredient)
admin.site.register(Meal)