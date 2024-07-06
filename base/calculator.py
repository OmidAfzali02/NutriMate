def nutritional_calc(data, ourData): # to calculate the total nutritions in all of the ingredients
    total_calorie = 0
    total_protein = 0
    total_carbohydrates = 0
    total_fat = 0
    total_sugar = 0
    total_creatine = 0
    total_glutamine = 0
    for key,value in data.items(): # to get each of the ingredients in user input
        value = float(value)
        base_data = ourData.get(key) # ourdata is the information of each ingrediant and their nutritional values
        calorie = base_data.get('calorie')
        calorie_gain = value * calorie /100
        total_calorie += calorie_gain

        protein = base_data.get('protein')
        protein_gain = value * protein/100
        total_protein += protein_gain

        carbohydrates = base_data.get('carbohydrates')
        carbohydrates_gain = value * carbohydrates/100
        total_carbohydrates += carbohydrates_gain

        fat = base_data.get('fat')
        fat_gain = value * fat/100
        total_fat += fat_gain

        sugar = base_data.get('sugar')
        sugar_gain = value * sugar/100
        total_sugar += sugar_gain

        creatine = base_data.get('creatine')
        creatine_gain = value * creatine/100
        total_creatine += creatine_gain

        glutamine = base_data.get('glutamine')
        glutamine_gain = value * glutamine/100
        total_glutamine += glutamine_gain

    result = { # the final output
        'total_calorie':round(total_calorie, 2),
        'total_protein': round(total_protein, 2),
        'total_carbohydrates':round(total_carbohydrates, 2),
        'total_fat':round(total_fat, 2),
        'total_sugar':round(total_sugar, 2),
        'total_creatine':round(total_creatine, 2),
        'total_glutamine':round(total_glutamine, 2),
    }
    return result
