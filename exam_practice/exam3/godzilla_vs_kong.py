budget = float(input())
statists = int(input())
price_for_clothes_one_statist = float(input())

decors = budget * 0.1
price_for_clothes = price_for_clothes_one_statist * statists
if statists > 150:
    price_for_clothes = price_for_clothes - price_for_clothes * 0.1
difference = abs(decors + price_for_clothes - budget)
if decors + price_for_clothes > budget:

    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")
