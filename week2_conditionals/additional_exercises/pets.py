from math import ceil, floor

days = int(input())
food = int(input())
dog_food_per_day = float(input())
cat_food_per_day = float(input())
tortoise_food_per_day_gr = float(input())

dog_food_total = days * dog_food_per_day
cat_food_total = days * cat_food_per_day
tortoise_food_per_day_kg = tortoise_food_per_day_gr / 1000
tortoise_food_total = days * tortoise_food_per_day_kg

food_needed = dog_food_total + cat_food_total + tortoise_food_total

if food >= food_needed:

    print(f"{floor(food - food_needed)} kilos of food left.")
else:
    print(f"{ceil(food_needed - food)} more kilos of food are needed.")
