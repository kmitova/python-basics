from math import ceil

days = int(input())
total = float(input())
final = 0
first_day = total

for day in range(days):
    percent_increase = int(input())
    previous_day = total
    total = previous_day + previous_day * percent_increase / 100
    final = final + total

ran_for_all_days = first_day + final
diff = abs(ran_for_all_days - 1000)

if ran_for_all_days < 1000:
    print(f"Sorry Mrs. Ivanova, you need to run {ceil(diff)} more kilometers")
else:
    print(f"You've done a great job running {ceil(diff)} more kilometers!")
