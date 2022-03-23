from math import ceil, floor

days = int(input())
food_total = int(input())
food_for_deer_1 = float(input())
food_for_deer_2 = float(input())
food_for_deer_3 = float(input())

total_deer_1 = food_for_deer_1 * days
total_deer_2 = food_for_deer_2 * days
total_deer_3 = food_for_deer_3 * days
total_needed = total_deer_3 + total_deer_1 + total_deer_2
diff = abs(food_total - total_needed)
if total_needed <= food_total:
    print(f"{floor(diff)} kilos of food left.")
else:
    print(f"{ceil(diff)} more kilos of food are needed.")
