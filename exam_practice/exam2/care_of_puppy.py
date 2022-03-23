food_available_kg = int(input())
food_available = food_available_kg * 1000
total_eaten = 0
command = input()

while command != "Adopted":
    food_per_meal = int(command)
    total_eaten = total_eaten + food_per_meal
    command = input()

difference = abs(food_available - total_eaten)
if total_eaten <= food_available:
    print(f"Food is enough! Leftovers: {difference} grams." )
else:
    print(f"Food is not enough. You need {difference} grams more." )
