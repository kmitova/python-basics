fat_percent = int(input())
protein_percent = int(input())
carbs_percent = int(input())
total_calories = int(input())
water_content_total_percent = int(input())

total_fat_gr = (fat_percent / 100 * total_calories) / 9
total_protein_gr = (protein_percent / 100 * total_calories) / 4
total_carbs_gr = (carbs_percent / 100 * total_calories) / 4

total_gr = total_carbs_gr + total_fat_gr + total_protein_gr
calories = total_calories / total_gr
calories_not_water = 1 - water_content_total_percent / 100
final_calories = calories_not_water * calories
print(f"{final_calories:.4f}")

