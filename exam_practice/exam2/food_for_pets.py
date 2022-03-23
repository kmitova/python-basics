days = int(input())
total_food_to_eat = float(input())
total_food_dog = 0
total_food_cat = 0
biscuits = 0
total_biscuits = 0


for day in range(1, days + 1):
    food_eaten_by_dog = int(input())
    food_eaten_by_cat = int(input())
    total_food_dog = total_food_dog + food_eaten_by_dog
    total_food_cat = total_food_cat + food_eaten_by_cat
    if day in range(3, days + 1, 3):
        biscuits = 0.1 * (food_eaten_by_dog + food_eaten_by_cat)
        total_biscuits = total_biscuits + biscuits

total_food = total_food_dog + total_food_cat
percent_eaten = total_food / total_food_to_eat * 100
dog_food_percent = total_food_dog / total_food * 100
cat_food_percent = total_food_cat / total_food * 100

print(f"Total eaten biscuits: {int(total_biscuits)}gr.")
print(f"{percent_eaten:.2f}% of the food has been eaten.")
print(f"{dog_food_percent:.2f}% eaten from the dog.")
print(f"{cat_food_percent:.2f}% eaten from the cat.")
