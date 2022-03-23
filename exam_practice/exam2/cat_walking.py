minutes_walk_per_day = int(input())
number_of_walks_per_day = int(input())
calories_per_day = int(input())
calories = 0

total_walk_minutes = minutes_walk_per_day * number_of_walks_per_day
burned_calories = total_walk_minutes * 5

if burned_calories >= calories_per_day / 2:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {burned_calories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {burned_calories}.")
