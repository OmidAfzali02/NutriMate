
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NutriMate.settings')

django.setup()
from base.models import Ingredient

def nutri_calc(data):
    total_calorie = 0
    total_protein = 0
    total_carbohydrates = 0
    total_fat = 0
    total_sugar = 0
    total_creatine = 0
    total_glutamine = 0
    for key,value in data.items():
        ing = Ingredient.objects.filter(name=key).first()
        if ing is not None:
            calorie = ing.calorie
            calorie_gain = round(value*calorie/100, 2)
            total_calorie += calorie_gain

            protein = ing.protein
            protein_gain = round(value*protein/100, 2)
            total_protein += protein_gain

            carbohydrates = ing.carbohydrates
            carbohydrates_gain = round(value*carbohydrates/100, 2)
            total_carbohydrates += carbohydrates_gain

            fat = ing.fat
            fat_gain = round(value*fat/100, 2)
            total_fat += fat_gain

            sugar = ing.sugar
            sugar_gain = round(value*sugar/100, 2)
            total_sugar += sugar_gain

            creatine = ing.creatine
            creatine_gain = round(value*creatine/100, 2)
            total_creatine += creatine_gain

            glutamine = ing.glutamine
            glutamine_gain = round(value*glutamine/100, 2)
            total_glutamine += glutamine_gain

    result = {
        'total_calorie':total_calorie,
        'total_protein': total_protein,
        'total_carbohydrates':total_carbohydrates,
        'total_fat':total_fat,
        'total_sugar':total_sugar,
        'total_creatine':total_creatine,
        'total_glutamine':total_glutamine,
    }

    return result

print(nutri_calc({'chicken (cooked)':20}))