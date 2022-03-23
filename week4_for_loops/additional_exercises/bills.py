months = int(input())
all_water = 0
all_internet = 0
all_others = 0
all_electricity = 0
all_bills = 0

for month in range(months):
    electricity = float(input())
    all_electricity = all_electricity + electricity
    all_water = all_water + 20
    all_internet = all_internet + 15
    others = electricity + 20 + 15
    all_others = all_others + others + others * 0.2
    all_bills = all_electricity + all_water + all_internet + all_others

average = all_bills / months

print(f"Electricity: {all_electricity:.2f} lv")
print(f"Water: {all_water:.2f} lv")
print(f"Internet: {all_internet:.2f} lv")
print(f"Other: {all_others:.2f} lv")
print(f"Average: {average:.2f} lv")
