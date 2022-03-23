cats = int(input())
group_1 = 0
group_2 = 0
group_3 = 0
total_food = 0

for cat in range(cats):
    food = float(input())
    if food < 200:
        group_1 += 1
    elif food < 300:
        group_2 += 1
    elif food < 400:
        group_3 += 1
    total_food += food

total_food_kg = total_food / 1000
total_price = total_food_kg * 12.45

print(f"Group 1: {group_1} cats.")
print(f"Group 2: {group_2} cats.")
print(f"Group 3: {group_3} cats.")
print(f"Price for food per day: {total_price:.2f} lv.")
