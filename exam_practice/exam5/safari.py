fuel_l_price = 2.10
tour_guide_price = 100

budget = float(input())
fuel_needed = float(input())
day = input()

fuel_price = fuel_l_price * fuel_needed
total = fuel_price + tour_guide_price

if day == "Saturday":
    total = total - total * 0.1
elif day == "Sunday":
    total = total - total * 0.2

difference = abs(budget - total)
if total > budget:
    print(f"Not enough money! Money needed: {difference:.2f} lv.")
else:
    print(f"Safari time! Money left: {difference:.2f} lv. ")
